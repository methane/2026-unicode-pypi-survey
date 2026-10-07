#!/usr/bin/env python3
"""Verify published frozen rows/ranking/hashes locally. No network requests."""
import collections
import csv
import hashlib
import json
from pathlib import Path
import re

PUB = Path(__file__).resolve().parent.parent

def main():
    provenance = json.loads((PUB / 'data/reproducibility-provenance.json').read_bytes())
    for relative, expected in provenance['reproduction_asset_sha256'].items():
        actual = hashlib.sha256((PUB / relative).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError('published asset SHA256 mismatch: ' + relative)
    rows = [json.loads(line) for line in (PUB / 'data/source-metadata.jsonl').read_text(encoding='utf-8').splitlines()]
    names = (PUB / 'data/top4000.txt').read_text(encoding='utf-8').splitlines()
    with (PUB / 'data/top4000.csv').open(encoding='utf-8', newline='') as stream:
        ranking = list(csv.DictReader(stream))
    assert len(rows) == len(names) == len(ranking) == 4000
    assert [row['rank'] for row in rows] == list(range(1, 4001))
    assert [row['package'] for row in rows] == names == [row['project'] for row in ranking]
    assert len(set(names)) == 4000
    for row, rank in zip(rows, ranking):
        assert row['download_count'] == int(rank['download_count'])
        if row['current_sdist_url']:
            assert re.fullmatch(r'[0-9a-f]{64}', row['current_sdist_sha256'])
            assert row['current_sdist_sha256'] == row['archive_verified_sha256']
            assert row['current_sdist_size'] > 0
            assert row['version']
            assert row['status'] in ('scanned', 'partial_scan')
            assert row['recovery_status'] == 'scanned'
        else:
            assert row['status'] in ('no_current_sdist', 'metadata_unavailable')
    raw_ranking = PUB / 'data/ranking-snapshot.json'
    if raw_ranking.exists():
        assert hashlib.sha256(raw_ranking.read_bytes()).hexdigest() == provenance['ranking']['ranking_sha256']
        full = json.loads(raw_ranking.read_bytes())
        assert full['rows'][:4000] == [{'project':row['project'],'download_count':int(row['download_count'])} for row in ranking]
    print(json.dumps({'verified_rows': len(rows), 'verified_frozen_sdist_digests': sum(bool(row['current_sdist_url']) for row in rows),
                      'statuses': dict(collections.Counter(row['status'] for row in rows)), 'network_requests': 0}, indent=2))

if __name__ == '__main__':
    main()
