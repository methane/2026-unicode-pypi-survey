# Unicode C API usage in 4,000 PyPI packages

Static source evidence for a proposed UTF-8 Python string representation. **Start with the reports below**; the source corpus and working files are not part of this repository. This is not a benchmark or a count of installed/executed code.

| Study | Main finding | Read next |
| --- | --- | --- |
| Construction, mutation and read access | Handwritten read scope:356 functions in42 packages;39 forward-pass,272 other-access,45 bulk/provider | [Report](REPORT.md) · [272 detailed cases](cases/README.md) |
| Repeated calls and view lifetime | Among52 other packages:28 confirmed reuse,11 possible,13 no;8 have strong successful-partial witnesses | [Lifetime report](LIFETIME.md) |
| Raw object layout | Eight packages have substantive Python3 full `PyUnicodeObject` layout dependencies; broader presence includes generated/legacy/vendor code | [Layout report](layout/REPORT.md) · [Evidence](layout/INDEX.md) |
| `PyUnicode_FromKindAndData` |32 packages;85 concrete constructor/emission sites,80 routed helper sites,3 test forwarders, counted separately | [Constructor report](fromkind/REPORT.md) · [Evidence](fromkind/INDEX.md) · [Qt/UTF16 detail](fromkind/QT-DETAIL.md) |

All studies use the same exact [4,000 names](data/top4000.txt): September2026 calendar-month download ranking, snapshot updated2026-10-01 12:41:32 UTC. Versions/sdists were selected on2026-10-02. Original write/read work was completed2026-10-02; lifetime/export refinement followed2026-10-03; layout and constructor follow-ups were completed2026-10-05 (local validation crossed into2026-10-06). This repository was consolidated2026-10-07. **3,788 selected sdists were scanned;211 releases had no sdist and one metadata request failed. Those212 outcomes are unknown, not zero usage.**

The units differ: source expressions/tokens, reviewed functions, package-level lifetime judgments, layout regions and constructor sites. Package sets, origins and call-path layers overlap; do not add the headline numbers. Build guards and generated/vendor copies are labelled. No package build, install or import code was executed.

[Methods](METHODS.md) · [Data definitions](DATA.md) · [Reproduction](scripts/README.md) · [Attribution](ATTRIBUTION.md) · [Packaging and publication](PUBLISHING.md) · [Validation](data/bundle-validation.json).

CSV/JSON evidence, frozen public source URLs/hashes and bounded code excerpts are included. Missing permanent GitHub source links are explicit. GitHub renders these Markdown files directly; **GitHub Pages is optional**. The [discussion draft](DISCUSSION-DRAFT.md) is a draft only. Preparing this repository did not publish it or post to Discourse.
