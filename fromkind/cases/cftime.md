# cftime 1.6.6

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0018: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `cftime-1.6.6/src/cftime/_cftime.c:56172–56173`; SHA-256 `b8e860024cc4ab34afc7a6913a3dd815400e4148d896a469c99748aa5ed4b153`.

`cftime-1.6.6/src/cftime/_cftime.c` lines 56148–56163 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    length = __Pyx_PyUnicode_GET_LENGTH(text);
    #if !CYTHON_ASSUME_SAFE_SIZE
    if (unlikely(length < 0)) return NULL;
    #endif
    if (start < 0) {
        start += length;
        if (start < 0)
            start = 0;
    }
    if (stop < 0)
        stop += length;
    else if (stop > length)
```

Closing lines 56170–56175 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 56148–56175 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/16/6c/a441b7760eff421d7165fafbe124dd8babb34461aa1574dce5628e80137f/cftime-1.6.6.tar.gz); archive SHA-256 `7b2716b3dce97ba1740189c424ce97bd6f8e65391b7fe323c6f0f817f6a8ad56`.

## K0060: __pyx_f_6cftime_7_cftime__strftime

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_t_2. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `cftime-1.6.6/src/cftime/_cftime.c:36250–36250`; SHA-256 `b8e860024cc4ab34afc7a6913a3dd815400e4148d896a469c99748aa5ed4b153`.

`cftime-1.6.6/src/cftime/_cftime.c` lines 36232–36247 (GitHub mapping not verified in saved evidence)

```
 *     twodigityear = '%y' in fmt1
 *     if twodigityear:             # <<<<<<<<<<<<<<
 *         sites1 = _findall(s1, str(year)[-2:])
 *     else:
*/
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_twodigityear); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 1720, __pyx_L1_error)
  if (__pyx_t_7) {


    /* "cftime/_cftime.pyx":1721
 *     twodigityear = '%y' in fmt1
 *     if twodigityear:
 *         sites1 = _findall(s1, str(year)[-2:])             # <<<<<<<<<<<<<<
 *     else:
 *         sites1 = _findall(s1, str(year))
*/
```

Closing lines 36253–36258 (GitHub mapping not verified in saved evidence)

```
    __pyx_t_2 = __pyx_f_6cftime_7_cftime__findall(__pyx_v_s1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1721, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_v_sites1 = __pyx_t_2;
    __pyx_t_2 = 0;

```

Original reviewed range 36232–36258 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/16/6c/a441b7760eff421d7165fafbe124dd8babb34461aa1574dce5628e80137f/cftime-1.6.6.tar.gz); archive SHA-256 `7b2716b3dce97ba1740189c424ce97bd6f8e65391b7fe323c6f0f817f6a8ad56`.

## K0061: __pyx_f_6cftime_7_cftime__strftime

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_t_4. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `cftime-1.6.6/src/cftime/_cftime.c:36360–36360`; SHA-256 `b8e860024cc4ab34afc7a6913a3dd815400e4148d896a469c99748aa5ed4b153`.

`cftime-1.6.6/src/cftime/_cftime.c` lines 36342–36357 (GitHub mapping not verified in saved evidence)

```
 *     else:
*/
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_twodigityear); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 1726, __pyx_L1_error)
  if (__pyx_t_7) {


    /* "cftime/_cftime.pyx":1727
 *     s2 = time.strftime(fmt1, (year + 28,) + timetuple[1:])
 *     if twodigityear:
 *        sites2 = _findall(s2, str(year + 28)[-2:])             # <<<<<<<<<<<<<<
 *     else:
 *        sites2 = _findall(s2, str(year + 28))
*/
    __pyx_t_3 = __Pyx_PyLong_AddObjC(__pyx_v_year, __pyx_mstate_global->__pyx_int_28, 28, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1727, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_Unicode(__pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 1727, __pyx_L1_error)
```

Closing lines 36363–36368 (GitHub mapping not verified in saved evidence)

```
    __pyx_t_4 = __pyx_f_6cftime_7_cftime__findall(__pyx_v_s2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 1727, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_v_sites2 = __pyx_t_4;
    __pyx_t_4 = 0;

```

Original reviewed range 36342–36368 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/16/6c/a441b7760eff421d7165fafbe124dd8babb34461aa1574dce5628e80137f/cftime-1.6.6.tar.gz); archive SHA-256 `7b2716b3dce97ba1740189c424ce97bd6f8e65391b7fe323c6f0f817f6a8ad56`.

## K0062: __pyx_f_6cftime_7_cftime__strftime

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_syear. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `cftime-1.6.6/src/cftime/_cftime.c:36598–36598`; SHA-256 `b8e860024cc4ab34afc7a6913a3dd815400e4148d896a469c99748aa5ed4b153`.

`cftime-1.6.6/src/cftime/_cftime.c` lines 36580–36595 (GitHub mapping not verified in saved evidence)

```
  /* "cftime/_cftime.pyx":1742
 *         syear = "%04d" % (dt.year,)
 *     n=4
 *     if twodigityear:             # <<<<<<<<<<<<<<
 *         syear = syear[-2:]
 *         if dt.year < 0:
*/
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_twodigityear); if (unlikely((__pyx_t_7 < 0))) __PYX_ERR(0, 1742, __pyx_L1_error)
  if (__pyx_t_7) {


    /* "cftime/_cftime.pyx":1743
 *     n=4
 *     if twodigityear:
 *         syear = syear[-2:]             # <<<<<<<<<<<<<<
 *         if dt.year < 0:
```

Closing lines 36601–36606 (GitHub mapping not verified in saved evidence)

```
    __pyx_t_4 = 0;

    /* "cftime/_cftime.pyx":1744
 *     if twodigityear:
 *         syear = syear[-2:]
 *         if dt.year < 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 36580–36606 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/16/6c/a441b7760eff421d7165fafbe124dd8babb34461aa1574dce5628e80137f/cftime-1.6.6.tar.gz); archive SHA-256 `7b2716b3dce97ba1740189c424ce97bd6f8e65391b7fe323c6f0f817f6a8ad56`.
