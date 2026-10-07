# biopython 1.88

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0114: Aligner_str wildcard display

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `&self->wildcard` — stored_numeric_codepoint_scalar. &self->wildcard is address of native int field, not Unicode data pointer; setter extracts one code point with READ_CHAR.

**Length:** `1`; code-point elements (not bytes).

**Confirmed:** Aligner stores wildcard as int. (biopython-1.88/Bio/Align/_pairwisealigner.h:50–60) Setter permits one-character str or None and copies numeric code point. (biopython-1.88/Bio/Align/_pairwisealigner.c:3838–3856)

**Inference / unresolved:** Uses fixed4 against native int storage; assumes a4-byte native-endian int on supported build platforms.

**Upstream representation coupling:** Stored numeric scalar comes from PyUnicode_READ_CHAR API, not raw DATA/KIND alias; conversion API can preserve code-point semantics.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Only wildcard != -1; display call additionally requires no substitution matrix.

**Source:** `biopython-1.88/Bio/Align/_pairwisealigner.c:1826–1966`; SHA-256 `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`.

`biopython-1.88/Bio/Align/_pairwisealigner.c` lines 1864–1865 ([verified immutable source](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L1864-L1865))

```
            wildcard = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND,
                                                 &self->wildcard, 1);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz); archive SHA-256 `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

## K0115: Aligner_get_wildcard

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `&self->wildcard` — stored_numeric_codepoint_scalar. &self->wildcard is address of native int field, not Unicode data pointer; setter extracts one code point with READ_CHAR.

**Length:** `1`; code-point elements (not bytes).

**Confirmed:** Aligner stores wildcard as int. (biopython-1.88/Bio/Align/_pairwisealigner.h:50–60) Setter permits one-character str or None and copies numeric code point. (biopython-1.88/Bio/Align/_pairwisealigner.c:3838–3856)

**Inference / unresolved:** Uses fixed4 against native int storage; assumes a4-byte native-endian int on supported build platforms.

**Upstream representation coupling:** Stored numeric scalar comes from PyUnicode_READ_CHAR API, not raw DATA/KIND alias; conversion API can preserve code-point semantics.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Only wildcard != -1; display call additionally requires no substitution matrix.

**Source:** `biopython-1.88/Bio/Align/_pairwisealigner.c:3826–3835`; SHA-256 `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`.

`biopython-1.88/Bio/Align/_pairwisealigner.c` lines 3833–3833 ([verified immutable source](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L3833-L3833))

```
        return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, &self->wildcard, 1);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz); archive SHA-256 `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

## K0116: Array_set_alphabet duplicate-character diagnostic

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** dynamic_1_2_4; expression `kind`.

**Input:** `&character` — constructed_scalar_extracted_from_unicode. kind is PyUnicode_KIND(arg); character is a Py_UCS4 local loaded with PyUnicode_READ(kind,characters,i). &character is scalar storage, not borrowed original DATA.

**Length:** `1`; code-point elements (not bytes).

**Confirmed:** Kind comes from input alphabet; duplicate path constructs single local Py_UCS4. (biopython-1.88/Bio/Align/substitution_matrices/_arraycore.c:102–140)

**Inference / unresolved:** For kind1/2 the constructor reads first1/2 bytes of a4-byte scalar. This reproduces character on little-endian for in-range values but is endian-sensitive; static inference only, not an executed failure.

**Upstream representation coupling:** Constructor scalar is copied from source Unicode READ; upstream fixed-width read separate from diagnostic constructor.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Only duplicate character in Unicode alphabet; size1 diagnostic, independent from normal accepted-input constructor paths.

**Source:** `biopython-1.88/Bio/Align/substitution_matrices/_arraycore.c:58–156`; SHA-256 `c18c8d807a578440746374b572e77badca2df191236cf3c3be459239c4739a3d`.

`biopython-1.88/Bio/Align/substitution_matrices/_arraycore.c` lines 133–133 ([verified immutable source](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/substitution_matrices/_arraycore.c#L133-L133))

```
                PyObject* c = PyUnicode_FromKindAndData(kind, &character, 1);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz); archive SHA-256 `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.
