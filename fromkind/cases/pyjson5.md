# pyjson5 2.0.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0019: __pyx_fuse_0__pyx_f_7pyjson5__decode_string_sub

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderUCS1Ref has two verified source paths: Python Unicode DATA/KIND or external Py_buffer. The constructor consumes an independently owned UCS4 decoded-output buffer in both paths.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:28817–28817`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 28813–28821 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 219 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 218, __pyx_L1_error)

#line 219 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 28371–28375 (GitHub mapping not verified in saved evidence)

```
#line 185 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 185 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 28586–28590 (GitHub mapping not verified in saved evidence)

```

#line 201 "src/_decoder.pyx"
      __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 201, __pyx_L1_error)

      /* "src/_decoder.pyx":202
```

`pyjson5-2.0.1/pyjson5.cpp` lines 28725–28729 (GitHub mapping not verified in saved evidence)

```

#line 212 "src/_decoder.pyx"
        __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 212, __pyx_L1_error)

        /* "src/_decoder.pyx":210
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0020: __pyx_fuse_1__pyx_f_7pyjson5__decode_string_sub

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderUCS2Ref has two verified source paths: Python Unicode DATA/KIND or external Py_buffer. The constructor consumes an independently owned UCS4 decoded-output buffer in both paths.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:29324–29324`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 29320–29328 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 219 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 218, __pyx_L1_error)

#line 219 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 28878–28882 (GitHub mapping not verified in saved evidence)

```
#line 185 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 185 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 29093–29097 (GitHub mapping not verified in saved evidence)

```

#line 201 "src/_decoder.pyx"
      __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 201, __pyx_L1_error)

      /* "src/_decoder.pyx":202
```

`pyjson5-2.0.1/pyjson5.cpp` lines 29232–29236 (GitHub mapping not verified in saved evidence)

```

#line 212 "src/_decoder.pyx"
        __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 212, __pyx_L1_error)

        /* "src/_decoder.pyx":210
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0021: __pyx_fuse_2__pyx_f_7pyjson5__decode_string_sub

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderUCS4Ref has two verified source paths: Python Unicode DATA/KIND or external Py_buffer. The constructor consumes an independently owned UCS4 decoded-output buffer in both paths.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:29831–29831`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 29827–29835 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 219 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 218, __pyx_L1_error)

#line 219 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 29385–29389 (GitHub mapping not verified in saved evidence)

```
#line 185 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 185 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 29600–29604 (GitHub mapping not verified in saved evidence)

```

#line 201 "src/_decoder.pyx"
      __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 201, __pyx_L1_error)

      /* "src/_decoder.pyx":202
```

`pyjson5-2.0.1/pyjson5.cpp` lines 29739–29743 (GitHub mapping not verified in saved evidence)

```

#line 212 "src/_decoder.pyx"
        __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 212, __pyx_L1_error)

        /* "src/_decoder.pyx":210
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0022: __pyx_fuse_3__pyx_f_7pyjson5__decode_string_sub

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** UTF-8 input and owned UCS4 output are distinct. Any UTF-8 caching/transcoding by the public export is separate from borrowed FSR materialization.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:30338–30338`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 30334–30342 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 219 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 218, __pyx_L1_error)

#line 219 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 29892–29896 (GitHub mapping not verified in saved evidence)

```
#line 185 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 185 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 30107–30111 (GitHub mapping not verified in saved evidence)

```

#line 201 "src/_decoder.pyx"
      __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 201, __pyx_L1_error)

      /* "src/_decoder.pyx":202
```

`pyjson5-2.0.1/pyjson5.cpp` lines 30246–30250 (GitHub mapping not verified in saved evidence)

```

#line 212 "src/_decoder.pyx"
        __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 212, __pyx_L1_error)

        /* "src/_decoder.pyx":210
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0023: __pyx_fuse_4__pyx_f_7pyjson5__decode_string_sub

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderCallback path has no local borrowed FSR pointer. Output constructor still consumes an independently owned UCS4 array.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:30845–30845`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 30841–30849 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 219 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 218, __pyx_L1_error)

#line 219 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 30399–30403 (GitHub mapping not verified in saved evidence)

```
#line 185 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 185 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 30614–30618 (GitHub mapping not verified in saved evidence)

```

#line 201 "src/_decoder.pyx"
      __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 201, __pyx_L1_error)

      /* "src/_decoder.pyx":202
```

`pyjson5-2.0.1/pyjson5.cpp` lines 30753–30757 (GitHub mapping not verified in saved evidence)

```

#line 212 "src/_decoder.pyx"
        __pyx_t_5 = __pyx_v_buf.push_back(__pyx_v_c0); if (unlikely(__pyx_t_5 == ((int)0))) __PYX_ERR(11, 212, __pyx_L1_error)

        /* "src/_decoder.pyx":210
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0024: __pyx_fuse_0__pyx_f_7pyjson5__decode_identifier_name

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderUCS1Ref has two verified source paths: Python Unicode DATA/KIND or external Py_buffer. The constructor consumes an independently owned UCS4 decoded-output buffer in both paths.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:49168–49168`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 49164–49172 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 526 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 525, __pyx_L1_error)

#line 526 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 48690–48694 (GitHub mapping not verified in saved evidence)

```
#line 486 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 486 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 49013–49017 (GitHub mapping not verified in saved evidence)

```

#line 513 "src/_decoder.pyx"
    __pyx_t_2 = __pyx_v_buf.push_back(__pyx_v_c1); if (unlikely(__pyx_t_2 == ((int)0))) __PYX_ERR(11, 513, __pyx_L1_error)

    /* "src/_decoder.pyx":515
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0025: __pyx_fuse_1__pyx_f_7pyjson5__decode_identifier_name

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderUCS2Ref has two verified source paths: Python Unicode DATA/KIND or external Py_buffer. The constructor consumes an independently owned UCS4 decoded-output buffer in both paths.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:49724–49724`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 49720–49728 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 526 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 525, __pyx_L1_error)

#line 526 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 49246–49250 (GitHub mapping not verified in saved evidence)

```
#line 486 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 486 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 49569–49573 (GitHub mapping not verified in saved evidence)

```

#line 513 "src/_decoder.pyx"
    __pyx_t_2 = __pyx_v_buf.push_back(__pyx_v_c1); if (unlikely(__pyx_t_2 == ((int)0))) __PYX_ERR(11, 513, __pyx_L1_error)

    /* "src/_decoder.pyx":515
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0026: __pyx_fuse_2__pyx_f_7pyjson5__decode_identifier_name

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderUCS4Ref has two verified source paths: Python Unicode DATA/KIND or external Py_buffer. The constructor consumes an independently owned UCS4 decoded-output buffer in both paths.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:50280–50280`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 50276–50284 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 526 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 525, __pyx_L1_error)

#line 526 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 49802–49806 (GitHub mapping not verified in saved evidence)

```
#line 486 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 486 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 50125–50129 (GitHub mapping not verified in saved evidence)

```

#line 513 "src/_decoder.pyx"
    __pyx_t_2 = __pyx_v_buf.push_back(__pyx_v_c1); if (unlikely(__pyx_t_2 == ((int)0))) __PYX_ERR(11, 513, __pyx_L1_error)

    /* "src/_decoder.pyx":515
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0027: __pyx_fuse_3__pyx_f_7pyjson5__decode_identifier_name

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** UTF-8 input and owned UCS4 output are distinct. Any UTF-8 caching/transcoding by the public export is separate from borrowed FSR materialization.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:50836–50836`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 50832–50840 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 526 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 525, __pyx_L1_error)

#line 526 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 50358–50362 (GitHub mapping not verified in saved evidence)

```
#line 486 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 486 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 50681–50685 (GitHub mapping not verified in saved evidence)

```

#line 513 "src/_decoder.pyx"
    __pyx_t_2 = __pyx_v_buf.push_back(__pyx_v_c1); if (unlikely(__pyx_t_2 == ((int)0))) __PYX_ERR(11, 513, __pyx_L1_error)

    /* "src/_decoder.pyx":515
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0028: __pyx_fuse_4__pyx_f_7pyjson5__decode_identifier_name

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_buf.data()` — constructed_codepoint_array. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `__pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Local StackHeapString<uint32_t> declaration and push_back operations. Five fused reader variants share each algorithm; they are physical generated copies of two source algorithms.

**Inference / unresolved:** Input reader encoding/width does not change the fixed-4 output array passed here.

**Upstream representation coupling:** ReaderCallback path has no local borrowed FSR pointer. Output constructor still consumes an independently owned UCS4 array.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Internal fused JSON5 string or identifier decoder, used from generated JSON5 parser.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:51392–51392`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 51388–51396 (GitHub mapping not verified in saved evidence)

```
 * 
*/

#line 526 "src/_decoder.pyx"
  __pyx_t_7 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_buf.data(), __pyx_v_buf.size()); if (unlikely(!__pyx_t_7)) __PYX_ERR(11, 525, __pyx_L1_error)

#line 526 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_7);

```

`pyjson5-2.0.1/pyjson5.cpp` lines 50914–50918 (GitHub mapping not verified in saved evidence)

```
#line 486 "src/_decoder.pyx"
;
  JSON5EncoderCpp::StackHeapString<std::uint32_t>  __pyx_v_buf
#line 486 "src/_decoder.pyx"
;
```

`pyjson5-2.0.1/pyjson5.cpp` lines 51237–51241 (GitHub mapping not verified in saved evidence)

```

#line 513 "src/_decoder.pyx"
    __pyx_t_2 = __pyx_v_buf.push_back(__pyx_v_c1); if (unlikely(__pyx_t_2 == ((int)0))) __PYX_ERR(11, 513, __pyx_L1_error)

    /* "src/_decoder.pyx":515
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0029: __pyx_pymod_exec_pyjson5

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `JSON5EncoderCpp::VERSION` — static_char_array. Verified ASCII static const char VERSION[] or LONGDESCRIPTION[] assembled from a retained .inc payload. LENGTH is sizeof(array)-1, excluding trailing NUL.

**Length:** `JSON5EncoderCpp::VERSION_LENGTH`; one_byte_codepoint_elements_equal_bytes.

**Confirmed:** native.hpp declares char arrays and LENGTH = sizeof(array)-1. VERSION.inc retained exact bytes verified against SHA256 2d26c80219037aa60a1557aae78cb2bbc258cc05f5f63ce371adc966ea07e3b4; 8 source bytes, all ASCII, with only ASCII-producing C escapes.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** UUID helpers transform binary UUID bytes; static metadata uses confirmed ASCII char arrays. This is a local dependency statement, not a package-wide independence claim.

**Migration implication:** These verified ASCII constants map directly to UTF-8 bytes. Preserve the public fixed1 constructor semantics of one-byte numeric Unicode elements.

**Activation / tracing:** Module initialization creates __version__ or __doc__; this is executable generated code, distinct from nearby source echo comments.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:106696–106696`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 106692–106700 (GitHub mapping not verified in saved evidence)

```
 * Current library version.
*/

#line 8 "src/_exports.pyx"
  __pyx_t_2 = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, JSON5EncoderCpp::VERSION, JSON5EncoderCpp::VERSION_LENGTH); if (unlikely(!__pyx_t_2)) __PYX_ERR(15, 8, __pyx_L1_error)

#line 8 "src/_exports.pyx"
  __Pyx_GOTREF(__pyx_t_2);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0030: __pyx_pymod_exec_pyjson5

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `JSON5EncoderCpp::LONGDESCRIPTION` — static_char_array. Verified ASCII static const char VERSION[] or LONGDESCRIPTION[] assembled from a retained .inc payload. LENGTH is sizeof(array)-1, excluding trailing NUL.

**Length:** `JSON5EncoderCpp::LONGDESCRIPTION_LENGTH`; one_byte_codepoint_elements_equal_bytes.

**Confirmed:** native.hpp declares char arrays and LENGTH = sizeof(array)-1. DESCRIPTION.inc retained exact bytes verified against SHA256 819832984201570c2aad0df9ea0d52b2a503c57f5299bd10105ad1e3c15ecbbc; 717 source bytes, all ASCII, with only ASCII-producing C escapes.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** UUID helpers transform binary UUID bytes; static metadata uses confirmed ASCII char arrays. This is a local dependency statement, not a package-wide independence claim.

**Migration implication:** These verified ASCII constants map directly to UTF-8 bytes. Preserve the public fixed1 constructor semantics of one-byte numeric Unicode elements.

**Activation / tracing:** Module initialization creates __version__ or __doc__; this is executable generated code, distinct from nearby source echo comments.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:107177–107177`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 107173–107181 (GitHub mapping not verified in saved evidence)

```
 * __license__ = 'MIT OR Apache-2.0'
*/

#line 620 "src/_exports.pyx"
  __pyx_t_6 = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, JSON5EncoderCpp::LONGDESCRIPTION, JSON5EncoderCpp::LONGDESCRIPTION_LENGTH); if (unlikely(!__pyx_t_6)) __PYX_ERR(15, 620, __pyx_L1_error)

#line 620 "src/_exports.pyx"
  __Pyx_GOTREF(__pyx_t_6);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0078: __pyx_fuse_0__pyx_f_7pyjson5__decode_string

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:31063–31063`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 31059–31067 (GitHub mapping not verified in saved evidence)

```
 *     c_in_out[0] = NO_EXTRA_DATA
*/

#line 238 "src/_decoder.pyx"
  __pyx_t_6 = __pyx_fuse_0__pyx_f_7pyjson5__decode_string_sub(__pyx_v_reader, __pyx_v_delim, __pyx_v_start, __pyx_v_c0); if (unlikely(!__pyx_t_6)) __PYX_ERR(11, 238, __pyx_L1_error)

#line 238 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_6);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0079: __pyx_fuse_1__pyx_f_7pyjson5__decode_string

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:31304–31304`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 31300–31308 (GitHub mapping not verified in saved evidence)

```
 *     c_in_out[0] = NO_EXTRA_DATA
*/

#line 238 "src/_decoder.pyx"
  __pyx_t_6 = __pyx_fuse_1__pyx_f_7pyjson5__decode_string_sub(__pyx_v_reader, __pyx_v_delim, __pyx_v_start, __pyx_v_c0); if (unlikely(!__pyx_t_6)) __PYX_ERR(11, 238, __pyx_L1_error)

#line 238 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_6);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0080: __pyx_fuse_2__pyx_f_7pyjson5__decode_string

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:31545–31545`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 31541–31549 (GitHub mapping not verified in saved evidence)

```
 *     c_in_out[0] = NO_EXTRA_DATA
*/

#line 238 "src/_decoder.pyx"
  __pyx_t_6 = __pyx_fuse_2__pyx_f_7pyjson5__decode_string_sub(__pyx_v_reader, __pyx_v_delim, __pyx_v_start, __pyx_v_c0); if (unlikely(!__pyx_t_6)) __PYX_ERR(11, 238, __pyx_L1_error)

#line 238 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_6);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0081: __pyx_fuse_3__pyx_f_7pyjson5__decode_string

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:31786–31786`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 31782–31790 (GitHub mapping not verified in saved evidence)

```
 *     c_in_out[0] = NO_EXTRA_DATA
*/

#line 238 "src/_decoder.pyx"
  __pyx_t_6 = __pyx_fuse_3__pyx_f_7pyjson5__decode_string_sub(__pyx_v_reader, __pyx_v_delim, __pyx_v_start, __pyx_v_c0); if (unlikely(!__pyx_t_6)) __PYX_ERR(11, 238, __pyx_L1_error)

#line 238 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_6);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0082: __pyx_fuse_4__pyx_f_7pyjson5__decode_string

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:32027–32027`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 32023–32031 (GitHub mapping not verified in saved evidence)

```
 *     c_in_out[0] = NO_EXTRA_DATA
*/

#line 238 "src/_decoder.pyx"
  __pyx_t_6 = __pyx_fuse_4__pyx_f_7pyjson5__decode_string_sub(__pyx_v_reader, __pyx_v_delim, __pyx_v_start, __pyx_v_c0); if (unlikely(!__pyx_t_6)) __PYX_ERR(11, 238, __pyx_L1_error)

#line 238 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_6);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0083: __pyx_fuse_0__pyx_f_7pyjson5__decode_object

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:51737–51737`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 51733–51741 (GitHub mapping not verified in saved evidence)

```
 *                 break
*/

#line 551 "src/_decoder.pyx"
      __pyx_t_4 = __pyx_fuse_0__pyx_f_7pyjson5__decode_identifier_name(__pyx_v_reader, (&__pyx_v_c0)); if (unlikely(!__pyx_t_4)) __PYX_ERR(11, 551, __pyx_L1_error)

#line 551 "src/_decoder.pyx"
      __Pyx_GOTREF(__pyx_t_4);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0084: __pyx_fuse_1__pyx_f_7pyjson5__decode_object

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:52780–52780`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 52776–52784 (GitHub mapping not verified in saved evidence)

```
 *                 break
*/

#line 551 "src/_decoder.pyx"
  __pyx_t_4 = __pyx_fuse_1__pyx_f_7pyjson5__decode_identifier_name(__pyx_v_reader, (&__pyx_v_c0)); if (unlikely(!__pyx_t_4)) __PYX_ERR(11, 551, __pyx_L1_error)

#line 551 "src/_decoder.pyx"
  __Pyx_GOTREF(__pyx_t_4);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0085: __pyx_fuse_2__pyx_f_7pyjson5__decode_object

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:53823–53823`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 53819–53827 (GitHub mapping not verified in saved evidence)

```
 *                 break
*/

#line 551 "src/_decoder.pyx"
__pyx_t_4 = __pyx_fuse_2__pyx_f_7pyjson5__decode_identifier_name(__pyx_v_reader, (&__pyx_v_c0)); if (unlikely(!__pyx_t_4)) __PYX_ERR(11, 551, __pyx_L1_error)

#line 551 "src/_decoder.pyx"
__Pyx_GOTREF(__pyx_t_4);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0086: __pyx_fuse_3__pyx_f_7pyjson5__decode_object

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:54866–54866`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 54862–54870 (GitHub mapping not verified in saved evidence)

```
 *                 break
*/

#line 551 "src/_decoder.pyx"
__pyx_t_4 = __pyx_fuse_3__pyx_f_7pyjson5__decode_identifier_name(__pyx_v_reader, (&__pyx_v_c0)); if (unlikely(!__pyx_t_4)) __PYX_ERR(11, 551, __pyx_L1_error)

#line 551 "src/_decoder.pyx"
__Pyx_GOTREF(__pyx_t_4);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0087: __pyx_fuse_4__pyx_f_7pyjson5__decode_object

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_buf.data()` — constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. JSON5EncoderCpp::StackHeapString<std::uint32_t> accumulates decoded numeric Unicode elements via push_back. data() returns its stack/heap uint32_t storage; size() counts stored elements.

**Length:** `callee-local: __pyx_v_buf.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Retain fixed-width construction support for decoded codepoint arrays; no Python FSR input pointer is passed to this call.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:55909–55909`; SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

`pyjson5-2.0.1/pyjson5.cpp` lines 55905–55913 (GitHub mapping not verified in saved evidence)

```
 *                 break
*/

#line 551 "src/_decoder.pyx"
__pyx_t_4 = __pyx_fuse_4__pyx_f_7pyjson5__decode_identifier_name(__pyx_v_reader, (&__pyx_v_c0)); if (unlikely(!__pyx_t_4)) __PYX_ERR(11, 551, __pyx_L1_error)

#line 551 "src/_decoder.pyx"
__Pyx_GOTREF(__pyx_t_4);

```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0168: extern Python.h declarations

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** Cython extern declaration of the public C API; no implementation or invocation here.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** 

**Source:** `pyjson5-2.0.1/src/_imports.pyx:157–157`; SHA-256 `5c41ef9c67c2fdebda15cd0cd1c294e35b1ca1e637d2231a7538f129e2758aa2`.

`pyjson5-2.0.1/src/_imports.pyx` lines 157–157 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_imports.pyx#L157-L157))

```
    object PyUnicode_FromKindAndData(int kind, const void *buf, Py_ssize_t size)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0174: _decode_string_sub

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `buf.data()` — owned_native_output. Local StackHeapString[uint32_t] with an initial 64-element stack array and optional owned heap allocation. Parser pushes reader/escape-derived code point values; this buffer is already decoded/assembled output, not the raw external input.

**Length:** `buf.size()`; uint32_t elements / output code point values, not bytes.

**Confirmed:** StackHeapString.data() returns its stack or heap pointer; size() returns m_size. push_back stores one T and increments m_size. Destructor frees the optional heap. ReaderRef dispatches to UCS1/UCS2/UCS4 readers, a UTF-8 reader, or a callback reader. The constructor always receives the accumulated uint32_t buffer regardless of reader specialization. \u high/low escape pairs are explicitly combined by _get_escaped_unicode_maybe_surrogate before insertion; the constructor is not a UTF-16 decoder.

**Inference / unresolved:** Code point values need not be Unicode scalar values: reader input can carry surrogate values, and constructor validation still applies. No claim that all input modes produce only valid scalars.

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: owned_native_output; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: conditional_upstream_borrowed_fsr; borrowed_fsr_dependency: conditional; api_symbols: PyUnicode_KIND PyUnicode_GET_LENGTH PyUnicode_1BYTE_DATA PyUnicode_2BYTE_DATA PyUnicode_4BYTE_DATA; public_owned_export_dependency: False; explanation: The constructor always gets its own uint32_t builder. CPython decode(str) selects a typed reader from KIND and BYTE_DATA and therefore borrows an input FSR view; the same UCS reader specializations also accept external Py_buffer storage. UTF-8 and callback readers do not require a borrowed input FSR view.; input_paths: path: decode(str) -> _decode_unicode -> _decode_ucs1/2/4; borrowed_fsr: True; condition: Non-PyPy branch; typed pointer is obtained from Python Unicode BYTE_DATA. path: decode(str) -> _decode_unicode -> _decode_utf8; borrowed_fsr: False; condition: CYTHON_COMPILING_IN_PYPY branch obtains the public AsUTF8AndSize export. path: decode_buffer -> _decode_buffer -> _decode_utf8 or _decode_ucs1/2/4; borrowed_fsr: False; condition: Reader points to external view.buf; wordlength selects byte/UCS element interpretation. path: decode_callback/decode_io -> _decode_callback -> ReaderCallback; borrowed_fsr: False; condition: Callback produces ordinal values; no Python Unicode DATA pointer is acquired by this reader.; support_span_refs: package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 854; end: 876; snippet_sha256: f297a83e7dbd6ce554b80ea6843182bba8ed0d42b12caab82370f55a17fe03ce; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L854-L876 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 818; end: 842; snippet_sha256: 30972f61187548aee8d6f909d6d207de41361aa6b59ae89d8b1077d0a640523a; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L818-L842 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 845; end: 851; snippet_sha256: 830c8c175cbbcbecf8a6bd80460e1773068dc9c433ed6797ad4600a2e9316f7d; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L845-L851 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 879; end: 902; snippet_sha256: 6f5bc94a4a5001a88492a04c446691e7fad8c8899cd3ef08d37be9c459cd1d9b; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L879-L902 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 905; end: 913; snippet_sha256: 2b8fe502eb0b6113ff2858f954e1313117612614ea1b411227b1183cba7c6a1e; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L905-L913 package: pyjson5; path: pyjson5-2.0.1/src/_readers.pyx; source_sha256: 1b65c055ea330034a07d22feff85c22de3c52d9610c49579d446cb1e4a6567b9; evidence_path: read-access-analysis/sources/pyjson5/1b65c055ea330034a07d22feff85c22de3c52d9610c49579d446cb1e4a6567b9.pyx; start: 26; end: 34; snippet_sha256: 5d02f3ac8e582ba87d9c528377aca8847244d1582c7386f7483326c23c5df247; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_readers.pyx#L26-L34 package: pyjson5; path: pyjson5-2.0.1/src/_reader_ucs.pyx; source_sha256: 20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0; evidence_path: read-access-analysis/sources/pyjson5/20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0.pyx; start: 52; end: 59; snippet_sha256: b51ee25ed6e3f24cef0f381ed1d7f12dd59e48bd74266cf0644911c78e316035; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_reader_ucs.pyx#L52-L59 package: pyjson5; path: pyjson5-2.0.1/src/_reader_callback.pyx; source_sha256: d6c7b7ef9920f6b48c134ea53bad4dcc70b772dbf120fe9cfe72b4405910d5aa; evidence_path: read-access-analysis/sources/pyjson5/d6c7b7ef9920f6b48c134ea53bad4dcc70b772dbf120fe9cfe72b4405910d5aa.pyx; start: 24; end: 50; snippet_sha256: 0d47b10bdb07b420e984f4a918e75eaefc95efcb97a2e7dfe079f3ddeade6a09; verified_permalink: 

**Migration implication:** The public constructor can transcode this owned kind-4 output for UTF-8 storage while preserving code point/surrogate semantics. Any upstream Python DATA/KIND reader dependency is distinct from the output constructor.

**Activation / tracing:** Active parser routine constructs a parsed JSON5 string value or quoted object key. Fused reader specializations may generate multiple C functions; count this handwritten call once.

**Source:** `pyjson5-2.0.1/src/_decoder.pyx:218–220`; SHA-256 `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

`pyjson5-2.0.1/src/_decoder.pyx` lines 218–220 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L218-L220))

```
    return PyUnicode_FromKindAndData(
        PyUnicode_4BYTE_KIND, buf.data(), buf.size(),
    )
```

`pyjson5-2.0.1/src/_decoder.pyx` lines 185–200 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L185-L200))

```
cdef object _decode_string_sub(ReaderRef reader, uint32_t delim,
                               Py_ssize_t start, uint32_t c0):
    cdef int32_t c1
    cdef StackHeapString[uint32_t] buf

    while True:
        if expect(c0 == delim, False):
            break

        if expect(not _reader_good(reader), False):
            _raise_unclosed(b'string', start)

        if expect(c0 != b'\\', True):
            if expect(c0 in (0xA, 0xD), False):
                _raise_unclosed(b'string', start)

```

Closing lines 201–202 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L201-L202))

```
            buf.push_back(c0)
            c0 = _reader_get(reader)
```

Original reviewed range 185–202 is recorded in `data/sites.json`; public excerpts are bounded.

`pyjson5-2.0.1/src/_decoder.pyx` lines 117–132 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L117-L132))

```

# >=  0: character to append
cdef int32_t _get_escaped_unicode_maybe_surrogate(ReaderRef reader, Py_ssize_t start) except -1:
    cdef uint32_t c0
    cdef uint32_t c1

    c0 = cast_to_uint32(_get_hex_character(reader, 4))
    if expect(unicode_is_lo_surrogate(c0), False):
        _raise_expected_s('high surrogate before low surrogate', start, c0)
    elif not unicode_is_hi_surrogate(c0):
        return c0

    _accept_string(reader, b'\\u')

    c1 = cast_to_uint32(_get_hex_character(reader, 4))
    if expect(not unicode_is_lo_surrogate(c1), False):
```

Closing lines 133–135 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L133-L135))

```
        _raise_expected_s('low surrogate', start, c1)

    return unicode_join_surrogates(c0, c1)
```

Original reviewed range 117–135 is recorded in `data/sites.json`; public excerpts are bounded.

`pyjson5-2.0.1/src/_decoder.pyx` lines 205–216 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L205-L216))

```
        c1 = _get_escape_sequence(reader, start)
        if c1 >= -1:
            if expect(not _reader_good(reader), False):
                _raise_unclosed(b'string', start)

            if c1 >= 0:
                c0 = cast_to_uint32(c1)
                buf.push_back(c0)

            c0 = _reader_get(reader)
        else:
            c0 = cast_to_uint32(-(c1 + 1))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0175: _decode_identifier_name

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `buf.data()` — owned_native_output. Local StackHeapString[uint32_t] with an initial 64-element stack array and optional owned heap allocation. Parser pushes reader/escape-derived code point values; this buffer is already decoded/assembled output, not the raw external input.

**Length:** `buf.size()`; uint32_t elements / output code point values, not bytes.

**Confirmed:** StackHeapString.data() returns its stack or heap pointer; size() returns m_size. push_back stores one T and increments m_size. Destructor frees the optional heap. ReaderRef dispatches to UCS1/UCS2/UCS4 readers, a UTF-8 reader, or a callback reader. The constructor always receives the accumulated uint32_t buffer regardless of reader specialization. \u high/low escape pairs are explicitly combined by _get_escaped_unicode_maybe_surrogate before insertion; the constructor is not a UTF-16 decoder.

**Inference / unresolved:** Code point values need not be Unicode scalar values: reader input can carry surrogate values, and constructor validation still applies. No claim that all input modes produce only valid scalars.

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: owned_native_output; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: conditional_upstream_borrowed_fsr; borrowed_fsr_dependency: conditional; api_symbols: PyUnicode_KIND PyUnicode_GET_LENGTH PyUnicode_1BYTE_DATA PyUnicode_2BYTE_DATA PyUnicode_4BYTE_DATA; public_owned_export_dependency: False; explanation: The constructor always gets its own uint32_t builder. CPython decode(str) selects a typed reader from KIND and BYTE_DATA and therefore borrows an input FSR view; the same UCS reader specializations also accept external Py_buffer storage. UTF-8 and callback readers do not require a borrowed input FSR view.; input_paths: path: decode(str) -> _decode_unicode -> _decode_ucs1/2/4; borrowed_fsr: True; condition: Non-PyPy branch; typed pointer is obtained from Python Unicode BYTE_DATA. path: decode(str) -> _decode_unicode -> _decode_utf8; borrowed_fsr: False; condition: CYTHON_COMPILING_IN_PYPY branch obtains the public AsUTF8AndSize export. path: decode_buffer -> _decode_buffer -> _decode_utf8 or _decode_ucs1/2/4; borrowed_fsr: False; condition: Reader points to external view.buf; wordlength selects byte/UCS element interpretation. path: decode_callback/decode_io -> _decode_callback -> ReaderCallback; borrowed_fsr: False; condition: Callback produces ordinal values; no Python Unicode DATA pointer is acquired by this reader.; support_span_refs: package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 854; end: 876; snippet_sha256: f297a83e7dbd6ce554b80ea6843182bba8ed0d42b12caab82370f55a17fe03ce; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L854-L876 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 818; end: 842; snippet_sha256: 30972f61187548aee8d6f909d6d207de41361aa6b59ae89d8b1077d0a640523a; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L818-L842 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 845; end: 851; snippet_sha256: 830c8c175cbbcbecf8a6bd80460e1773068dc9c433ed6797ad4600a2e9316f7d; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L845-L851 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 879; end: 902; snippet_sha256: 6f5bc94a4a5001a88492a04c446691e7fad8c8899cd3ef08d37be9c459cd1d9b; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L879-L902 package: pyjson5; path: pyjson5-2.0.1/src/_decoder.pyx; source_sha256: c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78; evidence_path: read-access-analysis/sources/pyjson5/c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78.pyx; start: 905; end: 913; snippet_sha256: 2b8fe502eb0b6113ff2858f954e1313117612614ea1b411227b1183cba7c6a1e; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L905-L913 package: pyjson5; path: pyjson5-2.0.1/src/_readers.pyx; source_sha256: 1b65c055ea330034a07d22feff85c22de3c52d9610c49579d446cb1e4a6567b9; evidence_path: read-access-analysis/sources/pyjson5/1b65c055ea330034a07d22feff85c22de3c52d9610c49579d446cb1e4a6567b9.pyx; start: 26; end: 34; snippet_sha256: 5d02f3ac8e582ba87d9c528377aca8847244d1582c7386f7483326c23c5df247; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_readers.pyx#L26-L34 package: pyjson5; path: pyjson5-2.0.1/src/_reader_ucs.pyx; source_sha256: 20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0; evidence_path: read-access-analysis/sources/pyjson5/20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0.pyx; start: 52; end: 59; snippet_sha256: b51ee25ed6e3f24cef0f381ed1d7f12dd59e48bd74266cf0644911c78e316035; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_reader_ucs.pyx#L52-L59 package: pyjson5; path: pyjson5-2.0.1/src/_reader_callback.pyx; source_sha256: d6c7b7ef9920f6b48c134ea53bad4dcc70b772dbf120fe9cfe72b4405910d5aa; evidence_path: read-access-analysis/sources/pyjson5/d6c7b7ef9920f6b48c134ea53bad4dcc70b772dbf120fe9cfe72b4405910d5aa.pyx; start: 24; end: 50; snippet_sha256: 0d47b10bdb07b420e984f4a918e75eaefc95efcb97a2e7dfe079f3ddeade6a09; verified_permalink: 

**Migration implication:** The public constructor can transcode this owned kind-4 output for UTF-8 storage while preserving code point/surrogate semantics. Any upstream Python DATA/KIND reader dependency is distinct from the output constructor.

**Activation / tracing:** Active parser routine constructs a parsed unquoted identifier object key. Fused reader specializations may generate multiple C functions; count this handwritten call once.

**Source:** `pyjson5-2.0.1/src/_decoder.pyx:525–527`; SHA-256 `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

`pyjson5-2.0.1/src/_decoder.pyx` lines 525–527 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L525-L527))

```
    return PyUnicode_FromKindAndData(
        PyUnicode_4BYTE_KIND, buf.data(), buf.size(),
    )
```

`pyjson5-2.0.1/src/_decoder.pyx` lines 486–490 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L486-L490))

```
cdef unicode _decode_identifier_name(ReaderRef reader, int32_t *c_in_out):
    cdef int32_t c0
    cdef uint32_t c1
    cdef Py_ssize_t start
    cdef StackHeapString[uint32_t] buf
```

`pyjson5-2.0.1/src/_decoder.pyx` lines 117–132 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L117-L132))

```

# >=  0: character to append
cdef int32_t _get_escaped_unicode_maybe_surrogate(ReaderRef reader, Py_ssize_t start) except -1:
    cdef uint32_t c0
    cdef uint32_t c1

    c0 = cast_to_uint32(_get_hex_character(reader, 4))
    if expect(unicode_is_lo_surrogate(c0), False):
        _raise_expected_s('high surrogate before low surrogate', start, c0)
    elif not unicode_is_hi_surrogate(c0):
        return c0

    _accept_string(reader, b'\\u')

    c1 = cast_to_uint32(_get_hex_character(reader, 4))
    if expect(not unicode_is_lo_surrogate(c1), False):
```

Closing lines 133–135 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L133-L135))

```
        _raise_expected_s('low surrogate', start, c1)

    return unicode_join_surrogates(c0, c1)
```

Original reviewed range 117–135 is recorded in `data/sites.json`; public excerpts are bounded.

`pyjson5-2.0.1/src/_decoder.pyx` lines 499–514 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L499-L514))

```
    while True:
        if expect(c1 == b'\\', False):
            if not _reader_good(reader):
                _raise_unclosed('IdentifierName', start)
                break

            c1 = _reader_get(reader)
            if c1 == b'u':
                c1 = cast_to_uint32(_get_escaped_unicode_maybe_surrogate(reader, _reader_tell(reader)))
            elif c1 == b'U':
                c1 = cast_to_uint32(_get_hex_character(reader, 8))
            else:
                _raise_expected_s('UnicodeEscapeSequence', _reader_tell(reader), c1)

        buf.push_back(c1)

```

Closing lines 519–524 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L519-L524))

```
        c1 = _reader_get(reader)
        if not _is_identifier_part(c1):
            c0 = cast_to_int32(c1)
            break

    c_in_out[0] = c0
```

Original reviewed range 499–524 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0176: module initialization: __version__

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `VERSION` — static_metadata. Static const char[] assembled by native.hpp from src/VERSION.inc. Saved include source is ASCII, with no hex/Unicode/octal escapes that could introduce non-ASCII values. This is compiled package metadata, not an external/user input buffer.

**Length:** `VERSION_LENGTH`; one-byte code point elements; also ASCII bytes here; sizeof(array)-1 excludes terminating zero.

**Confirmed:** native.hpp defines VERSION and computes VERSION_LENGTH as sizeof(VERSION) - 1. Reproducer checks ASCII source and absence of non-ASCII numeric escapes in the include.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: static_metadata; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Static ASCII VERSION/LONGDESCRIPTION char arrays, not data borrowed from a Python Unicode object.; support_span_refs: package: pyjson5; path: pyjson5-2.0.1/src/native.hpp; source_sha256: 37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085; evidence_path: read-access-analysis/sources/pyjson5/37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085.hpp; start: 242; end: 245; snippet_sha256: 63c87f570e461d914fb4b26ebb6786af4f2c9d1b25f8dbb832f8c8c30c40a4bd; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L242-L245

**Migration implication:** Constructing static ASCII metadata can use a compatible UTF-8-backed implementation of this API; it is not a raw user-buffer interoperability requirement.

**Activation / tracing:** Runs at extension-module initialization. Static storage lifetime.

**Source:** `pyjson5-2.0.1/src/_exports.pyx:8–8`; SHA-256 `d687310af5345a2e5dfc7cb90433739f8873fb55c33ad4da14094061350edb8a`.

`pyjson5-2.0.1/src/_exports.pyx` lines 8–8 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_exports.pyx#L8-L8))

```
__version__ = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, VERSION, VERSION_LENGTH)
```

`pyjson5-2.0.1/src/native.hpp` lines 242–245 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L242-L245))

```
const char VERSION[] =
#   include "./VERSION.inc"
;
static constexpr std::size_t VERSION_LENGTH = sizeof(VERSION) - 1;
```

`pyjson5-2.0.1/src/_imports.pyx` lines 79–85 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_imports.pyx#L79-L85))

```
    enum:
        VERSION_LENGTH
    const char VERSION[]

    enum:
        LONGDESCRIPTION_LENGTH
    const char LONGDESCRIPTION[]
```

`pyjson5-2.0.1/src/VERSION.inc` lines 1–1 (GitHub mapping not verified in saved evidence)

```
"2.0.1"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## K0177: module initialization: __doc__

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `LONGDESCRIPTION` — static_metadata. Static const char[] assembled by native.hpp from src/DESCRIPTION.inc. Saved include source is ASCII, with no hex/Unicode/octal escapes that could introduce non-ASCII values. This is compiled package metadata, not an external/user input buffer.

**Length:** `LONGDESCRIPTION_LENGTH`; one-byte code point elements; also ASCII bytes here; sizeof(array)-1 excludes terminating zero.

**Confirmed:** native.hpp defines LONGDESCRIPTION and computes LONGDESCRIPTION_LENGTH as sizeof(LONGDESCRIPTION) - 1. Reproducer checks ASCII source and absence of non-ASCII numeric escapes in the include.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: static_metadata; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Static ASCII VERSION/LONGDESCRIPTION char arrays, not data borrowed from a Python Unicode object.; support_span_refs: package: pyjson5; path: pyjson5-2.0.1/src/native.hpp; source_sha256: 37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085; evidence_path: read-access-analysis/sources/pyjson5/37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085.hpp; start: 247; end: 250; snippet_sha256: ab70b2573a190f61ed366aa4c21bcf6bb5bc6865095859ca7437423ff0ef9b4b; verified_permalink: https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L247-L250

**Migration implication:** Constructing static ASCII metadata can use a compatible UTF-8-backed implementation of this API; it is not a raw user-buffer interoperability requirement.

**Activation / tracing:** Runs at extension-module initialization. Static storage lifetime.

**Source:** `pyjson5-2.0.1/src/_exports.pyx:620–620`; SHA-256 `d687310af5345a2e5dfc7cb90433739f8873fb55c33ad4da14094061350edb8a`.

`pyjson5-2.0.1/src/_exports.pyx` lines 620–620 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_exports.pyx#L620-L620))

```
__doc__ = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, LONGDESCRIPTION, LONGDESCRIPTION_LENGTH)
```

`pyjson5-2.0.1/src/native.hpp` lines 247–250 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L247-L250))

```
const char LONGDESCRIPTION[] =
#   include "./DESCRIPTION.inc"
;
static constexpr std::size_t LONGDESCRIPTION_LENGTH = sizeof(LONGDESCRIPTION) - 1;
```

`pyjson5-2.0.1/src/_imports.pyx` lines 79–85 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_imports.pyx#L79-L85))

```
    enum:
        VERSION_LENGTH
    const char VERSION[]

    enum:
        LONGDESCRIPTION_LENGTH
    const char LONGDESCRIPTION[]
```

`pyjson5-2.0.1/src/DESCRIPTION.inc` lines 1–10 (GitHub mapping not verified in saved evidence)

```
"""\
PyJSON5\n\
=======\n\
\n\
A `JSON5 <https://spec.json5.org/>`_ serializer and parser library for Python 3 written in Cython.\n\
\n\
The serializer returns ASCII data that can safely be used in an HTML template.\n\
Apostrophes, ampersands, greater-than, and less-then signs are encoded as\n\
unicode escaped sequences. E.g. this snippet is safe for any and all input:\n\
\n\
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.
