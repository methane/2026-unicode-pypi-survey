# Data and counting definitions

All paths below are relative to this publication directory. JSONL is one JSON record per line; CSV has a header. SHA256 hashes refer to source bytes, not normalized displayed excerpts.

| File | Contents |
|---|---|
| `data/top4000.txt`, `top4000.csv` | Exact ranked names/order and download counts |
| `data/ranking-snapshot.json`, `snapshot-provenance.json` | Full immutable ranking and date/window/hash provenance |
| `data/source-metadata.jsonl` | All 4,000 frozen release/URL/hash selections and coverage exceptions |
| `data/coverage4000.csv` | Final per-package source coverage and semantic counts, with missing-not-zero interpretation |
| `data/write-counts.csv` | Per-API source expressions, direct calls, forwarding macros, raw tokens and origin/filter splits |
| `data/write-packages-per-api.csv` | Package names/versions per selected API |
| `data/construction-api-hits.jsonl` | Physical source locations, lexical disposition, bounded call-expression context and source hashes |
| `data/functions.jsonl` | All 1,205 reviewed read function units and logical sites, classes, origins, source hashes and permanent-link status |
| `data/canonical-handwritten-B-cases.jsonl` | All 272 public B cases with bounded exact source/callee contexts and excerpt omissions |
| `data/classification-counts.json` | Scope/class function counts, package sets/intersections and early-exit flags |
| `data/scope-origin-counts.json`, `scope-definitions.json` | Original scope/origin breakdowns and literal headline scope predicates |
| `data/canonical-handwritten-B-subtypes.json` | Overlapping B subtype tags |
| `data/package-summary.csv` | Package-level semantic inventory and reconciliation counts |
| `data/read-api-site-audit.csv` | Lexical token locations and reviewed/excluded disposition; not API runtime counts |
| `data/exclusions.jsonl` | Explicit definition/output/forwarding/fixture and other semantic exclusions |
| `data/candidate-audit-summary.json` | Candidate reconciliation totals and unmatched-site/layout checks |
| `data/case-validation.json` | Exact-excerpt and 551-site coverage checks for the public case pages |
| `data/reuse-inventory.json`, `reuse-summary.json`, `reuse-excerpts.jsonl` | Narrow repeated-call/lifetime judgments, separate denominator and exact compact witnesses |
| `data/reproducibility-provenance.json` | Upstream filter references and original/reproduction script provenance |
| `data/publication-validation.json`, `publication-manifest.json` | Offline publication checks and relative-path content hashes |

The lexical construction dataset includes non-code and excluded hit metadata to make disposition reviewable. Publication omits their source snippets, including irrelevant binary-document payloads, while retaining locations/hashes and all occurrence rows. Long physical call lines above4,000 characters have an explicit context-omission reason; source scanning/counts are unchanged. Do not count every row as a call. Read function counts use the unique key `package|version|archive_path|function_start`; count one function once even when it has many DATA/KIND/READ expressions. Package category sets and subtype flags overlap.

The public B JSON stores trimmed contextual excerpts. Every recorded logical site has exact contextual evidence, but a wide algorithm-level span does not mean that every line in that span is reproduced. Full function ranges and source provenance permit further source inspection. See [the case index](cases/README.md) for excerpt policy.

The semantic judgments are reviewed data. Source scanning and hash/context checks are automated; rerunning the scanner does not automatically recreate manual function classifications or prove runtime exposure. Original analysis records are preserved separately; this public subset removes private working-file paths and workflow metadata.
