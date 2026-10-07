# marisa-trie 1.4.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0032: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:38529–38530`; SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

`marisa_trie-1.4.1/src/marisa_trie.cpp` lines 38503–38518 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L38503-L38518))

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

Closing lines 38527–38532 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L38527-L38532))

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 38503–38532 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.

## K0064: __pyx_f_11marisa_trie_9BytesTrie_prefixes

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_key. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:23064–23064`; SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

`marisa_trie-1.4.1/src/marisa_trie.cpp` lines 23046–23061 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L23046-L23061))

```
 *             prefix = key[:ind]
 *             b_prefix = <bytes>(prefix.encode('utf8') + self._b_value_separator)
*/
  while (1) {
    __pyx_t_7 = (__pyx_v_ind <= __pyx_v_key_len);
    if (!__pyx_t_7) break;

    /* "marisa_trie.pyx":871
 * 
 *         while ind <= key_len:
 *             prefix = key[:ind]             # <<<<<<<<<<<<<<
 *             b_prefix = <bytes>(prefix.encode('utf8') + self._b_value_separator)
 *             ag.set_query(b_prefix)
*/
    if (unlikely(__pyx_v_key == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 23067–23072 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L23067-L23072))

```
    __pyx_t_1 = 0;

    /* "marisa_trie.pyx":872
 *         while ind <= key_len:
 *             prefix = key[:ind]
 *             b_prefix = <bytes>(prefix.encode('utf8') + self._b_value_separator)             # <<<<<<<<<<<<<<
```

Original reviewed range 23046–23072 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.
