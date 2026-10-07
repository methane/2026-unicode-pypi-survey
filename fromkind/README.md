# PyUnicode_FromKindAndData survey publication

The [English report](REPORT.md) covers a frozen download-ranked top-4,000 PyPI corpus. It confirms 85 concrete constructor/emission sites in 32 packages, 80 routed helper sites and 3 executable fault forwarders. These categories overlap at the call-path level; source-site counts are not runtime counts.

- [Methods and reproduction](METHODS.md)
- [日本語要約](SUMMARY-JA.md)
- [Qt and UTF16: exact call paths](QT-DETAIL.md)
- [Complete sites: CSV](data/sites.csv) · [JSON](data/sites.json)
- [All 4,000 coverage outcomes](data/coverage4000.csv) · [exact ordered names](../data/top4000.txt)
- [Counts](data/counts.csv) · [raw token dispositions](data/token-audit.json) · [source file audit](data/file-audit.json)
- [Supplementary NumPy traces](data/supplementary-wrapper-traces.json)
- [Publication validation](../data/bundle-validation.json) · [artifact SHA-256 manifest](../PUBLICATION-MANIFEST.json)
- [Package evidence index](INDEX.md)

211 packages lack a selected-release sdist and one has unavailable metadata: all 212 remain unknown. No package build/install/import code was executed, no binary wheels were used, and no artifacts were published externally. Source evidence remains in the adjacent saved survey corpus; the publication contains excerpts and hashes, not a second full source corpus.

[Repository entry point](../README.md). Full working ledgers and source corpus remain local.
