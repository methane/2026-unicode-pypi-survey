# aiohttp 3.14.3

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0001: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:26566–26567`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 26540–26555 (GitHub mapping not verified in saved evidence)

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

Closing lines 26564–26569 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 26540–26569 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.

## K0037: __pyx_f_7aiohttp_12_http_parser_17HttpRequestParser__on_status_complete

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_self->__pyx_base._path. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:14197–14197`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 14179–14194 (GitHub mapping not verified in saved evidence)

```
 *                         path = self._path
 *                         fragment = ""
*/
          goto __pyx_L11;
        }

        /* "aiohttp/_http_parser.pyx":741
 *                         fragment = ""
 *                     else:
 *                         path = self._path[0: idx2]             # <<<<<<<<<<<<<<
 *                         fragment = self._path[idx2+1:]
 * 
*/
        /*else*/ {
          if (unlikely(__pyx_v_self->__pyx_base._path == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 14200–14205 (GitHub mapping not verified in saved evidence)

```
          __pyx_t_3 = 0;

          /* "aiohttp/_http_parser.pyx":742
 *                     else:
 *                         path = self._path[0: idx2]
 *                         fragment = self._path[idx2+1:]             # <<<<<<<<<<<<<<
```

Original reviewed range 14179–14205 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.

## K0038: __pyx_f_7aiohttp_12_http_parser_17HttpRequestParser__on_status_complete

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_self->__pyx_base._path. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:14213–14213`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 14195–14210 (GitHub mapping not verified in saved evidence)

```
            __PYX_ERR(0, 741, __pyx_L5_error)
          }
          __pyx_t_3 = __Pyx_PyUnicode_Substring(__pyx_v_self->__pyx_base._path, 0, __pyx_v_idx2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 741, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_v_path = ((PyObject*)__pyx_t_3);
          __pyx_t_3 = 0;

          /* "aiohttp/_http_parser.pyx":742
 *                     else:
 *                         path = self._path[0: idx2]
 *                         fragment = self._path[idx2+1:]             # <<<<<<<<<<<<<<
 * 
 *                 else:
*/
          if (unlikely(__pyx_v_self->__pyx_base._path == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 14216–14221 (GitHub mapping not verified in saved evidence)

```
          __pyx_t_3 = 0;
        }
        __pyx_L11:;

        /* "aiohttp/_http_parser.pyx":734
 *                 # https://datatracker.ietf.org/doc/html/rfc7230#section-5.3.1
```

Original reviewed range 14195–14221 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.

## K0039: __pyx_f_7aiohttp_12_http_parser_17HttpRequestParser__on_status_complete

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_self->__pyx_base._path. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:14242–14242`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 14224–14239 (GitHub mapping not verified in saved evidence)

```
 *                     query = ""
 *                     idx2 = self._path.find("#")
*/
        goto __pyx_L10;
      }

      /* "aiohttp/_http_parser.pyx":745
 * 
 *                 else:
 *                     path = self._path[0:idx1]             # <<<<<<<<<<<<<<
 *                     idx1 += 1
 *                     idx2 = self._path.find("#", idx1)
*/
      /*else*/ {
        if (unlikely(__pyx_v_self->__pyx_base._path == Py_None)) {
          PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 14245–14250 (GitHub mapping not verified in saved evidence)

```
        __pyx_t_3 = 0;

        /* "aiohttp/_http_parser.pyx":746
 *                 else:
 *                     path = self._path[0:idx1]
 *                     idx1 += 1             # <<<<<<<<<<<<<<
```

Original reviewed range 14224–14250 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.

## K0040: __pyx_f_7aiohttp_12_http_parser_17HttpRequestParser__on_status_complete

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_self->__pyx_base._path. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:14295–14295`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 14277–14292 (GitHub mapping not verified in saved evidence)

```
 *                     if idx2 == -1:             # <<<<<<<<<<<<<<
 *                         query = self._path[idx1:]
 *                         fragment = ""
*/
        __pyx_t_2 = (__pyx_v_idx2 == -1L);
        if (__pyx_t_2) {

          /* "aiohttp/_http_parser.pyx":749
 *                     idx2 = self._path.find("#", idx1)
 *                     if idx2 == -1:
 *                         query = self._path[idx1:]             # <<<<<<<<<<<<<<
 *                         fragment = ""
 *                     else:
*/
          if (unlikely(__pyx_v_self->__pyx_base._path == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 14298–14303 (GitHub mapping not verified in saved evidence)

```
          __pyx_t_3 = 0;

          /* "aiohttp/_http_parser.pyx":750
 *                     if idx2 == -1:
 *                         query = self._path[idx1:]
 *                         fragment = ""             # <<<<<<<<<<<<<<
```

Original reviewed range 14277–14303 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.

## K0041: __pyx_f_7aiohttp_12_http_parser_17HttpRequestParser__on_status_complete

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_self->__pyx_base._path. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:14332–14332`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 14314–14329 (GitHub mapping not verified in saved evidence)

```
 *                         query = self._path[idx1:]
 *                         fragment = ""
*/
          goto __pyx_L12;
        }

        /* "aiohttp/_http_parser.pyx":752
 *                         fragment = ""
 *                     else:
 *                         query = self._path[idx1: idx2]             # <<<<<<<<<<<<<<
 *                         fragment = self._path[idx2+1:]
 * 
*/
        /*else*/ {
          if (unlikely(__pyx_v_self->__pyx_base._path == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 14335–14340 (GitHub mapping not verified in saved evidence)

```
          __pyx_t_3 = 0;

          /* "aiohttp/_http_parser.pyx":753
 *                     else:
 *                         query = self._path[idx1: idx2]
 *                         fragment = self._path[idx2+1:]             # <<<<<<<<<<<<<<
```

Original reviewed range 14314–14340 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.

## K0042: __pyx_f_7aiohttp_12_http_parser_17HttpRequestParser__on_status_complete

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_self->__pyx_base._path. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `aiohttp-3.14.3/aiohttp/_http_parser.c:14348–14348`; SHA-256 `ebd8db7ea95ea2d9cefccaaf24d4703557bd4284968db551eba1923f3468aa7c`.

`aiohttp-3.14.3/aiohttp/_http_parser.c` lines 14330–14345 (GitHub mapping not verified in saved evidence)

```
            __PYX_ERR(0, 752, __pyx_L5_error)
          }
          __pyx_t_3 = __Pyx_PyUnicode_Substring(__pyx_v_self->__pyx_base._path, __pyx_v_idx1, __pyx_v_idx2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 752, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_v_query = ((PyObject*)__pyx_t_3);
          __pyx_t_3 = 0;

          /* "aiohttp/_http_parser.pyx":753
 *                     else:
 *                         query = self._path[idx1: idx2]
 *                         fragment = self._path[idx2+1:]             # <<<<<<<<<<<<<<
 * 
 *                 self._url = URL.build(
*/
          if (unlikely(__pyx_v_self->__pyx_base._path == Py_None)) {
            PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 14351–14356 (GitHub mapping not verified in saved evidence)

```
          __pyx_t_3 = 0;
        }
        __pyx_L12:;
      }
      __pyx_L10:;

```

Original reviewed range 14330–14356 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/58/d9/22ce5786ac0c1653ae8b6c23bded02c1686d11f0dbb45b31ce128e0df985/aiohttp-3.14.3.tar.gz); archive SHA-256 `9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc`.
