# PyUnicode_FromKindAndData in a frozen top-4,000 PyPI source survey

This static survey confirms **85 concrete constructor or constructor-emission sites in 32 packages**, plus **80 routed helper call sites** and **3 executable fault-injection forwarding expressions**. All 67 candidate files and 194 named tokens were reviewed. The three categories sum to 168 source sites; they are different layers of a call path and must not be interpreted as 168 independent algorithms or runtime calls.

The evidence supports keeping a constructor that accepts 1-, 2- and 4-byte integer-element buffers during a proposed UTF8 internal representation migration. Many inputs are independently constructed arrays or external library storage. Other sites borrow Python's current fixed-width representation directly; still others construct an independent output array after reading that representation upstream. These cases have different migration work. This compatibility conclusion is an inference from source patterns, not a measured performance result.

## Scope and coverage

The scope is the exact first 4,000 rows of the [public download-ranked snapshot](https://raw.githubusercontent.com/hugovk/top-pypi-packages/e6b5b398c1fcc783f593031f99bc2c772d64c6ef/top-pypi-packages.json), commit `e6b5b398c1fcc783f593031f99bc2c772d64c6ef`, updated **2026-10-01 12:41:32 UTC**, covering **2026-09-01 through 2026-09-30** calendar-month downloads from ClickHouse. The exact ordered [4,000 names](../data/top4000.txt) have SHA-256 `d3710dafb8a01c8f1b413d6188d5b9ae3670069d1bd4cc3b4456d1e36a557199`; the pinned complete ranking has SHA-256 `a0458d45ec5c696a482b44f94cc0eb83f7d5f3167e53c066b2a66cbfffa98358`.

Versions and one non-yanked sdist per selected current release were frozen during acquisition on 2026-10-02; the versions are acquisition-time versions, not necessarily September releases. The follow-up reuses those saved files and performs no new downloads or package execution.

| Outcome | Packages | Interpretation |
| --- | ---: | --- |
| Selected sdist scanned | 3,788 | Static retained-source scope available |
| No sdist in selected release | 211 | Unknown; no historical/wheel fallback |
| Metadata failure | 1 | Unknown; `aaaaaaaaa`, saved HTTP 404 |
| Total ranked scope | 4,000 | Every outcome recorded |

The retained corpus contains 131,701 logical native/Unicode-bearing text records in 583 packages (2,693,826,682 bytes), after inspection of 930,709 eligible regular text members. Native templates and nonnative Unicode-bearing text are included. There are 128,609 physical evidence files because some archive members share content. The remaining scanned packages have no retained native/Unicode-bearing records; that is a result within the original scan filter, not proof about omitted formats. [Coverage](data/coverage4000.csv) names every package, version, outcome and follow-up disposition. The 212 unavailable outcomes are never recorded as zero usage.

## Counting rules and results

An API expression inside an executable function or runtime provider counts even when its enclosing function is a definition. A declaration, symbol export, generated source-echo comment, import declaration, disabled comment, or constant-false type probe does not. Static presence under a compile guard is recorded without claiming the guard is enabled in distributed binaries.

| Site category | Sites | Interpretation |
| --- | ---: | --- |
| Ordinary concrete API expressions | 80 | Handwritten and generated C/C++/Cython runtime code |
| Concrete handwritten C template expressions | 2 | NumPy `.c.src`; expansions not multiplied |
| Concrete macro-dispatch expression | 1 | Pyahocorasick `F(PyUnicode_FromKindAndData)(...)` |
| C call emitted by a generator | 1 | NumPy f2py string template |
| LLVM call emitted by a generator | 1 | Numba C-API lookup followed by `builder.call` |
| Concrete subtotal | **85** | The input-kind/buffer tables below use this denominator |
| Routed helper call sites | **80** | 54 generated/runtime routes, 12 native routes, 14 C-native routes |
| Executable generic fault forwarding | **3** | Pyahocorasick 1 and APSW 2; no independent input algorithm |

APSW's additional `0 ? PyUnicode_FromKindAndData(__VA_ARGS__) : 0` expression is an unevaluated type probe and is excluded. Its two runtime forwarding branches remain visible separately. Five native wrapper branches known not to reach this constructor are negative records. Another 43 general NumPy scalar/macro/reader traces are supplied as [supplementary context](data/supplementary-wrapper-traces.json), with numeric/void exclusions and dtype conditions; they do not inflate the 85 concrete sites or the bounded 80 routed sites. No arbitrary transitive call graph is claimed.

The 38 packages with named candidates comprise the 32 consumers below and six without an observed consumer in retained source: `orjson`, `tokenizers`, `nanobind`, `pywinpty`, `rjsmin`, `rcssmin`. The first four contribute bindings, commented declarations, or export configuration. The minifiers contribute only obsolete compatibility macro definitions without an observed application invocation.

### Input kind at the 85 concrete sites

| Kind | Static sites |
| --- | --- |
| fixed_1 | 13 |
| fixed_2 | 6 |
| fixed_4 | 43 |
| dynamic_1_2_4 | 23 |

These are **input element widths**, not an output storage promise. A kind-1 buffer is an array of one-byte code-point values; it is not automatically a UTF8 byte stream. Kind-2 buffers do not automatically decode UTF16 surrogate pairs. Lengths count input elements, not byte lengths; for kind 1 these quantities happen to coincide. Each row in [sites.json](data/sites.json) preserves the exact length expression and its unit.

### Origin of the 85 concrete sites

| Origin | Static sites |
| --- | --- |
| handwritten | 47 |
| generated_cython | 34 |
| cython_template | 1 |
| codegen | 2 |
| vendor_or_compatibility | 1 |

The 47 handwritten sites include maintained Cython `.pyx` code and the two C templates. The 34 generated Cython sites and one Cython runtime-template site include **16 copies of the same substring provider family**. Thus package/site prevalence is not algorithm diversity. Srsly's JSON constructor is a vendored UltraJSON copy. MyPy and LibRT contain related runtime code and are counted as separate ranked distributions. Counts neither deduplicate cross-package families nor multiply generated template expansions.

### Complete consumer package list

| Package | Frozen version | Concrete | Routed | Fault forwarders | Concrete origin |
| --- | --- | --- | --- | --- | --- |
| [aiocsv](cases/aiocsv.md) | 1.4.1 | 2 | 0 | 0 | handwritten |
| [aiohttp](cases/aiohttp.md) | 3.14.3 | 1 | 6 | 0 | generated_cython |
| [apsw](cases/apsw.md) | 3.53.4.0 | 4 | 0 | 2 | handwritten |
| [asyncpg](cases/asyncpg.md) | 0.31.0 | 7 | 4 | 0 | generated_cython, handwritten |
| [biopython](cases/biopython.md) | 1.88 | 3 | 0 | 0 | handwritten |
| [cffi](cases/cffi.md) | 2.1.1 | 2 | 12 | 0 | handwritten |
| [cftime](cases/cftime.md) | 1.6.6 | 1 | 3 | 0 | generated_cython |
| [cython](cases/cython.md) | 3.3.0 | 1 | 0 | 0 | cython_template |
| [debugpy](cases/debugpy.md) | 1.8.22 | 2 | 4 | 0 | generated_cython |
| [dependency-injector](cases/dependency-injector.md) | 4.49.1 | 1 | 2 | 0 | generated_cython |
| [gensim](cases/gensim.md) | 4.4.0 | 1 | 1 | 0 | generated_cython |
| [gevent](cases/gevent.md) | 26.9.0 | 1 | 2 | 0 | generated_cython |
| [grapheme](cases/grapheme.md) | 0.6.0 | 1 | 1 | 0 | generated_cython |
| [levenshtein](cases/levenshtein.md) | 0.27.5 | 8 | 4 | 0 | generated_cython, handwritten |
| [librt](cases/librt.md) | 0.16.0 | 3 | 3 | 0 | handwritten |
| [lxml](cases/lxml.md) | 6.1.3 | 2 | 8 | 0 | generated_cython |
| [marisa-trie](cases/marisa-trie.md) | 1.4.1 | 1 | 1 | 0 | generated_cython |
| [mutf8](cases/mutf8.md) | 1.1.0 | 1 | 0 | 0 | handwritten |
| [mypy](cases/mypy.md) | 2.4.0 | 3 | 3 | 0 | handwritten |
| [numba](cases/numba.md) | 0.68.0 | 1 | 1 | 0 | codegen |
| [numpy](cases/numpy.md) | 2.5.3 | 6 | 2 | 0 | codegen, handwritten |
| [pyahocorasick](cases/pyahocorasick.md) | 2.3.1 | 1 | 0 | 1 | handwritten |
| [pydevd](cases/pydevd.md) | 3.5.0 | 2 | 4 | 0 | generated_cython |
| [pyjson5](cases/pyjson5.md) | 2.0.1 | 16 | 10 | 0 | generated_cython, handwritten |
| [pyqt5](cases/pyqt5.md) | 5.15.11 | 2 | 0 | 0 | handwritten |
| [pyqt6](cases/pyqt6.md) | 6.11.0 | 2 | 0 | 0 | handwritten |
| [pysam](cases/pysam.md) | 0.24.1 | 1 | 1 | 0 | generated_cython |
| [rapidfuzz](cases/rapidfuzz.md) | 3.14.6 | 5 | 6 | 0 | handwritten |
| [regex](cases/regex.md) | 2026.9.29 | 1 | 2 | 0 | handwritten |
| [srsly](cases/srsly.md) | 2.5.4 | 1 | 0 | 0 | vendor_or_compatibility |
| [ujson](cases/ujson.md) | 6.0.0 | 1 | 0 | 0 | handwritten |
| [yarl](cases/yarl.md) | 1.25.1 | 1 | 0 | 0 | handwritten |

## What the buffers establish

Sixteen concrete Cython substring provider copies receive borrowed Python FSR storage. `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` is byte-address arithmetic over the existing 1/2/4-byte element layout; it is not evidence that the input is UTF8. Their full-API branch reaches the constructor. Their limited-API branch delegates to `PyUnicode_Substring` and does not reach this API expression.

NumPy Unicode array/scalar constructors receive external UCS4 ndarray storage or an aligned/native-endian copy. NumPy reader conversion and asyncpg text-array parsing instead receive **owned `PyUnicode_AsUCS4Copy` exports**. Such exports are a public fixed-width conversion boundary; treating them as borrowed internal pointers would overstate their layout dependence.

RapidFuzz processing/edit application, Levenshtein medians, MyPy/LibRT StringWriter and case mapping, regex folding, Pyahocorasick key reconstruction, CSV/Yarl parsing, JSON decoding and modified-UTF8 decoding construct code-point arrays or scalars. Several upstream producers use `DATA/KIND/READ` or equivalent fixed-width readers, so an owned immediate buffer does not prove migration independence. Numba is mixed: the native payload can pin an unboxed Python Unicode FSR pointer or own native allocation, and boxing emits the constructor call without converting that payload first. Per-site evidence distinguishes these paths.

CFFI receives external `char16_t`/`char32_t`-style integer elements or local scalars. Its kind-2 constructor fast path excludes surrogate pairs; paired-surrogate processing follows another path. The four PyQt5/6 plugin-loader calls pass borrowed `QString.constData()` with `QString.length()`, a count of QChar/UTF16 code units. They do not combine surrogate pairs at this call. The separate general QString conversion code explicitly avoids this API and handles pairs itself; its references are supporting/non-use evidence. No runtime test establishes behavior for a particular plugin path.

These four calls pass the whole QString's `const QChar *` array, not a single QChar or a prior UCS4 conversion. By the constructor semantics, UTF16 values `D83D DE00` would produce two surrogate code-point values here, not one U+1F600 character. The call's presence is confirmed; this non-BMP consequence follows from the API contract and was not executed. [Qt details and exact locations](QT-DETAIL.md) distinguish these plugin calls from `qpycore_PyObject_FromQString`.

APSW's four kind-1 calls consume numeric ASCII or an ASCII-confirmed text slice from JSONB bytes. Asyncpg UUID arrays and Pyjson5 static metadata are other kind-1 cases. JSONB input being bytes does not make the general API a UTF8 decoder. The distinction must be preserved when interpreting or redesigning the API.

### Migration implications (inference)

Retaining an element-buffer constructor is compatible in principle with a UTF8 internal result: accept the specified integer elements, validate/convert them and preserve code-point and surrogate semantics. Its input need not have the result's storage format, and callers need not retain an output pointer. This survey does not establish allocation or conversion cost.

Borrowed-FSR substring consumers and the borrowed branch of Numba need a compatible fixed-width view/export or a rewritten operation. Generated Cython provider changes can address many packages through one upstream family. Independently allocated output buffers may continue to use the constructor, while their upstream FSR readers need separate changes. Owned public UCS4 exports form a different compatibility boundary from internal-data access. Switching kind-2 inputs to a UTF16 decoder would alter surrogate-pair interpretation; switching kind-1 inputs to UTF8 decoding would alter non-ASCII element interpretation. Those substitutions require explicit API semantics, not a pointer cast.

One Biopython diagnostic passes a `Py_UCS4` scalar address with a kind derived from the original string. The source pattern is confirmed; potential width/endianness sensitivity is an inference and has not been validated as a defect. It is retained in the evidence rather than generalized to normal constructors.

## Representative exact source excerpts

The following short excerpts are verbatim saved source. Package evidence pages retain each file SHA-256, sdist SHA-256/URL, physical LF ranges, compile guards, upstream traces and confirmed-versus-inferred claims. The machine-readable data include bounded exact snippets with explicit omitted intervals and original reviewed ranges. GitHub links appear only where the saved map proves immutable bytes or the entire mapped line range.

### Borrowed Python fixed-width slice

[aiohttp 3.14.3, K0001](cases/aiohttp.md) — `aiohttp-3.14.3/aiohttp/_http_parser.c:26566–26567`. Kind `dynamic_1_2_4`; length `stop-start` means codepoint_elements. A GitHub mapping for this range is unavailable in the saved map; the hashed sdist is the authoritative fallback.

```
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
```

Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

### External NumPy UCS4 storage

[numpy 2.5.3, K0091](cases/numpy.md) — `numpy-2.5.3/numpy/_core/src/multiarray/arraytypes.c.src:671–671`. Kind `fixed_4`; length `ucs4len` means code-point elements (not bytes). [Verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/arraytypes.c.src#L643-L674).

```
    PyObject *ret = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, src, ucs4len);
```

src aliases array element ip, or aligned/native-endian owned copy; trailing zero code points trimmed.

### Public owned UCS4 export

[asyncpg 0.31.0, K0006](cases/asyncpg.md) — `asyncpg-0.31.0/asyncpg/protocol/protocol.c:31544–31545`. Kind `fixed_4`; length `(__pyx_v_item_end - __pyx_v_item_start)` means four_byte_codepoint_elements. A GitHub mapping for this range is unavailable in the saved map; the hashed sdist is the authoritative fallback.

```
      __pyx_t_2 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, ((void *)__pyx_v_item_start), (__pyx_v_item_end - __pyx_v_item_start)); if (unlikely(!__pyx_t_2)) __PYX_ERR(2, 644, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
```

Py_UCS4 item_start/item_end delimit a range of the array_text allocation created by PyUnicode_AsUCS4Copy in textarray_decode. Parsing removes quoting/escapes in this allocation before reconstructing an item for its text codec.

### Constructed processed array, with upstream FSR reader

[rapidfuzz 3.14.6, K0105](cases/rapidfuzz.md) — `rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:13–13`. Kind `fixed_1`; length `(Py_ssize_t)proc_str.size()` means code-point elements (not bytes). [Verified immutable source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/utils_cpp.hpp#L5-L28).

```
        return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, proc_str.data(), (Py_ssize_t)proc_str.size());
```

default_process_copy creates vector<source element type>, transforms and trims it; vector data/size, not input sentence storage, enters constructor.

### Private StringWriter array, with upstream FSR reader

[mypy 2.4.0, K0098](cases/mypy.md) — `mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:542–542`. Kind `dynamic_1_2_4`; length `obj->len` means code-point elements (not bytes). [Verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/strings/librt_strings.c#L539-L543).

```
    return PyUnicode_FromKindAndData(obj->kind, obj->buf, obj->len);
```

Private embedded or allocated buffer, kind initialized1 and promoted2/4. append adds numeric code points; write copies/converts source Unicode into own buffer; len is element count.

### JIT-emitted call from a native string payload

[numba 0.68.0, K0108](cases/numba.md) — `numba-0.68.0/numba/core/pythonapi.py:1152–1154`. Kind `dynamic_1_2_4`; length `size` means code-point elements (not bytes). A GitHub mapping for this range is unavailable in the saved map; the hashed sdist is the authoritative fallback.

```
        fname = "PyUnicode_FromKindAndData"
        fn = self._get_function(fnty, name=fname)
        return self.builder.call(fn, [kind, string, size])
```

LLVM C function signature (int32, char*, Py_ssize_t) resolved by API-name string; box caller supplies native struct kind,data,length. Can alias unboxed Python Unicode or own NRT allocation.

### External QString QChar elements

[pyqt5 5.15.11, K0178](cases/pyqt5.md) — `PyQt5-5.15.11/designer/pluginloader.cpp:182–182`. Kind `fixed_2`; length `native_dir.length()` means QString UTF-16 code units / QChar elements; interpreted by the API as 16-bit code point values, not bytes and not decoded scalar count. A GitHub mapping for this range is unavailable in the saved map; the hashed sdist is the authoritative fallback.

```
    PyObject *dobj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, native_dir.constData(), native_dir.length());
```

Borrowed QString.constData() QChar array. Qt code treats each QChar::unicode() as ushort, checks paired high/low surrogates, and adjusts Python length when converting through its separate general QString converter. Here no such decoding step occurs: the raw 16-bit values are passed directly to the kind-2 constructor.

### External C integer elements

[cffi 2.1.1, K0134](cases/cffi.md) — `cffi-2.1.1/src/c/wchar_helper_3.h:17–17`. Kind `fixed_4`; length `size` means 32-bit codepoint elements. [Verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L14-L18).

```
    return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, w, size);
```

cffi_char32_t is uint32_t; size counts 32-bit elements. No UTF-8 bytes or Python FSR pointer is passed at observed callers.

### Decoded modified UTF8 code-point scratch array

[mutf8 1.1.0, K0164](cases/mutf8.md) — `mutf8-1.1.0/mutf8/cmutf8.c:130–130`. Kind `fixed_4`; length `cp_count` means Py_UCS4 codepoint elements, not input byte count. [Verified immutable source](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L12-L136).

```
        PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, cp_out, cp_count);
```

PyMem_Calloc(view.len,sizeof(Py_UCS4)) scratch; cp_count increments decoded scalars. Modified UTF8 special NUL and six-byte surrogate pair processed, isolated surrogate values possible. Input bytes received by y* buffer.


## Limits and evidence integrity

The survey is static. It measures saved source sites, not frequency, installation prevalence, reachable binaries, runtime activation, Unicode distributions, or migration performance. It makes no whole-program proof about dynamically computed symbol names, arbitrary transitive aliases, indirect calls, or sources absent from the retained corpus. The known-name and reviewed one-hop alias audit traversed all 131,701 retained records; 76 roots and 184 reference candidates were classified with no unresolved reviewed candidate. A wrapper consumer in an unretained nonnative file without Unicode indicators may be missed.

The original retention filters exclude document/data/web formats, binary/nested archives and nonnative text without Unicode indicators. A first-256-byte binary heuristic and UTF8 replacement decoding may miss unconventional encodings. There were **zero skipped eligible regular source members** in recovery. The original 71,683,718-byte PySpark `rocksdbjni-9.8.4.jar` omission is explicitly a binary dependency, not silently counted as source absence. A 128-MiB eligible-text guard existed but skipped no eligible source. **244 symlinks in 43 packages were not followed**; they and targets are enumerated in [coverage verification](data/coverage-verification.json). The discarded archives cannot be used to recover omitted members offline.

All 67 current candidate files were rehashed, all 194 named tokens reconciled, and snippet offsets use physical LF lines. The independent coverage audit reuses the prior completed full-corpus hash audit with unchanged input fingerprints; it independently rereads current candidates. The publisher separately hashes every evidence file it uses. Of 168 static-use records, 64 have verified GitHub mappings for the complete main range; shorter mapped snippets may also be linked. Unmapped evidence remains explicit, with immutable PyPI sdist URL and archive/member hashes. Absence of a verified GitHub link is not absence of source evidence.

See [methods and reproduction](METHODS.md), the [complete sites CSV](data/sites.csv), [JSON](data/sites.json), [token audit](data/token-audit.json), [file audit](data/file-audit.json), [coverage](data/coverage4000.csv), and [validation](../data/bundle-validation.json). These files describe the bounded evidence needed to assess the conclusions.
