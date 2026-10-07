# cython 3.3.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0010: declaration_or_module_region

**Disposition:** non-use context; `non_use`; `cython_template`.

**Kind:** None; expression `None`.

**Input:** `None` — None. None

**Length:** `None`; None.

**Confirmed:** Cython extern declaration; no buffer is supplied and no runtime invocation occurs.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Declaration only; no runtime input buffer.

**Migration implication:** Update declaration only if the public API signature changes.

**Activation / tracing:** 

**Source:** `cython-3.3.0/Cython/Includes/cpython/unicode.pxd:139–139`; SHA-256 `ebc720bae23770c25bb296eac113eece6a6325f3ac65efc8575d09be131df854`.

`cython-3.3.0/Cython/Includes/cpython/unicode.pxd` lines 139–139 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Includes/cpython/unicode.pxd#L139-L139))

```
    unicode PyUnicode_FromKindAndData(int kind, const void *buffer, Py_ssize_t size)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## K0011: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `cython_template`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `cython-3.3.0/Cython/Utility/StringTools.c:821–822`; SHA-256 `a9b4f6124f46993d8cd1d19e9402772663cd21e99166ce99f32f05f12410baf6`.

`cython-3.3.0/Cython/Utility/StringTools.c` lines 796–811 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/StringTools.c#L796-L811))

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

Closing lines 819–824 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/StringTools.c#L819-L824))

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 796–824 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.
