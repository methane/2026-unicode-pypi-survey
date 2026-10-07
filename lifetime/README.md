# Per-package lifetime evidence

[Summary and assumptions](../LIFETIME.md) · [Machine-readable inventory](../data/reuse-inventory.json)

## aiocsv

Frozen version: **1.4.1**. Result: **no**.

Operation: CSV Parser iteration; Dialect initialization

Parser retains buffer_str and buffer_idx across records; repeated next/send consumes persistent parser state rather than independent operations on a supplied str. Character configuration uses PyUnicode_ReadChar(0), not a borrowed DATA lease. A future parser could retain a lease with its chunk owner.

Implementation family: `aiocsv_parser`.

Uncertainty: Parser uses PyUnicode_READ_CHAR macro for chunk positions, which assumes FSR currently; this is a persistent-scanner design case, not evidence of independent repeat calls.

- `aiocsv-1.4.1/aiocsv/_parser.c`, lines 194–260, 282–312, 464–480, 625–654, 684–716; member SHA256 `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`.
  [Verified source reference 1](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L194-L260)
  [Verified source reference 2](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L282-L312)
  [Verified source reference 3](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L464-L480)
  [Verified source reference 4](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L625-L654)
  [Verified source reference 5](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L684-L716)
  [Frozen sdist](https://files.pythonhosted.org/packages/9c/18/bc63651e9d716f388678d5bf58fc004dd719a623b0ca7f4f401573883a89/aiocsv-1.4.1.tar.gz), archive SHA256 `bb663f9eabf88402ca2c325fd0df836eee7da34cf7c5476b5e6cf7d098cdebda`.

## apsw

Frozen version: **3.53.4.0**. Result: **yes**.

Operation: apsw Unicode grapheme_next_break(text,offset), has_category(text,start,end,mask)

Registered Python calls obtain local DATA/KIND and return without saving a view. An accepted long nonASCII str can be queried repeatedly for its first grapheme or a one-codepoint range. Existing work scales with selected boundary/range, while rebuilding a whole FSR after each return would scale with total string length.

Implementation family: `apsw_unicode_boundaries`.

- `apsw-3.53.4.0/src/unicode.c`, lines 185–234, 280–409, 1334–1358, 2612–2630; member SHA256 `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.
  [Verified source reference 1](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L185-L234)
  [Verified source reference 2](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L280-L409)
  [Verified source reference 3](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1334-L1358)
  [Verified source reference 4](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L2612-L2630)
  [Frozen sdist](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz), archive SHA256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## backports-datetime-fromisoformat

Frozen version: **2.0.3**. Result: **yes**.

Operation: _datetime_fromisoformat.datetime_fromisoformat(str)

Public wrapper calls sanitizer that gets local DATA and checks only candidate positions7,8,10. It then uses UTF8 parsing. Long malformed strings can fail after a short prefix; valid long fractional-second strings already require parsing their digit suffix, so fixed-position B alone is not a strong accepted scalable example.

Implementation family: `cpython_datetime_fromisoformat_backport`.

Uncertainty: On legacy FSR CPython a first strict UTF8 encoding can itself cost O(n); native UTF8 representation removes that existing conversion. Surrogate separator branch copies whole string. No claim that valid long input currently costs O(1).

- `backports_datetime_fromisoformat-2.0.3/backports/datetime_fromisoformat/module.c`, lines 24–40; member SHA256 `db674dedf8b2fdbfa3c162e9bcb4a69cbb5ef34ccdee5e0b4b747175d545b8d5`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/71/81/eff3184acb1d9dc3ce95a98b6f3c81a49b4be296e664db8e1c2eeabef3d9/backports_datetime_fromisoformat-2.0.3.tar.gz), archive SHA256 `b58edc8f517b66b397abc250ecc737969486703a66eb97e01e6d51291b1a139d`.
- `backports_datetime_fromisoformat-2.0.3/backports/datetime_fromisoformat/_datetimemodule.c`, lines 779–832, 935–1005; member SHA256 `6bec46488f758c0a5fcce918176db3a11285595499833412ae82aa20003d3710`.
  [Verified source reference 1](https://github.com/movermeyer/backports.datetime_fromisoformat/blob/abc03054a166a842cd2858a4fb97cd619ae7d4f3/backports/datetime_fromisoformat/_datetimemodule.c#L779-L832)
  [Verified source reference 2](https://github.com/movermeyer/backports.datetime_fromisoformat/blob/abc03054a166a842cd2858a4fb97cd619ae7d4f3/backports/datetime_fromisoformat/_datetimemodule.c#L935-L1005)
  [Frozen sdist](https://files.pythonhosted.org/packages/71/81/eff3184acb1d9dc3ce95a98b6f3c81a49b4be296e664db8e1c2eeabef3d9/backports_datetime_fromisoformat-2.0.3.tar.gz), archive SHA256 `b58edc8f517b66b397abc250ecc737969486703a66eb97e01e6d51291b1a139d`.

## biopython

Frozen version: **1.88**. Result: **yes**.

Operation: Bio.Align.substitution_matrices.Array.alphabet setter

Python getset exposes DATA/KIND alphabet mapping construction; pointer is local, output mapping is owned, and alphabet object is retained without its pointer. Reusing same alphabet for independent Array objects is possible, but accepted input is fully scanned and mapping allocation/initialization is substantial. Setter on the same already-prepared Array returns before acquisition.

Implementation family: `biopython_alphabet_mapping`.

Uncertainty: Not a regex-like cheap accepted repeated call on one prepared object; duplicate input can fail early after fixed-domain mapping initialization. Other BioPython B functions enforce length1 and do not establish long-string rematerialization.

- `biopython-1.88/Bio/Align/substitution_matrices/_arraycore.c`, lines 58–66, 102–159; member SHA256 `c18c8d807a578440746374b572e77badca2df191236cf3c3be459239c4739a3d`.
  [Verified source reference 1](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/substitution_matrices/_arraycore.c#L58-L66)
  [Verified source reference 2](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/substitution_matrices/_arraycore.c#L102-L159)
  [Frozen sdist](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz), archive SHA256 `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

## bitarray

Frozen version: **3.11.0**. Result: **yes**.

Operation: bitarray.extend(str) and constructor initialization

Public extend dispatch reads input with FSR-dependent READ_CHAR macro and finishes in one call, retaining no source pointer. Accepted input is a complete forward scan. Invalid first codepoint can reject before reading remainder, but resize allocates output based on full input length before validation.

Implementation family: `bitarray_unicode01`.

Uncertainty: Early rejection does not imply O(1) total work because output resize occurs first. ReadChar lowercase API is different from READ_CHAR macro. No extra asymptotic work for accepted full scans.

- `bitarray-3.11.0/bitarray/_bitarray.c`, lines 853–899, 1249–1275, 4578–4584; member SHA256 `014fc32ea7e8084eba4a4f7c91a3b8e9b6d03cf9c5193dc23adba762113188a3`.
  [Verified source reference 1](https://github.com/ilanschnell/bitarray/blob/ec1ea4ac828cb9f1530a94f58cc497e48a593aa8/bitarray/_bitarray.c#L853-L899)
  [Verified source reference 2](https://github.com/ilanschnell/bitarray/blob/ec1ea4ac828cb9f1530a94f58cc497e48a593aa8/bitarray/_bitarray.c#L1249-L1275)
  [Verified source reference 3](https://github.com/ilanschnell/bitarray/blob/ec1ea4ac828cb9f1530a94f58cc497e48a593aa8/bitarray/_bitarray.c#L4578-L4584)
  [Frozen sdist](https://files.pythonhosted.org/packages/04/f7/6765577df59e2345036e435f7e983e1c291d67b7d76a51918eff04ad1494/bitarray-3.11.0.tar.gz), archive SHA256 `bf19437ec00ec3d40aef82eaeedc14cf4000be9b635c4f5049796506e6630dd8`.

## cffi

Frozen version: **2.1.1**. Result: **yes**.

Operation: _cffi_backend.newp / ffi.new char16_t or wchar_t array initialized from str

Public newp path converts Unicode into owned CData. char16 helper borrows DATA4 to count supplementary characters then reads whole source forward to produce UTF16; source view does not persist into returned CData. Independent calls may repeat same str, but all accepted long char16 input already undergoes full conversion; char32 materializes an owned UCS4 copy.

Implementation family: `cffi_utf16_conversion`.

Uncertainty: One-character casts enforce length1 and are not scalable examples. No caller-selected small substring conversion established.

- `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1476–1571, 1637–1652, 3945–3953, 7652–7660; member SHA256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.
  [Verified source reference 1](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1476-L1571)
  [Verified source reference 2](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1637-L1652)
  [Verified source reference 3](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L3945-L3953)
  [Verified source reference 4](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L7652-L7660)
  [Frozen sdist](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz), archive SHA256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.
- `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 91–140; member SHA256 `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`.
  [Verified source reference 1](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L91-L140)
  [Frozen sdist](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz), archive SHA256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## cython

Frozen version: **3.3.0**. Result: **possible**.

Operation: Generated Unicode index/slice/iteration helpers

Utility source and compiler emitter prove code generation for scoped DATA/KIND reads, including arbitrary index, substring and loops. These are compiler/runtime implementations, not by themselves proof of an installed Python-visible Cython package operation repeatedly accepting the same input str.

Implementation family: `cython_unicode_index_slice_runtime`.

Uncertainty: Downstream generated clients must be checked individually; count copied helpers as one implementation family, not an independent library per copy.

- `cython-3.3.0/Cython/Utility/StringTools.c`, lines 605–624, 796–824; member SHA256 `a9b4f6124f46993d8cd1d19e9402772663cd21e99166ce99f32f05f12410baf6`.
  [Verified source reference 1](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/StringTools.c#L605-L624)
  [Verified source reference 2](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/StringTools.c#L796-L824)
  [Frozen sdist](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz), archive SHA256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## ddtrace

Frozen version: **4.15.4**. Result: **no**.

Operation: traceback_t / allocation-sampling path -> push_stacktrace_to_sample_no_refcount -> unicode_to_sv_no_alloc

Allocation sampling repeatedly reads existing code-name and filename str objects; direct pointer route is compact ASCII only. Repeated pointer calls are verified, but their successful path is ASCII-only or length-one configuration; native UTF8 needs no full non-ASCII FSR conversion for that path.

Implementation family: `ddtrace`.

Lifetime: Borrowed frame/code references own strings during synchronous sampling. Sample::push_frame interns string views to external libdatadog dictionary IDs; sample locations hold function IDs. External insert implementation is not present, so ownership guarantee beyond this ABI is not independently audited here.

Persistent state: Interned output dictionary, not a Python FSR cache keyed by str identity.

- `ddtrace-4.15.4/ddtrace/profiling/collector/_memalloc_tb.cpp`, lines 8–27; member SHA256 `1d78e3fe56d1075ad0e2a25a7eb9667145375b452422b615dfcc0211ea63162b`.
  [Verified source reference 1](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/profiling/collector/_memalloc_tb.cpp#L8-L27)
  [Frozen sdist](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz), archive SHA256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.
- `ddtrace-4.15.4/ddtrace/profiling/collector/_memalloc_tb.cpp`, lines 69–112; member SHA256 `1d78e3fe56d1075ad0e2a25a7eb9667145375b452422b615dfcc0211ea63162b`.
  [Verified source reference 1](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/profiling/collector/_memalloc_tb.cpp#L69-L112)
  [Frozen sdist](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz), archive SHA256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.
- `ddtrace-4.15.4/ddtrace/internal/datadog/profiling/dd_wrapper/src/sample.cpp`, lines 24–42; member SHA256 `8bb5852d18eb810972a896bc8f70680fc20b5306a00d00f19a1ddbb3a7d22c76`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz), archive SHA256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.
- `ddtrace-4.15.4/ddtrace/internal/datadog/profiling/dd_wrapper/src/sample.cpp`, lines 114–153; member SHA256 `8bb5852d18eb810972a896bc8f70680fc20b5306a00d00f19a1ddbb3a7d22c76`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz), archive SHA256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## duckdb

Frozen version: **1.5.6**. Result: **yes**.

Operation: Registered pandas_scan table function -> PandasScanFunc -> PandasBackendScanSwitch -> NumpyScan::Scan object/string-column scanning

Repeating a scan on the same object can reborrow and, under immediate eviction, rematerialize non-ASCII FSR. This is a full-input conversion cost case, not the stronger asymptotic cheap-prefix example.

Implementation family: `duckdb-numpy-unicode-to-utf8`.

Uncertainties: Python dataframe registration call was not traced; registered native pandas_scan provider and its callback chain are verified. Provider may choose scan-lifetime leases; future queries remain separate. UTF8 cache presence bypasses FSR decoding.

Borrow lifetime: Non-ASCII codepoint pointers are used synchronously by DecodePythonUnicode then discarded. It creates owned UTF8 output in the result vector. ASCII/UTF8 branch output strings can retain source-backed storage, so these are not call-scoped FSR conversions.

Persistent or prepared alternative: Scan bind data retains the object array/source owners, but no cached non-ASCII FSR view is recorded in this conversion path; a redesigned scan-bound lease could cover a scan.

- `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 113–131, 359–451; member SHA256 `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`.
  [Verified source reference 1](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L113-L131)
  [Verified source reference 2](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L359-L451)
  [Frozen sdist](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz), archive SHA256 `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.
- `duckdb-1.5.6/src/duckdb_py/pandas/scan.cpp`, lines 16–36, 62–71, 170–212; member SHA256 `97c730e10a56d5bc5cabd7b07d1cc6b9cfe86957f65643ad884361f82d3deb70`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz), archive SHA256 `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.

## frozendict

Frozen version: **2.4.7**. Result: **possible**.

Operation: frozendict.__getitem__ / mapping lookup through copied dict_subscript -> lookdict_unicode_nodummy -> unicode_eq

Conditional source pattern for repeated same query str exists if nonidentity same-hash matching-kind comparison is reached. No unconditional cheap-prefix guarantee: identity/hash gating and libc behavior matter.

Implementation family: `cpython-unicode-eq-frozendict-copy`.

Uncertainties: Retained copied implementation variants are 3_6 through3_10; saved context does not establish that this exact copy is selected in a future/current interpreter build. Do not count as unconditional modern-native cheap reuse.

Borrow lifetime: Pointers local to comparator/lookup. Stored keys are retained by mapping; a separately supplied query string is not retained as a prepared query.

Persistent or prepared alternative: Stored-key lifetime can support a lease, but retaining a query lease across independent lookups would require a new query cache/owner.

- `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/stringlib/eq.h`, lines 7–25; member SHA256 `c4fdd9e41f8748397cd3c0c5d5ecf77662b6c66c1cdd020d50b77fe9ddd1163c`.
  [Verified source reference 1](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/stringlib/eq.h#L7-L25)
  [Frozen sdist](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz), archive SHA256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.
- `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c`, lines 692–731, 946–972; member SHA256 `e3d6d3f04dfad62332dac09457c007102bf83db42ee05663f766d4e1eb3caadd`.
  [Verified source reference 1](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L692-L731)
  [Verified source reference 2](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L946-L972)
  [Frozen sdist](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz), archive SHA256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.
- `frozendict-2.4.7/src/frozendict/c_src/3_10/frozendictobject.c`, lines 360–369, 1344–1350; member SHA256 `bfd0a550ee69bb5406e9a14bef64472aa82cbbcc906af217ddd515bad150a7d8`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz), archive SHA256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## gevent

Frozen version: **26.9.0**. Result: **possible**.

Operation: Greenlet representation formats repr(x)[:50]

Actual generated greenlet code calls scoped Unicode substring provider for first50 codepoints of a repr result. Normally repr constructs a fresh temporary (and may already scan full object string). A user __repr__ could return the same cached long nonASCII str across calls, but that reuse is conditional and not established by this package source.

Implementation family: `cython_unicode_index_slice_runtime`.

Uncertainty: Do not count mere generated helper presence; conditional cached custom repr could qualify, ordinary repr temporary does not demonstrate same-string cache reuse.

- `gevent-26.9.0/src/gevent/greenlet.c`, lines 9205–9266, 9337–9349, 27449–27476; member SHA256 `70f2f5cea5e112badf4a7237713d5018f99cffc8ac9809473b8f415d268991bb`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz), archive SHA256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## jpype1

Frozen version: **1.7.1**. Result: **no**.

Operation: JPPyString::asCharUTF16 / JChar conversion and arithmetic; Java class/value attribute access hooks

Do not classify a scalar ReadChar call as full-view materialization/release. A proposed implementation choosing to materialize FSR inside ReadChar would be a separate core design choice.

Implementation family: `jpype-scalar-readchar`.

Borrow lifetime: No retained native FSR pointer/view in these routes; immediate scalar reads.

Persistent or prepared alternative: Not needed for a scalar API; persistent Java objects do not establish string-view borrowing here.

- `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–282; member SHA256 `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`.
  [Verified source reference 1](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L220-L282)
  [Frozen sdist](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz), archive SHA256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.
- `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 437–507; member SHA256 `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`.
  [Verified source reference 1](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L437-L507)
  [Frozen sdist](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz), archive SHA256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.
- `jpype1-1.7.1/native/python/pyjp_value.cpp`, lines 190–246; member SHA256 `033dc39e9780b86520c3fcb1567b05822d62f4b7258906229e789adc655be83e`.
  [Verified source reference 1](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_value.cpp#L190-L246)
  [Frozen sdist](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz), archive SHA256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

## levenshtein

Frozen version: **0.27.5**. Result: **yes**.

Operation: levenshtein_cpp median/quickmedian/median_improve/setmedian/setratio/seqratio

Each native entry extracts local RF_String vectors for the supplied original strings. Repeated independent calls borrow the same source again. Median/set routines traverse or copy input; these verified own entries do not establish the cheap cutoff0 distance facade.

Implementation family: `levenshtein-own-median-set-seq`.

Uncertainties: Levenshtein.distance Python facade (__init__.py) is absent from saved source catalog. Bundled uniform cutoff0 implementation proves engine behavior but not facade routing; do not add this package to strong partial count from vendor headers alone.

Persistent lease or owned copy alternative: No reusable prepared median object is exposed in saved native entries; within a call CachedLevenshtein/CachedIndel own source copies and pattern maps.

- `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx`, lines 28–32; member SHA256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx`, lines 57–64; member SHA256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx`, lines 83–114; member SHA256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx`, lines 148–169; member SHA256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx`, lines 205–232; member SHA256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 76–90; member SHA256 `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.
  [Verified source reference 1](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L76-L90)
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 106–125; member SHA256 `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.
  [Verified source reference 1](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L106-L125)
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
- `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 478–526; member SHA256 `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.
  [Verified source reference 1](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L478-L526)
  [Frozen sdist](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz), archive SHA256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## librt

Frozen version: **0.16.0**. Result: **yes**.

Operation: librt.strings.StringWriter.write(str)

Actual Python method registration and wrapper call StringWriter_write_internal. It gets local DATA/KIND then copies the entire string or widens it once; retains owned output bytes, not source lease. Same input can be written repeatedly but already performs O(n) work each call.

Implementation family: `mypyc_librt_string_runtime`.

Uncertainty: CPyStr_GetItem runtime supports cheap indexed reads but direct installed-package Python exposure was not established; StringWriter is the verified full-scan/full-copy case. Scalar codepoint wrappers take ints, not long str.

- `librt-0.16.0/strings/librt_strings.c`, lines 609–620, 650–715; member SHA256 `3288ec85ef0e7d6d406fb8d32041c449f1fce94d120389fc6484997d8f52f804`.
  [Verified source reference 1](https://github.com/mypyc/librt/blob/b2508063e86e012301e09432a6d58e74224f1e24/lib-rt/strings/librt_strings.c#L609-L620)
  [Verified source reference 2](https://github.com/mypyc/librt/blob/b2508063e86e012301e09432a6d58e74224f1e24/lib-rt/strings/librt_strings.c#L650-L715)
  [Frozen sdist](https://files.pythonhosted.org/packages/04/f5/9dc696772d241814bacac7880bac32f2930b5a6ebc1f85317b83161a011c/librt-0.16.0.tar.gz), archive SHA256 `ac38d6d8d66bf3d744148dbbc0b8e193e195a51e364ed55e224631f5721891fc`.

## lxml

Frozen version: **6.1.3**. Result: **yes**.

Operation: lxml.html.diff.cleanup_delete; objectify registered type_check

Compiled cleanup_delete invokes mark_unbalanced/tag_name_of_chunk on valid long opening-tag chunks; tag-name extraction reads only through first whitespace or >, yielding a short name while preserving original long chunk in a list. A tag with short name and arbitrarily long nonASCII attributes supports cheap accepted prefix work across independent calls. Objectify also publishes registered int/float type_check functions; invalid first character can reject early, valid numeric text is fully scanned.

Implementation family: `lxml_html_tag_prefix`.

Uncertainty: Public cleanup_delete operates on token/chunk lists, not raw full-document parsing; requires long tag chunk with short leading name. Full libxml2 parse/serialization cases are not counted as cheap prefix examples.

- `lxml-6.1.3/src/lxml/html/diff.py`, lines 299–317, 344–430, 482–510; member SHA256 `65ad01cbec9e6254048d4bbb9bbc4a076f3c90a8b2f15052e604f444f39a158d`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz), archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.
- `lxml-6.1.3/src/lxml/html/diff.c`, lines 9268–9496, 9683–9699, 9990–10010, 11190–11214, 25402–25447; member SHA256 `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz), archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.
- `lxml-6.1.3/src/lxml/objectify.pyx`, lines 950–1031, 1082–1089, 1201–1218, 1242–1254; member SHA256 `1fad182fbaa8c2be9af1502af4bf626c77770675c0251e88c7908c61d64c01e3`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz), archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## markupsafe

Frozen version: **3.0.3**. Result: **yes**.

Operation: markupsafe._speedups._escape_inner(s)

Exposed METH_O entry dispatches to kind-specific readers. All input codepoints are scanned for escape delta, even when it returns the original str; local input pointers do not establish future-call retention.

Implementation family: `markupsafe-escape`.

Persistent lease or owned copy alternative: No prepared escape context shown. Same input object returned when no escaping is needed does not preserve a separate FSR lease under immediate-eviction policy.

- `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 3–17; member SHA256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.
  [Verified source reference 1](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L3-L17)
  [Frozen sdist](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz), archive SHA256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.
- `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 101–149; member SHA256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.
  [Verified source reference 1](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L101-L149)
  [Frozen sdist](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz), archive SHA256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.
- `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 152–175; member SHA256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.
  [Verified source reference 1](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L152-L175)
  [Frozen sdist](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz), archive SHA256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

## msgspec

Frozen version: **0.22.0**. Result: **no**.

Operation: msgspec.json.Decoder.decode / decode_lines; JSON encode/convert string and keyword helpers

Repeating the same str may reuse its UTF8 cache today; retaining or evicting a hypothetical FSR companion is irrelevant to this reviewed path.

Implementation family: `msgspec-cached-utf8`.

Borrow lifetime: ms_get_buffer INCREFs the input and places UTF8 in a call-local JSONDecoderState; ms_release_buffer clears that owner after decode. A persistent Decoder retains schema/configuration, not input buffer state.

Persistent or prepared alternative: Decoder can retain an input lease if redesigned, but current buffer is UTF8 and native UTF8 migration can supply it directly.

- `msgspec-0.22.0/src/msgspec/_core.c`, lines 193–247, 19836–19874; member SHA256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.
  [Verified source reference 1](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L193-L247)
  [Verified source reference 2](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L19836-L19874)
  [Frozen sdist](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz), archive SHA256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## multidict

Frozen version: **7.0.0**. Result: **yes**.

Operation: MultiDict equality exact-string values; identity comparison conditional on hash/pointer gates

Verified nonidentical exact non-ASCII string values of equal length/kind reach str_cmp and scoped DATA/memcmp in exposed equality. Repeating equality on persistent dictionaries repeats this view acquisition. Same-object values/keys skip DATA; normal failed-key lookup usually hash-skips comparison, so generic repeated get/set is not evidence.

Implementation family: `multidict-identity-value-compare`.

Uncertainties: External platform memcmp algorithm is not in saved corpus. Hash-collision query paths exist but are not needed for verified value-equality path or used as scalable strong evidence.

Persistent lease or owned copy alternative: Stored keys/values and istr canonical objects have persistent ownership and could retain a lease/copy until entry/canonical lifetime ends, rather than release at each comparison. Existing code stores PyObjects, not cached FSR data pointers.

- `multidict-7.0.0/multidict/_multilib/identity.h`, lines 22–63; member SHA256 `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`.
  [Verified source reference 1](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L22-L63)
  [Frozen sdist](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz), archive SHA256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.
- `multidict-7.0.0/multidict/_multilib/identity.h`, lines 160–185; member SHA256 `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`.
  [Verified source reference 1](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L160-L185)
  [Frozen sdist](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz), archive SHA256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.
- `multidict-7.0.0/multidict/_multilib/hashtable.h`, lines 1879–1904; member SHA256 `531149bd8163f67d6348dfd815ba5d7d9a0984fd08465ccfe8dafb4c58764330`.
  [Verified source reference 1](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/hashtable.h#L1879-L1904)
  [Frozen sdist](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz), archive SHA256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.
- `multidict-7.0.0/multidict/_multidict.c`, lines 584–612; member SHA256 `dfb3a305ae85df0c4f81c74f0c53355c0df2a419b76ca556664c8b4a53a27787`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz), archive SHA256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.
- `multidict-7.0.0/multidict/_multilib/istr.h`, lines 194–208; member SHA256 `13509ec863d9a1a80aa505507a0327c0204ed12c0d91b03214a42f34936cbe7b`.
  [Verified source reference 1](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/istr.h#L194-L208)
  [Frozen sdist](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz), archive SHA256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.

## mutf8

Frozen version: **1.1.0**. Result: **yes**.

Operation: mutf8.cmutf8.encoded_size / encode_modified_utf8

Each exposed size/encode call obtains DATA on original Unicode input. Local borrowed representation is reused only inside that call; independent future size/encode calls have no persistent library view.

Implementation family: `mutf8-count-encode`.

Persistent lease or owned copy alternative: UTF8/surrogatepass fast encoding path can avoid dedicated FSR via a native UTF8 implementation; special MUTF8 NUL/supplementary semantics still require transformation.

- `mutf8-1.1.0/mutf8/cmutf8.c`, lines 138–158; member SHA256 `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`.
  [Verified source reference 1](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L138-L158)
  [Frozen sdist](https://files.pythonhosted.org/packages/5c/74/bfce3ab421b39503c6cd11a6bc812a763154082a4f69d55831d762e58fcd/mutf8-1.1.0.tar.gz), archive SHA256 `279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a`.
- `mutf8-1.1.0/mutf8/cmutf8.c`, lines 166–181; member SHA256 `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`.
  [Verified source reference 1](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L166-L181)
  [Frozen sdist](https://files.pythonhosted.org/packages/5c/74/bfce3ab421b39503c6cd11a6bc812a763154082a4f69d55831d762e58fcd/mutf8-1.1.0.tar.gz), archive SHA256 `279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a`.
- `mutf8-1.1.0/mutf8/cmutf8.c`, lines 189–258; member SHA256 `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`.
  [Verified source reference 1](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L189-L258)
  [Frozen sdist](https://files.pythonhosted.org/packages/5c/74/bfce3ab421b39503c6cd11a6bc812a763154082a4f69d55831d762e58fcd/mutf8-1.1.0.tar.gz), archive SHA256 `279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a`.
- `mutf8-1.1.0/mutf8/cmutf8.c`, lines 260–264; member SHA256 `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`.
  [Verified source reference 1](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L260-L264)
  [Frozen sdist](https://files.pythonhosted.org/packages/5c/74/bfce3ab421b39503c6cd11a6bc812a763154082a4f69d55831d762e58fcd/mutf8-1.1.0.tar.gz), archive SHA256 `279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a`.

## mypy

Frozen version: **2.4.0**. Result: **possible**.

Operation: mypyc-emitted str.__getitem__/strip primitives

Saved primitive registrations map Python string operations to CPyStr_GetItem and related local DATA consumers. Runtime code is byte-identical to librt in these files, but a shipped Python-visible native entry accepting the caller str was not proved here. Do not count bundled source symbol as verified independent repeat operation.

Implementation family: `mypyc_librt_string_runtime`.

Uncertainty: Compiled user code would qualify; no builds or imports performed and deployment/exposure is not assumed. Vendored StringWriter registration mirrors librt but not proof of importable mypy API.

- `mypy-2.4.0/mypyc/primitives/str_ops.py`, lines 127–152; member SHA256 `bc323787d381eca419d2634e4add68161471f93edfab1c186704e54b6458e882`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz), archive SHA256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.
- `mypy-2.4.0/mypyc/lib-rt/str_ops.c`, lines 98–142, 330–395; member SHA256 `bef63a64f41f8c6eb8f4c1cc12be2385f5a7e6d0bad0a47d85e5e2385a5658d4`.
  [Verified source reference 1](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L98-L142)
  [Verified source reference 2](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L330-L395)
  [Frozen sdist](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz), archive SHA256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## mysql-connector

Frozen version: **2.2.9**. Result: **possible**.

Operation: MySQL.convert_to_mysql; mysql-connector-python prepared-statement execute converter_str_fallback

Only a conditional dynamic-provider route: custom numeric __str__, or enabled converter_str_fallback, could return the same cached non-ASCII kind1 str on repeated calls. That would reuse a transient raw 1BYTE buffer; ordinary original-str inputs do not establish the requested pattern.

Implementation family: `mysql-connector-native-conversion`.

Uncertainties: No execution checked __str__ provider behavior; freshly produced formatting results cannot establish independent reuse. Raw 1BYTE assumptions are themselves ASCII/Latin1-sensitive. Both distributions share the native connector conversion lineage, not two independent families.

Borrow lifetime: Formatting-result DATA use is local to conversion. Modern str result is DECREFed immediately after byte copy. Prepared-statement Unicode parameters borrow UTF8 through execute, then bindings are freed.

Persistent or prepared alternative: Prepared statement retains SQL/server state, while string parameters are supplied anew each execution. This does not prove repeated borrowed FSR of original str arguments.

- `mysql-connector-2.2.9/src/mysql_capi.c`, lines 1672–1813; member SHA256 `d823465869086f9418dfcebb32894e18c52d3f3b342c9fff76ecfd2314d0d933`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/28/04/e40098f3730e75bbe36a338926f566ea803550a34fb50535499f4fc4787a/mysql-connector-2.2.9.tar.gz), archive SHA256 `1733e6ce52a049243de3264f1fbc22a852cb35458c4ad739ba88189285efdf32`.

## mysql-connector-python

Frozen version: **26.7.0**. Result: **possible**.

Operation: MySQL.convert_to_mysql; mysql-connector-python prepared-statement execute converter_str_fallback

Only a conditional dynamic-provider route: custom numeric __str__, or enabled converter_str_fallback, could return the same cached non-ASCII kind1 str on repeated calls. That would reuse a transient raw 1BYTE buffer; ordinary original-str inputs do not establish the requested pattern.

Implementation family: `mysql-connector-native-conversion`.

Uncertainties: No execution checked __str__ provider behavior; freshly produced formatting results cannot establish independent reuse. Raw 1BYTE assumptions are themselves ASCII/Latin1-sensitive. Both distributions share the native connector conversion lineage, not two independent families.

Borrow lifetime: Formatting-result DATA use is local to conversion. Modern str result is DECREFed immediately after byte copy. Prepared-statement Unicode parameters borrow UTF8 through execute, then bindings are freed.

Persistent or prepared alternative: Prepared statement retains SQL/server state, while string parameters are supplied anew each execution. This does not prove repeated borrowed FSR of original str arguments.

- `mysql_connector_python-26.7.0/src/mysql_capi.c`, lines 1972–2076, 3437–3445, 3461–3523; member SHA256 `e00d4cbed94b6378ee0d3370eec9ccc769cdf4b468c88cc033f2f2bd27a2dea7`.
  [Verified source reference 1](https://github.com/mysql/mysql-connector-python/blob/79f3435138368bbb1f86926c376952caa8411099/mysql-connector-python/src/mysql_capi.c#L1972-L2076)
  [Verified source reference 2](https://github.com/mysql/mysql-connector-python/blob/79f3435138368bbb1f86926c376952caa8411099/mysql-connector-python/src/mysql_capi.c#L3437-L3445)
  [Verified source reference 3](https://github.com/mysql/mysql-connector-python/blob/79f3435138368bbb1f86926c376952caa8411099/mysql-connector-python/src/mysql_capi.c#L3461-L3523)
  [Frozen sdist](https://files.pythonhosted.org/packages/f2/ce/a53b169388f8c6a595cfa9a653138381f3afef1d2af60f5c1972d015f52f/mysql_connector_python-26.7.0.tar.gz), archive SHA256 `d8ff5ee236ea46661ee639336323e124ed868e37f3ea991bdc5de5a146f39fd5`.

## numba

Frozen version: **0.68.0**. Result: **yes**.

Operation: UnicodeType Python-to-native unbox; a separately invoked compiled first-character operation

Unbox emits numba_extract_unicode on original Python str and creates new NRT MemInfo retaining owner/data. Separate boundary crossings create separate native ownership scopes; cheap native getitem can follow. Repeated native operations on one live unboxed value share that same view and must not be counted as separate rematerializations.

Implementation family: `numba-native-unbox-boundary`.

Uncertainties: Saved corpus lacks core/callwrapper.py full generated wrapper cleanup sequence, so exact last-owner destruction timing for every compiled signature is not proved here. Known MemInfo destruction releases owner; long-lived native values can pin lease.; No memoization in the verified unicode extraction/unbox emitted path; compilation/signature caching is distinct from caching input Unicode payload.

Persistent lease or owned copy alternative: Attach lease to NRT MemInfo: native owner/slices can retain representation across arbitrary native operations and survive beyond one call if native values are retained. PyObject ownership alone currently guarantees FSR pointer lifetime.

- `numba-0.68.0/numba/cpython/unicode.py`, lines 177–197; member SHA256 `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.
  [Verified source reference 1](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L177-L197)
  [Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz), archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
- `numba-0.68.0/numba/core/pythonapi.py`, lines 1108–1137; member SHA256 `62e3d815e9ce1168118ad9fd595ca468fb78e70023a83f2f5172680d05284c2e`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz), archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
- `numba-0.68.0/numba/_helperlib.c`, lines 1143–1170; member SHA256 `b30132af3313c175b639ab2b205b681848634afd5540e578f99af83a9d5c8076`.
  [Verified source reference 1](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/_helperlib.c#L1143-L1170)
  [Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz), archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
- `numba-0.68.0/numba/core/runtime/_nrt_python.c`, lines 18–36; member SHA256 `53334b5db0e22f1b00fc0b73426176561b746bb8c3a0779a210c440225835a8e`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz), archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
- `numba-0.68.0/numba/cpython/unicode.py`, lines 1821–1831; member SHA256 `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.
  [Verified source reference 1](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1821-L1831)
  [Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz), archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
- `numba-0.68.0/numba/cpython/unicode.py`, lines 1786–1811; member SHA256 `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.
  [Verified source reference 1](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1786-L1811)
  [Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz), archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

## numpy

Frozen version: **2.5.3**. Result: **yes**.

Operation: _multiarray_umath._load_from_filelike -> per-read stream provider

Each load entry creates a stream, provider gets Unicode chunk/line DATA, tokenizer retains borrowed buffer across row scans within that stream, and load closes/releases stream. Independent loads receiving the same original non-ASCII str can reacquire/rematerialize. NumPy Unicode scalar owned-UCS4 caching is a counterexample that retains representation.

Implementation family: `numpy-textreading-stream`.

Uncertainties: A custom filelike .read(size) returning arbitrarily large cached Unicode str is accepted by this native code (no size check), and max_rows can stop after first row, but normal provider chunk size is bounded; treat scalability of this variant as possible, not normal strong evidence.

Persistent lease or owned copy alternative: Provider can pin one lease until its chunk/line replacement or stream_close; Unicode scalar_value already owns an obval UCS4 copy across scalar lifetime. Array data uses owned buffers. Independent complete stream calls have no future-input-reuse signal.

- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/stream_pyobject.c`, lines 68–85; member SHA256 `14d865b71ddffe1975944670e27f34c28d4f8784e77f8b1ae069ba9e43c7195e`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/stream_pyobject.c#L68-L85)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/stream_pyobject.c`, lines 89–125; member SHA256 `14d865b71ddffe1975944670e27f34c28d4f8784e77f8b1ae069ba9e43c7195e`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/stream_pyobject.c#L89-L125)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/stream_pyobject.c`, lines 178–211; member SHA256 `14d865b71ddffe1975944670e27f34c28d4f8784e77f8b1ae069ba9e43c7195e`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/stream_pyobject.c#L178-L211)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/readtext.c`, lines 182–226; member SHA256 `d9270da4cef5e51a72b3ddc9acbe60df07fcaa8cfcbae0219cc232c5dfe26729`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/readtext.c#L182-L226)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/readtext.c`, lines 297–314; member SHA256 `d9270da4cef5e51a72b3ddc9acbe60df07fcaa8cfcbae0219cc232c5dfe26729`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/readtext.c#L297-L314)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/multiarraymodule.c`, lines 4797–4800; member SHA256 `1bfda5658c09101dd6557fcb6f235ed63b0f57cdf01b07fb9e3166a25f724c64`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/rows.c`, lines 204–230; member SHA256 `f8f80b9ee59e8551e111d6094326fe867726a2a9dc5d377e49389bcc4084919b`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 348–377; member SHA256 `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L348-L377)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/scalarapi.c`, lines 75–85; member SHA256 `a0079090d38f07c9f1ee7f9177b3e3e9c525b5498713ddd1252bea0a25620bb3`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/scalarapi.c#L75-L85)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
- `numpy-2.5.3/numpy/_core/src/multiarray/arraytypes.c.src`, lines 697–730; member SHA256 `382dc34bc41836700b065dec331559fd013a7a050b221bea79bd469a42ee88a9`.
  [Verified source reference 1](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/arraytypes.c.src#L697-L730)
  [Frozen sdist](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz), archive SHA256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## oracledb

Frozen version: **26.0.1**. Result: **yes**.

Operation: is_simple_sql_name / is_qualified_sql_name exposed extension functions; ConnectParams parsing via _parse_connect_string -> ConnectStringParser.parse

Repeated same untrimmed caller str with a non-whitespace invalid initial character can be rejected cheaply while a hypothetical full FSR rematerialization costs whole input each time. Parser lifetime prevents per-character churn but cannot identify last future independent validation call.

Implementation family: `oracledb-base-parser`.

Uncertainties: Name validators are described as internal functions by their docstrings; package-level public call graph invoking them was not found in saved context. ConnectParams route verified, but no runtime repeat frequency measured. strip may create a new input when whitespace is present; cheap same-object example excludes that.

Borrow lifetime: Borrow survives method boundaries inside the private parser object; it can be leased for that entire object lifetime. Name-check calls create a fresh NameParser and return bool; connect parsing creates a local parser per top-level call.

Persistent or prepared alternative: A lease on the parser solves all within-parser accesses. Saved connect/name providers nevertheless construct fresh parsers for independent calls; retaining a lease beyond their destruction needs a higher-level reuse cache/owner.

- `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 174–192, 974–1042; member SHA256 `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.
  [Verified source reference 1](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L174-L192)
  [Verified source reference 2](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L974-L1042)
  [Frozen sdist](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz), archive SHA256 `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.
- `oracledb-26.0.1/src/oracledb/impl/base/connect_params.pyx`, lines 352–383, 526–537; member SHA256 `340d01174bd34f279d70baf336433821a647a4052479edf31439a2f48adb0a1e`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz), archive SHA256 `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

## orjson

Frozen version: **3.12.0**. Result: **no**.

Operation: orjson.loads str input; string serialization via PyStrRef.as_str

No repeat-input FSR materialization established. Do not confuse output hash computation or UTF8-cache/raw-layout dependence with input FSR borrowing.

Implementation family: `orjson-utf8-input-output-hash`.

Borrow lifetime: Borrowed parser/serializer input slice is UTF8. Raw FSR hashing operates on owned freshly constructed output/cache-key objects.

Persistent or prepared alternative: Output key caches retain their constructed keys; input string view is UTF8 and requires no FSR lease under a UTF8 core.

- `orjson-3.12.0/src/ffi/pystrref/object.rs`, lines 14–25, 120–139, 170–228; member SHA256 `4ceba4b9f57151e7148638b8488041a57df42183d1acda3e5b4ad62c916261f1`.
  [Verified source reference 1](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L14-L25)
  [Verified source reference 2](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L120-L139)
  [Verified source reference 3](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L170-L228)
  [Frozen sdist](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz), archive SHA256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.
- `orjson-3.12.0/src/deserialize/input.rs`, lines 10–76; member SHA256 `1fbc1a059dcf8cbfdc5939a7a1470fa5997cbf8fba7b96ed0e2b26e516da6cba`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz), archive SHA256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## ormsgpack

Frozen version: **1.12.2**. Result: **no**.

Operation: packb string serialization; unpackb constructed string/key hash

No repeat-input FSR companion problem established by these paths. Shared stylistic ancestry with orjson is explicit but implementation/source family remains separately identified.

Implementation family: `ormsgpack-utf8-input-output-hash`.

Borrow lifetime: Input serializer slice is UTF8. OPT_REPLACE_SURROGATES uses AsEncodedString(UTF8,replace), creating owned bytes for serialization and DECREFing them after. Output keys may remain cached.

Persistent or prepared alternative: Persistent decode-key cache owns its created Unicode keys; no borrowed input FSR lease needs surviving independent serialization calls.

- `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs`, lines 83–130; member SHA256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.
  [Verified source reference 1](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L83-L130)
  [Frozen sdist](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz), archive SHA256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.
- `ormsgpack-1.12.2/src/ffi/unicode.rs`, lines 19–31; member SHA256 `70402315c3e18568c4aa89ea03df33d835e5677aeb52f5331757667abcd92f23`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz), archive SHA256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.
- `ormsgpack-1.12.2/src/serialize/str.rs`, lines 9–69; member SHA256 `78e25a11baf2a8905998e9141af960562544908b9d41253569e2903c133a9877`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz), archive SHA256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.
- `ormsgpack-1.12.2/src/deserialize/cache.rs`, lines 59–79; member SHA256 `d1ce263ac5cafdec553c6a22e02fa251e3ebaeb3470b5c1a37220dea659db98c`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz), archive SHA256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## pillow

Frozen version: **12.3.0**. Result: **yes**.

Operation: Font.getlength / getsize / render -> text_layout -> fallback

Independent font methods on the same str can reborrow/rematerialize after eviction. Full scan means extra conversion is a constant-factor/memory concern rather than the cheap-prefix asymptotic example. Avoid per-character acquire/evict inside READ_CHAR lowering.

Implementation family: `pillow-imagingft-layout`.

Borrow lifetime: Fallback access remains within synchronous text_layout/font method. Result glyph_info contains glyph indices/metrics and scalar cluster values, not a retained string DATA pointer; callers free it. Font object persists but does not prepare this text.

Persistent or prepared alternative: A lease can cover one layout call. Font reuse does not automatically preserve a lease for one particular text; a newly added prepared-layout/text cache could do so.

- `pillow-12.3.0/src/_imagingft.c`, lines 272–283, 405–493, 521–569, 1515–1520; member SHA256 `ac833fac38fb87d53b82e49327395ee0952134e09869df2ae206b74dd90d0a20`.
  [Verified source reference 1](https://github.com/python-pillow/Pillow/blob/bb1d8e8ab8d29048624d96e3ee53cecf7c13d13d/src/_imagingft.c#L272-L283)
  [Verified source reference 2](https://github.com/python-pillow/Pillow/blob/bb1d8e8ab8d29048624d96e3ee53cecf7c13d13d/src/_imagingft.c#L405-L493)
  [Verified source reference 3](https://github.com/python-pillow/Pillow/blob/bb1d8e8ab8d29048624d96e3ee53cecf7c13d13d/src/_imagingft.c#L521-L569)
  [Verified source reference 4](https://github.com/python-pillow/Pillow/blob/bb1d8e8ab8d29048624d96e3ee53cecf7c13d13d/src/_imagingft.c#L1515-L1520)
  [Frozen sdist](https://files.pythonhosted.org/packages/1c/3d/bb7fca845737cf9d7dbde16ed1843984665ff2e0a518f5db43e77ec540b9/pillow-12.3.0.tar.gz), archive SHA256 `3b8182a766685eaa002637e28b4ec8d6b18819a0c71f579bf0dbaa5830297cce`.

## polyleven

Frozen version: **0.11.0**. Result: **yes**.

Operation: polyleven.levenshtein(s1,s2,k=1..3)

Each accepted call creates local strbuf views; same long non-ASCII equal-length strings differing throughout take only bounded reads per finite edit model before rejecting above cutoff, though whole DATA is acquired first.

Implementation family: `polyleven-mbleven`.

Persistent lease or owned copy alternative: No prepared scorer or retained string view in this entry; representation retention requires caller/runtime cache or API redesign.

- `polyleven-0.11.0/polyleven.c`, lines 20–27; member SHA256 `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.
  [Verified source reference 1](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L20-L27)
  [Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz), archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.
- `polyleven-0.11.0/polyleven.c`, lines 88–135; member SHA256 `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.
  [Verified source reference 1](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L88-L135)
  [Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz), archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.
- `polyleven-0.11.0/polyleven.c`, lines 332–355; member SHA256 `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.
  [Verified source reference 1](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L332-L355)
  [Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz), archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.
- `polyleven-0.11.0/polyleven.c`, lines 357–382; member SHA256 `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.
  [Verified source reference 1](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L357-L382)
  [Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz), archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

## pyahocorasick

Frozen version: **2.3.1**. Result: **yes**.

Operation: Automaton.exists / __contains__ / match / get / longest_prefix; find_all(start,end); iter / iter_long as separate persistent providers

Strong conditional borrowed-FSR repeat case: repeated exists/match/get/longest_prefix calls with same kind4 str cannot infer last future query from local Input destruction. Lease through one iterator solves that iterator lifetime but not unrelated synchronous future calls.

Implementation family: `pyahocorasick-trie-input`.

Borrow lifetime: Synchronous query providers prepare Input locally then destroy_input at return, DECREFing borrowed input or freeing copy. Search iterator stores Input until destructor or set(), so can retain a representation lease across next() calls. Items iterator copies its pattern.

Persistent or prepared alternative: Automaton persists prepared trie state but does not retain synchronous query Input. Search iterators genuinely retain query input and offer a lease lifetime; retained items patterns are owned copies.

- `pyahocorasick-2.3.1/src/utils.c`, lines 146–170, 361–407; member SHA256 `65469c0f2300135739ecac734c3bc9784b5307cf3ec3f6bf45be945d0e24832c`.
  [Verified source reference 1](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/utils.c#L146-L170)
  [Verified source reference 2](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/utils.c#L361-L407)
  [Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz), archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.
- `pyahocorasick-2.3.1/src/Automaton.c`, lines 419–523, 653–719; member SHA256 `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`.
  [Verified source reference 1](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L419-L523)
  [Verified source reference 2](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L653-L719)
  [Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz), archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.
- `pyahocorasick-2.3.1/src/trie.c`, lines 140–174; member SHA256 `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`.
  [Verified source reference 1](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L140-L174)
  [Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz), archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.
- `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`, lines 65–141, 309–355; member SHA256 `c0e94d24881f38281da0e9a23d7a21741244b5f03ae958400b470a6a0c76da51`.
  [Verified source reference 1](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L65-L141)
  [Verified source reference 2](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L309-L355)
  [Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz), archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.
- `pyahocorasick-2.3.1/src/AutomatonItemsIter.c`, lines 26–98; member SHA256 `b010104775bbe531e249bfa36c00b9b7fe60e14bf1c939245916e805613524c3`.
  [Verified source reference 1](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonItemsIter.c#L26-L98)
  [Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz), archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

## pybase64

Frozen version: **1.5.0**. Result: **yes**.

Operation: b64decode / b64decode_as_bytearray -> pybase64_decode_impl

Independent b64decode calls reacquire one-byte Unicode data. Valid ordinary inputs are ASCII; custom byte altchars also admit Latin1 source bytes on the fast path.

Implementation family: `pybase64`.

Lifetime: Arguments retain in_object during the call, including output allocations and GIL-released libbase64 decoding. Raw pointer is local; output owns decoded bytes. There is no explicit FSR release API in current code.

Persistent state: Module configuration/SIMD state, not a prepared source string.

- `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 919–964; member SHA256 `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.
  [Verified source reference 1](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L919-L964)
  [Frozen sdist](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz), archive SHA256 `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.
- `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 1009–1043; member SHA256 `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.
  [Verified source reference 1](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L1009-L1043)
  [Frozen sdist](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz), archive SHA256 `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.
- `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 1165–1210; member SHA256 `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.
  [Verified source reference 1](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L1165-L1210)
  [Frozen sdist](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz), archive SHA256 `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.
- `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 1252–1278; member SHA256 `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.
  [Verified source reference 1](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L1252-L1278)
  [Frozen sdist](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz), archive SHA256 `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.
- `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 84–131; member SHA256 `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.
  [Verified source reference 1](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L84-L131)
  [Frozen sdist](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz), archive SHA256 `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.
- `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 1610–1616; member SHA256 `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.
  [Verified source reference 1](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L1610-L1616)
  [Frozen sdist](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz), archive SHA256 `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.

## pygame

Frozen version: **2.6.1**. Result: **no**.

Operation: Surface get_view argument converter _view_kind; equivalent pixelcopy converter.

The relevant primary consumer reads a length-one view-kind argument via READ_CHAR; it does not acquire or retain a raw FSR pointer.

Implementation family: `pygame`.

Lifetime: Scalar read is completed inside argument conversion; no raw pointer lifetime to release.

Persistent state: No prepared string state needed.

- `pygame-2.6.1/src_c/surface.c`, lines 2868–2884; member SHA256 `ad5433d3bfd6d4ab0f2efab910d47d3d852555fc1495063d2eb9fccf51dc5721`.
  [Verified source reference 1](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/surface.c#L2868-L2884)
  [Frozen sdist](https://files.pythonhosted.org/packages/49/cc/08bba60f00541f62aaa252ce0cfbd60aebd04616c0b9574f755b583e45ae/pygame-2.6.1.tar.gz), archive SHA256 `56fb02ead529cee00d415c3e007f75e0780c655909aaa8e8bf616ee09c9feb1f`.
- `pygame-2.6.1/src_c/surface.c`, lines 3458–3481; member SHA256 `ad5433d3bfd6d4ab0f2efab910d47d3d852555fc1495063d2eb9fccf51dc5721`.
  [Verified source reference 1](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/surface.c#L3458-L3481)
  [Frozen sdist](https://files.pythonhosted.org/packages/49/cc/08bba60f00541f62aaa252ce0cfbd60aebd04616c0b9574f755b583e45ae/pygame-2.6.1.tar.gz), archive SHA256 `56fb02ead529cee00d415c3e007f75e0780c655909aaa8e8bf616ee09c9feb1f`.
- `pygame-2.6.1/src_c/pixelcopy.c`, lines 122–146; member SHA256 `bae071baaf3de69c46a4c9932b594f69af2481c94e21446ac171034a359bd63d`.
  [Verified source reference 1](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/pixelcopy.c#L122-L146)
  [Frozen sdist](https://files.pythonhosted.org/packages/49/cc/08bba60f00541f62aaa252ce0cfbd60aebd04616c0b9574f755b583e45ae/pygame-2.6.1.tar.gz), archive SHA256 `56fb02ead529cee00d415c3e007f75e0780c655909aaa8e8bf616ee09c9feb1f`.

## pygeohash

Frozen version: **3.5.1**. Result: **no**.

Operation: geohash_decode / geohash_decode_exactly -> decode_call -> decode_from_utf8 -> decode_to_doubles.

decode/decode_exactly directly borrow compact ASCII data on independent calls; successful geohash length is at most twelve. Repeated pointer calls are verified, but their successful path is ASCII-only or length-one configuration; native UTF8 needs no full non-ASCII FSR conversion for that path.

Implementation family: `pygeohash`.

Lifetime: Raw pointer is local to decode; source args (or folded temporary) own string until scalar result returned.

Persistent state: Static decode table, not source string preparation/cache.

- `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 122–135; member SHA256 `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`.
  [Verified source reference 1](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L122-L135)
  [Frozen sdist](https://files.pythonhosted.org/packages/d1/fe/c7ade848a10c697d48f19859ec7a71a992b5597fd6ce8d5f16ba867853d5/pygeohash-3.5.1.tar.gz), archive SHA256 `d9a6ed89cfb023e0eba041a06ed676444413450be52e6a3b2c89b4a7908673ec`.
- `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 216–269; member SHA256 `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`.
  [Verified source reference 1](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L216-L269)
  [Frozen sdist](https://files.pythonhosted.org/packages/d1/fe/c7ade848a10c697d48f19859ec7a71a992b5597fd6ce8d5f16ba867853d5/pygeohash-3.5.1.tar.gz), archive SHA256 `d9a6ed89cfb023e0eba041a06ed676444413450be52e6a3b2c89b4a7908673ec`.
- `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 304–313; member SHA256 `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`.
  [Verified source reference 1](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L304-L313)
  [Frozen sdist](https://files.pythonhosted.org/packages/d1/fe/c7ade848a10c697d48f19859ec7a71a992b5597fd6ce8d5f16ba867853d5/pygeohash-3.5.1.tar.gz), archive SHA256 `d9a6ed89cfb023e0eba041a06ed676444413450be52e6a3b2c89b4a7908673ec`.

## pyjson5

Frozen version: **2.0.1**. Result: **yes**.

Operation: decode(data,maxdepth=None,some=False) -> _decode_unicode -> _decode_ucs1/2/4 -> _decode_all

decode(data, some=True) can parse a short initial value and stop with a long non-ASCII suffix unconsumed. Reader objects belong to this call, not a persistent scanner.

Implementation family: `pyjson5`.

Lifetime: Stack ReaderUCS holds and advances the borrowed pointer until decode returns. It is not stored in a public prepared object.

Persistent state: Global parser configuration and immutable lookup tables; each ReaderUCS is created anew.

- `pyjson5-2.0.1/src/_exports.pyx`, lines 14–56; member SHA256 `d687310af5345a2e5dfc7cb90433739f8873fb55c33ad4da14094061350edb8a`.
  [Verified source reference 1](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_exports.pyx#L14-L56)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz), archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.
- `pyjson5-2.0.1/src/_decoder.pyx`, lines 771–802; member SHA256 `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.
  [Verified source reference 1](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L771-L802)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz), archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.
- `pyjson5-2.0.1/src/_decoder.pyx`, lines 818–876; member SHA256 `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.
  [Verified source reference 1](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L818-L876)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz), archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.
- `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 34–59; member SHA256 `20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0`.
  [Verified source reference 1](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_reader_ucs.pyx#L34-L59)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz), archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## pymupdf

Frozen version: **1.28.2**. Result: **possible**.

Operation: Classic SWIG Font.text_length(text)/char_lengths(text); current Python Font.text_length.

Bundled src_classic Font text_length/char_lengths has per-call DATA/KIND loops; current src/__init__.py text_length uses Python iteration instead. Frozen sdist alone does not establish that classic route is the installed/default binding.

Implementation family: `pymupdf`.

Lifetime: Classic raw pointer is local while text argument remains alive; only scalar glyph values are handed to MuPDF. No source view cache. Default Python path has no explicit FSR acquisition.

Persistent state: Font/glyph state is persistent; source text/view is not cached by these functions.

- `pymupdf-1.28.2/src_classic/fitz_old.i`, lines 12477–12545; member SHA256 `1858ebd9508deeae1ca4769796e758f54c2c8f2f1edb1048ddb81b1a181156bf`.
  [Verified source reference 1](https://github.com/pymupdf/pymupdf/blob/12786d12b2962a1d77fd13b103162eddf749644c/src_classic/fitz_old.i#L12477-L12545)
  [Frozen sdist](https://files.pythonhosted.org/packages/a3/fb/b6761fa2d5266f2cdb24c3b91f4023070ab7848381417678e7a289a1d52a/pymupdf-1.28.2.tar.gz), archive SHA256 `5e0be7908a715aa20333caddd73f1d6f01e4cd0c26e869fa2dd0b7f344da2249`.
- `pymupdf-1.28.2/src/__init__.py`, lines 8508–8525; member SHA256 `e8cdb45ed0afa21f919cec30e69b7b572c3db7bc80d203e4e07e4c7ea2b19cce`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/a3/fb/b6761fa2d5266f2cdb24c3b91f4023070ab7848381417678e7a289a1d52a/pymupdf-1.28.2.tar.gz), archive SHA256 `5e0be7908a715aa20333caddd73f1d6f01e4cd0c26e869fa2dd0b7f344da2249`.

## pyobjc-core

Frozen version: **12.2.2**. Result: **possible**.

Operation: OC_PythonUnicode __realObject__, invoked by NSString length/characterAtIndex/getCharacters; separate PyObjC_is_ascii_string/prefix used by attribute slots.

Main NSString conversion keeps a cached realObject and may retain borrowed FSR through NoCopy initializers. This is not call-scoped release. Separate attribute-name comparisons are ephemeral but ASCII guarded.

Implementation family: `pyobjc-core`.

Lifetime: realObject is cached until proxy dealloc; value stays alive until cached NSString release. The safe migration must retain an FSR view for the proxy/NSString lifetime, not release after every NSString method call.

Persistent state: Persistent NSString proxy and underlying Python value; utilities themselves hold no prepared source state.

- `pyobjc_core-12.2.2/Modules/objc/OC_PythonUnicode.m`, lines 50–158; member SHA256 `262dd24e63ffd12211e087a69673392b8559c0629e1632751c34e8fb97e64bfc`.
  [Verified source reference 1](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/OC_PythonUnicode.m#L50-L158)
  [Frozen sdist](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz), archive SHA256 `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.
- `pyobjc_core-12.2.2/Modules/objc/objc_util.m`, lines 1474–1500; member SHA256 `c36a9c7bf3e23fe2a65ea0c7615f09b91160f6ba510de7f95df3615a0809eba3`.
  [Verified source reference 1](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/objc_util.m#L1474-L1500)
  [Frozen sdist](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz), archive SHA256 `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.
- `pyobjc_core-12.2.2/Modules/objc/method-accessor.m`, lines 400–439; member SHA256 `8ecbfa1802847039536880e3f86a19b613f8be4295c1ce83ade8094a8d52926f`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz), archive SHA256 `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.

## pyqt5

Frozen version: **5.15.11**. Result: **yes**.

Operation: QString %ConvertToTypeCode -> new QString(qpycore_PyObject_AsQString(sipPy))

Exposed QString mapped-type conversions independently acquire SIP Unicode data and create a QString value.

Implementation family: `Qt/SIP`.

Lifetime: Borrowed pointer is local to qpycore conversion. Returned QString owns its converted value; no prepared Python str/view cache appears in retained conversion source. Qt implementation is external and not re-fetched.

Persistent state: Resulting Qt QString may persist in caller/Qt; source conversion does not memoize it by Python str.

- `PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp`, lines 162–199; member SHA256 `fbca7258407b4ac067e09875a73d0130aa1a40ab006414685406ec56d8837533`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/0e/07/c9ed0bd428df6f87183fca565a79fee19fa7c88c7f00a7f011ab4379e77a/PyQt5-5.15.11.tar.gz), archive SHA256 `fda45743ebb4a27b4b1a51c6d8ef455c4c1b5d610c90d2934c7802b5c1557c52`.
- `PyQt5-5.15.11/sip/QtCore/qstring.sip`, lines 23–49; member SHA256 `4ab1b2b701dfb0761263bdcad6b5fa700cf872d3bbce87464edb6109858f66e6`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/0e/07/c9ed0bd428df6f87183fca565a79fee19fa7c88c7f00a7f011ab4379e77a/PyQt5-5.15.11.tar.gz), archive SHA256 `fda45743ebb4a27b4b1a51c6d8ef455c4c1b5d610c90d2934c7802b5c1557c52`.

## pyqt5-sip

Frozen version: **12.19.0**. Result: **possible**.

Operation: sip_api_unicode_data through SIP API table; used via sipUnicodeData alias in PyQt.

SIP exports a borrowed pointer getter; it cannot infer how long independent clients hold the view. Proven consumers are the PyQt QString conversions.

Implementation family: `Qt/SIP`.

Lifetime: No release or lease token exists in current ABI; raw pointer can escape to client. Provider cannot assume every receiver is call-scoped. The proven Qt receiver consumes it during conversion.

Persistent state: No source-pointer cache/lease bookkeeping in this getter.

- `pyqt5_sip-12.19.0/siplib.c`, lines 12901–12936; member SHA256 `7a6396e9b5285a1204074091a218f54f6e145d5b468cc046fc9f3b9751ee5573`.
  [Verified source reference 1](https://github.com/Python-SIP/sip/blob/07ca2f8fb253b11c73b5425f11a45e8f4641b6a6/sipbuild/module/source/12/19/siplib.c#L12901-L12936)
  [Frozen sdist](https://files.pythonhosted.org/packages/0d/9d/5179b8e619fe084218a87f963f1648cba4c5aa5bb98dd5661d2cbb9eb1e4/pyqt5_sip-12.19.0.tar.gz), archive SHA256 `71cacf1879da2cd3e50cb239e21673cfe02d358af70ab6768817c960428868c3`.

## pyqt6

Frozen version: **6.11.0**. Result: **yes**.

Operation: QString %ConvertToTypeCode -> new QString(qpycore_PyObject_AsQString(sipPy))

Exposed QString mapped-type conversions independently acquire SIP Unicode data and create a QString value.

Implementation family: `Qt/SIP`.

Lifetime: Borrowed pointer is local to qpycore conversion. Returned QString owns its converted value; no prepared Python str/view cache appears in retained conversion source. Qt implementation is external and not re-fetched.

Persistent state: Resulting Qt QString may persist in caller/Qt; source conversion does not memoize it by Python str.

- `pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp`, lines 131–147; member SHA256 `3b8abccbdaaa1aa82845e2c0d099d4ed7b8d675ba76431e08c0dcc02b166441a`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz), archive SHA256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.
- `pyqt6-6.11.0/sip/QtCore/qstring.sip`, lines 21–42; member SHA256 `a942925150d052b457ecf29136eb722038d8d496adf30d64efcaffc36b18769d`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz), archive SHA256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.

## pyqt6-sip

Frozen version: **13.12.0**. Result: **possible**.

Operation: sip_api_unicode_data through SIP API table; used via sipUnicodeData alias in PyQt.

SIP exports a borrowed pointer getter; it cannot infer how long independent clients hold the view. Proven consumers are the PyQt QString conversions.

Implementation family: `Qt/SIP`.

Lifetime: No release or lease token exists in current ABI; raw pointer can escape to client. Provider cannot assume every receiver is call-scoped. The proven Qt receiver consumes it during conversion.

Persistent state: No source-pointer cache/lease bookkeeping in this getter.

- `pyqt6_sip-13.12.0/sip_core.c`, lines 11442–11477; member SHA256 `ca9da3af9ad9a4d5ff98038f5319a414e43d2ee3986b71f3c08e4592990a15e8`.
  [Verified source reference 1](https://github.com/Python-SIP/sip/blob/07ca2f8fb253b11c73b5425f11a45e8f4641b6a6/sipbuild/module/source/13/12/sip_core.c#L11442-L11477)
  [Frozen sdist](https://files.pythonhosted.org/packages/d1/23/16c583dbb6b53e0494dfcf7d1a44778c82e324edda62326727b37f1a5b34/pyqt6_sip-13.12.0.tar.gz), archive SHA256 `a7ad45c1e3cec3a2473d37ea9870b6c3baeccc560298623c8eb59265714c06e2`.

## pyroscope-io

Frozen version: **1.2.5**. Result: **no**.

Operation: traceback_t / allocation-sampling path -> push_stacktrace_to_sample_no_refcount -> unicode_to_sv_no_alloc

Allocation sampling repeatedly reads existing code-name and filename str objects; direct pointer route is compact ASCII only. Repeated pointer calls are verified, but their successful path is ASCII-only or length-one configuration; native UTF8 needs no full non-ASCII FSR conversion for that path.

Implementation family: `pyroscope-io`.

Lifetime: Borrowed frame/code references own strings during synchronous sampling. C++ Sample interns each view through Rust STRING_TABLE; StringTable::add stores s.to_owned() on first insertion and returns ID. Sample frames hold interned IDs.

Persistent state: Interned output dictionary, not a Python FSR cache keyed by str identity.

- `pyroscope_io-1.2.5/cpp/_memalloc_tb.cpp`, lines 8–25; member SHA256 `c360b6a6190bef401e8c2d4bb8c9fa86a13cab14300533951406c275b81f85bc`.
  [Verified source reference 1](https://github.com/grafana/pyroscope-python/blob/080e93b039ea0ceb2a4bae907ec144b423cc2958/cpp/_memalloc_tb.cpp#L8-L25)
  [Frozen sdist](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz), archive SHA256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.
- `pyroscope_io-1.2.5/cpp/_memalloc_tb.cpp`, lines 71–113; member SHA256 `c360b6a6190bef401e8c2d4bb8c9fa86a13cab14300533951406c275b81f85bc`.
  [Verified source reference 1](https://github.com/grafana/pyroscope-python/blob/080e93b039ea0ceb2a4bae907ec144b423cc2958/cpp/_memalloc_tb.cpp#L71-L113)
  [Frozen sdist](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz), archive SHA256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.
- `pyroscope_io-1.2.5/cpp/Pyroscope.h`, lines 29–45; member SHA256 `59244f096076610a6d89d3cd8bad8396fbc5e1c69c2b153e2fbedbd835d6889a`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz), archive SHA256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.
- `pyroscope_io-1.2.5/cpp/Pyroscope.h`, lines 105–112; member SHA256 `59244f096076610a6d89d3cd8bad8396fbc5e1c69c2b153e2fbedbd835d6889a`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz), archive SHA256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.
- `pyroscope_io-1.2.5/rust/src/memory.rs`, lines 104–119; member SHA256 `f70d24b8b6f7d3c7c69bcabfee4fb5a7e933e28a3e40df0f267d9ddfe5372cdb`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz), archive SHA256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.
- `pyroscope_io-1.2.5/rust/src/encode/pprof.rs`, lines 345–370; member SHA256 `e4cbe481fcdfa0ed5f2246998655745ee8c3fb1c96b92d5ca93116151f04fc97`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz), archive SHA256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.

## pysam

Frozen version: **0.24.1**. Result: **yes**.

Operation: pysam.libcalignedsegment.reverse_complement(str)

Public reverse_complement obtains full length and delegates local borrowed DATA1/full Unicode iteration; pointer is call-scoped and result is owned. It accepts broad nonASCII strings (nonbase codepoints unchanged), so independent calls on same str are verified, but input is fully traversed. Other indexed reads in count_coverage use read.seq DNA ASCII and get_tag index0 uses internally-created length1/2 type string.

Implementation family: `pysam_reverse_complement`.

Uncertainty: DNA ASCII selected-position cases do not require a wide nonASCII FSR materialization under native UTF8; they are not a strong long-Unicode partial example.

- `pysam-0.24.1/pysam/libcalignedsegment.pyx`, lines 146–169, 184–212, 2685–2707; member SHA256 `b5a7e57d45c50764fc6ba34dfc5e697a8c37ced8b1597db1d58a72aeb52b34f9`.
  [Verified source reference 1](https://github.com/pysam-developers/pysam/blob/ba2e6c124398bdcd963db741d6f01164fed4f9b7/pysam/libcalignedsegment.pyx#L146-L169)
  [Verified source reference 2](https://github.com/pysam-developers/pysam/blob/ba2e6c124398bdcd963db741d6f01164fed4f9b7/pysam/libcalignedsegment.pyx#L184-L212)
  [Verified source reference 3](https://github.com/pysam-developers/pysam/blob/ba2e6c124398bdcd963db741d6f01164fed4f9b7/pysam/libcalignedsegment.pyx#L2685-L2707)
  [Frozen sdist](https://files.pythonhosted.org/packages/01/d0/e9271669f97ce454d1aa97f9ce0d3e84376295f352ad6c5d2c3998e38f66/pysam-0.24.1.tar.gz), archive SHA256 `90f612afccdb454d2447ecb5229266c6e7f991093deed4ed0a791db01f7fc994`.
- `pysam-0.24.1/pysam/libcalignmentfile.pyx`, lines 1578–1608; member SHA256 `312cbfefe9da01ea6c6e3b4f802f44e38b974d70733c6a151cfb2c924f5f6b15`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/01/d0/e9271669f97ce454d1aa97f9ce0d3e84376295f352ad6c5d2c3998e38f66/pysam-0.24.1.tar.gz), archive SHA256 `90f612afccdb454d2447ecb5229266c6e7f991093deed4ed0a791db01f7fc994`.

## rapidfuzz

Frozen version: **3.14.6**. Result: **yes**.

Operation: distance.metrics_cpp prefix_similarity/postfix_similarity; levenshtein_distance with default weights, processor=None, score_cutoff=0

Same original non-ASCII inputs are captured in local RF_String wrappers on each independent pair call. Long strings differing at first (Prefix/cutoff0) or last (Postfix) codepoint need only a mismatch read; immediate eviction adds whole-string materialization per call.

Implementation family: `rapidfuzz-engine`.

Persistent lease or owned copy alternative: process batch/generator keeps query/scorer across comparisons; cached scorer can own copies or retain a lease until scorer/generator destruction. Standalone pair entries provide no future-reuse boundary.

- `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp`, lines 110–165; member SHA256 `7365fa1397d9b9cfd85de296aab17f5b553f7ee7e5b85d7bc96d7c22901b1fcb`.
  [Verified source reference 1](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/cpp_common.hpp#L110-L165)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp`, lines 294–310; member SHA256 `7365fa1397d9b9cfd85de296aab17f5b553f7ee7e5b85d7bc96d7c22901b1fcb`.
  [Verified source reference 1](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/cpp_common.hpp#L294-L310)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.pxd`, lines 398–418; member SHA256 `540af9abf7f62facb74c46261f37bf4a132a27c51d6741d620cb85bdb495daeb`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics_cpp.pyx`, lines 1045–1078; member SHA256 `4dafe9d5b67bfffbbb730e6fd782a80b49c9632ec4d6e59d2337dc58e5e06368`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics_cpp.pyx`, lines 1121–1154; member SHA256 `4dafe9d5b67bfffbbb730e6fd782a80b49c9632ec4d6e59d2337dc58e5e06368`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics.hpp`, lines 1090–1095; member SHA256 `c1e6e2ea8e3b1dc41ea0f6dde8952f17e5d32906896d0c734a52d6d1e0906f6c`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics.hpp`, lines 1185–1191; member SHA256 `c1e6e2ea8e3b1dc41ea0f6dde8952f17e5d32906896d0c734a52d6d1e0906f6c`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance/Prefix_impl.hpp`, lines 23–27; member SHA256 `ff483568dee2fc4a14a21d49004c83fc0e94ff3ded85323562369598eb9bad0a`.
  [Verified source reference 1](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/distance/Prefix_impl.hpp#L23-L27)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance/Postfix_impl.hpp`, lines 23–27; member SHA256 `f24da62c37f46518d030db78bdfd0d0c571dfea9a72d3af06da0d2b3b199b20b`.
  [Verified source reference 1](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/distance/Postfix_impl.hpp#L23-L27)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/details/common_impl.hpp`, lines 38–81; member SHA256 `2d59c0f890ded1668a399e1b0d671727054540e9ed5ea3a9ba365483e1721293`.
  [Verified source reference 1](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/details/common_impl.hpp#L38-L81)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics_cpp.pyx`, lines 235–245; member SHA256 `4dafe9d5b67bfffbbb730e6fd782a80b49c9632ec4d6e59d2337dc58e5e06368`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics.hpp`, lines 5–13; member SHA256 `c1e6e2ea8e3b1dc41ea0f6dde8952f17e5d32906896d0c734a52d6d1e0906f6c`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein_impl.hpp`, lines 908–929; member SHA256 `2315a041cb04a8254e1c2e374b252b9a164716b0515a5502b72a287bfe2a71d3`.
  [Verified source reference 1](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/distance/Levenshtein_impl.hpp#L908-L929)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/details/Range.hpp`, lines 203–215; member SHA256 `86f3809dea9db6d935f64131b6294a6537f6c3bd1ddfd52977362f2d0df0b1ac`.
  [Verified source reference 1](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/details/Range.hpp#L203-L215)
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
- `rapidfuzz-3.14.6/src/rapidfuzz/process_cpp_impl.pyx`, lines 1283–1330; member SHA256 `e0ef32397f46650fd7d72c0a04c3572dc0c8d910511850737d8a59e3c281041f`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz), archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## regex

Frozen version: **2026.9.29**. Result: **yes** (regex baseline; excluded from other-package counts).

Operation: Pattern.match/search versus persistent Scanner.match/search

Each independent Pattern match/search creates local RE_State, borrows subject DATA and ends state after producing result. Small caller-selected match windows can be cheap on a long non-ASCII subject. Scanner retains RE_State until scanner destruction, so it can retain one lease across calls. A compiled Pattern alone caches pattern state, not every future subject view.

Implementation family: `regex-matching-engine`.

- `regex-2026.9.29/src/_regex.c`, lines 18230–18246, 18436–18439, 18490–18495, 18605–18635, 18733–18743, 20947–20954, 21023–21031, 21140–21154, 21622–21636; member SHA256 `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.
  [Verified source reference 1](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18230-L18246)
  [Verified source reference 2](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18436-L18439)
  [Verified source reference 3](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18490-L18495)
  [Verified source reference 4](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18605-L18635)
  [Verified source reference 5](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18733-L18743)
  [Verified source reference 6](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L20947-L20954)
  [Verified source reference 7](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L21023-L21031)
  [Verified source reference 8](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L21140-L21154)
  [Verified source reference 9](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L21622-L21636)
  [Frozen sdist](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz), archive SHA256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

## simplejson

Frozen version: **4.1.2**. Result: **yes**.

Operation: scanner_call(string,idx) -> scan_once_unicode; encoding and scanstring entrypoints are additional whole/range consumers.

The callable scanner is reusable configuration, not a prepared input/view object. scan_once(string,idx) independently gets DATA; successful null needs only four scalar reads.

Implementation family: `simplejson`.

Lifetime: pystr is supplied afresh as a call argument. The result includes next_idx; memo is cleared before return. No input/view field is populated on Scanner.

Persistent state: Scanner retains encoding, strict flag, callbacks, module, and key memo. scanner_new loads no input string; scanner_call clears memo. It does not cache the FSR.

- `simplejson-4.1.2/simplejson/_speedups.c`, lines 2263–2283; member SHA256 `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.
  [Verified source reference 1](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2263-L2283)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz), archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.
- `simplejson-4.1.2/simplejson/_speedups.c`, lines 2306–2352; member SHA256 `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.
  [Verified source reference 1](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2306-L2352)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz), archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.
- `simplejson-4.1.2/simplejson/_speedups.c`, lines 2380–2446; member SHA256 `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.
  [Verified source reference 1](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2380-L2446)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz), archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.
- `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 430–479; member SHA256 `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`.
  [Verified source reference 1](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L430-L479)
  [Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz), archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

## spacy

Frozen version: **3.8.16**. Result: **yes**.

Operation: spacy.matcher.levenshtein.levenshtein and levenshtein_compare(fuzzy=1..3)

Cython entry directly invokes vendored polyleven on supplied original strings; same threshold-small accepted dense-mismatch pattern and scoped strbuf borrowing as polyleven.

Implementation family: `polyleven-mbleven`.

Persistent lease or owned copy alternative: No persistent query view retained by this native pair wrapper. Higher-level matcher lifetime may supply a broader context but is not needed for exposed pair-call evidence.

- `spacy-3.8.16/spacy/matcher/levenshtein.pyx`, lines 10–27; member SHA256 `371220e1bc5092dd2e338ececfa46880083439faac91c61548bbc7591069fc27`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz), archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.
- `spacy-3.8.16/spacy/matcher/polyleven.c`, lines 49–56; member SHA256 `8d6cc95a1e44c334c3a5c1ffe3011f7e8d7a0afea27345d769a7db7d16abce0a`.
  [Verified source reference 1](https://github.com/explosion/spaCy/blob/26b4d1dc04a812f426e4bef3e8a1b6f159d6f048/spacy/matcher/polyleven.c#L49-L56)
  [Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz), archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.
- `spacy-3.8.16/spacy/matcher/polyleven.c`, lines 117–164; member SHA256 `8d6cc95a1e44c334c3a5c1ffe3011f7e8d7a0afea27345d769a7db7d16abce0a`.
  [Verified source reference 1](https://github.com/explosion/spaCy/blob/26b4d1dc04a812f426e4bef3e8a1b6f159d6f048/spacy/matcher/polyleven.c#L117-L164)
  [Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz), archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.
- `spacy-3.8.16/spacy/matcher/polyleven.c`, lines 361–384; member SHA256 `8d6cc95a1e44c334c3a5c1ffe3011f7e8d7a0afea27345d769a7db7d16abce0a`.
  [Verified source reference 1](https://github.com/explosion/spaCy/blob/26b4d1dc04a812f426e4bef3e8a1b6f159d6f048/spacy/matcher/polyleven.c#L361-L384)
  [Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz), archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.

## stpyv8

Frozen version: **13.1.201.22**. Result: **yes**.

Operation: JSObject __setattr__/__setitem__ -> SetAttr -> CPythonObject::Wrap -> WrapInternal -> ToString(py::object)

Python values crossing to JavaScript independently pass Unicode to ToString, which copies every scalar into an owned uint16 vector.

Implementation family: `stpyv8`.

Lifetime: Python object parameter owns str during full loop. Borrowed Python pointer does not escape; V8 receives vector storage, returning V8 string.

Persistent state: JS objects/context persist, converted JavaScript strings may persist; source view is not a prepared persistent object.

- `stpyv8-13.1.201.22/src/Wrapper.cpp`, lines 39–55; member SHA256 `8cdc0ede06dd5dd4c44e3f5c9f7e4926a7e6113e91036a955c39b2414cbe2303`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/17/69/26132fcd57f54a3f1f3688d2ab0a07dadc140b2d54edf28e44933ee7dccc/stpyv8-13.1.201.22.tar.gz), archive SHA256 `2bdbc7307dbf86cfc4bd0a11f0ae1f1c6f91d1b3366a7b409f9fc5d01f69441d`.
- `stpyv8-13.1.201.22/src/Wrapper.cpp`, lines 1115–1135; member SHA256 `8cdc0ede06dd5dd4c44e3f5c9f7e4926a7e6113e91036a955c39b2414cbe2303`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/17/69/26132fcd57f54a3f1f3688d2ab0a07dadc140b2d54edf28e44933ee7dccc/stpyv8-13.1.201.22.tar.gz), archive SHA256 `2bdbc7307dbf86cfc4bd0a11f0ae1f1c6f91d1b3366a7b409f9fc5d01f69441d`.
- `stpyv8-13.1.201.22/src/Wrapper.cpp`, lines 977–990; member SHA256 `8cdc0ede06dd5dd4c44e3f5c9f7e4926a7e6113e91036a955c39b2414cbe2303`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/17/69/26132fcd57f54a3f1f3688d2ab0a07dadc140b2d54edf28e44933ee7dccc/stpyv8-13.1.201.22.tar.gz), archive SHA256 `2bdbc7307dbf86cfc4bd0a11f0ae1f1c6f91d1b3366a7b409f9fc5d01f69441d`.
- `stpyv8-13.1.201.22/src/Utils.cpp`, lines 59–98; member SHA256 `a3a62ee3f1762efcefd7ce959e849d8614f0033f9d6fc39d3dc72821d84a426d`.
  [Verified source reference 1](https://github.com/cloudflare/stpyv8/blob/57e881c7fbe178c598262cb5da53d2bce1b41684/src/Utils.cpp#L59-L98)
  [Frozen sdist](https://files.pythonhosted.org/packages/17/69/26132fcd57f54a3f1f3688d2ab0a07dadc140b2d54edf28e44933ee7dccc/stpyv8-13.1.201.22.tar.gz), archive SHA256 `2bdbc7307dbf86cfc4bd0a11f0ae1f1c6f91d1b3366a7b409f9fc5d01f69441d`.

## tensorstore

Frozen version: **0.1.85**. Result: **no**.

Operation: pybind11 type_caster<ContiguousLayoutOrder>::load -> GetContiguousLayoutOrderOrThrow

The order type caster accepts a fresh Python object and reads one character, but successful values are only ASCII C/F and length must equal one. Repeated pointer calls are verified, but their successful path is ASCII-only or length-one configuration; native UTF8 needs no full non-ASCII FSR conversion for that path.

Implementation family: `tensorstore`.

Lifetime: View local to immediate scalar conversion; no prepared source or escaped pointer.

Persistent state: Array/layout objects persist, order source does not.

- `tensorstore-0.1.85/python/tensorstore/array_type_caster.h`, lines 234–248; member SHA256 `4432e637a6c6d2530b04d73e5628c07a35b618e8083b99f72854c9bdeb20ed98`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/26/16/a6530387ed22d07e974af2ef55e34fb19a7251a6911c85a0be029a4dcf9c/tensorstore-0.1.85.tar.gz), archive SHA256 `26698bded0278e98e0988eb8f7d76ad248762afc5f55a38b9122ffd1474e505f`.
- `tensorstore-0.1.85/python/tensorstore/array_type_caster.cc`, lines 311–335; member SHA256 `f96557908a14838ea7ce4031b3a2d2b7fbd4b1e501919ccda790d20f7ab4db54`.
  [Verified source reference 1](https://github.com/google/tensorstore/blob/bc4fbc11f69ee5379b2f611a934663006e1f573f/python/tensorstore/array_type_caster.cc#L311-L335)
  [Frozen sdist](https://files.pythonhosted.org/packages/26/16/a6530387ed22d07e974af2ef55e34fb19a7251a6911c85a0be029a4dcf9c/tensorstore-0.1.85.tar.gz), archive SHA256 `26698bded0278e98e0988eb8f7d76ad248762afc5f55a38b9122ffd1474e505f`.

## typed-ast

Frozen version: **1.5.5**. Result: **no**.

Operation: ast27/ast3 parser literal escape conversion

FSR pointer is acquired from freshly decoded temporary w created by decode_utf8 inside parse call. It is scanned forward completely and decref immediately. Repeating parse does not reacquire FSR of the caller same str here; source input is bytes/UTF8 and new w each time.

Implementation family: `cpython_ast_literal_decode_backport`.

Uncertainty: This conclusion is for reviewed raw FSR consumers; no broader guarantee about all high-level parsing costs.

- `typed_ast-1.5.5/ast27/Python/ast.c`, lines 3584–3647; member SHA256 `3c3e83a7094a8b63a7c64a5b5b0e07bca4c1e13d6e9a99d95016e424320b5277`.
  [Verified source reference 1](https://github.com/python/typed_ast/blob/567af09d8fc0c3607b90f96fce25b0cfdf25c8ff/ast27/Python/ast.c#L3584-L3647)
  [Frozen sdist](https://files.pythonhosted.org/packages/f9/7e/a424029f350aa8078b75fd0d360a787a273ca753a678d1104c5fa4f3072a/typed_ast-1.5.5.tar.gz), archive SHA256 `94282f7a354f36ef5dbce0ef3467ebf6a258e370ab33d5b40c249fa996e590dd`.
- `typed_ast-1.5.5/ast3/Python/ast.c`, lines 4459–4530; member SHA256 `12610d95a60145d701f50563c679110992ebd955299c6c4f415d6072cdd5a17a`.
  [Verified source reference 1](https://github.com/python/typed_ast/blob/567af09d8fc0c3607b90f96fce25b0cfdf25c8ff/ast3/Python/ast.c#L4459-L4530)
  [Frozen sdist](https://files.pythonhosted.org/packages/f9/7e/a424029f350aa8078b75fd0d360a787a273ca753a678d1104c5fa4f3072a/typed_ast-1.5.5.tar.gz), archive SHA256 `94282f7a354f36ef5dbce0ef3467ebf6a258e370ab33d5b40c249fa996e590dd`.

## ujson

Frozen version: **6.0.0**. Result: **no**.

Operation: Integer encode context -> PyNumber_ToBase(obj,10) -> PyLongToINTSTR -> Object_getStringValue.

The direct FSR pointer belongs to a newly generated decimal representation of a large integer, not the caller str reused in independent calls.

Implementation family: `ujson`.

Lifetime: TypeContext owns rawJSONValue until Object_endTypeContext decrefs it after copy into output. The caller does not hold this internal string for later reuse.

Persistent state: Per-value TypeContext; no caller string FSR prepared object.

- `ujson-6.0.0/src/ujson/encode.c`, lines 125–170; member SHA256 `da61bec77a4dc8bdfe194bc748125cdc647d53eacb2a2c22992fef42ba575135`.
  [Verified source reference 1](https://github.com/ultrajson/ultrajson/blob/12492c2deb0e60ac66da40dc15f06ba967ed3e0a/src/ujson/encode.c#L125-L170)
  [Frozen sdist](https://files.pythonhosted.org/packages/64/7c/e1fa3fb70b53192436d751b5cb671f0ee960baa188b8351a7fec735223d3/ujson-6.0.0.tar.gz), archive SHA256 `80e23393feb707582e0ad495c397a4477b646d08094d2df64f7316f9fafd8aae`.
- `ujson-6.0.0/src/ujson/encode.c`, lines 419–431; member SHA256 `da61bec77a4dc8bdfe194bc748125cdc647d53eacb2a2c22992fef42ba575135`.
  [Verified source reference 1](https://github.com/ultrajson/ultrajson/blob/12492c2deb0e60ac66da40dc15f06ba967ed3e0a/src/ujson/encode.c#L419-L431)
  [Frozen sdist](https://files.pythonhosted.org/packages/64/7c/e1fa3fb70b53192436d751b5cb671f0ee960baa188b8351a7fec735223d3/ujson-6.0.0.tar.gz), archive SHA256 `80e23393feb707582e0ad495c397a4477b646d08094d2df64f7316f9fafd8aae`.
- `ujson-6.0.0/src/ujson/encode.c`, lines 589–605; member SHA256 `da61bec77a4dc8bdfe194bc748125cdc647d53eacb2a2c22992fef42ba575135`.
  [Verified source reference 1](https://github.com/ultrajson/ultrajson/blob/12492c2deb0e60ac66da40dc15f06ba967ed3e0a/src/ujson/encode.c#L589-L605)
  [Frozen sdist](https://files.pythonhosted.org/packages/64/7c/e1fa3fb70b53192436d751b5cb671f0ee960baa188b8351a7fec735223d3/ujson-6.0.0.tar.gz), archive SHA256 `80e23393feb707582e0ad495c397a4477b646d08094d2df64f7316f9fafd8aae`.

## vercel-runtime

Frozen version: **0.23.2**. Result: **possible**.

Operation: Vendored MarkupSafe _speedups escape registration

Native source is byte-identical to MarkupSafe, including per-call borrowed DATA and complete escape passes, but native build/import exposure of the vendored code in this distribution was not established from retained sources. Do not count a second engine merely from this source copy.

Implementation family: `markupsafe-escape`.

- `vercel_runtime-0.23.2/src/vercel_runtime/_vendor/markupsafe/_speedups.c`, lines 75–98; member SHA256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.
  No verified permanent repository link for these ranges.
  [Frozen sdist](https://files.pythonhosted.org/packages/35/d6/c689033a2b3a2d69caf39e39f17ac0aba3f0d7570af0d22fc01eb0b367ca/vercel_runtime-0.23.2.tar.gz), archive SHA256 `252e517b6b7aadbd3edf5faac7bc387adde32b3801c1d5cfeb118ea29e89cb8a`.

## wcwidth

Frozen version: **0.9.1**. Result: **no**.

Operation: wcwidth(char); wcswidth / wcstwidth / width string methods

Do not claim full-FSR materialization from scalar ReadChar. Repeated owned-copy cost exists today and is not evidence of call-scoped borrowed FSR regression.

Implementation family: `wcwidth-scalar-and-owned-ucs4`.

Borrow lifetime: No borrowed FSR input view retained. Codepoint buffer is owned per call and freed after native width routine.

Persistent or prepared alternative: Could retain an owned prepared codepoint buffer via a new object, but this is existing copying behavior rather than a newly evicted borrowed representation.

- `wcwidth-0.9.1/wcwidth/_wcwidth_c.c`, lines 34–49, 470–481, 561–575; member SHA256 `fc6deed5f987ab2d64a4f8951c128dac6cbef6646eaa3c1ceb097d4b3673f199`.
  [Verified source reference 1](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L34-L49)
  [Verified source reference 2](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L470-L481)
  [Verified source reference 3](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L561-L575)
  [Frozen sdist](https://files.pythonhosted.org/packages/dc/ac/3a943d2792c9bb368aaa8b50121c0f778460ba2d7fbdc0a0366201d9e761/wcwidth-0.9.1.tar.gz), archive SHA256 `5823209b0d43af322ce698c689380d7c15ca31fa8e6e3be8459f27031bef0af5`.

## yarl

Frozen version: **1.25.1**. Result: **yes**.

Operation: _Quoter.__call__(val) / _Unquoter.__call__(val)

Quoter/Unquoter instances retain configuration but accept val anew each call. Quote acquires DATA, scans backward to first unsafe character, then scans forward; unquote searches percent then processes/copies ranges.

Implementation family: `yarl`.

Lifetime: Raw view remains local to operation and helper calls; output is Python Unicode, with safe/unchanged paths returning val. Writer memory is released in finally.

Persistent state: ASCII safe/protected/keep-escaped tables and flags, not source strings.

- `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 318–354; member SHA256 `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.
  [Verified source reference 1](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L318-L354)
  [Frozen sdist](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz), archive SHA256 `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.
- `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 356–418; member SHA256 `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.
  [Verified source reference 1](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L356-L418)
  [Frozen sdist](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz), archive SHA256 `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.
- `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 570–633; member SHA256 `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.
  [Verified source reference 1](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L570-L633)
  [Frozen sdist](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz), archive SHA256 `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.
- `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 635–715; member SHA256 `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.
  [Verified source reference 1](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L635-L715)
  [Frozen sdist](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz), archive SHA256 `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

