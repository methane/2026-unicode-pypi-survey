# Findings

## Construction and mutation APIs

The sample contains 3,788 available frozen sdists out of 4,000 ranked packages. Missing sources are separate outcomes. The first table reports source call expressions, not runtime calls; forwarding macros are included and separately tabulated in the [CSV](data/write-counts.csv).

| API | Canonical-default packages / expressions | All-origin packages / expressions | Handwritten-candidate packages / expressions |
|---|---:|---:|---:|
| `PyUnicode_New` | 29 / 89 | 64 / 267 | 24 / 73 |
| `PyUnicode_WRITE` | 9 / 25 | 58 / 230 | 6 / 22 |
| `PyUnicode_WriteChar` | 5 / 9 | 5 / 9 | 4 / 8 |
| `PyUnicode_CopyCharacters` | 6 / 11 | 38 / 109 | 4 / 7 |
| `PyUnicode_Fill` | 0 / 0 | 0 / 0 | 0 / 0 |

Canonical-default primary APIs affect a union of **30 packages**; the all-origin primary union is **78**. Zero `Fill` calls is an observation for the available releases and selected-symbol scan, not proof of absence across PyPI. [write-packages-per-api.csv](data/write-packages-per-api.csv) lists every relevant package/version; [construction-api-hits.jsonl](data/construction-api-hits.jsonl) distinguishes calls, macro bodies, definitions and other occurrences. Public and private Writer APIs are separately recorded in the tables rather than added to the primary totals.

Generated Cython and compatibility copies explain much of the difference between default and all-origin columns. Handwritten-candidate labels in this lexical phase are heuristic and differ from the manually reviewed handwritten read-function inventory below.

## Read patterns

| Scope | Function total | A | B | C | U | Package union |
|---|---:|---:|---:|---:|---:|---:|
| Canonical handwritten | 356 | 39 | 272 | 45 | 0 | 42 |
| Canonical native, all origins | 560 | 62 | 428 | 70 | 0 | 53 |
| Primary representation including generated | 1,036 | 88 | 661 | 287 | 0 | 91 |
| All recorded scopes | 1,205 | 96 | 766 | 343 | 0 | 95 |

In the handwritten scope, A/B/C package counts are **15/27/20**, whose union is **42**, and logical access-site counts are **49/551/54**. Eighteen of the 39 A functions may exit early. In canonical native scope, package counts are **20/35/27**, whose union is **53**; logical site counts are **83/881/85**. Category package counts must not be summed.

The **272 handwritten B functions** have these overlapping tags:

| Tag | Functions |
|---|---:|
| Caller-selected start/range | 169 |
| Index expression (`arbitrary_index` label) | 90 |
| Multiple passes | 62 |
| Lookahead/lookbehind | 58 |
| Backward | 48 |
| Reset/backtracking | 38 |
| Mixed | 24 |
| Explicit scalar-single-character flag | 19 |
| Nonzero subset start | 4 |

The index-expression tag includes fixed scalar cases. It is **not 90 confirmed random-access algorithms**, and subtracting the scalar flag does not derive such a count. Per-case code, reasons and bounds provide the distinction. **B is not a materialized-FSR requirement count.**

## Representative migration requirements

- **regex** retains a kind-tagged subject view while matching. The native inventory has 87 units (A2/B85), including one pointer acquisition and four primitive readers; removing those leaves 82 algorithms (A2/B80). Reverse search, boundaries, backreferences and backtracking are verified. Independent match/search calls and persistent scanner objects have different lifetimes; see [LIFETIME.md](LIFETIME.md).
- **MarkupSafe** performs a GET_DELTA pass, resets its input pointer, then escapes and copies previously inspected runs. A UTF-8 rewrite must preserve this output behavior; an iterator can be restarted if the API supports that explicitly. [Cases](cases/markupsafe.md).
- **RapidFuzz/Levenshtein** use generic codepoint-range algorithms: affix removal, reverse/Hirschberg, cached pattern construction and token/partial windows. Package/source counts include copied vendor implementations; they are not independent engine counts. [Lifetime follow-up](LIFETIME.md).
- **Numba** exposes native Unicode data and caller-selected codepoint indexes. A Python-to-native boundary can retain a view through a compiled invocation; repeated independent invocations are a separate cache policy question. [Cases](cases/numba.md).
- **simplejson and pyjson5** have token/cursor readers. A current-cursor B function can still be a monotonic iterator consumer. Short successful partial decodes are relevant to per-call eviction; full-document decoding is different. [Lifetime follow-up](LIFETIME.md).
- **pybase64** treats kind 1 as Latin-1, not UTF-8. Non-ASCII Latin-1 with binary alternate characters can be meaningful input. Replacing this pointer with UTF-8 bytes without changing the codec contract alters behavior. [Cases](cases/pybase64.md).
- **msgspec** has five representation/layout providers/comparisons and 105 supporting UTF-8 byte functions. Byte grammar lookahead or reparsing does not establish random access in Python codepoint units. Strict UTF-8 fallback also differs for lone surrogates.
- **PyQt5/PyQt6** pass SIP Latin-1/UCS2/UCS4 views to QString with explicit lengths. Python codepoint offsets and Qt UTF-16 units differ. External recipients remain C where their algorithms are not bundled.
- **py-spy** reads target-process object layouts and copies remote memory. An in-process Unicode getter cannot be used through that architecture. Its UTF-16 and Rust-scalar branches have separate surrogate assumptions.
- **PyObjC** creates NoCopy NSString views retaining borrowed representation memory. Lifetime extends beyond the constructor call. **ddtrace/pyroscope** no-allocation views, recursive simplejson calls, MarkupSafe resets and Base64 GIL release illustrate allocation and pointer-stability contracts; these are requirements for a replacement API, not reports of current CPython bugs.

Byte replacements must use byte lengths rather than codepoint lengths and preserve embedded NUL where the current API is length-bounded. A surrogatepass representation must retain adjacent high/low surrogates as two codepoints rather than normalize them into a scalar. “UTF-8-compatible” is therefore not one universal replacement strategy.

## Baseline reconciliation

All 55 canonical-default raw-token consumer packages were reviewed. Six contain no primary input-representation reader after semantic exclusions: **jiter, pyodbc, pywinpty, stringzilla, whenever and xxhash**. Pyodbc retains supporting `CopyCharacters` source-operand context.

The native union becomes **53** by adding **wcwidth** (`ReadChar`-only), **msgspec** (layout bypass), and **PyQt5/PyQt6** (SIP alias consumers). Gensim's handwritten ceditdist embedded in generated C is separately recorded; it is excluded from canonical handwritten scope. All origin/scope splits and package names are in [classification-counts.json](data/classification-counts.json), [scope-origin-counts.json](data/scope-origin-counts.json) and [package-summary.csv](data/package-summary.csv).

These findings support identifying API contracts and migration work. They do not measure workload prevalence, predict a universal slowdown, or determine that every B function needs an FSR cache. [Methods and limitations](METHODS.md) define the denominator and evidence boundaries.
