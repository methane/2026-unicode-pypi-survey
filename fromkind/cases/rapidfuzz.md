# rapidfuzz 3.14.6

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0088: __pyx_pf_9rapidfuzz_8distance_15_initialize_cpp_7Editops_14apply

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local proc_str.data()` — external_library_constructed_codepoint_array. rf::editops_apply_vec<uint32_t> constructs a uint32_t result vector from source/destination RF_String sequences.

**Length:** `(Py_ssize_t)proc_str.size()`; fixed_width_codepoint_elements.

**Confirmed:** Generated actual helper invocation forwards into the named header implementation. Header invokes PyUnicode_FromKindAndData with result data() and element size().

**Inference / unresolved:** Input strings may use Python FSR through convert_string; the constructor argument itself is the algorithm result, not a borrowed FSR pointer.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Preserve construction from fixed-width algorithm result arrays. Separate input-view migration is handled by the RF_String converter.

**Activation / tracing:** Python-visible edit operation apply wrapper; successful helper execution reaches the UCS4 constructor.

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.cxx:16013–16013`; SHA-256 `a5e27e40a2678c7acb6afb383539b402a497f7e32241b952847e7342b48a66c2`.

`rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.cxx` lines 16009–16017 (GitHub mapping not verified in saved evidence)

```
 * 
 *     def remove_subsequence(self, Editops subsequence):
*/
  try {
    __pyx_t_4 = editops_apply(__pyx_v_self->editops, convert_string(__pyx_v_source_string), convert_string(__pyx_v_destination_string));
    if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 478, __pyx_L1_error)
  } catch(...) {
    __Pyx_CppExn2PyErr();
    __PYX_ERR(0, 478, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0089: __pyx_pf_9rapidfuzz_8distance_15_initialize_cpp_7Opcodes_14apply

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local proc_str.data()` — external_library_constructed_codepoint_array. rf::opcodes_apply_vec<uint32_t> constructs a uint32_t result vector from source/destination RF_String sequences.

**Length:** `(Py_ssize_t)proc_str.size()`; fixed_width_codepoint_elements.

**Confirmed:** Generated actual helper invocation forwards into the named header implementation. Header invokes PyUnicode_FromKindAndData with result data() and element size().

**Inference / unresolved:** Input strings may use Python FSR through convert_string; the constructor argument itself is the algorithm result, not a borrowed FSR pointer.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Preserve construction from fixed-width algorithm result arrays. Separate input-view migration is handled by the RF_String converter.

**Activation / tracing:** Python-visible edit operation apply wrapper; successful helper execution reaches the UCS4 constructor.

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.cxx:21725–21725`; SHA-256 `a5e27e40a2678c7acb6afb383539b402a497f7e32241b952847e7342b48a66c2`.

`rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.cxx` lines 21721–21729 (GitHub mapping not verified in saved evidence)

```
 * 
 *     @property
*/
  try {
    __pyx_t_4 = opcodes_apply(__pyx_v_self->opcodes, convert_string(__pyx_v_source_string), convert_string(__pyx_v_destination_string));
    if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 781, __pyx_L1_error)
  } catch(...) {
    __Pyx_CppExn2PyErr();
    __PYX_ERR(0, 781, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0090: __pyx_pf_9rapidfuzz_9utils_cpp_default_process

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `input RF_UINT8/RF_UINT16/RF_UINT32 selects PyUnicode_1BYTE_KIND/2BYTE_KIND/4BYTE_KIND`.

**Input:** `callee-local proc_str.data()` — external_library_constructed_codepoint_array. default_process_copy produces a width-preserving fixed-width numeric string

**Length:** `(Py_ssize_t)proc_str.size()`; fixed_width_codepoint_elements.

**Confirmed:** Generated actual helper invocation forwards into the named header implementation. Header invokes PyUnicode_FromKindAndData with result data() and element size().

**Inference / unresolved:** Input strings may use Python FSR through convert_string; the constructor argument itself is the algorithm result, not a borrowed FSR pointer.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Preserve construction from fixed-width algorithm result arrays. Separate input-view migration is handled by the RF_String converter.

**Activation / tracing:** default_process_impl uses the constructor in RF_UINT8/RF_UINT16/RF_UINT32 branches; its default branch returns the input without this API.

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.cxx:6087–6087`; SHA-256 `01e693a8a9864c7591f9c3eaf420d17009f8a2c6a60a839110c54e74ba78fd41`.

`rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.cxx` lines 6083–6091 (GitHub mapping not verified in saved evidence)

```
 * 
 * 
*/
  try {
    __pyx_t_1 = default_process_impl(__pyx_v_sentence);
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  } catch(...) {
    __Pyx_CppExn2PyErr();
    __PYX_ERR(0, 24, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0103: opcodes_apply

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `proc_str.data()` — constructed_edit_result_ucs4_vector. rf::*_apply_vec<uint32_t> creates owned vector from selected source/destination code-point ranges; proc_str is not borrowed RF_String data.

**Length:** `(Py_ssize_t)proc_str.size()`; code-point elements (not bytes).

**Confirmed:** Return from explicitly uint32_t vector algorithm; constructor data and size directly refer same vector. (rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp:678–684) Both apply_vec overload families return std::vector<CharT> by value; uint32_t specialization is an owned four-byte element vector. (rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance.hpp:139–165)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input converter can borrow Python Unicode FSR; constructor always receives newly constructed vector after processing/apply.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp:678–684`; SHA-256 `7365fa1397d9b9cfd85de296aab17f5b553f7ee7e5b85d7bc96d7c22901b1fcb`.

`rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp` lines 682–682 ([verified immutable source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/cpp_common.hpp#L682-L682))

```
        return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, proc_str.data(), (Py_ssize_t)proc_str.size());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0104: editops_apply

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `proc_str.data()` — constructed_edit_result_ucs4_vector. rf::*_apply_vec<uint32_t> creates owned vector from selected source/destination code-point ranges; proc_str is not borrowed RF_String data.

**Length:** `(Py_ssize_t)proc_str.size()`; code-point elements (not bytes).

**Confirmed:** Return from explicitly uint32_t vector algorithm; constructor data and size directly refer same vector. (rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp:686–692) Both apply_vec overload families return std::vector<CharT> by value; uint32_t specialization is an owned four-byte element vector. (rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance.hpp:139–165)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input converter can borrow Python Unicode FSR; constructor always receives newly constructed vector after processing/apply.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp:686–692`; SHA-256 `7365fa1397d9b9cfd85de296aab17f5b553f7ee7e5b85d7bc96d7c22901b1fcb`.

`rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp` lines 690–690 ([verified immutable source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/cpp_common.hpp#L690-L690))

```
        return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, proc_str.data(), (Py_ssize_t)proc_str.size());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0105: default_process_impl fixed_1

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `proc_str.data()` — constructed_processed_codepoint_vector. default_process_copy creates vector<source element type>, transforms and trims it; vector data/size, not input sentence storage, enters constructor.

**Length:** `(Py_ssize_t)proc_str.size()`; code-point elements (not bytes).

**Confirmed:** RF_UINT8/16/32 determines native type and fixed constructorkind. (rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:5–28) Copies source range to vector, processes, resizes and returns it. (rapidfuzz-3.14.6/src/rapidfuzz/utils.hpp:82–89) Maps code points and trims spaces in private buffer. (rapidfuzz-3.14.6/src/rapidfuzz/utils.hpp:57–79)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input converter can borrow Python Unicode FSR; constructor always receives newly constructed vector after processing/apply.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** convert_string(sentence) accepts Unicode fixed-width borrow, bytes, or supported sequence conversion; result buffer owned regardless of source provenance.

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:5–28`; SHA-256 `48f2f1bc52fcf0ef0a9b94d06df7ae37d3c7ea8666ff78a7361398ccebd74683`.

`rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp` lines 13–13 ([verified immutable source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/utils_cpp.hpp#L13-L13))

```
        return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, proc_str.data(), (Py_ssize_t)proc_str.size());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0106: default_process_impl fixed_2

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `proc_str.data()` — constructed_processed_codepoint_vector. default_process_copy creates vector<source element type>, transforms and trims it; vector data/size, not input sentence storage, enters constructor.

**Length:** `(Py_ssize_t)proc_str.size()`; code-point elements (not bytes).

**Confirmed:** RF_UINT8/16/32 determines native type and fixed constructorkind. (rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:5–28) Copies source range to vector, processes, resizes and returns it. (rapidfuzz-3.14.6/src/rapidfuzz/utils.hpp:82–89) Maps code points and trims spaces in private buffer. (rapidfuzz-3.14.6/src/rapidfuzz/utils.hpp:57–79)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input converter can borrow Python Unicode FSR; constructor always receives newly constructed vector after processing/apply.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** convert_string(sentence) accepts Unicode fixed-width borrow, bytes, or supported sequence conversion; result buffer owned regardless of source provenance.

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:5–28`; SHA-256 `48f2f1bc52fcf0ef0a9b94d06df7ae37d3c7ea8666ff78a7361398ccebd74683`.

`rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp` lines 18–18 ([verified immutable source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/utils_cpp.hpp#L18-L18))

```
        return PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, proc_str.data(), (Py_ssize_t)proc_str.size());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0107: default_process_impl fixed_4

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `proc_str.data()` — constructed_processed_codepoint_vector. default_process_copy creates vector<source element type>, transforms and trims it; vector data/size, not input sentence storage, enters constructor.

**Length:** `(Py_ssize_t)proc_str.size()`; code-point elements (not bytes).

**Confirmed:** RF_UINT8/16/32 determines native type and fixed constructorkind. (rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:5–28) Copies source range to vector, processes, resizes and returns it. (rapidfuzz-3.14.6/src/rapidfuzz/utils.hpp:82–89) Maps code points and trims spaces in private buffer. (rapidfuzz-3.14.6/src/rapidfuzz/utils.hpp:57–79)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input converter can borrow Python Unicode FSR; constructor always receives newly constructed vector after processing/apply.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** convert_string(sentence) accepts Unicode fixed-width borrow, bytes, or supported sequence conversion; result buffer owned regardless of source provenance.

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp:5–28`; SHA-256 `48f2f1bc52fcf0ef0a9b94d06df7ae37d3c7ea8666ff78a7361398ccebd74683`.

`rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.hpp` lines 23–23 ([verified immutable source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/utils_cpp.hpp#L23-L23))

```
        return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, proc_str.data(), (Py_ssize_t)proc_str.size());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0131: Editops.apply native helper invocation

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.pyx:478–478)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.pyx:478–478`; SHA-256 `95d3d10ea54d4458c62b2125e6e5adb9ba3c4deee24ff212d3536e0a5ee4e41f`.

`rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.pyx` lines 478–478 (GitHub mapping not verified in saved evidence)

```
        return editops_apply(self.editops, convert_string(source_string), convert_string(destination_string))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0132: Opcodes.apply native helper invocation

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.pyx:781–781)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.pyx:781–781`; SHA-256 `95d3d10ea54d4458c62b2125e6e5adb9ba3c4deee24ff212d3536e0a5ee4e41f`.

`rapidfuzz-3.14.6/src/rapidfuzz/distance/_initialize_cpp.pyx` lines 781–781 (GitHub mapping not verified in saved evidence)

```
        return opcodes_apply(self.opcodes, convert_string(source_string), convert_string(destination_string))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

## K0133: default_process

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.pyx:24–24)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.pyx:22–24`; SHA-256 `bf145ab8af9e5dc3bd7c6ad16dbdfa1fe13bb0c46e0fdafa3f79ab24f20b5265`.

`rapidfuzz-3.14.6/src/rapidfuzz/utils_cpp.pyx` lines 24–24 (GitHub mapping not verified in saved evidence)

```
    return default_process_impl(sentence)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA-256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.
