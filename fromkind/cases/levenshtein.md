# levenshtein 0.27.5

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0013: __pyx_pf_11Levenshtein_15levenshtein_cpp_median

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_median.data()` — external_library_constructed_codepoint_array. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `__pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Generated local declaration is std::vector<uint32_t>. Algorithm return assigned to median before data()/size() conversion.

**Inference / unresolved:** The library median algorithms produce Unicode numeric elements from input sequences.

**Upstream representation coupling:** Borrowed FSR depends on input type and occurs before the output constructor. Supporting converter is retained in this package _levenshtein.hpp; no cross-package cpp_common.hpp assumption is needed.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Python-visible median-family functions; copied input converter and algorithm readers are separate from this output conversion.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:3488–3488`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3484–3492 (GitHub mapping not verified in saved evidence)

```
 *     return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())             # <<<<<<<<<<<<<<
 * 
 * def quickmedian(strlist, wlist = None, *):
*/
  __pyx_t_4 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_median.data(), __pyx_v_median.size()); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 91, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  {
    PyObject *__pyx_temp;
    {
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3432–3436 (GitHub mapping not verified in saved evidence)

```
  std::vector<RF_String>  __pyx_v_strings;
  std::vector<double>  __pyx_v_weights;
  std::vector<uint32_t>  __pyx_v_median;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3437–3441 (GitHub mapping not verified in saved evidence)

```
  std::vector<RF_String>  __pyx_t_1;
  std::vector<double>  __pyx_t_2;
  std::vector<uint32_t>  __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3459–3463 (GitHub mapping not verified in saved evidence)

```
 *     weights = extract_weightlist(wlist, strings.size())             # <<<<<<<<<<<<<<
 * 
 *     median = lev_greedy_median(strings, weights)
*/
  __pyx_t_2 = __pyx_f_11Levenshtein_15levenshtein_cpp_extract_weightlist(__pyx_v_wlist, __pyx_v_strings.size()); if (unlikely(PyErr_Occurred())) __PYX_ERR(0, 88, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0014: __pyx_pf_11Levenshtein_15levenshtein_cpp_2quickmedian

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_median.data()` — external_library_constructed_codepoint_array. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `__pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Generated local declaration is std::vector<uint32_t>. Algorithm return assigned to median before data()/size() conversion.

**Inference / unresolved:** The library median algorithms produce Unicode numeric elements from input sequences.

**Upstream representation coupling:** Borrowed FSR depends on input type and occurs before the output constructor. Supporting converter is retained in this package _levenshtein.hpp; no cross-package cpp_common.hpp assumption is needed.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Python-visible median-family functions; copied input converter and algorithm readers are separate from this output conversion.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:3689–3689`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3685–3693 (GitHub mapping not verified in saved evidence)

```
 *     return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())             # <<<<<<<<<<<<<<
 * 
 * def median_improve(string, strlist, wlist = None, *):
*/
  __pyx_t_4 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_median.data(), __pyx_v_median.size()); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 114, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  {
    PyObject *__pyx_temp;
    {
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3633–3637 (GitHub mapping not verified in saved evidence)

```
  std::vector<RF_String>  __pyx_v_strings;
  std::vector<double>  __pyx_v_weights;
  std::vector<uint32_t>  __pyx_v_median;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3638–3642 (GitHub mapping not verified in saved evidence)

```
  std::vector<RF_String>  __pyx_t_1;
  std::vector<double>  __pyx_t_2;
  std::vector<uint32_t>  __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3650–3654 (GitHub mapping not verified in saved evidence)

```
 *     strings = extract_stringlist(strlist)             # <<<<<<<<<<<<<<
 *     weights = extract_weightlist(wlist, strings.size())
 *     median = lev_quick_median(strings, weights)
*/
  __pyx_t_1 = __pyx_f_11Levenshtein_15levenshtein_cpp_extract_stringlist(__pyx_v_strlist); if (unlikely(PyErr_Occurred())) __PYX_ERR(0, 111, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0015: __pyx_pf_11Levenshtein_15levenshtein_cpp_4median_improve

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_median.data()` — external_library_constructed_codepoint_array. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `__pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Generated local declaration is std::vector<uint32_t>. Algorithm return assigned to median before data()/size() conversion.

**Inference / unresolved:** The library median algorithms produce Unicode numeric elements from input sequences.

**Upstream representation coupling:** Borrowed FSR depends on input type and occurs before the output constructor. Supporting converter is retained in this package _levenshtein.hpp; no cross-package cpp_common.hpp assumption is needed.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Python-visible median-family functions; copied input converter and algorithm readers are separate from this output conversion.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:3910–3910`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3906–3914 (GitHub mapping not verified in saved evidence)

```
 *     return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())             # <<<<<<<<<<<<<<
 * 
 * def setmedian(strlist, wlist = None, *):
*/
  __pyx_t_5 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_median.data(), __pyx_v_median.size()); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 146, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  {
    PyObject *__pyx_temp;
    {
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3843–3847 (GitHub mapping not verified in saved evidence)

```
  std::vector<double>  __pyx_v_weights;
  RF_String __pyx_v_query;
  std::vector<uint32_t>  __pyx_v_median;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3849–3853 (GitHub mapping not verified in saved evidence)

```
  std::vector<double>  __pyx_t_2;
  RF_String __pyx_t_3;
  std::vector<uint32_t>  __pyx_t_4;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3871–3875 (GitHub mapping not verified in saved evidence)

```
 *     weights = extract_weightlist(wlist, strings.size())             # <<<<<<<<<<<<<<
 *     query = conv_sequence(string)
 *     median = lev_median_improve(query, strings, weights)
*/
  __pyx_t_2 = __pyx_f_11Levenshtein_15levenshtein_cpp_extract_weightlist(__pyx_v_wlist, __pyx_v_strings.size()); if (unlikely(PyErr_Occurred())) __PYX_ERR(0, 143, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0016: __pyx_pf_11Levenshtein_15levenshtein_cpp_6setmedian

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `__pyx_v_median.data()` — external_library_constructed_codepoint_array. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `__pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Generated local declaration is std::vector<uint32_t>. Algorithm return assigned to median before data()/size() conversion.

**Inference / unresolved:** The library median algorithms produce Unicode numeric elements from input sequences.

**Upstream representation coupling:** Borrowed FSR depends on input type and occurs before the output constructor. Supporting converter is retained in this package _levenshtein.hpp; no cross-package cpp_common.hpp assumption is needed.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Python-visible median-family functions; copied input converter and algorithm readers are separate from this output conversion.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:4112–4112`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 4108–4116 (GitHub mapping not verified in saved evidence)

```
 *     return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())             # <<<<<<<<<<<<<<
 * 
 * def setratio(strlist1, strlist2, *):
*/
  __pyx_t_4 = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, __pyx_v_median.data(), __pyx_v_median.size()); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 168, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  {
    PyObject *__pyx_temp;
    {
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 4056–4060 (GitHub mapping not verified in saved evidence)

```
  std::vector<RF_String>  __pyx_v_strings;
  std::vector<double>  __pyx_v_weights;
  std::vector<uint32_t>  __pyx_v_median;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 4061–4065 (GitHub mapping not verified in saved evidence)

```
  std::vector<RF_String>  __pyx_t_1;
  std::vector<double>  __pyx_t_2;
  std::vector<uint32_t>  __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
```

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 4073–4077 (GitHub mapping not verified in saved evidence)

```
 *     strings = extract_stringlist(strlist)             # <<<<<<<<<<<<<<
 *     weights = extract_weightlist(wlist, strings.size())
 *     median = lev_set_median(strings, weights)
*/
  __pyx_t_1 = __pyx_f_11Levenshtein_15levenshtein_cpp_extract_stringlist(__pyx_v_strlist); if (unlikely(PyErr_Occurred())) __PYX_ERR(0, 165, __pyx_L1_error)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0074: __pyx_pw_11Levenshtein_15levenshtein_cpp_1median

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_median.data()` — external_library_constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `callee-local: __pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:3421–3421`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3417–3425 (GitHub mapping not verified in saved evidence)

```
  __Pyx_AddTraceback("Levenshtein.levenshtein_cpp.median", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_11Levenshtein_15levenshtein_cpp_median(__pyx_self, __pyx_v_strlist, __pyx_v_wlist);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0075: __pyx_pw_11Levenshtein_15levenshtein_cpp_3quickmedian

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_median.data()` — external_library_constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `callee-local: __pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:3622–3622`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3618–3626 (GitHub mapping not verified in saved evidence)

```
  __Pyx_AddTraceback("Levenshtein.levenshtein_cpp.quickmedian", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_11Levenshtein_15levenshtein_cpp_2quickmedian(__pyx_self, __pyx_v_strlist, __pyx_v_wlist);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0076: __pyx_pw_11Levenshtein_15levenshtein_cpp_5median_improve

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_median.data()` — external_library_constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `callee-local: __pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:3831–3831`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 3827–3835 (GitHub mapping not verified in saved evidence)

```
  __Pyx_AddTraceback("Levenshtein.levenshtein_cpp.median_improve", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_11Levenshtein_15levenshtein_cpp_4median_improve(__pyx_self, __pyx_v_string, __pyx_v_strlist, __pyx_v_wlist);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0077: __pyx_pw_11Levenshtein_15levenshtein_cpp_7setmedian

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `callee-local: __pyx_v_median.data()` — external_library_constructed_codepoint_array. This caller activates the reviewed provider; the actual constructor buffer is prepared inside that callee. std::vector<uint32_t> median returned by lev_greedy_median/lev_quick_median/lev_median_improve/lev_set_median. data() supplies uint32_t elements; size() is vector element count.

**Length:** `callee-local: __pyx_v_median.size()`; four_byte_codepoint_elements.

**Confirmed:** Actual invocation of a same-file function containing the target API expression.

**Inference / unresolved:** Whether target execution occurs depends on the provider control flow (decoding success, nonempty items, etc.).

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Keep conversion from constructed UCS4 arrays; this call does not assume Python output FSR layout.

**Activation / tracing:** Generated Python entry wrapper or parser provider activation; counted separately from the direct API expression in its callee.

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx:4045–4045`; SHA-256 `0802cd92c59a314b3865ffcedd9d99ca639c7344f59c354ff9d07bd58ea38d4a`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.cxx` lines 4041–4049 (GitHub mapping not verified in saved evidence)

```
  __Pyx_AddTraceback("Levenshtein.levenshtein_cpp.setmedian", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_11Levenshtein_15levenshtein_cpp_6setmedian(__pyx_self, __pyx_v_strlist, __pyx_v_wlist);

  /* function exit code */
  for (Py_ssize_t __pyx_temp=0; __pyx_temp < (Py_ssize_t)(sizeof(values)/sizeof(values[0])); ++__pyx_temp) {
    Py_XDECREF(values[__pyx_temp]);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0109: Cython extern constructor declaration

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** declaration; expression `int kind`.

**Input:** `const void *buffer` — none. Type declaration only; no buffer consumed.

**Length:** `Py_ssize_t size`; declaration only.

**Confirmed:** Declares C API and uint32_t vector-returning median algorithms. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:8–16)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Declaration only.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:8–10`; SHA-256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx` lines 10–10 (GitHub mapping not verified in saved evidence)

```
    object PyUnicode_FromKindAndData(int kind, const void *buffer, Py_ssize_t size)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0110: median

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `median.data()` — constructed_median_ucs4_vector. median returns vector[uint32_t] from lev_* routine; median.data/size is owned vector. setmedian selects input string but returns copied code points in vector.

**Length:** `median.size()`; code-point elements (not bytes).

**Confirmed:** All median native routines explicitly return vector[uint32_t]. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:12–16) Wrapper computes vector before construction. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:86–91)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Native median algorithm consumes converted RF_String and returns independent uint32_t vector, even when selecting an input string.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:64–91`; SHA-256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx` lines 91–91 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0111: quickmedian

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `median.data()` — constructed_median_ucs4_vector. median returns vector[uint32_t] from lev_* routine; median.data/size is owned vector. setmedian selects input string but returns copied code points in vector.

**Length:** `median.size()`; code-point elements (not bytes).

**Confirmed:** All median native routines explicitly return vector[uint32_t]. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:12–16) Wrapper computes vector before construction. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:109–114)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Native median algorithm consumes converted RF_String and returns independent uint32_t vector, even when selecting an input string.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:93–114`; SHA-256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx` lines 114–114 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0112: median_improve

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `median.data()` — constructed_median_ucs4_vector. median returns vector[uint32_t] from lev_* routine; median.data/size is owned vector. setmedian selects input string but returns copied code points in vector.

**Length:** `median.size()`; code-point elements (not bytes).

**Confirmed:** All median native routines explicitly return vector[uint32_t]. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:12–16) Wrapper computes vector before construction. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:141–146)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Native median algorithm consumes converted RF_String and returns independent uint32_t vector, even when selecting an input string.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:116–146`; SHA-256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx` lines 146–146 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

## K0113: setmedian

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `median.data()` — constructed_median_ucs4_vector. median returns vector[uint32_t] from lev_* routine; median.data/size is owned vector. setmedian selects input string but returns copied code points in vector.

**Length:** `median.size()`; code-point elements (not bytes).

**Confirmed:** All median native routines explicitly return vector[uint32_t]. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:12–16) Wrapper computes vector before construction. (levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:163–168) Selected input range is copied into returned std::vector<uint32_t>; not a borrowed pointer. (levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp:523–527)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Native median algorithm consumes converted RF_String and returns independent uint32_t vector, even when selecting an input string.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** 

**Source:** `levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx:148–168`; SHA-256 `b5aea2c13b5d2d3bce616b1e9423951cb27e5568b65f1968c0cbbc6ad3598ba7`.

`levenshtein-0.27.5/src/Levenshtein/levenshtein_cpp.pyx` lines 168–168 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, median.data(), median.size())
```

[Frozen source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz); archive SHA-256 `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.
