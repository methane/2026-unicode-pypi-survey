# asyncpg 0.31.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0004: __pyx_pf_7asyncpg_7pgproto_7pgproto_4UUID_4__str__

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `((void *)__pyx_v_out)` — constructed_codepoint_array. Local char out[36] written by uuid_to_str/uuid_to_hex from 16-byte UUID binary data. ASCII hexadecimal and optional dashes; one-byte elements are not an external UTF-8 text stream.

**Length:** `36`; one_byte_codepoint_elements_equal_bytes.

**Confirmed:** Local char array declaration and UUID conversion call precede the constructor. tohex.h uses the ASCII hex table 0123456789abcdef and dash literals to write the complete fixed-length result.

**Inference / unresolved:** This is not borrowed Python FSR.

**Upstream representation coupling:** UUID helpers transform binary UUID bytes; static metadata uses confirmed ASCII char arrays. This is a local dependency statement, not a package-wide independence claim.

**Migration implication:** Construction from external one-byte codepoint arrays remains needed; ASCII can map directly to UTF-8 storage.

**Activation / tracing:** Python-visible UUID.__str__ or hex property; generated body corresponds to handwritten uuid.pyx.

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/pgproto.c:17557–17557`; SHA-256 `b56ca053f10020f2f57e16753a1e1ef6e4760cb469834fa317784b9c2c48014f`.

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17553–17561 (GitHub mapping not verified in saved evidence)

```
 * 
 *     @property
*/
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, ((void *)__pyx_v_out), 36); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17530–17533 (GitHub mapping not verified in saved evidence)

```
static PyObject *__pyx_pf_7asyncpg_7pgproto_7pgproto_4UUID_4__str__(struct __pyx_obj_7asyncpg_7pgproto_7pgproto_UUID *__pyx_v_self) {
  char __pyx_v_out[36];
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
```

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17541–17545 (GitHub mapping not verified in saved evidence)

```
 *     def __str__(self):
 *         cdef char out[36]
 *         uuid_to_str(self._data, out)             # <<<<<<<<<<<<<<
 *         return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, <void*>out, 36)
 * 
```

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17545–17549 (GitHub mapping not verified in saved evidence)

```
 * 
*/
  uuid_to_str(__pyx_v_self->_data, __pyx_v_out);

  /* "asyncpg/pgproto/uuid.pyx":191
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0005: __pyx_pf_7asyncpg_7pgproto_7pgproto_4UUID_3hex___get__

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `((void *)__pyx_v_out)` — constructed_codepoint_array. Local char out[32] written by uuid_to_str/uuid_to_hex from 16-byte UUID binary data. ASCII hexadecimal and optional dashes; one-byte elements are not an external UTF-8 text stream.

**Length:** `32`; one_byte_codepoint_elements_equal_bytes.

**Confirmed:** Local char array declaration and UUID conversion call precede the constructor. tohex.h uses the ASCII hex table 0123456789abcdef and dash literals to write the complete fixed-length result.

**Inference / unresolved:** This is not borrowed Python FSR.

**Upstream representation coupling:** UUID helpers transform binary UUID bytes; static metadata uses confirmed ASCII char arrays. This is a local dependency statement, not a package-wide independence claim.

**Migration implication:** Construction from external one-byte codepoint arrays remains needed; ASCII can map directly to UTF-8 storage.

**Activation / tracing:** Python-visible UUID.__str__ or hex property; generated body corresponds to handwritten uuid.pyx.

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/pgproto.c:17632–17632`; SHA-256 `b56ca053f10020f2f57e16753a1e1ef6e4760cb469834fa317784b9c2c48014f`.

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17628–17636 (GitHub mapping not verified in saved evidence)

```
 * 
 *     def __repr__(self):
*/
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, ((void *)__pyx_v_out), 32); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 197, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;
```

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17605–17608 (GitHub mapping not verified in saved evidence)

```
static PyObject *__pyx_pf_7asyncpg_7pgproto_7pgproto_4UUID_3hex___get__(struct __pyx_obj_7asyncpg_7pgproto_7pgproto_UUID *__pyx_v_self) {
  char __pyx_v_out[32];
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
```

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17616–17620 (GitHub mapping not verified in saved evidence)

```
 *     def hex(self):
 *         cdef char out[32]
 *         uuid_to_hex(self._data, out)             # <<<<<<<<<<<<<<
 *         return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, <void*>out, 32)
 * 
```

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17620–17624 (GitHub mapping not verified in saved evidence)

```
 * 
*/
  uuid_to_hex(__pyx_v_self->_data, __pyx_v_out);

  /* "asyncpg/pgproto/uuid.pyx":197
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0006: __pyx_f_7asyncpg_8protocol_8protocol__textarray_decode

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `((void *)__pyx_v_item_start)` — owned_unicode_copy. Py_UCS4 item_start/item_end delimit a range of the array_text allocation created by PyUnicode_AsUCS4Copy in textarray_decode. Parsing removes quoting/escapes in this allocation before reconstructing an item for its text codec.

**Length:** `(__pyx_v_item_end - __pyx_v_item_start)`; four_byte_codepoint_elements.

**Confirmed:** Provider accepts Py_UCS4 *array_text; item pointers are Py_UCS4*. Caller uses PyUnicode_AsUCS4Copy(s) and frees array_text after the callee returns.

**Inference / unresolved:** This API argument is an owned UCS4 copy, not borrowed Python internal storage.

**Upstream representation coupling:** This is a Unicode conversion dependency through an owned-copy public API, not a direct borrowed-FSR dependency.

**Migration implication:** Still needs construction from a UCS4 slice; a UTF-8 Python representation would move transcoding to the owned-copy provider rather than require writable Python FSR.

**Activation / tracing:** Internal PostgreSQL text-array decoder; empty and NULL items take other branches.

**Source:** `asyncpg-0.31.0/asyncpg/protocol/protocol.c:31544–31544`; SHA-256 `2fb2b4aceaf57b686741b02e641aff9e78a52d08f3d879f3474cf749988ff5fe`.

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 31540–31548 (GitHub mapping not verified in saved evidence)

```
 *                 item_end - item_start)             # <<<<<<<<<<<<<<
 * 
 *             # Prepare the element buffer and call the text decoder
*/
      __pyx_t_2 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, ((void *)__pyx_v_item_start), (__pyx_v_item_end - __pyx_v_item_start)); if (unlikely(!__pyx_t_2)) __PYX_ERR(2, 644, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);

      /* "asyncpg/protocol/codecs/array.pyx":644
 *             # XXX: find a way to avoid the redundant encode/decode
```

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 30144–30148 (GitHub mapping not verified in saved evidence)

```
  int __pyx_v_strip_spaces;
  int __pyx_v_in_quotes;
  Py_UCS4 *__pyx_v_item_start;
  Py_UCS4 *__pyx_v_item_ptr;
  Py_UCS4 *__pyx_v_item_end;
```

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 30146–30150 (GitHub mapping not verified in saved evidence)

```
  Py_UCS4 *__pyx_v_item_start;
  Py_UCS4 *__pyx_v_item_ptr;
  Py_UCS4 *__pyx_v_item_end;
  int __pyx_v_i;
  PyObject *__pyx_v_item = 0;
```

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 30869–30873 (GitHub mapping not verified in saved evidence)

```
 * 
*/
    __pyx_v_item_start = __pyx_v_ptr;
    __pyx_v_item_end = __pyx_v_ptr;
    __pyx_v_item_ptr = __pyx_v_ptr;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0007: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `asyncpg-0.31.0/asyncpg/protocol/protocol.c:98118–98119`; SHA-256 `2fb2b4aceaf57b686741b02e641aff9e78a52d08f3d879f3474cf749988ff5fe`.

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 98092–98107 (GitHub mapping not verified in saved evidence)

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

Closing lines 98116–98121 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 98092–98121 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0051: __pyx_f_7asyncpg_8protocol_8protocol_22PreparedStatementState__encode_bind_msg

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_value_repr. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `asyncpg-0.31.0/asyncpg/protocol/protocol.c:57241–57241`; SHA-256 `2fb2b4aceaf57b686741b02e641aff9e78a52d08f3d879f3474cf749988ff5fe`.

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 57223–57238 (GitHub mapping not verified in saved evidence)

```
              PyErr_SetString(PyExc_TypeError, "object of type 'NoneType' has no len()");
              __PYX_ERR(17, 201, __pyx_L41_error)
            }
            __pyx_t_10 = __Pyx_PyUnicode_GET_LENGTH(__pyx_v_value_repr); if (unlikely(__pyx_t_10 == ((Py_ssize_t)-1))) __PYX_ERR(17, 201, __pyx_L41_error)
            __pyx_t_1 = (__pyx_t_10 > 40);
            if (__pyx_t_1) {

              /* "asyncpg/protocol/prepared_stmt.pyx":202
 *                     value_repr = repr(arg)
 *                     if len(value_repr) > 40:
 *                         value_repr = value_repr[:40] + '...'             # <<<<<<<<<<<<<<
 * 
 *                     raise exceptions.DataError(
*/
              if (unlikely(__pyx_v_value_repr == Py_None)) {
                PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 57244–57249 (GitHub mapping not verified in saved evidence)

```
              __Pyx_GOTREF(__pyx_t_12);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __Pyx_DECREF_SET(__pyx_v_value_repr, ((PyObject*)__pyx_t_12));
              __pyx_t_12 = 0;

              /* "asyncpg/protocol/prepared_stmt.pyx":201
```

Original reviewed range 57223–57249 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0071: __pyx_pw_7asyncpg_7pgproto_7pgproto_4UUID_5__str__

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `callee-local: ((void *)__pyx_v_out)` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. Local char out[36] written by uuid_to_str/uuid_to_hex from 16-byte UUID binary data. ASCII hexadecimal and optional dashes; one-byte elements are not an external UTF-8 text stream.

**Length:** `callee-local: 36`; one_byte_codepoint_elements_equal_bytes.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Construction from external one-byte codepoint arrays remains needed; ASCII can map directly to UTF-8 storage.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/pgproto.c:17523–17523`; SHA-256 `b56ca053f10020f2f57e16753a1e1ef6e4760cb469834fa317784b9c2c48014f`.

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17519–17527 (GitHub mapping not verified in saved evidence)

```
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__str__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_7asyncpg_7pgproto_7pgproto_4UUID_4__str__(((struct __pyx_obj_7asyncpg_7pgproto_7pgproto_UUID *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0072: __pyx_pw_7asyncpg_7pgproto_7pgproto_4UUID_3hex_1__get__

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `callee-local: ((void *)__pyx_v_out)` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. Local char out[32] written by uuid_to_str/uuid_to_hex from 16-byte UUID binary data. ASCII hexadecimal and optional dashes; one-byte elements are not an external UTF-8 text stream.

**Length:** `callee-local: 32`; one_byte_codepoint_elements_equal_bytes.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Construction from external one-byte codepoint arrays remains needed; ASCII can map directly to UTF-8 storage.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/pgproto.c:17598–17598`; SHA-256 `b56ca053f10020f2f57e16753a1e1ef6e4760cb469834fa317784b9c2c48014f`.

`asyncpg-0.31.0/asyncpg/pgproto/pgproto.c` lines 17594–17602 (GitHub mapping not verified in saved evidence)

```
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__get__ (wrapper)", 0);
  __pyx_kwvalues = __Pyx_KwValues_VARARGS(__pyx_args, __pyx_nargs);
  __pyx_r = __pyx_pf_7asyncpg_7pgproto_7pgproto_4UUID_3hex___get__(((struct __pyx_obj_7asyncpg_7pgproto_7pgproto_UUID *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0073: __pyx_f_7asyncpg_8protocol_8protocol_textarray_decode

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: ((void *)__pyx_v_item_start)` — owned_unicode_copy. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. Py_UCS4 item_start/item_end delimit a range of the array_text allocation created by PyUnicode_AsUCS4Copy in textarray_decode. Parsing removes quoting/escapes in this allocation before reconstructing an item for its text codec.

**Length:** `callee-local: (__pyx_v_item_end - __pyx_v_item_start)`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Still needs construction from a UCS4 slice; a UTF-8 Python representation would move transcoding to the owned-copy provider rather than require writable Python FSR.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `asyncpg-0.31.0/asyncpg/protocol/protocol.c:29864–29864`; SHA-256 `2fb2b4aceaf57b686741b02e641aff9e78a52d08f3d879f3474cf749988ff5fe`.

`asyncpg-0.31.0/asyncpg/protocol/protocol.c` lines 29860–29868 (GitHub mapping not verified in saved evidence)

```
 *             settings, array_text, decoder, decoder_arg, typdelim)             # <<<<<<<<<<<<<<
 *     except ValueError as e:
 *         raise exceptions.ProtocolError(
*/
        __pyx_t_1 = __pyx_f_7asyncpg_8protocol_8protocol__textarray_decode(__pyx_v_settings, __pyx_v_array_text, __pyx_v_decoder, __pyx_v_decoder_arg, __pyx_v_typdelim); if (unlikely(!__pyx_t_1)) __PYX_ERR(2, 426, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_r = __pyx_t_1;
        __pyx_t_1 = 0;
        goto __pyx_L10_try_return;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0165: extern Python.h declarations

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** Cython extern declaration of the public C API; no implementation or invocation here.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** 

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/cpythonx.pxd:22–23`; SHA-256 `07d7c07dab1782858df99f924c60b16eed2c5be411f046e50886f19733e8d147`.

`asyncpg-0.31.0/asyncpg/pgproto/cpythonx.pxd` lines 22–23 (GitHub mapping not verified in saved evidence)

```
    object PyUnicode_FromKindAndData(
        int kind, const void *buffer, Py_ssize_t size)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0166: extern Python.h declarations

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** Cython extern declaration of the public C API; no implementation or invocation here.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** 

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx:15–16`; SHA-256 `85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7`.

`asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx` lines 15–16 (GitHub mapping not verified in saved evidence)

```
    object PyUnicode_FromKindAndData(
        int kind, const void *buffer, Py_ssize_t size)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0167: extern Python.h declarations

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** Cython extern declaration of the public C API; no implementation or invocation here.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** 

**Source:** `asyncpg-0.31.0/asyncpg/protocol/cpythonx.pxd:16–17`; SHA-256 `557ef58383e2c175864d8f81cc13e6ed2f80897e72491ad8e34a808201fe0480`.

`asyncpg-0.31.0/asyncpg/protocol/cpythonx.pxd` lines 16–17 (GitHub mapping not verified in saved evidence)

```
    object PyUnicode_FromKindAndData(
        int kind, const void *buffer, Py_ssize_t size)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0170: UUID.__str__

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `<void*>out` — owned_native_output. char out[36] on the method stack; uuid_to_str(self._data, out) converts the object's 16-byte UUID to lowercase ASCII hex and hyphens.

**Length:** `36`; one-byte code point elements; also ASCII bytes here.

**Confirmed:** Explicit-size, fully initialized stack buffer. HEX_PRELUDE is the ASCII alphabet 0123456789abcdef; all producer writes derive from it or literal hyphens.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: owned_native_output; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Formatting reads UUID._data[16], a native byte array, and writes ASCII to local char out[]. Neither the formatter nor constructor operands require a Python Unicode FSR view.; support_span_refs: package: asyncpg; path: asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx; source_sha256: 85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7; evidence_path: read-access-analysis/sources/asyncpg/85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7.pyx; start: 138; end: 143; snippet_sha256: 3d3389f88c0220d473c43c7316aa45f6743cdf48eeee8a7b70128b73739c9e69; verified_permalink:  package: asyncpg; path: asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx; source_sha256: 85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7; evidence_path: read-access-analysis/sources/asyncpg/85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7.pyx; start: 188; end: 191; snippet_sha256: c51db3d22c6a717abe2e761d6fc3f510b3630dedb9986aee4e508b688f93a84f; verified_permalink:  package: asyncpg; path: asyncpg-0.31.0/asyncpg/pgproto/tohex.h; source_sha256: 2f0f0264c87ef1eb1cdcdb94f3c40d9d717e7c871c1b5a2ed74fff8643e23858; evidence_path: read-access-analysis/sources/asyncpg/2f0f0264c87ef1eb1cdcdb94f3c40d9d717e7c871c1b5a2ed74fff8643e23858.h; start: 1; end: 9; snippet_sha256: fc06a8389cbf74167a23375bb0f38d7f7891f4fb14e259420960aadc236d00a3; verified_permalink: 

**Migration implication:** The constructor can accept this external kind-1 buffer under a UTF-8 internal representation. No dependence on a Python Unicode object's internal layout in the constructor operands.

**Activation / tracing:** Normal synchronous method/property execution. Buffer remains alive through the copying constructor; no pointer escapes.

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx:188–191`; SHA-256 `85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7`.

`asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx` lines 188–191 (GitHub mapping not verified in saved evidence)

```
    def __str__(self):
        cdef char out[36]
        uuid_to_str(self._data, out)
        return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, <void*>out, 36)
```

`asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx` lines 138–143 (GitHub mapping not verified in saved evidence)

```
cdef class UUID(__UUIDReplaceMe):

    cdef:
        char _data[16]
        object _int
        object _hash
```

`asyncpg-0.31.0/asyncpg/pgproto/tohex.h` lines 1–9 (GitHub mapping not verified in saved evidence)

```
#define HEX_PRELUDE \
    const char *__hexm = "0123456789abcdef";

#define HEX_1_BYTE(buf, dest)                   \
    {                                           \
        char byte = (buf)[0];                   \
        (dest)[0] = __hexm[(byte >> 4) & 0x0F]; \
        (dest)[1] = __hexm[byte & 0x0F];        \
    }
```

`asyncpg-0.31.0/asyncpg/pgproto/tohex.h` lines 30–45 (GitHub mapping not verified in saved evidence)

```
static inline void
uuid_to_str(const char *source, char *dest)
{
    HEX_PRELUDE

    HEX_4_BYTES(source, dest)
    dest[8] = '-';
    HEX_2_BYTES(source + 4, dest + 9)
    dest[13] = '-';
    HEX_2_BYTES(source + 6, dest + 14)
    dest[18] = '-';
    HEX_2_BYTES(source + 8, dest + 19)
    dest[23] = '-';
    HEX_4_BYTES(source + 10, dest + 24)
    HEX_2_BYTES(source + 14, dest + 32)
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0171: UUID.hex

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `<void*>out` — owned_native_output. char out[32] on the method stack; uuid_to_hex(self._data, out) converts the object's 16-byte UUID to lowercase ASCII hex.

**Length:** `32`; one-byte code point elements; also ASCII bytes here.

**Confirmed:** Explicit-size, fully initialized stack buffer. HEX_PRELUDE is the ASCII alphabet 0123456789abcdef; all producer writes derive from it or literal hyphens.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: owned_native_output; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Formatting reads UUID._data[16], a native byte array, and writes ASCII to local char out[]. Neither the formatter nor constructor operands require a Python Unicode FSR view.; support_span_refs: package: asyncpg; path: asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx; source_sha256: 85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7; evidence_path: read-access-analysis/sources/asyncpg/85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7.pyx; start: 138; end: 143; snippet_sha256: 3d3389f88c0220d473c43c7316aa45f6743cdf48eeee8a7b70128b73739c9e69; verified_permalink:  package: asyncpg; path: asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx; source_sha256: 85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7; evidence_path: read-access-analysis/sources/asyncpg/85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7.pyx; start: 194; end: 197; snippet_sha256: cb343cf2ad40d4d10622c6ed09bd74ba6bce83e923fabdae1ab76eec7919f4ac; verified_permalink:  package: asyncpg; path: asyncpg-0.31.0/asyncpg/pgproto/tohex.h; source_sha256: 2f0f0264c87ef1eb1cdcdb94f3c40d9d717e7c871c1b5a2ed74fff8643e23858; evidence_path: read-access-analysis/sources/asyncpg/2f0f0264c87ef1eb1cdcdb94f3c40d9d717e7c871c1b5a2ed74fff8643e23858.h; start: 1; end: 9; snippet_sha256: fc06a8389cbf74167a23375bb0f38d7f7891f4fb14e259420960aadc236d00a3; verified_permalink: 

**Migration implication:** The constructor can accept this external kind-1 buffer under a UTF-8 internal representation. No dependence on a Python Unicode object's internal layout in the constructor operands.

**Activation / tracing:** Normal synchronous method/property execution. Buffer remains alive through the copying constructor; no pointer escapes.

**Source:** `asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx:194–197`; SHA-256 `85e52daf42b125248d43dd96cfdc580876eecd2fee307cea989ac4b4a5bfd1c7`.

`asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx` lines 194–197 (GitHub mapping not verified in saved evidence)

```
    def hex(self):
        cdef char out[32]
        uuid_to_hex(self._data, out)
        return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, <void*>out, 32)
```

`asyncpg-0.31.0/asyncpg/pgproto/uuid.pyx` lines 138–143 (GitHub mapping not verified in saved evidence)

```
cdef class UUID(__UUIDReplaceMe):

    cdef:
        char _data[16]
        object _int
        object _hash
```

`asyncpg-0.31.0/asyncpg/pgproto/tohex.h` lines 1–9 (GitHub mapping not verified in saved evidence)

```
#define HEX_PRELUDE \
    const char *__hexm = "0123456789abcdef";

#define HEX_1_BYTE(buf, dest)                   \
    {                                           \
        char byte = (buf)[0];                   \
        (dest)[0] = __hexm[(byte >> 4) & 0x0F]; \
        (dest)[1] = __hexm[byte & 0x0F];        \
    }
```

`asyncpg-0.31.0/asyncpg/pgproto/tohex.h` lines 48–54 (GitHub mapping not verified in saved evidence)

```
static inline void
uuid_to_hex(const char *source, char *dest)
{
    HEX_PRELUDE
    HEX_8_BYTES(source, dest)
    HEX_8_BYTES(source + 8, dest + 16)
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.

## K0172: _textarray_decode

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `cpythonx.PyUnicode_4BYTE_KIND`.

**Input:** `<void *>item_start` — owned_native_output. Py_UCS4 element slice in array_text, an owned PyUnicode_AsUCS4Copy(s) allocation. The parser compacts quoting/escapes in place and excludes its added zero terminator.

**Length:** `item_end - item_start`; Py_UCS4 elements / code point values, not bytes.

**Confirmed:** textarray_decode calls pgproto.text_decode, then PyUnicode_AsUCS4Copy, invokes _textarray_decode, and frees array_text in finally. item_start/item_end/item_ptr are Py_UCS4 pointers; the backslash branch moves the escaped value to item_ptr. Unquoted NULL elements avoid the constructor. Other items are rebuilt as Unicode, converted to connection-encoded text via as_pg_string_and_size, and passed to the element decoder.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: owned_native_output; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: public_owned_ucs4_export; borrowed_fsr_dependency: none; api_symbols: PyUnicode_AsUCS4Copy PyMem_Free; public_owned_export_dependency: True; explanation: The upstream Python string is exported by public AsUCS4Copy into independently owned UCS4 storage, mutated by the parser, then freed in finally. This export can be implemented independently for UTF-8 storage and is not a borrowed DATA/KIND view.; support_span_refs: package: asyncpg; path: asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx; source_sha256: d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29; evidence_path: read-access-analysis/sources/asyncpg/d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29.pyx; start: 413; end: 432; snippet_sha256: 0132aa43da130fb63bde299d17801ae089332395bc8a8757d4e10ad48d57dc93; verified_permalink: https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L413-L432 package: asyncpg; path: asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx; source_sha256: d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29; evidence_path: read-access-analysis/sources/asyncpg/d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29.pyx; start: 461; end: 464; snippet_sha256: 5dfbb7b090c5de130b75e14974a17f5d5fe07a1494ed539ff788809b8decffee; verified_permalink: https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L461-L464 package: asyncpg; path: asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx; source_sha256: d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29; evidence_path: read-access-analysis/sources/asyncpg/d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29.pyx; start: 565; end: 577; snippet_sha256: e2237e227d7d059856853f69272bba7639de2f6fbd10c610266307015d4563f5; verified_permalink: https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L565-L577

**Migration implication:** An independent UTF-8-backed implementation of FromKindAndData can transcode this owned UCS4 slice. The upstream public AsUCS4Copy export is independently implementable for UTF-8 storage; this is not a borrowed FSR pointer.

**Activation / tracing:** Synchronous PostgreSQL text-array decoder; the array allocation outlives every item constructor.

**Source:** `asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx:638–654`; SHA-256 `d52ffac5d8319651bcff52dbebc5dd3e41f542017ade00009a3874f7543b0f29`.

`asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx` lines 638–653 ([verified immutable source](https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L638-L653))

```
        if not has_quoting and apg_strcasecmp(item_start, APG_NULL) == 0:
            # NULL element.
            item = None
        else:
            # XXX: find a way to avoid the redundant encode/decode
            # cycle here.
            item_text = cpythonx.PyUnicode_FromKindAndData(
                cpythonx.PyUnicode_4BYTE_KIND,
                <void *>item_start,
                item_end - item_start)

            # Prepare the element buffer and call the text decoder
            # for the element type.
            pgproto.as_pg_string_and_size(
                settings, item_text, &pg_item_str, &pg_item_len)
            frb_init(&item_buf, pg_item_str, pg_item_len)
```

Closing lines 654–654 ([verified immutable source](https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L654-L654))

```
            item = decoder(settings, &item_buf, decoder_arg)
```

Original reviewed range 638–654 is recorded in `data/sites.json`; public excerpts are bounded.

`asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx` lines 413–428 ([verified immutable source](https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L413-L428))

```
cdef textarray_decode(ConnectionSettings settings, FRBuffer *buf,
                      decode_func_ex decoder, const void *decoder_arg,
                      Py_UCS4 typdelim):
    cdef:
        Py_UCS4 *array_text
        str s

    # Make a copy of array data since we will be mutating it for
    # the purposes of element decoding.
    s = pgproto.text_decode(settings, buf)
    array_text = cpythonx.PyUnicode_AsUCS4Copy(s)

    try:
        return _textarray_decode(
            settings, array_text, decoder, decoder_arg, typdelim)
    except ValueError as e:
```

Closing lines 429–432 ([verified immutable source](https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L429-L432))

```
        raise exceptions.ProtocolError(
            'malformed array literal {!r}: {}'.format(s, e.args[0]))
    finally:
        cpython.PyMem_Free(array_text)
```

Original reviewed range 413–432 is recorded in `data/sites.json`; public excerpts are bounded.

`asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx` lines 461–464 ([verified immutable source](https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L461-L464))

```
        bint in_quotes = False
        Py_UCS4 *item_start
        Py_UCS4 *item_ptr
        Py_UCS4 *item_end
```

`asyncpg-0.31.0/asyncpg/protocol/codecs/array.pyx` lines 543–553 ([verified immutable source](https://github.com/MagicStack/asyncpg/blob/71775a67277fc0aa5bd2b9f15e848826d7078c4d/asyncpg/protocol/codecs/array.pyx#L543-L553))

```
    while not end_of_array:
        # We iterate over the literal character by character
        # and modify the string in-place removing the array-specific
        # quoting and determining the boundaries of each element.
        end_of_item = has_quoting = in_quotes = False
        strip_spaces = True

        # Pointers to array element start, end, and the current pointer
        # tracking the position where characters are written when
        # escaping is folded.
        item_start = item_end = item_ptr = ptr
```

[Frozen source distribution](https://files.pythonhosted.org/packages/fe/cc/d18065ce2380d80b1bcce927c24a2642efd38918e33fd724bc4bca904877/asyncpg-0.31.0.tar.gz); archive SHA-256 `c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735`.
