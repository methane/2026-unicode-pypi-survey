# Methods, scope and limitations

## Frozen sample and source selection

The population is the **first 4,000 rows, in order**, of the [immutable ranking snapshot](https://raw.githubusercontent.com/hugovk/top-pypi-packages/e6b5b398c1fcc783f593031f99bc2c772d64c6ef/top-pypi-packages.json), rather than a newly queried ranking. Its generator uses ClickHouse downloads for **2026-09-01 through 2026-09-30**, a calendar month. The snapshot update time is **2026-10-01 12:41:32 UTC**. A filename containing “30 days” is not the definition of the ranking window.

- Full snapshot SHA256: `a0458d45ec5c696a482b44f94cc0eb83f7d5f3167e53c066b2a66cbfffa98358`.
- Ordered `top4000.txt` SHA256: `d3710dafb8a01c8f1b413d6188d5b9ae3670069d1bd4cc3b4456d1e36a557199`.
- Package release metadata was fetched on 2026-10-02. Use the recorded versions and URLs in [source-metadata.jsonl](data/source-metadata.jsonl), not current latest releases, to replay this survey.

One non-yanked source distribution was selected from each package's then-current `info.version`; no historical-release fallback or wheel substitution was made. Selection was reconciled against the official first-current-sdist rule, with **zero URL differences** across this frozen sample. The official ranking and source-selection functions were replayed with frozen responses; this was an adapted function-level replay, not a fresh archive CLI invocation.

An earlier minified ranking alias had update time 12:40:51. Its first 4,000 names, order and download counts matched the corrected full snapshot. All headline provenance here uses the full snapshot above.

## Archive processing and coverage

Sdists were downloaded with bounded retries, resumable per-package outcomes, 10 workers and a ceiling of 10 request starts per second. Each archive was SHA256-verified before inspection. Archive members were streamed without extraction, executing code or following links. Unsafe paths and member limits were explicit, never silently treated as zero.

Final source recovery inspected **930,709 regular text candidates** and retained **131,701 native or Unicode-bearing files**, totaling **2,693,826,682 bytes** of source content in the working corpus. Retention was for later static review; those full files are not distributed in this publication subset.

The canonical non-code extension and binary-header filters exclude binary/dependency archives and other non-code resources. There was no total expanded-archive cap. The 128 MiB text-member safety bound was never reached. **No regular text source member was skipped for size.** Six source-looking link entries were resolved by reading four regular targets already inside the same archives, without following filesystem links; none contained read-family or layout indicators.

The original construction scan counted 1,095,068 regular archive members, including resources. One large bundled binary JAR in PySpark was explicitly omitted there; it contained no identified top-level source omission and is excluded by the canonical filter in final recovery. The two inspection totals have different definitions and must not be compared as source-file counts.

Final outcomes are **3,788 scanned, 211 without a current-release sdist, and one metadata 404** (`aaaaaaaaa`, rank 3,683). [coverage4000.csv](data/coverage4000.csv) keeps all 4,000 rows and distinguishes missing source from negative candidate observations. No sources fetched at build time, nested archives, binary extension internals or alternative releases are included.

## Construction and mutation counts

The primary symbols are `PyUnicode_New`, `PyUnicode_WRITE`, `PyUnicode_WriteChar`, `PyUnicode_CopyCharacters` and `PyUnicode_Fill`. Read-family symbols and public/private `PyUnicodeWriter_*` APIs are supporting context.

These tables count **physical source call expressions**, including separately identifiable forwarding-macro bodies. They exclude API declarations/definitions, the API's own macro definition, comments, string literals, non-code text and bare references. They are not runtime invocation counts, expanded template instances or unique algorithm counts. Direct calls and forwarding macros have separate columns in [write-counts.csv](data/write-counts.csv). Exact-file deduplication and origin columns are also retained.

Comment/literal masking, declaration recognition and origin labels use static heuristics. Source evidence is retained for independent review. API aliases or dynamically constructed FFI calls can evade an exact-symbol scan; the read follow-up traces known aliases and raw layouts, but does not claim exhaustive discovery of arbitrary dynamic code.

The canonical file policy follows the pinned [Victor Stinner `search_pypi_top.py`](https://github.com/vstinner/misc/blob/f1ba71b20c650f0e63920fe6f25292794c38f94a/cpython/search_pypi_top.py) and [download script](https://github.com/vstinner/misc/blob/f1ba71b20c650f0e63920fe6f25292794c38f94a/cpython/download_pypi_top.py). Default mode excludes files marked generated by Cython on their first line and `pythoncapi_compat.h`; Cython mode includes generated files but still excludes that compatibility header. All-origin counts retain compatibility context. Upstream script hashes and adaptations are in [reproducibility-provenance.json](data/reproducibility-provenance.json).

## Read-access semantic inventory

Read roots include `PyUnicode_DATA`, the 1/2/4-byte variants, `PyUnicode_KIND`, `PyUnicode_READ`, `PyUnicode_READ_CHAR`, and **`PyUnicode_ReadChar`**. Review follows helpers, pointer aliases, offsets, generic algorithms, available external recipients and direct layout bypasses. A read function can be included without a literal API call if its input pointer was traced to a Unicode representation.

The headline unit is **one source function identified by package, version, archive member path and function start line**. Primitive readers and genuine pointer providers have explicit roles and count once. Multiple DATA/KIND/READ expressions inside a function are not separate headline units. A function's contextual logical access sites are counted separately; they are not a frequency estimate. Different package/file copies remain separate source units, even if their bytes match.

Functions are assigned mutually exclusive A/B/C/U classes:

- **A:** one forward traversal from original index zero; possible early termination is flagged.
- **B:** caller-selected ranges/starts, scalar or arbitrary positions, reverse reads, lookaround, reset/backtracking, multiple passes, or mixed operations. Reasons distinguish fixed scalar access from true arbitrary indexing and monotonic continuation.
- **C:** genuine bulk copy/comparison, pointer provider or external recipient. Known callees are inspected; C is not shorthand for random access.
- **U:** unresolved access behavior. There are no U records in this documented inventory.

Pure forwarding, opaque-object comparison wrappers, metadata-only code, declarations, comments and output-only buffers are excluded. This avoids counting every call through a shared string helper as an independent read algorithm.

Scope predicates are literal, recorded in [scope-definitions.json](data/scope-definitions.json):

| Scope | Predicate |
|---|---|
| Canonical handwritten | `handwritten && scope_api == "fsr_read" && canonical_default_included` |
| Canonical native, all origins | `scope_api == "fsr_read" && canonical_default_included` |
| Primary representation, including generated | `scope_api == "fsr_read"` |
| All recorded scopes | All classified function records |

Canonical default selection excludes the Cython-marked files and compatibility header above. “Handwritten” is the reviewed origin flag; compiler/runtime, CPython-copy/backport and vendor/generic bodies are separately labeled. All-scopes supplements include legacy wchar/pointer APIs, caller-owned UCS4 copies, UTF-8 byte/cache consumers, remote layout reads, tests and write-API source operands.

The generated supplement inventories functions containing direct read-family tokens, aliases or traced helper accesses. It **does not enumerate every transitive caller** of general Cython Equals/GetItem/Substring helpers. Conditional old-Python, platform/SIMD and debug branches are source evidence, not proof of runtime activation.

## Evidence and limitations

All **272 canonical handwritten B functions**, with **551 logical sites**, are accessible from [the package case index](cases/README.md). Source excerpts are exact, with line ranges and explicit omissions. Large functions are represented by contextual windows, not copied wholesale. Available callee excerpts supplement the function's reason. Source archive URLs/hashes and member hashes remain present when no permanent repository link can be verified.

Across the full inventory, validation rehashed **336 function/callee source files** for **1,205 function records** and found zero hash, range, duplicate or missing-B-context errors. Candidate reconciliation found zero unmatched default/generated lexical sites or unmatched raw-layout files within the documented scan scope. This is an internal evidence-completeness check, not a claim that every dynamic dependency was discovered.

**744 function-level permanent links** were assigned. At file level, 227 files matched exact bytes, four differed only in newline encoding, and five had verified unchanged line blocks. Links into partially matching files are permitted only within those blocks. Another 173 candidate files have explicit unavailable/unverified-link outcomes; no latest-HEAD link is substituted.

Access class U=0 does not mean all lifetime risks are proved safe. Across all scopes, lifetime fields are: no 578; possible 208; yes 2; not assessed 416; not applicable 1. Most unassessed cases are generated. The [lifetime follow-up](LIFETIME.md) applies a different, narrower question to the 53-package canonical native scope.

No benchmark, build, package import, complete preprocessor reachability analysis, arbitrary dynamic FFI discovery or universal UTF-8 migration verdict was performed. Source branches and ABI contracts can identify design requirements; runtime frequency, allocation cost and performance need separate measurement.
