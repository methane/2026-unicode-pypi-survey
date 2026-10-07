#!/usr/bin/env python3
"""Render reviewed lifetime data and exact excerpt witnesses. No network."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INTRO = """# Repeated calls, borrowed views and immediate eviction

**At least eight packages other than regex have verified successful, scalable partial-work examples: APSW, lxml, RapidFuzz, polyleven, spaCy, pyahocorasick, simplejson and pyjson5.** Polyleven and spaCy share an implementation, so these are **seven implementation families**. Numba adds a separate Python-to-native boundary example: including that category gives **nine package names and eight families**.

This is a conservative lower bound among the **53 canonical-native candidate package names** from the frozen survey. Excluding regex leaves **52 individually reviewed packages: 28 yes, 11 possible, 13 no** under the strict criterion below. It is not a population estimate across all 4,000 packages or all PyPI. The 28 yes results include full scans/copies, bounded stream providers, bulk comparisons and early-invalid cases; they are not 28 demonstrated regex-like asymptotic regressions.

## Question and assumptions

The question is narrower than random access: can independent operations reacquire a borrowed non-ASCII-capable fixed-width representation of the **same caller-owned str**, after their own view/owner scope has ended? A library can finish its current operation without knowing whether the caller will submit that str again.

The performance inference assumes a hypothetical API/policy that materializes the **whole** FSR from UTF-8 and immediately evicts it when the last active view lease ends. It is not a benchmark of CPython or a claim that the reference implementation currently evicts its cache. An active lease protects pointer lifetime; release does not identify the last future use.

For a length-n string and q independent calls doing k characters of work, immediate whole-view rebuilding can add O(q*n), whereas retaining the first representation can give O(n + q*k). This matters most when k is much smaller than n. If every successful call already scans or copies n characters, conversion can still add allocation and constant-factor cost, but this evidence does not show a new asymptotic cost.

All findings are static. Workload frequency, native-build activation, allocator cost and actual timings were not measured. UTF-8-aware rewrites, scalar decoding, range exports and persistent prepared owners can change the result; these counts do not establish that every identified operation must use a full FSR.

## Confirmed scalable partial examples

| Package | Verified operation and lifetime | Important restriction |
|---|---|---|
| [APSW](lifetime/apsw.md) | grapheme boundary or selected category range; local DATA/KIND in each registered call | Work depends on requested boundary/range, not the unread suffix |
| [RapidFuzz](lifetime/rapidfuzz.md) | native Prefix/Postfix metrics convert to local RF_String wrappers, then stop at a first mismatch | Standalone pair calls; batch/cached scorer scopes can retain preparation |
| [polyleven](lifetime/polyleven.md), [spaCy](lifetime/spacy.md) | threshold k=1..3 mBLeven can stop after bounded mismatches, after borrowing DATA | One engine family; length-gap rejection before DATA is excluded |
| [simplejson](lifetime/simplejson.md) | scanner(string, idx) returns a short null/true token with caller-selected start | Scanner caches configuration/memo, not the input's representation |
| [pyjson5](lifetime/pyjson5.md) | decode(s, some=True) returns the first value after a framing delimiter | Default complete-document decode has different work |
| [pyahocorasick](lifetime/pyahocorasick.md) | synchronous trie query can return on its first missing edge | Only kind4 borrows; kind1/2 already make full owned UCS4 copies |
| [lxml](lifetime/lxml.md) | compiled html.diff cleanup_delete extracts a short tag name from a long tag chunk, retaining chunk references | Compiled generated helper path; full document parse is not this example |

These inputs can be valid ordinary operations on a long non-ASCII str while leaving most codepoints unread. A trie no-match is a successful lookup result. The separate [Numba boundary](lifetime/numba.md) unboxes Unicode data into native ownership before a cheap operation, such as an integer-returning `ord(s[0])` compiled function. One live native owner can retain the lease across many native operations; those helpers are not independent acquisitions. Every compiled-signature cleanup sequence was not available in the retained corpus, so the boundary category stays separate.

## Full scans, invalid prefixes and persistent owners

Verified scoped users also include complete escaping/encoding, UTF-16 or layout conversion, native bulk metric work, writer copying and comparisons. For example, MarkupSafe, mutf8, Pillow fallback layout, Qt/SIP conversions and Levenshtein's own native median/set/sequence routines already consume or copy the input. No new big-O cost is inferred for those successful paths.

Backported fromisoformat, bitarray invalid-input handling and Oracle name checks have short-prefix/early-invalid evidence, kept outside the eight-case conservative successful-partial subset. Bitarray resizes output before validation, so its first-character rejection is not proof of O(1) total work. Oracle validators return a boolean but operate on an invalid-name case; their public call graph also has explicit uncertainty. Bulk `memcmp`/comparison behavior is not assumed to be a proven partial scan without its implementation.

The Levenshtein distance facade was not in the retained corpus. Bundled RapidFuzz metric headers alone do not prove that facade's entry/lifetime or justify counting another cheap engine. Verified Levenshtein-owned bulk operations remain yes. PyQt5/PyQt6 and SIP share a conversion/provider family; providers alone do not establish every external recipient's holder lifetime. Vendored MarkupSafe in vercel-runtime is byte-identical but native exposure is unproved, so it is possible rather than a second confirmed engine.

[Regex itself](lifetime/regex.md) has both lifetimes: standalone Pattern match/search creates and finalizes a local RE_State, while Scanner keeps state and subject storage until scanner destruction. A compiled Pattern's preparation is not a prepared view of every future subject.

Other persistent scopes include aiocsv's chunk parser, Numba native MemInfo/slices, pyahocorasick search iterators, RapidFuzz batch/generator scorers and PyObjC's cached NoCopy NSString. A lease can follow these actual owner lifetimes. Ending each small method call would be too early. Even a correctly retained scanner lease says nothing about a later unrelated caller's operation after that owner is destroyed.

ASCII-only aliases in ddtrace/pyroscope, length-one C/F configuration in tensorstore, ASCII geohash fastpaths, scalar ReadChar selectors, owned UCS4 copies, UTF-8 input paths and internally fresh output strings do not demonstrate the non-ASCII caller-reuse materialization problem. Their source-level distinctions are retained in the appendix.

## Complete scoped classification

**Yes** means a verified independently repeatable non-ASCII-capable scoped borrow/boundary path, not a prediction of inevitable slowdown. **Possible** preserves missing native exposure, runtime/template/copy, conditional source identity or recipient-lifetime uncertainty. **No** means the inspected paths do not establish this narrowly defined pattern; it is not proof that the whole package can never be affected.

"""

def escaped(value):
    if isinstance(value, list):
        value = '; '.join(value)
    return str(value).replace('|', '\\|').replace('\n', ' ')

def main():
    rows = json.loads((ROOT / 'data/reuse-inventory.json').read_text(encoding='utf-8'))
    snippets = [json.loads(line) for line in (ROOT / 'data/reuse-excerpts.jsonl').read_text(encoding='utf-8').splitlines()]
    others = [r for r in rows if r['package'] != 'regex']
    assert len(rows) == 53 and len(others) == 52
    assert collections.Counter(r['status'] for r in others) == {'yes': 28, 'possible': 11, 'no': 13}
    target = ROOT / 'lifetime'
    target.mkdir(exist_ok=True)
    appendix = ['# Per-package lifetime evidence', '', '[Summary and assumptions](../LIFETIME.md) · [Machine-readable inventory](../data/reuse-inventory.json)', '']
    summary = [INTRO, '| Package | Result | Inspected operation | Evidence |', '|---|---|---|---|']
    for r in rows:
        p = r['package']
        if p != 'regex':
            links = [url for e in r['evidence'] for url in e['verified_permalinks']]
            source = f'[permanent source]({links[0]})' if links else f"[frozen sdist]({r['evidence'][0]['sdist_url']})"
            summary.append(f"| [{p}](lifetime/README.md#{p}) | {r['status']} | {escaped(r['operation'])} | {source} |")
        appendix += [f'## {p}', '', f"Frozen version: **{r['version']}**. Result: **{r['status']}**" + (' (regex baseline; excluded from other-package counts).' if p == 'regex' else '.'), '', f"Operation: {escaped(r['operation'])}", '', r['basis'], '', f"Implementation family: `{r['implementation_family']}`.", '']
        details = r.get('details', {})
        for key in ['uncertainty', 'uncertainties', 'borrow_lifetime', 'lifetime', 'persistent_or_prepared_alternative', 'persistent_lease_or_owned_copy_alternative', 'persistent_state']:
            value = details.get(key)
            if value:
                appendix += [f"{key.replace('_',' ').capitalize()}: {escaped(value)}", '']
        for e in r['evidence']:
            ranges = ', '.join(f'{a}–{b}' for a,b in e['line_ranges'])
            appendix += [f"- `{e['archive_path']}`, lines {ranges}; member SHA256 `{e['source_sha256']}`."]
            if e['verified_permalinks']:
                appendix += [f'  [Verified source reference {i+1}]({u})' for i,u in enumerate(e['verified_permalinks'])]
            else:
                appendix += ['  No verified permanent repository link for these ranges.']
            appendix += [f"  [Frozen sdist]({e['sdist_url']}), archive SHA256 `{e['sdist_sha256']}`."]
        appendix.append('')
    summary += ['', 'See [the per-package appendix](lifetime/README.md) for every source range/hash, pointer lifetime, origin, uncertainty and prepared-owner distinction. The [machine-readable inventory](data/reuse-inventory.json) and [summary](data/reuse-summary.json) preserve the exact judgments. The evidence review rehashed 112 source files and checked 219 recorded ranges. Exact compact witnesses for the strong examples are linked above.', '', 'This study reused the frozen source corpus; no recrawl, build, install, package import or runtime experiment was performed. It analyzes a possible immediate-eviction policy, not a new API implementation.']
    (ROOT / 'LIFETIME.md').write_text('\n'.join(summary)+'\n', encoding='utf-8')
    (target / 'README.md').write_text('\n'.join(appendix)+'\n', encoding='utf-8')
    bypkg = collections.defaultdict(list)
    for s in snippets:
        bypkg[s['package']].append(s)
    for p, ss in bypkg.items():
        row = next(r for r in rows if r['package'] == p)
        out = [f'# {p}: lifetime witnesses', '', '[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#'+p+')', '', row['basis'], '', 'These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.', '']
        for s in ss:
            a,z = s['lines']
            out += [f"## {Path(s['archive_path']).name}: {a}–{z}", '', s['role'], '', f"Archive member: `{s['archive_path']}`", '', f"Member SHA256: `{s['source_sha256']}`", '', f"[Frozen sdist]({s['sdist_url']}); archive SHA256 `{s['sdist_sha256']}`.", '']
            out += [f"[Verified permanent source]({s['verified_permalink']})." if s['verified_permalink'] else 'No verified permanent repository link for this range; use the frozen archive and member hash above.', '', '```', s['code'], '```', '']
        (target / (p+'.md')).write_text('\n'.join(out), encoding='utf-8')
    print('Rendered 52-other-package table, 53-package appendix and', len(bypkg), 'exact witness pages.')

if __name__ == '__main__':
    main()
