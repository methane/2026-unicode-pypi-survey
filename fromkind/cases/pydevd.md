# pydevd 3.5.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0033: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `pydevd-3.5.0/_pydevd_bundle/pydevd_cython.c:47519–47520`; SHA-256 `9f57b23b07531601098ff7eedd635f7e5299ba76aa1f9844c36a43696d1b594b`.

`pydevd-3.5.0/_pydevd_bundle/pydevd_cython.c` lines 47493–47508 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    #if !CYTHON_COMPILING_IN_LIMITED_API
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    #endif
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
```

Closing lines 47517–47522 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 47493–47522 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/6f/ae/d8020162aed46bef5394ce6a4cb5afaa4c3307371ff70339e3e61dd9b109/pydevd-3.5.0.tar.gz); archive SHA-256 `2f0ef00281d6082a501cc3591fbb2e3ad32939007ebbe978f7c0cbfd95b71399`.

## K0034: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `pydevd-3.5.0/_pydevd_frame_eval/pydevd_frame_evaluator.c:19855–19856`; SHA-256 `3a705c0e793f9bcc1e8cf3afc0b3e8b5368b4e8dda7f58ef379a20a629030e02`.

`pydevd-3.5.0/_pydevd_frame_eval/pydevd_frame_evaluator.c` lines 19829–19844 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    #if !CYTHON_COMPILING_IN_LIMITED_API
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    #endif
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
```

Closing lines 19853–19858 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 19829–19858 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/6f/ae/d8020162aed46bef5394ce6a4cb5afaa4c3307371ff70339e3e61dd9b109/pydevd-3.5.0.tar.gz); archive SHA-256 `2f0ef00281d6082a501cc3591fbb2e3ad32939007ebbe978f7c0cbfd95b71399`.

## K0065: __pyx_pf_14_pydevd_bundle_13pydevd_cython_18fix_top_level_trace_and_get_trace_func

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_name. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `pydevd-3.5.0/_pydevd_bundle/pydevd_cython.c:29720–29720`; SHA-256 `9f57b23b07531601098ff7eedd635f7e5299ba76aa1f9844c36a43696d1b594b`.

`pydevd-3.5.0/_pydevd_bundle/pydevd_cython.c` lines 29702–29717 (GitHub mapping not verified in saved evidence)

```
 *             name = name[i + 1 :]             # <<<<<<<<<<<<<<
 *         # remove ext
 *         i = name.rfind(".")
*/
      if (unlikely(__pyx_v_name == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
        __PYX_ERR(0, 1740, __pyx_L1_error)
      }
      __pyx_t_2 = __Pyx_PyLong_AddObjC(__pyx_v_i, __pyx_mstate_global->__pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1740, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_1 = (__pyx_t_2 == Py_None);
      if (__pyx_t_1) {
        __pyx_t_4 = 0;
      } else {
        __pyx_t_5 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_5 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 1740, __pyx_L1_error)
        __pyx_t_4 = __pyx_t_5;
```

Closing lines 29723–29728 (GitHub mapping not verified in saved evidence)

```
      __pyx_t_2 = 0;

      /* "_pydevd_bundle/pydevd_cython.pyx":1739
 *         if j > i:
 *             i = j
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 29702–29728 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/6f/ae/d8020162aed46bef5394ce6a4cb5afaa4c3307371ff70339e3e61dd9b109/pydevd-3.5.0.tar.gz); archive SHA-256 `2f0ef00281d6082a501cc3591fbb2e3ad32939007ebbe978f7c0cbfd95b71399`.

## K0066: __pyx_pf_14_pydevd_bundle_13pydevd_cython_18fix_top_level_trace_and_get_trace_func

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_name. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `pydevd-3.5.0/_pydevd_bundle/pydevd_cython.c:29784–29784`; SHA-256 `9f57b23b07531601098ff7eedd635f7e5299ba76aa1f9844c36a43696d1b594b`.

`pydevd-3.5.0/_pydevd_bundle/pydevd_cython.c` lines 29766–29781 (GitHub mapping not verified in saved evidence)

```
 *             name = name[:i]             # <<<<<<<<<<<<<<
 * 
 *         if name == "threading":
*/
      if (unlikely(__pyx_v_name == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
        __PYX_ERR(0, 1744, __pyx_L1_error)
      }
      __Pyx_INCREF(__pyx_v_i);
      __pyx_t_2 = __pyx_v_i;
      __pyx_t_1 = (__pyx_t_2 == Py_None);
      if (__pyx_t_1) {
        __pyx_t_4 = PY_SSIZE_T_MAX;
      } else {
        __pyx_t_5 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_5 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 1744, __pyx_L1_error)
        __pyx_t_4 = __pyx_t_5;
```

Closing lines 29787–29792 (GitHub mapping not verified in saved evidence)

```
      __pyx_t_2 = 0;

      /* "_pydevd_bundle/pydevd_cython.pyx":1743
 *         # remove ext
 *         i = name.rfind(".")
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 29766–29792 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/6f/ae/d8020162aed46bef5394ce6a4cb5afaa4c3307371ff70339e3e61dd9b109/pydevd-3.5.0.tar.gz); archive SHA-256 `2f0ef00281d6082a501cc3591fbb2e3ad32939007ebbe978f7c0cbfd95b71399`.

## K0067: __pyx_f_18_pydevd_frame_eval_22pydevd_frame_evaluator_10ThreadInfo_initialize

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_basename. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `pydevd-3.5.0/_pydevd_frame_eval/pydevd_frame_evaluator.c:3522–3522`; SHA-256 `3a705c0e793f9bcc1e8cf3afc0b3e8b5368b4e8dda7f58ef379a20a629030e02`.

`pydevd-3.5.0/_pydevd_frame_eval/pydevd_frame_evaluator.c` lines 3504–3519 (GitHub mapping not verified in saved evidence)

```
 *             basename = basename[i + 1:]             # <<<<<<<<<<<<<<
 *         # remove ext
 *         i = basename.rfind('.')
*/
    if (unlikely(__pyx_v_basename == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
      __PYX_ERR(0, 63, __pyx_L1_error)
    }
    __pyx_t_5 = __Pyx_PyLong_AddObjC(__pyx_v_i, __pyx_mstate_global->__pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 63, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_1 = (__pyx_t_5 == Py_None);
    if (__pyx_t_1) {
      __pyx_t_4 = 0;
    } else {
      __pyx_t_6 = __Pyx_PyIndex_AsSsize_t(__pyx_t_5); if (unlikely((__pyx_t_6 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 63, __pyx_L1_error)
      __pyx_t_4 = __pyx_t_6;
```

Closing lines 3525–3530 (GitHub mapping not verified in saved evidence)

```
    __pyx_t_5 = 0;

    /* "_pydevd_frame_eval/pydevd_frame_evaluator.pyx":62
 *         if j > i:
 *             i = j
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 3504–3530 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/6f/ae/d8020162aed46bef5394ce6a4cb5afaa4c3307371ff70339e3e61dd9b109/pydevd-3.5.0.tar.gz); archive SHA-256 `2f0ef00281d6082a501cc3591fbb2e3ad32939007ebbe978f7c0cbfd95b71399`.

## K0068: __pyx_f_18_pydevd_frame_eval_22pydevd_frame_evaluator_10ThreadInfo_initialize

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_basename. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `pydevd-3.5.0/_pydevd_frame_eval/pydevd_frame_evaluator.c:3586–3586`; SHA-256 `3a705c0e793f9bcc1e8cf3afc0b3e8b5368b4e8dda7f58ef379a20a629030e02`.

`pydevd-3.5.0/_pydevd_frame_eval/pydevd_frame_evaluator.c` lines 3568–3583 (GitHub mapping not verified in saved evidence)

```
 *             basename = basename[:i]             # <<<<<<<<<<<<<<
 * 
 *         co_name = <str> frame_obj.f_code.co_name
*/
    if (unlikely(__pyx_v_basename == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
      __PYX_ERR(0, 67, __pyx_L1_error)
    }
    __Pyx_INCREF(__pyx_v_i);
    __pyx_t_5 = __pyx_v_i;
    __pyx_t_1 = (__pyx_t_5 == Py_None);
    if (__pyx_t_1) {
      __pyx_t_4 = PY_SSIZE_T_MAX;
    } else {
      __pyx_t_6 = __Pyx_PyIndex_AsSsize_t(__pyx_t_5); if (unlikely((__pyx_t_6 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 67, __pyx_L1_error)
      __pyx_t_4 = __pyx_t_6;
```

Closing lines 3589–3594 (GitHub mapping not verified in saved evidence)

```
    __pyx_t_5 = 0;

    /* "_pydevd_frame_eval/pydevd_frame_evaluator.pyx":66
 *         # remove ext
 *         i = basename.rfind('.')
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 3568–3594 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/6f/ae/d8020162aed46bef5394ce6a4cb5afaa4c3307371ff70339e3e61dd9b109/pydevd-3.5.0.tar.gz); archive SHA-256 `2f0ef00281d6082a501cc3591fbb2e3ad32939007ebbe978f7c0cbfd95b71399`.
