# Unicode object layout dependencies in the top 4,000 PyPI packages

## Findings

The saved corpus confirms substantive Python 3 `PyUnicodeObject` layout dependencies in **eight packages**: [cython](cases/cython.md), [ddtrace](cases/ddtrace.md), [lxml](cases/lxml.md), [multidict](cases/multidict.md), [numba](cases/numba.md), [numpy](cases/numpy.md), [py-spy](cases/py-spy.md), [pyobjc-core](cases/pyobjc-core.md). These include embedding the complete object in a subclass, testing its size and offsets, and decoding its fields from a remote process. The Cython GDB debugger and py-spy are tooling consumers; this list is not a count of eight native extension modules.

`PyASCIIObject` and `PyCompactUnicodeObject` reveal additional dependencies that a search for `PyUnicodeObject` alone misses: cached hash access, length mutation, UTF-8 cache reads, direct output initialization, state-bit overlays and payload addresses calculated from header sizes. Ordinary `PyUnicode_DATA` / `KIND` calls, casts whose values only feed these APIs, and bare declarations are excluded from direct-layout consumer counts.

## Counts and their interpretation

All counts below describe **confirmed layout operations or implementations present in the selected source distributions**, including conditional/obsolete source branches. They do not assert compilation or execution on any particular Python release. All three structs overlap, as do package sets across origins.

| Struct | Packages | Source files | Reviewed layout records |
|---|---:|---:|---:|
| `PyUnicodeObject` | 22 | 45 | 50 |
| `PyASCIIObject` | 65 | 272 | 821 |
| `PyCompactUnicodeObject` | 58 | 218 | 232 |

The union is **67 packages, 277 files and 1041 layout records**. There are 1137 total reviewed records including non-direct context. A record is a curated function/region or one implementation family in one generated source file, with nonadjacent sites explicitly listed. It is not a raw token, call, runtime frequency, or uniformly sized unit. Raw occurrences of type names were only the inventory denominator: 4,057 tokens in 309 candidate files across 74 packages. Every candidate and token has a disposition; no unresolved candidate remains.

| Origin / role | Packages | Files | Layout records |
|---|---:|---:|---:|
| Project source, including remote tools | 15 | 26 | 61 |
| Generated distribution code | 49 | 219 | 847 |
| Cython utility template source | 1 | 3 | 5 |
| pythoncapi compatibility headers | 5 | 5 | 5 |
| Bundled FFI implementation | 1 | 1 | 2 |
| Adopted CPython variants; activation unresolved | 1 | 10 | 35 |
| Copied CPython core/reference/tools | 2 | 10 | 81 |
| Tests, fuzzers, demonstrations | 4 | 4 | 5 |

The large generated count is chiefly repeated Cython cached-hash helpers. Among the audited first-line-marked Cython files, the only substantive contemporary `PyUnicodeObject` dependency is lxml's subclass embedding and size check. The other direct full-object field references are non-PEP393/Python 2 branches; pythoncapi's full-object `.hash` branch is also Python 2-only. Generated `PyCompactUnicodeObject.wstr_length` references are older-Python branches. Exact guards are retained per site; “Python 3 branch” does not mean active on Python 3.15 or every feature configuration.

The project-source group has 15 packages across any of the three structs: [cython](cases/cython.md), [ddtrace](cases/ddtrace.md), [duckdb](cases/duckdb.md), [jpype1](cases/jpype1.md), [librt](cases/librt.md), [msgspec](cases/msgspec.md), [multidict](cases/multidict.md), [mypy](cases/mypy.md), [numba](cases/numba.md), [numpy](cases/numpy.md), [orjson](cases/orjson.md), [ormsgpack](cases/ormsgpack.md), [py-spy](cases/py-spy.md), [pyjson5](cases/pyjson5.md), [pyobjc-core](cases/pyobjc-core.md). The eight-package principal finding adds lxml's generated subclass to the seven project-source packages using the full object. Frozendict's adopted versioned CPython code is separated because its build selector is absent from the retained corpus. The bundled PythonARM CPython headers and generators in pywinpty do not establish that pywinpty's extension activates those layouts.

## Representative dependencies

| Package / role | Verified use | Consequence for a UTF-8 internal representation |
|---|---|---|
| [NumPy](cases/numpy.md) | `PyUnicodeScalarObject` embeds a complete `PyUnicodeObject`; scalar type initialization uses `sizeof` the derived scalar | Complete prefix size and offsets affect subclass allocation and following private fields. An opaque/removed complete type requires redesign; a layout change alone may require rebuilding |
| [multidict](cases/multidict.md), [lxml](cases/lxml.md), [PyObjC](cases/pyobjc-core.md) | Unicode-subclass bases and allocation sizes; PyObjC also initializes the noncompact Unicode header/data union directly | Separate supported Unicode subtype allocation from manual object construction; retaining payload access APIs alone cannot satisfy these dependencies |
| [Numba](cases/numba.md) | `sizeof`/`offsetof` assertions check nested headers; cached `.hash` read | Assertions and offsets must change; cached-hash access can be replaced independently of payload representation |
| [ddtrace](cases/ddtrace.md), [py-spy](cases/py-spy.md) | Copy remote headers, inspect kind/compact/ascii/length/cache/data, compute header-plus-one addresses, decode width-specific data | Remote profilers cannot call APIs in the target process; they need new versioned layout decoders and correct UTF-8 byte/code-point handling |
| [Cython GDB](cases/cython.md) | Executable GDB field lookups use strings such as `_base`, `state`, `data` and compute inline payload addresses | String-literal masking must not erase these consumers; debugger layout support must track target CPython |
| [orjson](cases/orjson.md), [ormsgpack](cases/ormsgpack.md), [msgspec](cases/msgspec.md) | Fresh outputs use selected header plus one as their writable destination; metadata/cache/hash fast paths read/write headers | Replace header arithmetic and width-specific writes, potentially with constructors/writers; state/cache/hash semantics require separate handling |
| [JPype](cases/jpype1.md), [pyjson5](cases/pyjson5.md) | Custom Unicode output layout, header fields and payload offsets; pyjson5 constructs an ASCII object in its encoder allocation | Public allocation/writer contracts or an explicit UTF-8 construction API are needed; this is not only input decoding |
| [MyPy](cases/mypy.md), [LibRT](cases/librt.md) | Same source family allocates a larger ASCII Unicode object, fills decimal characters, then assigns `PyASCIIObject.length` | Shrinking logical length by assigning a private lvalue must be replaced alongside destination-buffer handling |
| [DuckDB](cases/duckdb.md) | Direct `utf8` / `utf8_length` reads in NumPy string scanning | A UTF-8-native representation can simplify the path, but field/cache layout assumptions remain a porting requirement |
| [ddtrace IAST](cases/ddtrace.md) | Overlays `PyASCIIObject.state` with a local bitfield and stores a taint marker in 24 high bits | Reserved padding/bit positions are an undocumented state contract; this requires a replacement independent of character storage |

Each package page contains short exact snippets, frozen version/member path, source SHA-256, field list, purpose, migration implication, activation caveats, and verified immutable GitHub links when the saved map covers the range. Machine-readable records preserve every reviewed snippet range, including all generated copies. 229 layout records have a verified link for their entire main range; additional individual snippet ranges may be verified even when a nonadjacent whole range is not. Unmapped ranges retain an immutable PyPI sdist URL and verified archive/source hashes.

## Negative and supporting findings

MarkupSafe and its vercel-runtime vendor copy use `PyUnicodeObject*` parameters/casts but obtain payload/length via Unicode APIs. Pybind11/catboost mentions are comments. Pydevd attachment headers declare old structs but no saved use was found. Jiter and pyroscope-io remain API-only negatives in the reviewed alias-closure context. These are not independent layout algorithms.

Rust bindgen/PyO3 mirrors are definitions/providers until an actual field consumer is traced. Py-spy's many embedded global-string declarations are not counted as thousands of remote reads. The SentencePiece compact-header offset/cache mutation is a test-only consumer. Copied CPython accessors and code generators are implementation context, not proof of an extension's activation.

## Scope and limits

Ranking: September 2026 calendar-month downloads, ClickHouse, `hugovk/top-pypi-packages` snapshot updated 2026-10-01 12:41:32 UTC and pinned to commit `e6b5b398c1fcc783f593031f99bc2c772d64c6ef`. The exact first 4,000 names and hashes are included. Package versions/sdists are the selections frozen by the preceding survey, rather than refreshed latest releases.

All 4,000 packages have coverage classifications: **3,788 scanned sdists; 211 selected releases with no current sdist; one metadata failure (`aaaaaaaaa`, HTTP 404)**. Those 212 unknown packages are not zero-use packages. The previous recovery inspected 930,709 eligible regular text files; the present analysis reread the 131,701 retained native/Unicode-bearing source records (2,693,826,682 catalog bytes) across 583 packages. Remaining scanned packages had no retained candidate within the original scope, not proof of absence in wheels or external repositories.

This is a static saved-source survey. Ignored documentation/web formats, binaries, nested archives, unusual encodings, unfollowed symlinks, missing external provider sources and differently named/unrecognized raw layouts limit completeness. No large retained source was silently capped; archive recovery recorded no oversized/skipped eligible source member. Known aliases were traced, but token-pasting, dynamically produced C and generic raw offsets can escape the candidate strategy. Build guards and package activation were not executed. Frozendict's build-variant selector and unmapped upstream links remain explicit evidence gaps. See [methods](METHODS.md) and [the independent verification record](data/coverage-verification.json).
