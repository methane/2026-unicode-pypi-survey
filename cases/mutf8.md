# mutf8 — non-simple Unicode reads

[All packages](README.md)

Version: 1.1.0. **1 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`encode_modified_utf8`](#case-001)

<a id="case-001"></a>

## 1. `encode_modified_utf8`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Slow path calls _encoded_size then reads input again in encoding loop; fast path searches NUL then delegates surrogatepass encoder.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

surrogatepass directly matches MUTF8 only when no supplementary codepoint and no NUL. NUL uses C0 80 and supplementary characters become two surrogate triples.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/5c/74/bfce3ab421b39503c6cd11a6bc812a763154082a4f69d55831d762e58fcd/mutf8-1.1.0.tar.gz). Archive SHA-256: `279796be8926ea53ac226a831727725387f3acadcfc5aa723f8a5ada559dae3a`.

**Function source:** `mutf8-1.1.0/mutf8/cmutf8.c`, lines 189–258. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`.

[Verified immutable function link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L189-L258).

### Read sites

- Site 1: lines 197–221; derived read; index expression `data[i], i=0..length-1; _encoded_size`. Two full slow-path passes

### Contextual source excerpts

Omitted from `mutf8-1.1.0/mutf8/cmutf8.c`: lines 210–215, 226–255. The original contextual region was lines 189–258.
Omitted from `mutf8-1.1.0/mutf8/cmutf8.c`: lines 210–215, 226–255. The original contextual region was lines 197–258.

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 138–158. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L138-L158).

```c
inline Py_ssize_t _encoded_size(void *data, Py_ssize_t length, int kind) {
    Py_ssize_t byte_count = 0;

    for (Py_ssize_t i = 0; i < length; i++) {
        Py_UCS4 cp = PyUnicode_READ(kind, data, i);
        if (cp == 0x00) {
            // NULLs will get encoded as C0 80.
            byte_count += 2;
        } else if (cp <= 0x7F) {
            byte_count++;
        } else if (cp <= 0x7FF) {
            byte_count += 2;
        } else if (cp <= 0xFFFF) {
            byte_count += 3;
        } else {
            byte_count += 6;
        }
    }

    return byte_count;
}
```

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 189–209. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L189-L209).

```c
encode_modified_utf8(PyObject *self, PyObject *args)
{
    PyObject *src = NULL;

    if (!PyArg_ParseTuple(args, "U", &src)) {
        return NULL;
    }

    void *data = PyUnicode_DATA(src);
    Py_ssize_t length = PyUnicode_GET_LENGTH(src);
    int kind = PyUnicode_KIND(src);

    // Fast path: with no supplementary char (kind < 4-byte) and no embedded
    // NUL, MUTF-8 == UTF-8 with "surrogatepass" (same 3-byte form for lone
    // surrogates). Offload to CPython's optimized encoder.
    if (kind != PyUnicode_4BYTE_KIND &&
        PyUnicode_FindChar(src, 0, 0, length, 1) == -1) {
        return PyUnicode_AsEncodedString(src, "utf-8", "surrogatepass");
    }

    // Allocate the result up front at its exact size and write straight into
```

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 216–225. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L216-L225).

```c
    char *byte_out = PyBytes_AS_STRING(out);

    Py_ssize_t byte_count = 0;

    for (Py_ssize_t i = 0; i < length; i++) {
        Py_UCS4 cp = PyUnicode_READ(kind, data, i);
        if (cp == 0x00) {
            // NULL byte encoding shortcircuit.
            byte_out[byte_count++] = 0xC0;
            byte_out[byte_count++] = 0x80;
```

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 256–258. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L256-L258).

```c

    return out;
}
```

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 197–209. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L197-L209).

```c
    void *data = PyUnicode_DATA(src);
    Py_ssize_t length = PyUnicode_GET_LENGTH(src);
    int kind = PyUnicode_KIND(src);

    // Fast path: with no supplementary char (kind < 4-byte) and no embedded
    // NUL, MUTF-8 == UTF-8 with "surrogatepass" (same 3-byte form for lone
    // surrogates). Offload to CPython's optimized encoder.
    if (kind != PyUnicode_4BYTE_KIND &&
        PyUnicode_FindChar(src, 0, 0, length, 1) == -1) {
        return PyUnicode_AsEncodedString(src, "utf-8", "surrogatepass");
    }

    // Allocate the result up front at its exact size and write straight into
```

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 216–225. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L216-L225).

```c
    char *byte_out = PyBytes_AS_STRING(out);

    Py_ssize_t byte_count = 0;

    for (Py_ssize_t i = 0; i < length; i++) {
        Py_UCS4 cp = PyUnicode_READ(kind, data, i);
        if (cp == 0x00) {
            // NULL byte encoding shortcircuit.
            byte_out[byte_count++] = 0xC0;
            byte_out[byte_count++] = 0x80;
```

Archive member `mutf8-1.1.0/mutf8/cmutf8.c`, lines 256–258. Member SHA-256: `cdc0f6db34572efce66af958590224e9e0c91c1509bd465b185302f1d83aaa2e`. [Verified immutable source link](https://github.com/TkTech/mutf8/blob/fb540a896811cf38fc4e7d36ac7cb9bd97cab3a3/mutf8/cmutf8.c#L256-L258).

```c

    return out;
}
```
