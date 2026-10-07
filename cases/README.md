# Non-simple Unicode read access: case index

This collection contains **272 function-level B cases in 27 packages** from the frozen top-4,000 PyPI source survey. These are the canonical-default, handwritten cases involving the FSR read interface; generated code, compatibility definitions, vendor copies and the broader legacy/raw-layout groups are outside this collection.

A means a single forward pass from position zero through the full string, with early exit recorded separately. B includes other access patterns: a scalar check, a supplied range, continuation from a nonzero position, backward traversal, lookahead, backtracking or multiple passes. Consequently, **B is not a count of functions that necessarily require random access or an FSR view**. Function records are counted once; subtypes can overlap.

Python codepoints include surrogate codepoints. Here, “scalar check” describes a one-character operation, not a claim that the input excludes surrogates. Codepoint offsets must not be substituted with UTF-8 byte offsets without considering each function’s semantics.

The pages contain source excerpts, source provenance, immutable links where verified, and relevant callee excerpts. Source text is reproduced unchanged from the recorded excerpt data. A missing permalink does not mean the source is missing: the sdist URL, archive hash and member hash identify it.

**Excerpting policy:** Keep source regions of 35 lines or fewer. For longer regions, retain bounded windows around recorded reads and relevant entry, loop-bound and reset evidence. Explicit omitted line ranges accompany disjoint excerpts. Every one of the 551 recorded semantic access-site records has at least one contextual window; this is not a claim to reproduce every statement in a broad algorithm span. Quoted code contains no inserted ellipsis.

| Package | Version | B functions |
|---|---|---:|
| [aiocsv](aiocsv.md) | 1.4.1 | 2 |
| [apsw](apsw.md) | 3.53.4.0 | 18 |
| [biopython](biopython.md) | 1.88 | 5 |
| [bitarray](bitarray.md) | 3.11.0 | 1 |
| [cffi](cffi.md) | 2.1.1 | 7 |
| [duckdb](duckdb.md) | 1.5.6 | 2 |
| [jpype1](jpype1.md) | 1.7.1 | 22 |
| [levenshtein](levenshtein.md) | 0.27.5 | 7 |
| [markupsafe](markupsafe.md) | 3.0.3 | 3 |
| [msgspec](msgspec.md) | 0.22.0 | 1 |
| [multidict](multidict.md) | 7.0.0 | 2 |
| [mutf8](mutf8.md) | 1.1.0 | 1 |
| [numba](numba.md) | 0.68.0 | 31 |
| [numpy](numpy.md) | 2.5.3 | 4 |
| [oracledb](oracledb.md) | 26.0.1 | 24 |
| [polyleven](polyleven.md) | 0.11.0 | 4 |
| [pyahocorasick](pyahocorasick.md) | 2.3.1 | 5 |
| [pybase64](pybase64.md) | 1.5.0 | 2 |
| [pygame](pygame.md) | 2.6.1 | 2 |
| [pygeohash](pygeohash.md) | 3.5.1 | 2 |
| [pyjson5](pyjson5.md) | 2.0.1 | 20 |
| [pyobjc-core](pyobjc-core.md) | 12.2.2 | 2 |
| [regex](regex.md) | 2026.9.29 | 85 |
| [simplejson](simplejson.md) | 4.1.2 | 11 |
| [tensorstore](tensorstore.md) | 0.1.85 | 1 |
| [wcwidth](wcwidth.md) | 0.9.1 | 1 |
| [yarl](yarl.md) | 1.25.1 | 7 |

[Machine-readable case records](../data/canonical-handwritten-B-cases.jsonl). Pages can be rebuilt with [render_cases.py](../scripts/render_cases.py) using only that public JSONL file.
