#!/usr/bin/env python3
"""Render the public case pages from the self-contained sanitized JSONL data."""
import argparse, collections, json, pathlib, re
LABELS = {'arbitrary_index':'arbitrary or fixed-position indexing','caller_start_range':'caller-provided start or range','backward':'backward traversal','lookahead_lookbehind':'lookahead or lookbehind','reset_backtracking':'reset or backtracking','multiple_passes':'multiple passes','subset_nonzero_start':'a subset starting after position zero','mixed':'mixed access patterns','scalar_single_character':'a scalar or single-character check'}
def inline(s): return '`'+str(s).replace('`','\\`').replace('\n',' ')+'`'
def language(path):
    suffix=pathlib.PurePosixPath(path).suffix.lower()
    return {'.c':'c','.h':'c','.cc':'cpp','.cpp':'cpp','.cxx':'cpp','.hpp':'cpp','.m':'objective-c','.rs':'rust','.py':'python','.pyx':'cython','.pxi':'cython','.pxd':'cython'}.get(suffix,'text')
def fenced(code,path):
    fence='`'*max(3, max((len(x) for x in re.findall(r'`+',code)),default=0)+1)
    return fence+language(path)+'\n'+code+'\n'+fence

def source_description(s):
    start,end=s['lines']
    text=f"Archive member {inline(s['path'])}, lines {start}–{end}. Member SHA-256: {inline(s['source_sha256'])}."
    if s.get('verified_permalink'): text+=' [Verified immutable source link]('+s['verified_permalink']+').'
    else:text+=' **No verified GitHub permalink is available for this excerpt.**'
    return text

def text_value(value):
    if isinstance(value,list):return '\n'.join('- '+text_value(x) for x in value)
    if isinstance(value,dict):return '; '.join(str(k)+': '+text_value(v) for k,v in value.items())
    return str(value)

def interpretation(f):
    parts=[]
    if f.get('monotonic_stream'):
        parts.append('This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.')
    if 'scalar_single_character' in f['subtypes']:
        parts.append('The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.')
    if not parts:
        parts.append('This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.')
    if f.get('migration_feasibility'):parts.append(f['migration_feasibility'])
    return '\n\n'.join(parts)

def omissions(groups):
    result=[]
    for group in groups:
        if group.get('omitted_ranges'):
            ranges=', '.join(str(a) if a==b else f'{a}–{b}' for a,b in group['omitted_ranges'])
            result.append(f"Omitted from {inline(group['path'])}: lines {ranges}. The original contextual region was lines {group['original_lines'][0]}–{group['original_lines'][1]}.")
    return result

def write_pages(records,out):
    out.mkdir(parents=True,exist_ok=True)
    grouped=collections.defaultdict(list)
    for f in records:grouped[f['package']].append(f)
    index=['# Non-simple Unicode read access: case index','',f"This collection contains **{len(records)} function-level B cases in {len(grouped)} packages** from the frozen top-4,000 PyPI source survey. These are the canonical-default, handwritten cases involving the FSR read interface; generated code, compatibility definitions, vendor copies and the broader legacy/raw-layout groups are outside this collection.",'','A means a single forward pass from position zero through the full string, with early exit recorded separately. B includes other access patterns: a scalar check, a supplied range, continuation from a nonzero position, backward traversal, lookahead, backtracking or multiple passes. Consequently, **B is not a count of functions that necessarily require random access or an FSR view**. Function records are counted once; subtypes can overlap.','',"Python codepoints include surrogate codepoints. Here, “scalar check” describes a one-character operation, not a claim that the input excludes surrogates. Codepoint offsets must not be substituted with UTF-8 byte offsets without considering each function’s semantics.",'','The pages contain source excerpts, source provenance, immutable links where verified, and relevant callee excerpts. Source text is reproduced unchanged from the recorded excerpt data. A missing permalink does not mean the source is missing: the sdist URL, archive hash and member hash identify it.','', "**Excerpting policy:** Keep source regions of 35 lines or fewer. For longer regions, retain bounded windows around recorded reads and relevant entry, loop-bound and reset evidence. Explicit omitted line ranges accompany disjoint excerpts. Every one of the 551 recorded semantic access-site records has at least one contextual window; this is not a claim to reproduce every statement in a broad algorithm span. Quoted code contains no inserted ellipsis.",'', '| Package | Version | B functions |','|---|---|---:|']
    contexts=callees=0
    for pkg,items in sorted(grouped.items()):
        items.sort(key=lambda f:(f['path'],f['function_start'],f['function']))
        versions=sorted({f['version'] for f in items});index.append(f"| [{pkg}]({pkg}.md) | {', '.join(versions)} | {len(items)} |")
        page=[f'# {pkg} — non-simple Unicode reads','', '[All packages](README.md)', '',f"Version: {', '.join(versions)}. **{len(items)} B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.",'','## Contents','']
        for i,f in enumerate(items,1):page.append(f"- [{inline(f['function'])}](#case-{i:03d})")
        helpers={};helperlist=[]
        for f in items:
            for s in f.get('callee_snippets',[]):
                key=(s['path'],tuple(s['lines']),s['source_sha256'],s['code'])
                if key not in helpers:helpers[key]=len(helperlist)+1;helperlist.append(s)
        if helperlist:page.append('- [Shared callee excerpts](#callee-excerpts)')
        for i,f in enumerate(items,1):
            page+=['',f'<a id="case-{i:03d}"></a>','',f"## {i}. {inline(f['function'])}",'',f"**Classification:** B. **Subtypes:** {', '.join(LABELS.get(x,x.replace('_',' ')) for x in f['subtypes'])}. **Early exit recorded:** {'yes' if f['early_exit'] else 'no'}.",'',f"**Scope:** {inline(f['scope_api'])}; canonical-default included; handwritten source. **Origin:** {inline(f['origin'])}." ]
            if f.get('role'):page+=['',f"**Role:** {f['role'].replace('_',' ')}."]
            page+=['',f['reason'],'',interpretation(f),'',f"**Offsets and character semantics:** {text_value(f['byte_vs_codepoint'])}",'']
            risk=f['fsr_lifetime_risk']
            if risk=='no':page.append('**FSR lifetime assessment:** No risk was identified in this case.')
            elif risk=='possible':page.append('**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.')
            else:page.append('**FSR lifetime assessment:** '+text_value(risk)+'.')
            if f.get('fsr_lifetime_evidence'):page+=['',text_value(f['fsr_lifetime_evidence'])]
            if f.get('notes'):page+=['',text_value(f['notes'])]
            page+=['',f"**Archive:** [source distribution]({f['sdist_url']}). Archive SHA-256: {inline(f['sdist_sha256'])}.",'',f"**Function source:** {inline(f['path'])}, lines {f['function_start']}–{f['function_end']}. Member SHA-256: {inline(f['source_sha256'])}."]
            if f.get('verified_permalink'):page+=['', '[Verified immutable function link]('+f['verified_permalink']+').']
            else:page+=['','**No verified GitHub permalink is available for the complete function range.** Excerpt links below may still be verified.']
            page+=['','### Read sites','']
            for site_number,s in enumerate(f['access_sites'],1):
                lines=s.get('lines',[]);location=f'lines {lines[0]}–{lines[-1]}' if lines else 'line range not separately recorded'
                page.append(f"- Site {site_number}: {location}; {s.get('kind','read').replace('_',' ')}; index expression {inline(s.get('index_expression','not separately recorded'))}. {s.get('reason','')}")
            page+=['','### Contextual source excerpts','']
            page+=omissions(f.get('excerpt_groups',[]))
            if omissions(f.get('excerpt_groups',[])):page+=['']
            for s in f['context_snippets']:
                page+=[source_description(s),'',fenced(s['code'],s['path']),''];contexts+=1
            if f.get('callee_trace'):
                page+=['### Callee analysis','']
                for c in f['callee_trace']:
                    entry=f"- {inline(c['callee'])}"
                    if c.get('path'):entry+=' in '+inline(c['path'])
                    if c.get('lines'):entry+=f", lines {c['lines'][0]}–{c['lines'][-1]}"
                    entry+=': '+text_value(c.get('evidence',''))
                    if c.get('result'):entry+=' '+text_value(c['result'])
                    page.append(entry)
            if f.get('callee_snippets'):
                page+=['','Available source context:']
                page+=omissions(f.get('callee_excerpt_groups',[]))
                page+=['']
                for s in f['callee_snippets']:
                    key=(s['path'],tuple(s['lines']),s['source_sha256'],s['code']);h=helpers[key]
                    page.append(f"- [{inline(s.get('callee','Callee excerpt'))}](#helper-{h:03d}) ({inline(s['path'])}, lines {s['lines'][0]}–{s['lines'][1]}).")
        if helperlist:
            page+=['','<a id="callee-excerpts"></a>','','## Shared callee excerpts','', 'These excerpts are shared by the function records linked above. Each is reproduced once on this package page.']
            for h,s in enumerate(helperlist,1):
                page+=['',f'<a id="helper-{h:03d}"></a>','',f"### {h}. {inline(s.get('callee','Callee'))}",'',source_description(s),'',fenced(s['code'],s['path'])];callees+=1
        (out/(pkg+'.md')).write_text('\n'.join(page).rstrip()+'\n',encoding='utf-8')
    index+=['','[Machine-readable case records](../data/canonical-handwritten-B-cases.jsonl). Pages can be rebuilt with [render_cases.py](../scripts/render_cases.py) using only that public JSONL file.','']
    (out/'README.md').write_text('\n'.join(index),encoding='utf-8')
    return {'cases':len(records),'packages':len(grouped),'context_snippets':contexts,'unique_package_callee_snippets':callees,'markdown_files':len(grouped)+1}
def main():
    pub=pathlib.Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,default=pub/'data/canonical-handwritten-B-cases.jsonl');p.add_argument('--output',type=pathlib.Path,default=pub/'cases');a=p.parse_args()
    records=[json.loads(x) for x in a.input.read_text(encoding='utf-8').splitlines() if x]
    assert len(records)==272 and len({f['package'] for f in records})==27
    assert all(f['class']=='B' and f['handwritten'] and f['canonical_default_included'] for f in records)
    print(json.dumps(write_pages(records,a.output),indent=2))
if __name__=='__main__':main()
