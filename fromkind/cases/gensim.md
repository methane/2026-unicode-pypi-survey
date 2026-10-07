# gensim 4.4.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0031: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `gensim-4.4.0/gensim/models/fasttext_inner.c:9839–9840`; SHA-256 `9353c181221c9f127d63b0b2627c548d18a22d274a1abe8cdbde8f85c7f21782`.

`gensim-4.4.0/gensim/models/fasttext_inner.c` lines 9822–9837 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    length = __Pyx_PyUnicode_GET_LENGTH(text);
    if (start < 0) {
        start += length;
        if (start < 0)
            start = 0;
    }
    if (stop < 0)
        stop += length;
    else if (stop > length)
        stop = length;
    if (stop <= start)
        return __Pyx_NewRef(__pyx_empty_unicode);
```

Closing lines 9839–9844 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#else
    return PyUnicode_FromUnicode(PyUnicode_AS_UNICODE(text)+start, stop-start);
#endif
}
```

Original reviewed range 9822–9844 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## K0063: __pyx_f_6gensim_6models_14fasttext_inner_compute_ngrams

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_extended_word. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `gensim-4.4.0/gensim/models/fasttext_inner.c:6477–6477`; SHA-256 `9353c181221c9f127d63b0b2627c548d18a22d274a1abe8cdbde8f85c7f21782`.

`gensim-4.4.0/gensim/models/fasttext_inner.c` lines 6459–6474 (GitHub mapping not verified in saved evidence)

```
      __pyx_t_11 = (__pyx_t_1 == Py_None);
      if (__pyx_t_11) {
        __pyx_t_10 = 0;
      } else {
        __pyx_t_12 = __Pyx_PyIndex_AsSsize_t(__pyx_t_1); if (unlikely((__pyx_t_12 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 666, __pyx_L1_error)
        __pyx_t_10 = __pyx_t_12;
      }
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = PyNumber_Add(__pyx_v_i, __pyx_v_ngram_length); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 666, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_11 = (__pyx_t_1 == Py_None);
      if (__pyx_t_11) {
        __pyx_t_12 = PY_SSIZE_T_MAX;
      } else {
        __pyx_t_13 = __Pyx_PyIndex_AsSsize_t(__pyx_t_1); if (unlikely((__pyx_t_13 == (Py_ssize_t)-1) && PyErr_Occurred())) __PYX_ERR(0, 666, __pyx_L1_error)
        __pyx_t_12 = __pyx_t_13;
```

Closing lines 6480–6485 (GitHub mapping not verified in saved evidence)

```
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      /* "gensim/models/fasttext_inner.pyx":665
 *     ngrams = []
 *     for ngram_length in range(min_n, min(len(extended_word), max_n) + 1):
 *         for i in range(0, len(extended_word) - ngram_length + 1):             # <<<<<<<<<<<<<<
```

Original reviewed range 6459–6485 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.
