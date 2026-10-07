Run these commands from the publication root with Python 3.10 or later. The scanner uses only the standard library. It never installs, builds, imports, or executes package code. Without `--download`, it prints a plan and makes no network requests.

```sh
python3 scripts/scan_sdists.py --limit 25
python3 scripts/test_scanner.py
python3 scripts/verify_frozen_inputs.py
```

An explicitly requested small source scan:

```sh
python3 scripts/scan_sdists.py --download --limit 25 --workers 2 --request-interval 0.25 --output scan-output
```

To reproduce the lexical survey for all frozen ranks:

```sh
python3 scripts/scan_sdists.py --download --limit 4000 --workers 2 --request-interval 0.25 --output scan-output
```

Rerun the same command to resume at package checkpoints. Completed and failed results are preserved; use `--retry --packages regex` to retry/rescan specific packages, or select a fresh output directory. Incomplete HTTP downloads are discarded, while complete cached archives are hash-verified before reuse. This is package-level resume, not HTTP byte-range resume. `--start-rank 1001 --limit 100` selects ranks 1001–1100. `--packages` filters the selected rank interval. `--attempts` controls transient HTTP request retries. All workers share the request-spacing limit. Keep ordinary concurrency modest.

Outputs include `results/<package>.json`, `coverage.csv`, `coverage-exceptions.json`, `hits.jsonl`, `candidate-files.jsonl`, and `summary.json`. `--aggregate-only --output scan-output` rebuilds the combined outputs without downloading. The output is portable: archive member paths and content hashes identify evidence; it contains no host-specific source paths. Choose an output directory for one frozen metadata/settings combination; incompatible resume settings are rejected.

The default saves metadata and lexical hits, with **zero third-party source files retained**. Sources are not shipped in this publication. To obtain exact bytes for additional manual review, explicitly request one of:

```sh
python3 scripts/scan_sdists.py --download --packages regex --retain-source candidates --output regex-review
python3 scripts/scan_sdists.py --download --packages numba oracledb --retain-source native --output derived-review
```

`candidates` retains files with Unicode C API/type indicators. `native` retains all supported native/Cython sources plus Unicode-bearing text, which helps trace accessors into files without direct API tokens. Files are saved by SHA256 under `sources/`, never by archive-controlled paths. Archives are deleted after each attempt by default; `--keep-archives` is an explicit disk-space opt-in. The full 4,000-package scan downloads approximately the declared byte total printed by the plan; it is not a compact operation despite the compact publication.

The frozen inputs are `data/source-metadata.jsonl` (exact 4,000 rows), `data/top4000.txt`, `data/top4000.csv`, `data/snapshot-provenance.json`, and `data/reproducibility-provenance.json`. Rankings are the first 4,000 rows from hugovk/top-pypi-packages commit `e6b5b398c1fcc783f593031f99bc2c772d64c6ef`, updated 2026-10-01 12:41:32 UTC, covering September 1–30, 2026. Version and current-release selection were frozen when PyPI metadata was fetched, not when this script is rerun. The metadata includes each selected URL, SHA256, and size. The original selector was checked against Victor Stinner's pinned `find_url` for all 4,000 names; there were no URL differences. No live metadata refresh or historical-version fallback occurs here.

Coverage is explicit: the frozen original survey had 3,787 fully scanned archives, one partial archive, 211 packages without a current sdist, and one unavailable PyPI metadata response. Expanded source recovery scanned all 3,788 selected sdists. The original partial member was a 71,683,718-byte RocksDB JAR bundled in PySpark, excluded by the canonical filename filter. Both original and expanded coverage/omissions remain separate fields. Unavailable or failed packages never mean zero API use.

The default and `canonical_cython` count tables follow the file-selection behavior of [Victor Stinner's pinned search script](https://github.com/vstinner/misc/blob/f1ba71b20c650f0e63920fe6f25292794c38f94a/cpython/search_pypi_top.py): exact filename suffix exclusions, first-256-byte binary detection, exact `pythoncapi_compat.h` basename exclusion, and Cython-generated first-line detection. `canonical_default` excludes those Cython files; `canonical_cython` includes them while still excluding the compatibility header. The `all` table includes retained generated/compatibility token candidates. Provenance categories such as vendor/generated are independent from this file filter, and do not establish handwritten use by themselves. Upstream scripts are linked and attributed, not redistributed or run by this reproduction.

Archive safety differs deliberately from upstream decompression: only safe regular members are read, links are recorded and never followed, and nested archives/binary files are excluded. Tar archives are streamed, ZIP members are read directly, and no member is extracted. There is no arbitrary total-expanded-archive cutoff. A candidate text member above `--max-member-mib` (default 128 MiB) is enumerated with its size and reason, and makes coverage partial. The recovery's 128 MiB limit never omitted a member in the observed corpus; this is not permission to silently omit a large future source. Increase the limit explicitly and retry if needed. Downloads must match both frozen archive SHA256 and exact declared size. Only public HTTPS `files.pythonhosted.org` source URLs and redirects are permitted; binary wheels are never requested.

`original_write` counts use the original five construction/mutation APIs, DATA/KIND/READ supporting tokens, and public/private `PyUnicodeWriter_*` names. `expanded` additionally finds `PyUnicode_ReadChar`, legacy Unicode buffer APIs, UCS4-copy APIs, and Cython accessor aliases. Raw-layout type names (`PyASCIIObject`, `PyCompactUnicodeObject`, `PyUnicodeObject`) create candidates, not presumed reads. Raw token counts include comments, definitions, declarations, references, and macro bodies. The offset-preserving lexical masker separates those from `call_like` and `macro_body_call`; these are **heuristics, not verified runtime calls**. Cython, Rust, generated headers, macros, dead conditional code, and indirect aliases can require manual correction. Occurrences are per package/archive member/byte offset; identical vendor copies remain separate unless a separate analysis deduplicates them. A matching line can contain several tokens, so token counts do not equal upstream raw matching-line counts.

The scanner copies the original analysis's lexical mask/classification/provenance rules into `static_lexical.py` and adapts acquisition/recovery to frozen metadata. Changes are recorded in `reproducibility-provenance.json`: combined token scope, optional rather than automatic source retention, and exact upstream `.js.map` filtering instead of the original recovery's broader `.map` suffix exclusion. The script does not claim to re-create manual semantic A/B/C/U classifications, handwritten/vendor attribution refinements, helper closure, or lifetime analysis automatically. Those results require exact source inspection, including consumers without a direct API name. Saved metadata and public source URLs/hashes make that inspection repeatable.

The offline test harness uses only synthetic tar/ZIP fixtures. It checks traversal/link rejection, explicit size omissions, binary/document filters, Cython/compatibility selection, comments versus calls, optional source hash retention, cached archive verification, and unavailable-package checkpoint resume. It makes no network requests and executes no third-party package code.

The reviewed Markdown can be regenerated offline without downloading sources:

```sh
python3 scripts/render_cases.py
python3 scripts/render_lifetime.py
python3 scripts/validate_publication.py
```

The renderers use the published reviewed JSON/exact-excerpt data. Validation checks source-function counts, the272/551 case/site coverage, the52-package lifetime denominator, code fences, relative links and host-path omissions. This does not replace fetching/hash-verifying a source member for a new independent semantic review.
