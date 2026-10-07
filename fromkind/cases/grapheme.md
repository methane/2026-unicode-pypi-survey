# grapheme 0.6.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0035: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `grapheme-0.6.0/grapheme/cython/finder.c:10705–10706`; SHA-256 `92a95c3f965b92e52899b4c279cd3c1069027c568758ddd4d218b2fa3bb930c1`.

`grapheme-0.6.0/grapheme/cython/finder.c` lines 10687–10702 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    length = __Pyx_PyUnicode_GET_LENGTH(text);
    if (start < 0) {
        start += length;
        if (start < 0)
            start = 0;
    }
    if (stop < 0)
        stop += length;
    else if (stop > length)
        stop = length;
    length = stop - start;
    if (length <= 0)
```

Closing lines 10705–10710 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#else
    return PyUnicode_FromUnicode(PyUnicode_AS_UNICODE(text)+start, stop-start);
#endif
}
```

Original reviewed range 10687–10710 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/ce/e7/bbaab0d2a33e07c8278910c1d0d8d4f3781293dfbc70b5c38197159046bf/grapheme-0.6.0.tar.gz); archive SHA-256 `44c2b9f21bbe77cfb05835fec230bd435954275267fea1858013b102f8603cca`.

## K0069: __pyx_f_8grapheme_6cython_6finder_c_length

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_string. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `grapheme-0.6.0/grapheme/cython/finder.c:6947–6947`; SHA-256 `92a95c3f965b92e52899b4c279cd3c1069027c568758ddd4d218b2fa3bb930c1`.

`grapheme-0.6.0/grapheme/cython/finder.c` lines 6929–6944 (GitHub mapping not verified in saved evidence)

```
 *     result = test_codepoint(FSM_default, get_group(string[0]))             # <<<<<<<<<<<<<<
 *     for codepoint in string[1:]:
 *         result = test_codepoint(result & SHOULD_BREAK_BIT_INVERSED, get_group(codepoint))
 */
  __pyx_t_3 = __Pyx_GetItemInt_Unicode(__pyx_v_string, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(__pyx_t_3 == (Py_UCS4)-1)) __PYX_ERR(0, 318, __pyx_L1_error)
  __pyx_v_result = __pyx_f_8grapheme_6cython_6finder_test_codepoint(__pyx_v_8grapheme_6cython_9constants_FSM_default, __pyx_f_8grapheme_6cython_23grapheme_property_group_c_get_group(__pyx_t_3));

  /* "grapheme/cython/finder.pyx":319
 *     break_count = 0
 *     result = test_codepoint(FSM_default, get_group(string[0]))
 *     for codepoint in string[1:]:             # <<<<<<<<<<<<<<
 *         result = test_codepoint(result & SHOULD_BREAK_BIT_INVERSED, get_group(codepoint))
 *         if result & SHOULD_BREAK_BIT:
 */
  if (unlikely(__pyx_v_string == Py_None)) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 6950–6955 (GitHub mapping not verified in saved evidence)

```
  for (__pyx_t_10 = 0; __pyx_t_10 < __pyx_t_6; __pyx_t_10++) {
    __pyx_t_5 = __pyx_t_10;
    __pyx_v_codepoint = __Pyx_PyUnicode_READ(__pyx_t_8, __pyx_t_7, __pyx_t_5);

    /* "grapheme/cython/finder.pyx":320
 *     result = test_codepoint(FSM_default, get_group(string[0]))
```

Original reviewed range 6929–6955 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/ce/e7/bbaab0d2a33e07c8278910c1d0d8d4f3781293dfbc70b5c38197159046bf/grapheme-0.6.0.tar.gz); archive SHA-256 `44c2b9f21bbe77cfb05835fec230bd435954275267fea1858013b102f8603cca`.
