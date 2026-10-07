# pysam 0.24.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0036: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `pysam-0.24.1/pysam/libcvcf.c:42117–42118`; SHA-256 `0eb79a3d0d7fe752b54d12e3fd541dc37acbd47ba8b69fbeb6afbd793a9eca91`.

`pysam-0.24.1/pysam/libcvcf.c` lines 42093–42108 (GitHub mapping not verified in saved evidence)

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

Closing lines 42115–42120 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 42093–42120 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/01/d0/e9271669f97ce454d1aa97f9ce0d3e84376295f352ad6c5d2c3998e38f66/pysam-0.24.1.tar.gz); archive SHA-256 `90f612afccdb454d2447ecb5229266c6e7f991093deed4ed0a791db01f7fc994`.

## K0070: __pyx_pf_5pysam_7libcvcf_3VCF_4parse_format

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_rest. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `pysam-0.24.1/pysam/libcvcf.c:12810–12810`; SHA-256 `0eb79a3d0d7fe752b54d12e3fd541dc37acbd47ba8b69fbeb6afbd793a9eca91`.

`pysam-0.24.1/pysam/libcvcf.c` lines 12792–12807 (GitHub mapping not verified in saved evidence)

```
      /* "pysam/libcvcf.pyx":393
 *                 data['descr'] = elts[1]
 *                 rest = '"'.join(elts[2:])
 *                 if rest.startswith(','): rest = rest[1:]             # <<<<<<<<<<<<<<
 *             else:
 *                 self.error(line,self.BADLY_FORMATTED_FORMAT_STRING)
*/
      if (unlikely(__pyx_v_rest == Py_None)) {
        PyErr_Format(PyExc_AttributeError, "\047NoneType\047 object has no attribute \047%.30s\047", "startswith");
        __PYX_ERR(0, 393, __pyx_L1_error)
      }
      __pyx_t_2 = __Pyx_PyUnicode_Tailmatch(__pyx_v_rest, __pyx_mstate_global->__pyx_kp_u__3, 0, PY_SSIZE_T_MAX, -1); if (unlikely(__pyx_t_2 == ((int)-1))) __PYX_ERR(0, 393, __pyx_L1_error)
      if (__pyx_t_2) {

        if (unlikely(__pyx_v_rest == Py_None)) {
          PyErr_SetString(PyExc_TypeError, "\047NoneType\047 object is not subscriptable");
```

Closing lines 12813–12818 (GitHub mapping not verified in saved evidence)

```
        __pyx_t_6 = 0;
      }

      /* "pysam/libcvcf.pyx":386
 *             elif first.startswith('Number='):      data['number'] = first.split('=')[1]
 *             elif first.startswith('Type='):        data['type'] = first.split('=')[1]
```

Original reviewed range 12792–12818 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/01/d0/e9271669f97ce454d1aa97f9ce0d3e84376295f352ad6c5d2c3998e38f66/pysam-0.24.1.tar.gz); archive SHA-256 `90f612afccdb454d2447ecb5229266c6e7f991093deed4ed0a791db01f7fc994`.
