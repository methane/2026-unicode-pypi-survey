# gevent 26.9.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0012: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `gevent-26.9.0/src/gevent/greenlet.c:27473–27474`; SHA-256 `70f2f5cea5e112badf4a7237713d5018f99cffc8ac9809473b8f415d268991bb`.

`gevent-26.9.0/src/gevent/greenlet.c` lines 27449–27464 (GitHub mapping not verified in saved evidence)

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

Closing lines 27471–27476 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 27449–27476 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## K0056: __pyx_f_6gevent_17_gevent_cgreenlet_8Greenlet__formatinfo

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_t_4. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `gevent-26.9.0/src/gevent/greenlet.c:9262–9262`; SHA-256 `70f2f5cea5e112badf4a7237713d5018f99cffc8ac9809473b8f415d268991bb`.

`gevent-26.9.0/src/gevent/greenlet.c` lines 9244–9259 (GitHub mapping not verified in saved evidence)

```
          if (__pyx_t_7 >= __pyx_temp) break;
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_4 = __Pyx_NewRef(PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_7));
        #else
        __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_2, __pyx_t_7);
        #endif
        ++__pyx_t_7;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 564, __pyx_L10_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_XDECREF_SET(__pyx_7genexpr__pyx_v_x, __pyx_t_4);
        __pyx_t_4 = 0;
        __pyx_t_4 = PyObject_Repr(__pyx_7genexpr__pyx_v_x); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 564, __pyx_L10_error)
        __Pyx_GOTREF(__pyx_t_4);
        if (unlikely(__pyx_t_4 == Py_None)) {
          PyErr_SetString(PyExc_TypeError, "\047NoneType\047 object is not subscriptable");
```

Closing lines 9265–9270 (GitHub mapping not verified in saved evidence)

```
        __Pyx_GIVEREF(__pyx_t_3);
        if (unlikely(__Pyx_ListComp_AppendAndDecref(__pyx_t_1, __pyx_t_3))) __PYX_ERR(0, 564, __pyx_L10_error)
        __pyx_t_3 = 0;
      }
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_7genexpr__pyx_v_x); __pyx_7genexpr__pyx_v_x = 0;
```

Original reviewed range 9244–9270 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## K0057: __pyx_f_6gevent_17_gevent_cgreenlet_8Greenlet__formatinfo

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_t_3. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `gevent-26.9.0/src/gevent/greenlet.c:9345–9345`; SHA-256 `70f2f5cea5e112badf4a7237713d5018f99cffc8ac9809473b8f415d268991bb`.

`gevent-26.9.0/src/gevent/greenlet.c` lines 9327–9342 (GitHub mapping not verified in saved evidence)

```
      while (1) {
        __pyx_t_10 = __Pyx_dict_iter_next(__pyx_t_2, __pyx_t_8, &__pyx_t_7, &__pyx_t_3, &__pyx_t_4, NULL, __pyx_t_9);
        if (unlikely(__pyx_t_10 == 0)) break;
        if (unlikely(__pyx_t_10 == -1)) __PYX_ERR(0, 566, __pyx_L18_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_XDECREF_SET(__pyx_8genexpr1__pyx_v_key, __pyx_t_3);
        __pyx_t_3 = 0;
        __Pyx_XDECREF_SET(__pyx_8genexpr1__pyx_v_value, __pyx_t_4);
        __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_FormatSimpleAndDecref(PyObject_Str(__pyx_8genexpr1__pyx_v_key), __pyx_mstate_global->__pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 566, __pyx_L18_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_3 = PyObject_Repr(__pyx_8genexpr1__pyx_v_value); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 566, __pyx_L18_error)
        __Pyx_GOTREF(__pyx_t_3);
        if (unlikely(__pyx_t_3 == Py_None)) {
          PyErr_SetString(PyExc_TypeError, "\047NoneType\047 object is not subscriptable");
```

Closing lines 9348–9353 (GitHub mapping not verified in saved evidence)

```
        __pyx_t_12[0] = __pyx_t_4;
        __pyx_t_12[1] = __pyx_mstate_global->__pyx_kp_u__9;
        __pyx_t_12[2] = __pyx_t_11;
        __pyx_t_13 = 1;
        #if __Pyx_PyUnicode_Join_CAN_USE_KIND_AND_LENGTH
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12[0]) + __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12[2]);
```

Original reviewed range 9327–9353 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.
