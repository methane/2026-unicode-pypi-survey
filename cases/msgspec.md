# msgspec — non-simple Unicode reads

[All packages](README.md)

Version: 0.22.0. **1 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`json_decode_dict_key`](#case-001)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `json_decode_dict_key`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_original`.

Mixed: parses selected JSON string through lookahead byte parser then hashes its view; compares existing cached compact ASCII FSR by full memcmp. Input JSON view may originate from Unicode or bytes; existing key is raw ASCII input.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** UTF8 bytes; inline ASCII byte offsets coincide with codepoints only in compact ASCII branch

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Raw read cache site 18040..18042; new output at18051 excluded. Supplementary parser behavior is byte-oriented, not arbitrary codepoint indexing.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz). Archive SHA-256: `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

**Function source:** `msgspec-0.22.0/src/msgspec/_core.c`, lines 18021–18061. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

[Verified immutable function link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18021-L18061).

### Read sites

- Site 1: lines 18021–18061; derived UTF8 byte read; index expression `self->input_pos subrange; existing ASCII[0:size]`. Mixed: parses selected JSON string through lookahead byte parser then hashes its view; compares existing cached compact ASCII FSR by full memcmp. Input JSON view may originate from Unicode or bytes; existing key is raw ASCII input.

### Contextual source excerpts

Omitted from `msgspec-0.22.0/src/msgspec/_core.c`: lines 18025–18031, 18042–18044. The original contextual region was lines 18021–18061.

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 18021–18024. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18021-L18024).

```c
json_decode_dict_key(JSONDecoderState *self, TypeNode *type, PathNode *path) {
    bool is_ascii = true;
    char *view = NULL;
    Py_ssize_t size;
```

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 18032–18041. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18032-L18041).

```c
        return json_decode_dict_key_fallback(self, view, size, is_ascii, type, path);
    }

    uint32_t hash = murmur2(view, size);
    uint32_t index = hash % STRING_CACHE_SIZE;
    PyObject *existing = string_cache[index];

    if (MS_LIKELY(existing != NULL)) {
        Py_ssize_t e_size = ((PyASCIIObject *)existing)->length;
        char *e_str = ascii_get_buffer(existing);
```

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 18045–18061. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18045-L18061).

```c
        }
    }

    /* Create a new ASCII str object */
    PyObject *new = PyUnicode_New(size, 127);
    if (MS_UNLIKELY(new == NULL)) return NULL;
    memcpy(ascii_get_buffer(new), view, size);

    /* Swap out the str in the cache */
    Py_XDECREF(existing);
    Py_INCREF(new);
    string_cache[index] = new;
    return new;
#else
    return json_decode_dict_key_fallback(self, view, size, is_ascii, type, path);
#endif
}
```

### Callee analysis

- `json_decode_string_view` in `msgspec-0.22.0/src/msgspec/_core.c`, lines 17673–17727: Exact recovered source, SHA256 83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c Selected range plus 8-byte lookahead
- `murmur2` in `msgspec-0.22.0/src/msgspec/_core.c`, lines 366–396: Exact recovered source, SHA256 83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c Byte hashing with tail reverse indexes
- `ascii_get_buffer` in `msgspec-0.22.0/src/msgspec/_core.c`, lines 216–218: Exact recovered source, SHA256 83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c Existing cached ASCII buffer compared in memcmp
- `json_decode_dict_key_fallback` in `msgspec-0.22.0/src/msgspec/_core.c`, lines 17963–18018: Exact recovered source, SHA256 83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c B: Selected parsed key view numeric/base64/date algorithms may reread or inspect tail; new ASCII object buffer is output-only.

Available source context:
Omitted from `msgspec-0.22.0/src/msgspec/_core.c`: lines 17680–17704, 17714–17724. The original contextual region was lines 17673–17727.
Omitted from `msgspec-0.22.0/src/msgspec/_core.c`: lines 17980–18015. The original contextual region was lines 17963–18018.

- [`json_decode_string_view`](#helper-001) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 17673–17679).
- [`json_decode_string_view`](#helper-002) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 17705–17713).
- [`json_decode_string_view`](#helper-003) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 17725–17727).
- [`murmur2`](#helper-004) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 366–396).
- [`ascii_get_buffer`](#helper-005) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 216–218).
- [`json_decode_dict_key_fallback`](#helper-006) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 17963–17979).
- [`json_decode_dict_key_fallback`](#helper-007) (`msgspec-0.22.0/src/msgspec/_core.c`, lines 18016–18018).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `json_decode_string_view`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 17673–17679. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17673-L17679).

```c
json_decode_string_view(JSONDecoderState *self, char **out, bool *is_ascii) {
    self->input_pos++; /* Skip '"' */
    unsigned char *start = self->input_pos;

    /* Loop until `"`, `\`, or a non-ascii character */
    while (self->input_end - self->input_pos >= 8) {
        repeat8(parse_ascii_pre);
```

<a id="helper-002"></a>

### 2. `json_decode_string_view`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 17705–17713. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17705-L17713).

```c
            self->input_pos += 8;
            continue;
            repeat8(parse_unicode_post);
        }
        while (true) {
            if (MS_UNLIKELY(self->input_pos == self->input_end)) return ms_err_truncated();
            if (MS_UNLIKELY(char_is_special(*self->input_pos))) break;
            self->input_pos++;
        }
```

<a id="helper-003"></a>

### 3. `json_decode_string_view`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 17725–17727. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17725-L17727).

```c

    return json_decode_string_view_copy(self, out, is_ascii, start);
}
```

<a id="helper-004"></a>

### 4. `murmur2`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 366–396. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L366-L396).

```c
murmur2(const char *p, Py_ssize_t len) {
    const unsigned char *buf = (unsigned char *)p;
    const size_t m = 0x5bd1e995;
    uint32_t hash = (uint32_t)len;

    while(len >= 4) {
        uint32_t k = unaligned_load(buf);
        k *= m;
        k ^= k >> 24;
        k *= m;
        hash *= m;
        hash ^= k;
        buf += 4;
        len -= 4;
    }

    switch(len) {
        case 3:
            hash ^= buf[2] << 16;
        case 2:
            hash ^= buf[1] << 8;
        case 1:
            hash ^= buf[0];
            hash *= m;
    };

    hash ^= hash >> 13;
    hash *= m;
    hash ^= hash >> 15;
    return hash;
}
```

<a id="helper-005"></a>

### 5. `ascii_get_buffer`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 216–218. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L216-L218).

```c
ascii_get_buffer(PyObject *str) {
    return (char *)(((PyASCIIObject *)str) + 1);
}
```

<a id="helper-006"></a>

### 6. `json_decode_dict_key_fallback`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 17963–17979. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17963-L17979).

```c
json_decode_dict_key_fallback(
    JSONDecoderState *self,
    const char *view, Py_ssize_t size, bool is_ascii, TypeNode *type, PathNode *path
) {
    if (type->types & (MS_TYPE_STR | MS_TYPE_ANY)) {
        PyObject *out;
        if (is_ascii) {
            out = PyUnicode_New(size, 127);
            if (MS_UNLIKELY(out == NULL)) return NULL;
            memcpy(ascii_get_buffer(out), view, size);
        }
        else {
            out = PyUnicode_DecodeUTF8(view, size, NULL);
        }
        if (MS_UNLIKELY(type->types & (MS_TYPE_CUSTOM | MS_TYPE_CUSTOM_GENERIC))) {
            return ms_decode_custom(out, self->dec_hook, type, path);
        }
```

<a id="helper-007"></a>

### 7. `json_decode_dict_key_fallback`

Archive member `msgspec-0.22.0/src/msgspec/_core.c`, lines 18016–18018. Member SHA-256: `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`. [Verified immutable source link](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18016-L18018).

```c
        return ms_validation_error("str", type, path);
    }
}
```
