# Publish this one directory

Publish the contents of this `publication/` directory as the repository root. Start at [README.md](README.md). Keep the other `unicode-pypi-survey/` directories local: retained sources, metadata caches, results/checkpoints, downloaded archives, full raw review ledgers, original separate follow-up publications and work logs.

The root files cover construction/read/lifetime; `layout/` and `fromkind/` contain the two follow-ups. Package evidence is split into small Markdown pages so readers need not download a large aggregate. Shared ranking and frozen source selections live in root `data/`; follow-up CSV/JSON preserve their separate counting units. Original README content is preserved verbatim as [ORIGINAL-README.md](ORIGINAL-README.md). Existing original-study files and both source follow-up publication directories were preserved. The historical `data/publication-manifest.json` describes the original pre-consolidation snapshot; substitute `ORIGINAL-README.md` for its `README.md` entry when checking that snapshot. The current consolidated artifact list is [PUBLICATION-MANIFEST.json](PUBLICATION-MANIFEST.json).

To verify without downloading anything, run from this directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_bundle.py
```

Create an empty GitHub repository, then run the following yourself from this directory, replacing YOUR-USER and YOUR-REPO. These steps have not been run by the survey:

```sh
git init
git add .
git commit -m "Publish static PyPI Unicode API survey"
git branch -M main
git remote add origin https://github.com/YOUR-USER/YOUR-REPO.git
git push -u origin main
```

GitHub Pages is unnecessary. After reviewing the repository online, link its README from discuss.python.org. Prefer a commit-specific report link for stable evidence, for example `https://github.com/YOUR-USER/YOUR-REPO/blob/COMMIT/README.md`. Include the ranking month, source availability and counting-unit caveats in any discussion post. The existing discussion draft predates the two follow-ups; update it with the new README links before posting. Nothing here grants permission to post or push automatically.

The bundle does not claim a single license for third-party source excerpts. Existing attribution notices, original package URLs/hashes and source-license boundaries are retained. Follow-up excerpts are limited to24 lines per original snippet, with explicit omitted spans; Markdown excerpts were already short. Inspect the final staged files before pushing; cache/output directories are ignored. Preparation has not installed tools, executed package code, deleted working evidence, committed or published anything.
