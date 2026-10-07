#!/usr/bin/env python3
"""Inventory named follow-up candidates from an explicitly retained scanner output.

No download/import/build is performed. This is a lexical aid, not semantic review.
"""
import argparse,collections,hashlib,json,re
from pathlib import Path
from static_lexical import mask_source,kind_of
TOKEN=re.compile(r'(?<!\w)(?:[A-Za-z_]\w*FromKindAndData\w*|Py(?:ASCII|CompactUnicode|Unicode)Object)(?!\w)')
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('scan_output',type=Path);p.add_argument('--output',type=Path,default=Path('followup-candidates.jsonl'));a=p.parse_args()
    root=a.scan_output.resolve();outcomes=[];hits=[];files=0;missing=[]
    for path in sorted((root/'results').glob('*.json')):
        r=json.loads(path.read_text(encoding='utf-8'));retained=0
        for f in r.get('native_files',[]):
            if not f.get('source_file'):continue
            source=(root/f['source_file']).resolve()
            if not source.is_relative_to(root):raise ValueError('source_file escapes scanner output')
            raw=source.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=f['sha256']:raise ValueError('source SHA mismatch: '+f['path'])
            files+=1;retained+=1;text=raw.decode('utf-8','replace');masked=mask_source(text,Path(f['path']).suffix)
            for m in TOKEN.finditer(text):
                hits.append(dict(package=f['package'],version=f['version'],path=f['path'],source_sha256=f['sha256'],symbol=m.group(),line=text.count('\n',0,m.start())+1,character_offset=m.start(),lexical_kind=kind_of(text,masked,m.start(),m.end(),Path(f['path']).suffix),interpretation='candidate only; declarations/comments/aliases need source review'))
        outcomes.append(dict(package=r['package'],source_status=r.get('status'),retained_files=retained))
        if not retained:missing.append(r['package'])
    if not outcomes:raise ValueError('No results/*.json; run the scanner separately with explicit source retention first')
    a.output.write_text(''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hits),encoding='utf-8')
    summary=dict(packages=len(outcomes),retained_source_records=files,candidate_tokens=len(hits),symbols=dict(collections.Counter(h['symbol'] for h in hits)),packages_without_retained_source=missing,outcomes=outcomes,source_execution=False,network_requests=0,scope='named candidates in explicitly retained scanner output; no semantic classification or alias-completeness proof')
    a.output.with_suffix('.summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in summary.items() if k not in ['outcomes','packages_without_retained_source']}))
if __name__=='__main__':main()
