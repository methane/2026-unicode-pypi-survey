# Methods, data dictionary and reproduction

## Frozen selection

`../data/top4000.txt` is the exact first 4,000 names, in order, from the shared `../data/ranking-snapshot.json`. `../data/snapshot-provenance.json` is the original ranking/acquisition provenance; its original primary-symbol list concerns the earlier construction survey. The current follow-up target is `PyUnicode_FromKindAndData`, prefix/suffix variants and reviewed local wrappers. `analysis-provenance.json` records that distinction. Versions, archive hashes and URLs come from the original saved recovery metadata and remain unchanged. Source-unavailable outcomes have no zero-use interpretation.

## Source retention and safe acquisition

The preceding survey fetched metadata and one selected sdist per package with bounded concurrency/retries and resumable per-package outcomes, then read regular members without extracting or executing package code. Path traversal, links and special members were not followed. Archives were cleaned up after scanning. This follow-up is entirely offline and reads the saved evidence corpus.

The recovery retained native suffixes `.c/.h/.cpp/.cxx/.hpp/.inc/.pxd/.pyx/.pxi/.rs/.go/.m/.mm/.swift/.i` and templates such as `.c.src/.h.in`, plus eligible nonnative text with Unicode indicators. `.sip` candidates were retained by the indicator rule. Nonnative files without indicators, ignored docs/data/web formats, binaries and nested archives are outside scope. The exact original scan/recovery scripts and coverage records remain in the adjacent earlier survey directories. This consolidated repository ships the portable root scanner and a candidate index; the nonportable original review programs stay local.

The recovery inspected 930,709 regular text-eligible members and retained 131,701 logical source records. Its 128-MiB eligible-text guard omitted zero eligible regular sources. The original PySpark RocksDB JAR omission, all 244 untraversed symlinks and every unavailable package are enumerated in the saved verification data. This is a bounded text/native-source survey, not a proof about every archive member or wheel-only distribution.

## Inventory and review

`inventory.py` visits every saved catalog record, byte-prefilters `FromKindAndData`, checks candidate SHA-256, and inventories every identifier matching `(?<!\w)[A-Za-z_]\w*FromKindAndData\w*(?!\w)`. The lexer masks strings/comments while retaining offsets and extracts balanced call-like arguments. That heuristic is a candidate generator: manual review corrects `.c.src` classification, source-echo comments, declarations, linker attributes, f2py emission, Numba LLVM emission, macro dispatch and compile guards.

Line numbers are physical LF lines (`decoded_text.split('\n')`), retaining CR if present. Offsets in the raw inventory are UTF8-decoded character offsets with replacement, not byte offsets. The independent candidate verifier recomputes all token lines/offsets and hashes. Manual review distinguishes actual executable API bodies from definitions/declarations that merely mention the name. Generated source-echo comments are not calls. The compiler/limited-API/test guards are preserved; no build or execution was performed to evaluate them.

The known-alias pass revisits all 131,701 retained source records. It searches reviewed provider/function/macro/JIT roots and their package-scoped callers, classifies the 184 reference candidates, excludes prototypes/name collisions/non-constructor branches, and records first-hop/transitively confirmed routes in the five review files. Arbitrarily computed names, unretained wrappers and whole-program transitive reachability remain outside this method. Forty-three additional general NumPy API/macro/reader traces are supplied separately with conditions and exclusions.

## Counting and schema

`data/sites.json` and `data/sites.csv` contain **194 semantic evidence records**, coincidentally the same number as the **194 raw named tokens**; these are different populations. Records include wrapper-only locations, a provider overview, derived executable fault-body rows and non-use context. Never join them by row number.

- `case_id` or `id` identifies an owner-reviewed case; `evidence_id` identifies its published row. `family_id` allows repeated-runtime-family analysis.
- `direct_use` denotes an API expression or C/LLVM emission, including the separately labelled executable fault forwarders. `static_use` additionally includes reviewed routed wrapper invocations whose constructor branch is possible. Neither implies runtime execution.
- `usage_form` separates concrete expressions, C templates, macro dispatch, C emission, LLVM emission, wrapper calls, fault forwarding, and non-use/provider context. `original_usage_form` preserves the original review label.
- The 85 concrete sites exclude the 3 generic fault forwarders. The 80 wrapper sites are counted at their own source locations, not as extra constructor implementations. Five known constructor-unreachable native wrapper cases remain negative. Template instantiation counts and dynamically compiled instructions are not multiplied.
- `origin` preserves the review classification; `report_group` aggregates handwritten, generated Cython, Cython template, code generator, vendor/compatibility, other generation and test instrumentation. `original_kind_class` preserves labels before width normalization.
- `kind_expression`, `buffer_expression`, `length_expression` and their classes/units describe the input at that site. `buffer_provenance`/`buffer_details` describe immediate storage. `upstream_fsr_dependency` describes upstream coupling where traced; fallback `see_evidence` is explicitly not a claim of independence. The original `upstream_unicode_coupling` field, where supplied, is also retained in JSON.
- `confirmed_evidence` and `inference` separate source observations from migration/design consequences. `constructor_reachable`, activation notes and implementation case IDs preserve route conditions.
- `start/end` are the reviewed main region. `actual_site_lines` or original `actual_api_site_lines` identify more precise API starts where supplied. `snippets[].published_excerpts` carry their own source package/path/SHA and LF range; supporting snippets may be in another file. CSV serializes lists/dictionaries as JSON strings.
- `source_sha256` hashes exact member bytes. `sdist_sha256`/`sdist_url` identify the selected immutable source distribution. Evidence paths are relative to the parent `unicode-pypi-survey/` directory.
- `verified_permalink` is null unless the saved strict map proves the entire requested main range. Snippets may have shorter verified ranges. A link exists only for an immutable GitHub commit with exact bytes, newline-only line identity, or a wholly contained matching-block mapping. Source-unmapped entries retain their sdist/member hashes and URL.

`data/token-audit.json` reconciles every raw token by package/path/symbol/LF line/character offset, independently of semantic records. `data/file-audit.json` covers every 67 named candidate files and supplementary closure evidence. `coverage4000.csv` includes every ranked package, version, acquisition status, retained-record counts and target disposition. No-candidate absence means no detected named/known-alias use in retained scope. `counts.csv` aggregates only `static_use`; use `usage_form` to select a population rather than adding overlapping group rows.

## Reproduction from this repository

The shared [scanner and instructions](../scripts/README.md) reproduce frozen acquisition with standard-library Python, if you explicitly choose to fetch sources. Use `--retain-source native`; the scanner's broad retention captures files with this API even though its original lexical-count table does not count FromKindAndData. `scripts/index_followup_sources.py` separately inventories this symbol and layout names from retained scan output. It does not infer actual calls or buffer provenance.

All194 semantic records are published with original reviewed ranges, bounded exact excerpts and explicit omissions. The85 concrete constructor/emission sites,80 routed sites and3 executable fault forwarders remain unchanged. `scripts/verify_bundle.py` validates the published counts/links/manifest offline. Reproducing semantic classification and arbitrary alias closure still requires manual source review. Original local review programs, raw owner ledgers and source caches remain local; they are not presented as portable scripts.

## Verification

The original full-corpus hash audit checked 128,609 physical evidence files. The independent follow-up coverage verifier checks unchanged fingerprints before reusing that prior audit, then rereads all 67 candidates and validates all 194 raw token ranges. Publication validation checks every site/source/snippet hash and LF slice, counts and CSV/JSON reconciliation, strict link mappings, local Markdown targets and the unchanged manifests of both earlier publications. The consolidated [manifest](../PUBLICATION-MANIFEST.json) records the final selected artifacts; [bundle validation](../data/bundle-validation.json) checks portable links, counts, privacy and excerpt bounds.
## Public excerpt policy

The consolidated repository keeps the semantic populations unchanged but trims the follow-up JSON/CSV excerpts to at most24 lines per original snippet. Longer snippets publish the first14 and last8 lines as separate exact spans, with omitted intervals and original bounds recorded. Individual physical lines over4,000 characters are explicitly omitted. Host/local storage fields are removed. Immutable source URLs and full-member/archive hashes remain; missing GitHub mappings remain explicit. Package Markdown pages retain their already short exact excerpts. Shared ranking/acquisition data appear only at the repository root.
