# numpy 2.5.3

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0091: UNICODE_getitem

**Disposition:** static use; `c_template_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `src` — external_numpy_ucs4_storage. src aliases array element ip, or aligned/native-endian owned copy; trailing zero code points trimmed.

**Length:** `ucs4len`; code-point elements (not bytes).

**Confirmed:** ITEMSIZE/sizeof(npy_ucs4), cast ip, optional byte swap, zero trimming. (numpy-2.5.3/numpy/_core/src/multiarray/arraytypes.c.src:643–672)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** No existing-PyUnicode fixed-width source required by this local constructor path; supplied external/constructed code-point representation still requires input decoding.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/arraytypes.c.src:643–674`; SHA-256 `382dc34bc41836700b065dec331559fd013a7a050b221bea79bd469a42ee88a9`.

`numpy-2.5.3/numpy/_core/src/multiarray/arraytypes.c.src` lines 671–671 ([verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/arraytypes.c.src#L671-L671))

```
    PyObject *ret = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, src, ucs4len);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0092: PyArray_Scalar NPY_UNICODE branch

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `buff` — external_numpy_ucs4_storage_copy. buff owns memcpy of dtype element bytes from data; byte swapped if necessary; itemsize rounded to4 after null-byte trimming.

**Length:** `itemsize / 4`; code-point elements (not bytes).

**Confirmed:** descr size and byteorder define array memory; new buffer copies data and swaps before constructor. (numpy-2.5.3/numpy/_core/src/multiarray/scalarapi.c:481–515)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** No existing-PyUnicode fixed-width source required by this local constructor path; supplied external/constructed code-point representation still requires input decoding.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/scalarapi.c:464–602`; SHA-256 `a0079090d38f07c9f1ee7f9177b3e3e9c525b5498713ddd1252bea0a25620bb3`.

`numpy-2.5.3/numpy/_core/src/multiarray/scalarapi.c` lines 514–514 ([verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/scalarapi.c#L514-L514))

```
        PyObject *u = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, buff, itemsize / 4);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0093: unicodetype_@form@ (repr,str)

**Disposition:** static use; `c_template_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `ip` — owned_unicode_ucs4_copy. ip is PyUnicode_AsUCS4Copy(self), caller-owned memory; trims trailing zero code points.

**Length:** `len`; code-point elements (not bytes).

**Confirmed:** Template form repr,str; owned UCS4 API copy created then released after constructor. (numpy-2.5.3/numpy/_core/src/multiarray/scalartypes.c.src:766–794)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Uses public PyUnicode_AsUCS4Copy export, not direct DATA/KIND; stable fixed-width export can convert from UTF8 internals.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Physical call expands into repr and str functions; count physical source expression once.

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/scalartypes.c.src:772–809`; SHA-256 `16645b91a059f3c11388cebf86e5a909991dc805d2442816954f26cc749ce38d`.

`numpy-2.5.3/numpy/_core/src/multiarray/scalartypes.c.src` lines 786–786 ([verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/scalartypes.c.src#L786-L786))

```
    new = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, ip, len);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0094: call_converter_function

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `str` — constructed_tokenizer_ucs4_field. str points into tokenizer owned field_buffer; length end-str excludes terminating marker.

**Length:** `length`; code-point elements (not bytes).

**Confirmed:** Converter wrapper passes field range. (numpy-2.5.3/numpy/_core/src/multiarray/textreading/conversions.c:364–377) Field source is ts.field_buffer+offset. (numpy-2.5.3/numpy/_core/src/multiarray/textreading/rows.c:378–386) Tokenizer allocates/grows field buffer and writes code points. (numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp:40–110)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Immediate buffer is tokenizer-owned UCS4; upstream stream reader can expose Python Unicode fixed-width DATA via typed getters and KIND.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Optional conversion to latin1 bytes after constructor for byte converters; custom Python converter or generic returned Unicode.

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/conversions.c:341–360`; SHA-256 `28435e05833020170fe7ac4a62dd45b6a6d4afe24423ba6c2a63e8db2a4ab611`.

`numpy-2.5.3/numpy/_core/src/multiarray/textreading/conversions.c` lines 344–344 (GitHub mapping not verified in saved evidence)

```
    PyObject *s = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, str, length);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0095: read_rows conversion-error branch

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `str` — constructed_tokenizer_ucs4_field. str = ts.field_buffer + fields[col].offset; end nextfieldoffset-1; length=end-str.

**Length:** `length`; code-point elements (not bytes).

**Confirmed:** Constructor builds error display field after parser failure. (numpy-2.5.3/numpy/_core/src/multiarray/textreading/rows.c:378–406) Tokenizer field storage owns copied code points. (numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp:40–110)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Immediate buffer is tokenizer-owned UCS4; upstream stream reader can expose Python Unicode fixed-width DATA via typed getters and KIND.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Only when selected field converter returns negative; diagnostic construction.

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/rows.c:167–470`; SHA-256 `f8f80b9ee59e8551e111d6094326fe867726a2a9dc5d377e49389bcc4084919b`.

`numpy-2.5.3/numpy/_core/src/multiarray/textreading/rows.c` lines 394–395 (GitHub mapping not verified in saved evidence)

```
                PyObject *string = PyUnicode_FromKindAndData(
                        PyUnicode_4BYTE_KIND, str, length);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0096: cfuncs['character_from_pyobj'] emitted C

**Disposition:** static use; `emitted_c_api_call`; `codegen`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `PyArray_BYTES(arr)` — external_numpy_ucs4_storage. First element of NumPy Unicode ndarray raw data, length 0 or 1; recursive ASCII conversion to Fortran character.

**Length:** `(PyArray_NBYTES(arr)>0?1:0)`; code-point elements (not bytes).

**Confirmed:** Executable generator dictionary stores C helper containing constructor; unicode ndarray guard and raw data argument. (numpy-2.5.3/numpy/f2py/cfuncs.py:798–835)

**Inference / unresolved:** Byteorder/alignment correction is absent in this local emitter; constructor assumes its input bytes are readable native-order UCS4. No unsupported-platform behavior executed.

**Upstream representation coupling:** No existing-PyUnicode fixed-width source required by this local constructor path; supplied external/constructed code-point representation still requires input decoding.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Generator-selected helper text emitted by f2py; no generator was executed. F2PY_IS_UNICODE_ARRAY branch only.

**Source:** `numpy-2.5.3/numpy/f2py/cfuncs.py:798–864`; SHA-256 `c6f0e44d6644416fe5a182b860541e2e1eee3f586413df14f39edb40e71097e0`.

`numpy-2.5.3/numpy/f2py/cfuncs.py` lines 820–823 (GitHub mapping not verified in saved evidence)

```
            PyObject* tmp = PyUnicode_FromKindAndData(
                              PyUnicode_4BYTE_KIND,
                              PyArray_BYTES(arr),
                              (PyArray_NBYTES(arr)>0?1:0));
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0117: npy_to_generic_with_converter

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (numpy-2.5.3/numpy/_core/src/multiarray/textreading/conversions.c:376–377)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/conversions.c:364–385`; SHA-256 `28435e05833020170fe7ac4a62dd45b6a6d4afe24423ba6c2a63e8db2a4ab611`.

`numpy-2.5.3/numpy/_core/src/multiarray/textreading/conversions.c` lines 376–377 (GitHub mapping not verified in saved evidence)

```
    PyObject *converted = call_converter_function(
            func, str, (size_t)(end - str), use_byte_converter);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0118: character_from_pyobj emitted C Unicode-array recursion

**Disposition:** non-use context; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (numpy-2.5.3/numpy/f2py/cfuncs.py:825–825)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** After conversion creates a Python Unicode scalar, recursion goes to ASCII export branch; this recursive invocation itself does not construct again.

**Source:** `numpy-2.5.3/numpy/f2py/cfuncs.py:798–864`; SHA-256 `c6f0e44d6644416fe5a182b860541e2e1eee3f586413df14f39edb40e71097e0`.

`numpy-2.5.3/numpy/f2py/cfuncs.py` lines 825–825 (GitHub mapping not verified in saved evidence)

```
                if (character_from_pyobj(v, tmp, errmess)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## K0119: character_from_pyobj emitted C sequence recursion

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (numpy-2.5.3/numpy/f2py/cfuncs.py:835–835)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** Sequence first item recursively converted; if item is Unicode ndarray, constructor path may be reached.

**Source:** `numpy-2.5.3/numpy/f2py/cfuncs.py:798–864`; SHA-256 `c6f0e44d6644416fe5a182b860541e2e1eee3f586413df14f39edb40e71097e0`.

`numpy-2.5.3/numpy/f2py/cfuncs.py` lines 835–835 (GitHub mapping not verified in saved evidence)

```
            if (character_from_pyobj(v, tmp, errmess)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
