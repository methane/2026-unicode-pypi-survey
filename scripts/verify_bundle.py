#!/usr/bin/env python3
"""Portable consolidated survey checks. Standard library; no network or source execution."""
from pathlib import Path
from urllib.parse import unquote
import collections,csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def jsonl(p):return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines()]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def selected():return sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in p.parts for x in ['__pycache__','.git']) and p.name!='.DS_Store' and not p.name.endswith('.pyc'))
def main():
    errors=[];checks=collections.Counter();blocks=[]
    def check(ok,kind,**details):
        checks[kind]+=1
        if not ok:errors.append(dict(kind=kind,**details))
    names=(ROOT/'data/top4000.txt').read_bytes();ranking=(ROOT/'data/ranking-snapshot.json').read_bytes()
    check(sha(names)=='d3710dafb8a01c8f1b413d6188d5b9ae3670069d1bd4cc3b4456d1e36a557199','names_sha')
    check(sha(ranking)=='a0458d45ec5c696a482b44f94cc0eb83f7d5f3167e53c066b2a66cbfffa98358','ranking_sha')
    ordered=names.decode().splitlines();check(len(ordered)==4000 and ordered==[r['project'] for r in json.loads(ranking)['rows'][:4000]],'exact_ranked_scope')
    metadata=jsonl(ROOT/'data/source-metadata.jsonl');check([r['package'] for r in metadata]==ordered,'4000_frozen_selections')
    functions=jsonl(ROOT/'data/functions.jsonl');check(len(functions)==1205,'read_functions')
    core=[r for r in functions if r['handwritten'] and r['scope_api']=='fsr_read' and r['canonical_default_included']]
    check(len(core)==356 and dict(collections.Counter(r['class'] for r in core))=={'A':39,'B':272,'C':45},'handwritten_read_counts')
    bc=jsonl(ROOT/'data/canonical-handwritten-B-cases.jsonl');check(len(bc)==272 and sum(len(r['access_sites']) for r in bc)==551,'B_case_site_counts')
    lifetime=read(ROOT/'data/reuse-inventory.json');other=[r for r in lifetime if r['package']!='regex']
    check(len(other)==52 and dict(collections.Counter(r['status'] for r in other))=={'yes':28,'possible':11,'no':13} and sum(r['strong_successful_partial'] for r in other)==8,'lifetime_counts')
    layout=read(ROOT/'layout/data/cases.json');kind=read(ROOT/'fromkind/data/sites.json')
    check(len(layout)==1137 and sum(r['direct_layout'] for r in layout)==1041 and len({r['package'] for r in layout if r['direct_layout']})==67,'layout_counts')
    principal=read(ROOT/'layout/data/principal-python3-full-object.json')
    check(len(principal)==8,'principal_layout_packages')
    con=[r for r in kind if r['concrete_constructor_site']];wr=[r for r in kind if r['static_use'] and r['usage_form']=='wrapper_call'];fw=[r for r in kind if r['usage_form']=='forwarding_api_call']
    check((len(kind),len(con),len(wr),len(fw),len({r['package'] for r in con}))==(194,85,80,3,32),'constructor_counts')
    check(dict(collections.Counter(r['kind_class'] for r in con))=={'fixed_1':13,'fixed_2':6,'fixed_4':43,'dynamic_1_2_4':23},'input_kind_counts')
    for study,stem,rows in [('layout','cases',layout),('fromkind','sites',kind)]:
        with (ROOT/study/'data'/f'{stem}.csv').open(encoding='utf-8',newline='') as f:csvrows=list(csv.DictReader(f))
        check([r['evidence_id'] for r in csvrows]==[r['evidence_id'] for r in rows],'CSV_JSON_order',study=study)
        with (ROOT/study/'data/coverage4000.csv').open(encoding='utf-8',newline='') as f:coverage=list(csv.DictReader(f))
        check([r['package'] for r in coverage]==ordered,'coverage_order',study=study)
        check(dict(collections.Counter(r['sdist_status'] for r in coverage))=={'scanned':3788,'no_current_sdist':211,'metadata_unavailable':1},'coverage_outcomes',study=study)
        for r in rows:
            for s in r['snippets']:
                for e in s['published_excerpts']:
                    t=e['text'];check(e['end']-e['start']+1==len(t.split('\n'))<=24 and max(map(len,t.split('\n')),default=0)<=4000,'excerpt_bounds',study=study,id=r['evidence_id'])
                    check(sha(t.encode('utf-8'))==e['excerpt_sha256'],'excerpt_hash',study=study,id=r['evidence_id'])
                    link=e.get('verified_permalink')
                    check(not link or bool(re.fullmatch(r'https://github.com/[^/]+/[^/]+/blob/[0-9a-f]{40}/[^#]+#L\d+-L\d+',link)),'immutable_snippet_link',study=study,id=r['evidence_id'])
                spans=[(e['start'],e['end']) for e in s['published_excerpts']]+[(e['start'],e['end']) for e in s['omitted_intervals']]
                spans.sort();cursor=s['reviewed_start']
                for a,b in spans:check(a==cursor and a<=b<=s['reviewed_end'],'excerpt_omission_partition',study=study,id=r['evidence_id']);cursor=b+1
                check(cursor==s['reviewed_end']+1,'excerpt_complete_partition',study=study,id=r['evidence_id'])
    host_patterns=[r'/Us'+r'ers/[^/\s]+',r'/ho'+r'me/[^/\s]+',r'Docu'+r'ments/Codex',r'/root/read_\w+',r'(?<![\w-])sk-[A-Za-z0-9_-]{20,}',r'AKIA[0-9A-Z]{16}',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',r'gh[pousr]_[A-Za-z0-9]{30,}',r'xox[baprs]-[A-Za-z0-9-]{20,}']
    forbidden_keys={'evidence_path','remote_cache_path','review_owner','source_thread_id'}
    def keys(obj,path):
        if isinstance(obj,dict):
            check(not forbidden_keys.intersection(obj),'no_local_workflow_fields',path=path)
            for v in obj.values():keys(v,path)
        elif isinstance(obj,list):
            for v in obj:keys(v,path)
    for p in selected():
        if p.name=='bundle-validation.json':continue
        text=p.read_text(encoding='utf-8');rel=p.relative_to(ROOT).as_posix()
        for pattern in host_patterns:check(not re.search(pattern,text),'privacy_secret_pattern',path=rel,pattern=pattern)
        if p.suffix=='.json':
            obj=json.loads(text)
            if rel.startswith(('layout/data/','fromkind/data/')):keys(obj,rel)
        if p.suffix=='.md':
            check(sum(l.startswith('```') for l in text.splitlines())%2==0,'balanced_fences',path=rel)
            plain=re.sub(r'(?ms)^```[^\n]*\n.*?^```[^\n]*\n?','',text)
            for target in re.findall(r'\]\(([^\n)]+)\)',plain):
                if target.startswith(('http://','https://','mailto:')):continue
                file,_,anchor=target.partition('#');dest=(p.parent/unquote(file)).resolve() if file else p
                deferred=dest in [ROOT/'PUBLICATION-MANIFEST.json',ROOT/'data/bundle-validation.json']
                check(dest.is_file() or deferred,'relative_link',path=rel,target=target)
                if anchor and dest.is_file() and dest.suffix=='.md':
                    content=dest.read_text(encoding='utf-8');ids=set(re.findall(r'id="([^"]+)"',content))
                    ids.update(re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#+ (.+)$',content,re.M))
                    check(anchor in ids,'relative_anchor',path=rel,target=target)
            for b in re.findall(r'(?ms)^```[^\n]*\n(.*?)^```',text):blocks.append((len(b.splitlines()),len(b)))
    manifest_path=ROOT/'PUBLICATION-MANIFEST.json'
    if manifest_path.exists():
        manifest=read(manifest_path)
        for r in manifest['files']:
            p=ROOT/r['path'];check(p.is_file() and p.stat().st_size==r['bytes'] and sha(p.read_bytes())==r['sha256'],'artifact_manifest',path=r['path'])
        expected={p.relative_to(ROOT).as_posix() for p in selected()}-set(manifest['excluded'])
        check(expected=={r['path'] for r in manifest['files']},'manifest_file_set')
    else:check(False,'manifest_exists')
    result=dict(passed=not errors,errors=errors,checks=dict(checks),read_functions=1205,handwritten_read_functions=356,B_cases=272,B_access_sites=551,lifetime_other_packages=52,layout_records=1137,direct_layout_regions=1041,constructor_records=194,concrete_constructor_sites=85,routed_helper_sites=80,test_forwarders=3,maximum_markdown_fence_lines=max((b[0] for b in blocks),default=0),network_requests=0,source_execution=False,scope='portable data/link/hash/privacy checks; source-byte/source-link verification occurred in frozen reviews and local consolidation audit')
    (ROOT/'data/bundle-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(passed=result['passed'],errors=errors,checks=sum(checks.values()),counts={k:v for k,v in result.items() if k.endswith(('functions','records','regions','sites','packages'))}),indent=2))
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
