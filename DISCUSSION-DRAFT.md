# Source survey for the UTF-8 string representation discussion

I surveyed the exact first 4,000 packages in a frozen September 2026 download ranking, using one current-release sdist per package. Source metadata was frozen on October 2. There are 3,788 verified sdists, 211 releases without an sdist, and one metadata 404. Missing source is recorded separately from no detected use. No package code was built, installed or imported.

The construction/mutation results, after excluding Cython-generated files and the compatibility header under the canonical default filter, are:

| API | Packages | Source call expressions |
|---|---:|---:|
| `PyUnicode_New` | 29 | 89 |
| `PyUnicode_WRITE` | 9 | 25 |
| `PyUnicode_WriteChar` | 5 | 9 |
| `PyUnicode_CopyCharacters` | 6 | 11 |
| `PyUnicode_Fill` | 0 | 0 |

These are physical source expressions, including separately identified forwarding macros, rather than runtime invocation counts. Generated/runtime/vendor splits and all-origin counts are retained in the data.

For read access, I followed pointers, helper calls, aliases and direct layout reads. The canonical handwritten scope has 356 source functions in 42 packages: 39 single forward traversals, 272 other access patterns, and 45 bulk/provider functions. Eighteen forward traversals can terminate early. All 272 other-access cases have contextual source excerpts. Scalar reads and sequential cursor continuations are identified explicitly; the 272 figure does **not** mean that 272 functions require an FSR cache.

I also checked a narrower question: whether a call-scoped borrowed view, immediately evicted when its last lease ends, would be rebuilt by independent operations on the same caller-owned str. There are at least **eight other package names, seven implementation families**, with verified successful scalable partial-work examples: APSW, RapidFuzz, polyleven/spaCy, simplejson, pyjson5, pyahocorasick and compiled lxml.html.diff. Numba adds a separate Python-to-native unboxing-boundary case. This is a conservative lower bound in the 53-package native candidate set, not an estimate across PyPI.

Examples include Prefix/Postfix metrics stopping at a mismatch, a selected Unicode boundary/range, reading one JSON term, and a trie lookup stopping at a missing edge. Pyahocorasick borrows only kind4 input; kind1/2 already copy to UCS4. Polyleven length rejection before acquiring DATA is excluded. Full scans/copies and early-invalid-only cases are kept separate.

The distinction seems relevant to API design: a lease can protect a pointer during its actual owner lifetime, but releasing that lease does not identify the last **future** use of the str. Under whole-FSR materialization plus immediate eviction, q independent calls doing k≪n work can add O(q*n), while retaining the first representation can give O(n+q*k). This is a static complexity argument, not a benchmark or a claim about the reference implementation's current eviction policy.

Persistent scanners/prepared objects can retain a lease: regex Scanner, aiocsv parser chunks, Numba native owners, pyahocorasick iterators, RapidFuzz batch scorers and PyObjC NoCopy NSString have identifiable owner scopes. A compiled regex Pattern alone does not prepare every future subject. For APIs that already scan/copy the complete input, conversion may still add memory and constant-factor cost without a new asymptotic cost.

The prepared evidence is available in [the report](REPORT.md), [methods](METHODS.md), [case index](cases/README.md), and [lifetime study](LIFETIME.md), with exact package versions, source URLs/hashes and permanent links where verified. These relative links work in the prepared repository tree; repository URLs need to be supplied when posting this text externally. No unverified latest-HEAD links are substituted. Generated-call-graph, external-recipient and static-exposure limits are explicit.
