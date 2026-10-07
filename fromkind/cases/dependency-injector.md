# dependency-injector 4.49.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0017: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `dependency_injector-4.49.1/src/dependency_injector/providers.c:172248–172249`; SHA-256 `71958fca07fb35d05dd281c134b84c13f0a5d17b317bc50ea66b21289b4d3565`.

`dependency_injector-4.49.1/src/dependency_injector/providers.c` lines 172222–172237 (GitHub mapping not verified in saved evidence)

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

Closing lines 172246–172251 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 172222–172251 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/d1/84/5e05c2997a196155b86446d48b9e5b2a055087c574746389fdc3c530f5b5/dependency_injector-4.49.1.tar.gz); archive SHA-256 `b4614fa3731ffec00a381aebc1d17317b0a3a407aa679f164a3ea03c347de691`.

## K0058: __pyx_f_19dependency_injector_9providers__resolve_config_env_markers

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_config_content. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `dependency_injector-4.49.1/src/dependency_injector/providers.c:13857–13857`; SHA-256 `71958fca07fb35d05dd281c134b84c13f0a5d17b317bc50ea66b21289b4d3565`.

`dependency_injector-4.49.1/src/dependency_injector/providers.c` lines 13839–13854 (GitHub mapping not verified in saved evidence)

```

    /* "dependency_injector/providers.pyx":98
 * 
 *         span_min, span_max = match.span()
 *         config_content = f"{config_content[:span_min]}{value}{config_content[span_max:]}"             # <<<<<<<<<<<<<<
 *     return config_content
 * 
*/
    __Pyx_INCREF(__pyx_v_span_min);
    __pyx_t_2 = __pyx_v_span_min;
    __pyx_t_7 = (__pyx_t_2 == Py_None);
    if (__pyx_t_7) {
      __pyx_t_13 = PY_SSIZE_T_MAX;
    } else {
      __pyx_t_14 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_14 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 98, __pyx_L1_error)
      __pyx_t_13 = __pyx_t_14;
```

Closing lines 13860–13865 (GitHub mapping not verified in saved evidence)

```
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_v_span_max);
    __pyx_t_11 = __pyx_v_span_max;
    __pyx_t_7 = (__pyx_t_11 == Py_None);
    if (__pyx_t_7) {
      __pyx_t_13 = 0;
```

Original reviewed range 13839–13865 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/d1/84/5e05c2997a196155b86446d48b9e5b2a055087c574746389fdc3c530f5b5/dependency_injector-4.49.1.tar.gz); archive SHA-256 `b4614fa3731ffec00a381aebc1d17317b0a3a407aa679f164a3ea03c347de691`.

## K0059: __pyx_f_19dependency_injector_9providers__resolve_config_env_markers

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_config_content. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `dependency_injector-4.49.1/src/dependency_injector/providers.c:13871–13871`; SHA-256 `71958fca07fb35d05dd281c134b84c13f0a5d17b317bc50ea66b21289b4d3565`.

`dependency_injector-4.49.1/src/dependency_injector/providers.c` lines 13853–13868 (GitHub mapping not verified in saved evidence)

```
      __pyx_t_14 = __Pyx_PyIndex_AsSsize_t(__pyx_t_2); if (unlikely((__pyx_t_14 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 98, __pyx_L1_error)
      __pyx_t_13 = __pyx_t_14;
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyUnicode_Substring(__pyx_v_config_content, 0, __pyx_t_13); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_value, __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_v_span_max);
    __pyx_t_11 = __pyx_v_span_max;
    __pyx_t_7 = (__pyx_t_11 == Py_None);
    if (__pyx_t_7) {
      __pyx_t_13 = 0;
    } else {
      __pyx_t_14 = __Pyx_PyIndex_AsSsize_t(__pyx_t_11); if (unlikely((__pyx_t_14 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 98, __pyx_L1_error)
      __pyx_t_13 = __pyx_t_14;
```

Closing lines 13874–13879 (GitHub mapping not verified in saved evidence)

```
    __pyx_t_10[1] = __pyx_t_3;
    __pyx_t_10[2] = __pyx_t_11;
    __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_10, 3, __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11), 127 | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) | __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11));
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
```

Original reviewed range 13853–13879 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/d1/84/5e05c2997a196155b86446d48b9e5b2a055087c574746389fdc3c530f5b5/dependency_injector-4.49.1.tar.gz); archive SHA-256 `b4614fa3731ffec00a381aebc1d17317b0a3a407aa679f164a3ea03c347de691`.
