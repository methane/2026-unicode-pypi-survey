#!/usr/bin/env python3
"""Check public counts, relative Markdown links and host-path omissions offline."""
import collections
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

def read_jsonl(name):
    return [json.loads(x) for x in (ROOT / 'data' / name).read_text(encoding='utf-8').splitlines()]

def source_key(row):
    return tuple(row[k] for k in ('package','version','path','function_start'))

def main():
    errors = []
    links = blocks = 0
    for p in ROOT.rglob('*.md'):
        text = p.read_text(encoding='utf-8')
        fences = sum(line.startswith('```') for line in text.splitlines())
        assert fences % 2 == 0, p
        blocks += fences // 2
        plain = re.sub(r'(?ms)^```[^\n]*\n.*?^```[^\n]*\n?', '', text)
        for ref in re.findall(r'\]\(([^\n)]+)\)', plain):
            if re.match(r'^(?:https?://|mailto:)', ref):
                continue
            file, _, anchor = ref.partition('#')
            target = (p.parent / file).resolve() if file else p.resolve()
            links += 1
            if not target.exists():
                errors.append({'file':str(p.relative_to(ROOT)), 'missing_link':ref})
            elif anchor and target.suffix == '.md':
                dest = target.read_text(encoding='utf-8')
                ids = set(re.findall(r'id="([^"]+)"', dest))
                for heading in re.findall(r'^#+ (.+)$',dest,re.M):
                    ids.add(re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-'))
                if anchor not in ids:
                    errors.append({'file':str(p.relative_to(ROOT)), 'missing_anchor':ref})
    functions = read_jsonl('functions.jsonl')
    assert len(functions) == len({source_key(x) for x in functions}) == 1205
    core = [x for x in functions if x['handwritten'] and x['scope_api']=='fsr_read' and x['canonical_default_included']]
    assert len(core) == 356
    assert collections.Counter(x['class'] for x in core) == {'A':39,'B':272,'C':45}
    cases = read_jsonl('canonical-handwritten-B-cases.jsonl')
    assert len(cases) == 272
    assert {source_key(x) for x in cases} == {source_key(x) for x in core if x['class']=='B'}
    assert sum(len(x['access_sites']) for x in cases) == 551
    reuse = json.loads((ROOT / 'data/reuse-inventory.json').read_text(encoding='utf-8'))
    others = [x for x in reuse if x['package'] != 'regex']
    assert len(reuse) == 53 and len(others) == 52
    status = collections.Counter(x['status'] for x in others)
    assert status == {'yes':28,'possible':11,'no':13}
    assert sum(x['strong_successful_partial'] for x in others) == 8
    forbidden = ['/Users'+'/', '/workspace'+'/', '/root'+'/read_', '"review'+'_owner"', 'source'+'_thread_id']
    privacy = []
    files = [p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in {'publication-validation.json','publication-manifest.json'}]
    for p in files:
        text = p.read_text(encoding='utf-8')
        for pattern in forbidden:
            if pattern in text:
                privacy.append({'file':str(p.relative_to(ROOT)), 'pattern':pattern})
    assert not errors, errors
    assert not privacy, privacy
    out = {'files_excluding_generated_validation_manifest':len(files), 'bytes_excluding_generated_validation_manifest':sum(p.stat().st_size for p in files),
           'markdown_pages':sum(p.suffix=='.md' for p in files), 'fenced_code_blocks':blocks, 'relative_links_checked':links,
           'read_functions':1205, 'handwritten_B_cases':272, 'handwritten_B_logical_sites':551,
           'reuse_other_packages':52, 'reuse_statuses':dict(status), 'strong_partial_other_packages':8,
           'private_path_findings':privacy, 'link_errors':errors, 'network_requests':0,
           'source_identity_checks':'Exact full-member hash and excerpt line checks were performed in the source review and public-case/reuse export; full corpus is not included here.'}
    (ROOT / 'data/publication-validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__ == '__main__':
    main()
