# PyPI Unicode struct-layout survey

An offline follow-up to the saved top-4,000 PyPI Unicode API survey, completed 2026-10-05.

[Read the report](REPORT.md), [methods and coverage](METHODS.md), and [package evidence index](INDEX.md).

The principal finding is **eight packages with substantive Python 3 `PyUnicodeObject` layout dependencies in project code or its generated implementation**: cython, ddtrace, lxml, multidict, numba, numpy, py-spy, and pyobjc-core. Cython GDB and py-spy are tooling consumers, so this is not a count of eight extension modules. Other packages directly use `PyASCIIObject` / `PyCompactUnicodeObject`.

The full source-presence union is 67 packages across all three structs, including legacy branches, generated copies, compatibility implementations, tests and copied CPython. Do not interpret that union as independently written algorithms or executed installations.

Deliverables: [cases CSV](data/cases.csv), [cases JSON](data/cases.json), [counts CSV](data/counts.csv), [4,000-package coverage CSV](data/coverage4000.csv), [exhaustive token audit](data/token-audit.csv), [Japanese summary](SUMMARY-JA.md). Existing publication files were preserved; this report is a separate directory. No build, install, import, repository change, commit, push or publication was performed.

[Repository entry point](../README.md). Full working ledgers and source corpus remain local.
