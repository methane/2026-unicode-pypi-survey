# Methods and reproduction

## Frozen input and safe processing

This analysis reuses the existing static sdist recovery in `unicode-pypi-survey/read-access-analysis`; it performs no new downloads, extraction, package builds, installations, imports, or code execution. Only our analysis scripts execute. Archive/source SHA-256 values come from the frozen recovery and are rechecked against retained files. Existing repositories and the prior `unicode-pypi-survey/publication` are preserved.

The underlying acquisition chose the exact first 4,000 ranked package names, then one non-yanked sdist from the release selected at metadata acquisition. There is no historical-release fallback. Resume/status records enumerate every package, including unavailable source. Source extraction inspected only safe-path regular archive members and did not follow archive links or unpack nested archives. A 128 MiB eligible-text member guard existed; no source member hit it. Ignored-suffix and binary-text heuristics are listed in the independent verification record.

There were 244 recorded symlinks across 43 packages. The earlier read-access audit separately resolved six source-looking links to four regular in-archive targets, all without Unicode indicators. Other symlinks remain unfollowed; a target available under a retained regular member is covered under that member. This is not a claim that every symlink's contents were scanned.

## Candidate inventory and semantic review

`inventory.py` reads all 131,701 retained source-member records and searches word-bounded `PyUnicodeObject`, `PyASCIIObject`, `PyCompactUnicodeObject`, plus `AsciiObject`/`CompactUnicodeObject`/`UnicodeObject` alias roots. It hashes candidates and preserves physical LF line/character offsets; CRLF bytes are preserved. A regex lexer masks comments and literals without changing offsets. This lexer is only an inventory aid.

Owned reviews examine all 309 candidate files, generated runtime families, local aliases, consumers of Rust layouts, and supporting source files. Actual cases include field read/write, header-size/pointer arithmetic, embedding, subtype size/offset, remote-layout decoding, custom metadata initialization and compatibility implementation. Bare declarations, imports, type aliases, comments/docs and API-only typed casts are separate. GDB string-key field accesses and generator strings are reviewed semantically despite lexical literal status. Core struct definitions remain definition-only until a consumer is traced. Output writes are included, even if the previous read survey excluded them.

Generated Cython helpers are reviewed by implementation family and expanded to each source file/region. Conditional guards remain on individual tokens. This controls duplicated evidence but does not prove which helper is emitted/compiled/called for a specific build. Frozendict reference and adopted variants, compatibility headers, copied CPython, bundled FFI definitions, tests and project source remain separate.

Package counts are distinct unions, not sums. A layout record is a source region or family/file record, not a token, call or execution count. Review family IDs group related implementations at differing granularities; they are not a count of independent algorithms. Exact token counts are available only as the audit denominator.

## Immutable evidence links

`publish.py` keys the saved 409-file upstream verification map by package, archive path and source SHA. Identity links require exact bytes or lines differing only in newline encoding. Partial matching-block links are emitted only if the entire requested excerpt lies inside a verified block. The output never invents a HEAD/latest link. Cached remote bytes are independently rehashed, and mapped line spans are checked. Unverified ranges retain immutable PyPI archive URL and archive/member hashes. No network refresh is asserted.

## Reproduction from this repository

Run the portable [root scanner](../scripts/README.md) with the shared frozen metadata if you independently choose to fetch the sources. No download is required to read or validate these results. Use `--retain-source native` to retain the native/Unicode-bearing source needed for alias/producer review. `scripts/index_followup_sources.py` inventories layout and constructor candidates from that output.

The published case ledger preserves all1,137 semantic records, source identities, original reviewed spans and bounded exact excerpts. `scripts/verify_bundle.py` checks its counts and the consolidated repository offline. Recreating semantic judgments requires source review; the acquisition scanner and token inventory are not a compiler or an automatic substitute for those judgments. Nonportable working-corpus publishing/review scripts and redundant raw owner ledgers stay local.

## Scope files

- `../data/top4000.txt`: exact names in ranked order; SHA-256 `d3710dafb8a01c8f1b413d6188d5b9ae3670069d1bd4cc3b4456d1e36a557199`.
- `../data/ranking-snapshot.json`: pinned public ranking bytes; SHA-256 `a0458d45ec5c696a482b44f94cc0eb83f7d5f3167e53c066b2a66cbfffa98358`.
- `../data/snapshot-provenance.json`: snapshot commit, date, window and acquisition policy.
- `data/coverage4000.csv`: package-by-package availability and layout classification; unknown-source rows remain unknown.
- `data/cases.csv` / `.json`: actual/non-direct records and original reviewed spans with bounded exact excerpts.
- `data/token-audit.csv`: exhaustive type-name dispositions plus traced supporting alias tokens.
- `data/file-audit.json`: candidate and supporting file review records.
- `data/counts.csv` / `.json`: reproducible distinct package/file and record totals by struct/origin.

## Public excerpt policy

The consolidated repository keeps the semantic populations unchanged but trims the follow-up JSON/CSV excerpts to at most24 lines per original snippet. Longer snippets publish the first14 and last8 lines as separate exact spans, with omitted intervals and original bounds recorded. Individual physical lines over4,000 characters are explicitly omitted. Host/local storage fields are removed. Immutable source URLs and full-member/archive hashes remain; missing GitHub mappings remain explicit. Package Markdown pages retain their already short exact excerpts. Shared ranking/acquisition data appear only at the repository root.
