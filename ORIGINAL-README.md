# Unicode C API usage in the top 4,000 PyPI packages

This static source survey examines Unicode construction, mutation and read access to inform the [UTF-8 string representation discussion](https://discuss.python.org/t/pre-pep-utf-8-string-representation/109197). It uses one frozen release per package from an exact download-ranked sample. It is source evidence, not a benchmark or a migration verdict.

All **4,000 package outcomes** are recorded: **3,788 sdists scanned and SHA256-verified**, **211 releases without an sdist**, and **one unavailable PyPI metadata response**. Unavailable source is not a zero-hit observation.

| Read-access scope | Functions | A: forward pass | B: other access | C: bulk/provider | U: unresolved | Package union |
|---|---:|---:|---:|---:|---:|---:|
| Canonical handwritten | 356 | 39 | 272 | 45 | 0 | 42 |
| Canonical native, all origins | 560 | 62 | 428 | 70 | 0 | 53 |
| Primary representation, including generated files | 1,036 | 88 | 661 | 287 | 0 | 91 |
| All recorded scopes | 1,205 | 96 | 766 | 343 | 0 | 95 |

Package sets overlap. **B does not mean that an FSR cache is required**: it includes scalar reads, selected ranges and sequential cursor continuations. Generated/runtime/vendor copies are labeled and do not inflate the handwritten column. Scope predicates and count units are specified in [METHODS.md](METHODS.md).

Read the results in this order:

1. [Survey findings and construction/mutation counts](REPORT.md).
2. [Repeated calls, view lifetime and immediate eviction](LIFETIME.md).
3. [All 272 handwritten B cases, split by package](cases/README.md). Each case has exact contextual excerpts, source hashes, archive paths and verified permanent links where available.
4. [Methods, exclusions and limitations](METHODS.md), then [data definitions](DATA.md).
5. [Frozen-source scanning and reproduction instructions](scripts/README.md).

The ranking covers **September 2026 calendar-month downloads**, using the snapshot last updated **2026-10-01 12:41:32 UTC**, pinned to `hugovk/top-pypi-packages` commit [`e6b5b398c1fcc783f593031f99bc2c772d64c6ef`](https://github.com/hugovk/top-pypi-packages/tree/e6b5b398c1fcc783f593031f99bc2c772d64c6ef). The [exact ordered 4,000 names](data/top4000.txt), [download counts](data/top4000.csv), [full snapshot](data/ranking-snapshot.json) and [frozen source selections](data/source-metadata.jsonl) are included. Release metadata was acquired on 2026-10-02.

This directory is the publication subset: Markdown, scripts, compact data and contextual excerpts. It excludes full downloaded source trees, binary distributions, archive caches and the working evidence bundle. No package build, install or import code was executed. [ATTRIBUTION.md](ATTRIBUTION.md) describes source attribution and excerpt licensing boundaries.

A [short discussion draft](DISCUSSION-DRAFT.md) is provided separately. Preparing these files does not publish them.
