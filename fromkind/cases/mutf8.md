# mutf8 1.1.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0164: decode_modified_utf8

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `cp_out` — constructed codepoint array. PyMem_Calloc(view.len,sizeof(Py_UCS4)) scratch; cp_count increments decoded scalars. Modified UTF8 special NUL and six-byte surrogate pair processed, isolated surrogate values possible. Input bytes received by y* buffer.

**Length:** `cp_count`; Py_UCS4 codepoint elements, not input byte count.

**Confirmed:** Exact retained source snippet included (mutf8-1.1.0/mutf8/cmutf8.c:30–62) Exact retained source snippet included (mutf8-1.1.0/mutf8/cmutf8.c:64–136)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Constructor occurs only special-byte path; uncomplicated bytes use PyUnicode_DecodeUTF8. Scratch and input view freed/released after call.

**Source:** `mutf8-1.1.0/mutf8/cmutf8.c:12–136`; SHA-256 `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`.

`mutf8-1.1.0/mutf8/cmutf8.c` lines 30–45 ([verified immutable source](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L30-L45))

```
    if (!PyArg_ParseTuple(args, "y*", &view)) {
        return NULL;
    }

    // MUTF-8 input.
    uint8_t *buf = (uint8_t *)view.buf;

    // Fast path: without 0xED (leads every surrogate/6-byte form), 0xC0 (the
    // NUL escape) or a raw 0x00 (illegal), the input is plain UTF-8. Offload
    // to CPython's optimized decoder; on any error fall back to the strict
    // loop below so the exception is still reported as mutf-8.
    if (memchr(buf, 0xED, view.len) == NULL &&
        memchr(buf, 0xC0, view.len) == NULL &&
        memchr(buf, 0x00, view.len) == NULL) {
        PyObject *fast = PyUnicode_DecodeUTF8((const char *)buf, view.len, NULL);
        if (fast != NULL) {
```

Closing lines 57–62 ([verified immutable source](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L57-L62))

```
    if (!cp_out) {
        return PyErr_NoMemory();
    }

    // # of codepoints we found & current index into cp_out.
    Py_ssize_t cp_count = 0;
```

Original reviewed range 30–62 is recorded in `data/sites.json`; public excerpts are bounded.

`mutf8-1.1.0/mutf8/cmutf8.c` lines 64–79 ([verified immutable source](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L64-L79))

```
    for (Py_ssize_t ix = 0; ix < view.len; ix++) {
        Py_UCS4 x = buf[ix];

        if (x == 0) {
            return_err("Embedded NULL byte in input.");
        }
        else if (x < 0x80) {
            // ASCII/one-byte codepoint.
            x &= 0x7F;
        }
        else if ((x & 0xE0) == 0xC0) {
            // Two-byte codepoint.
            if (ix + 1 >= view.len) {
                return_err(
                    "2-byte codepoint started, but input too short"
                    " to finish.");
```

Closing lines 131–136 ([verified immutable source](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L131-L136))

```

    PyMem_Free(cp_out);
    PyBuffer_Release(&view);
    return out;
#undef return_err
}
```

Original reviewed range 64–136 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/5c/74/bfce3ab421b39503c6cd11a6bc812a763154082a4f69d55831d762e58fcd/mutf8-1.1.0.tar.gz); archive SHA-256 `279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a`.
