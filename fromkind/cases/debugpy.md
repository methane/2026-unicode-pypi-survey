# debugpy 1.8.22

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0008: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:47721–47722`; SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

`debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c` lines 47695–47710 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L47695-L47710))

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

Closing lines 47719–47724 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L47719-L47724))

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 47695–47724 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## K0009: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:19856–19857`; SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

`debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c` lines 19830–19845 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L19830-L19845))

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

Closing lines 19854–19859 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L19854-L19859))

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 19830–19859 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## K0052: __pyx_pf_14_pydevd_bundle_13pydevd_cython_18fix_top_level_trace_and_get_trace_func

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_name. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:29893–29893`; SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

`debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c` lines 29875–29890 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L29875-L29890))

```
 *             name = name[i + 1 :]             # <<<<<<<<<<<<<<
 *         # remove ext
 *         i = name.rfind(".")
*/
      if (unlikely(__pyx_v_name == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
        __PYX_ERR(0, 1744, __pyx_L1_error)
      }
      __pyx_t_2 = __Pyx_PyLong_AddObjC(__pyx_v_i, __pyx_mstate_global->__pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1744, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_1 = (__pyx_t_2 == Py_None);
      if (__pyx_t_1) {
        __pyx_t_4 = 0;
      } else {
        __pyx_t_5 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_5 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 1744, __pyx_L1_error)
        __pyx_t_4 = __pyx_t_5;
```

Closing lines 29896–29901 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L29896-L29901))

```
      __pyx_t_2 = 0;

      /* "_pydevd_bundle/pydevd_cython.pyx":1743
 *         if j > i:
 *             i = j
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 29875–29901 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## K0053: __pyx_pf_14_pydevd_bundle_13pydevd_cython_18fix_top_level_trace_and_get_trace_func

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_name. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:29957–29957`; SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

`debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c` lines 29939–29954 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L29939-L29954))

```
 *             name = name[:i]             # <<<<<<<<<<<<<<
 * 
 *         if name == "threading":
*/
      if (unlikely(__pyx_v_name == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
        __PYX_ERR(0, 1748, __pyx_L1_error)
      }
      __Pyx_INCREF(__pyx_v_i);
      __pyx_t_2 = __pyx_v_i;
      __pyx_t_1 = (__pyx_t_2 == Py_None);
      if (__pyx_t_1) {
        __pyx_t_4 = PY_SSIZE_T_MAX;
      } else {
        __pyx_t_5 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_5 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 1748, __pyx_L1_error)
        __pyx_t_4 = __pyx_t_5;
```

Closing lines 29960–29965 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L29960-L29965))

```
      __pyx_t_2 = 0;

      /* "_pydevd_bundle/pydevd_cython.pyx":1747
 *         # remove ext
 *         i = name.rfind(".")
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 29939–29965 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## K0054: __pyx_f_18_pydevd_frame_eval_22pydevd_frame_evaluator_10ThreadInfo_initialize

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_basename. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:3523–3523`; SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

`debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c` lines 3505–3520 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L3505-L3520))

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

Closing lines 3526–3531 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L3526-L3531))

```
    __pyx_t_5 = 0;

    /* "_pydevd_frame_eval/pydevd_frame_evaluator.pyx":62
 *         if j > i:
 *             i = j
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 3505–3531 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## K0055: __pyx_f_18_pydevd_frame_eval_22pydevd_frame_evaluator_10ThreadInfo_initialize

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_basename. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:3587–3587`; SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

`debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c` lines 3569–3584 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L3569-L3584))

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

Closing lines 3590–3595 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L3590-L3595))

```
    __pyx_t_5 = 0;

    /* "_pydevd_frame_eval/pydevd_frame_evaluator.pyx":66
 *         # remove ext
 *         i = basename.rfind('.')
 *         if i >= 0:             # <<<<<<<<<<<<<<
```

Original reviewed range 3569–3595 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.
