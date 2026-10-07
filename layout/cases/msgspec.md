# msgspec 0.22.0

15 confirmed layout regions; 15 reviewed regions including non-direct context.

## L1109: unicode_str_and_size_nocheck and checked wrapper

**Classification:** direct layout dependency; project_source; `utf8_cache_header_read`.

**Purpose:** Fast borrowed UTF8 getter used by serializer/metadata/token helpers and input buffer setup.

**Migration effect:** Replace direct cache/header assumption with UTF8 API or new representation-aware getter.

**Fields / layout:** length, utf8_length, utf8, ASCII header+1. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:193–213`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Checked wrapper bypasses nocheck in Py_GIL_DISABLED; direct nocheck calls remain for prevalidated cached strings. ms_get_buffer stores owned source reference beside borrowed view at223-230.

Lines 193–210 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L193-L210))

```
/* XXX: Optimized `PyUnicode_AsUTF8AndSize` for strs that we know have
 * a cached unicode representation. */
static inline const char *
unicode_str_and_size_nocheck(PyObject *str, Py_ssize_t *size) {
    if (MS_LIKELY(PyUnicode_IS_COMPACT_ASCII(str))) {
        *size = ((PyASCIIObject *)str)->length;
        return (char *)(((PyASCIIObject *)str) + 1);
    }
    *size = ((PyCompactUnicodeObject *)str)->utf8_length;
    return ((PyCompactUnicodeObject *)str)->utf8;
}

/* XXX: Optimized `PyUnicode_AsUTF8AndSize` */
static inline const char *
unicode_str_and_size(PyObject *str, Py_ssize_t *size) {
#ifndef Py_GIL_DISABLED
    const char *out = unicode_str_and_size_nocheck(str, size);
    if (MS_LIKELY(out != NULL)) return out;
```

Excerpt shortened; the complete reviewed range 193–213 is in `data/cases.json`.

Closing lines 211–213 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L211-L213))

```
#endif
    return PyUnicode_AsUTF8AndSize(str, size);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1110: ascii_get_buffer

**Classification:** direct layout dependency; project_source; `inline_payload_header_arithmetic`.

**Purpose:** Return mutable ASCII payload address used for new outputs and cached ASCII comparisons.

**Migration effect:** This explicit physical destination/borrow address must change if ASCII header arrangement changes; native UTF8 bytes alone do not make header size safe.

**Fields / layout:** ASCII header+1. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:215–218`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** This helper is shared by output creation and cached input comparisons; callers enumerated in activation evidence.

Lines 215–218 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L215-L218))

```
static MS_INLINE char *
ascii_get_buffer(PyObject *str) {
    return (char *)(((PyASCIIObject *)str) + 1);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1111: dataclass_iter_next

**Classification:** direct layout dependency; project_source; `hash_metadata_read`.

**Purpose:** Read dictionary field name cached hash for _PyDict_GetItem_KnownHash.

**Migration effect:** Cached-hash access can be ported separately from character storage.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:9504–9542`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Name came from a dict, code comments assert it is already hashed.

Lines 9504–9521 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L9504-L9521))

```
static MS_INLINE bool
dataclass_iter_next(
    DataclassIter *iter,
    PyObject **field_name,
    PyObject **field_val
) {
    PyObject *name, *key, *val;

next_field:
    if (!PyDict_Next(iter->fields, &(iter->fields_pos), &name, NULL)) {
        return false;
    }
    if (MS_UNLIKELY(!PyUnicode_CheckExact(name))) goto next_field;

    if (MS_LIKELY(iter->fastpath)) {
        if (
            PyDict_Next(iter->dict, &(iter->dict_pos), &key, &val) &&
            (key == name)
```

Excerpt shortened; the complete reviewed range 9504–9542 is in `data/cases.json`.

Closing lines 9537–9542 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L9537-L9542))

```
            val = _PyDict_GetItem_KnownHash(iter->dict, name, hash);
            if (val != NULL) {
                Py_INCREF(val);
                goto found_val;
            }
        }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1112: mpack_decode_key

**Classification:** direct layout dependency; project_source; `ascii_cache_length_read`.

**Purpose:** Compare short cached ASCII keys by direct length and payload bytes; JSON miss directly writes new ASCII key.

**Migration effect:** Cached key comparison/output header assumptions require changing, but cache retains Python objects and this is not repeated whole-nonASCII materialization.

**Fields / layout:** length, ASCII payload via ascii_get_buffer. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:16255–16312`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Both cached-key branches excluded in Py_GIL_DISABLED. Family groups JSON and MessagePack key-cache implementation rather than counting each length token.

Lines 16255–16272 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L16255-L16272))

```
mpack_decode_key(DecoderState *self, TypeNode *type, PathNode *path) {
    char op;

    if (MS_UNLIKELY(self->input_pos == self->input_end)) {
        ms_err_truncated();
        return NULL;
    }
    /* Peek at the next op */
    op = *self->input_pos;

    bool is_str = type->types == MS_TYPE_ANY || type->types == MS_TYPE_STR;

    if (MS_LIKELY(is_str && '\xa0' <= op && op <= '\xbf')) {
        /* A short (<= 31 byte) unicode str */
        self->input_pos++; /* consume op */
        Py_ssize_t size = op & 0x1f;

        /* Don't cache the empty string */
```

Excerpt shortened; the complete reviewed range 16255–16312 is in `data/cases.json`.

Closing lines 16307–16312 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L16307-L16312))

```
        }
        return new;
    }
    /* Fallback to standard decode */
    return mpack_decode(self, type, path, true);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1113: json_decode_dict_key

**Classification:** direct layout dependency; project_source; `ascii_cache_length_read`.

**Purpose:** Compare short cached ASCII keys by direct length and payload bytes; JSON miss directly writes new ASCII key.

**Migration effect:** Cached key comparison/output header assumptions require changing, but cache retains Python objects and this is not repeated whole-nonASCII materialization.

**Fields / layout:** length, ASCII payload via ascii_get_buffer. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:18021–18061`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Both cached-key branches excluded in Py_GIL_DISABLED. Family groups JSON and MessagePack key-cache implementation rather than counting each length token.

Lines 18021–18038 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18021-L18038))

```
json_decode_dict_key(JSONDecoderState *self, TypeNode *type, PathNode *path) {
    bool is_ascii = true;
    char *view = NULL;
    Py_ssize_t size;

    size = json_decode_string_view(self, &view, &is_ascii);
    if (size < 0) return NULL;
#ifndef Py_GIL_DISABLED
    bool is_str = type->types == MS_TYPE_ANY || type->types == MS_TYPE_STR;
    bool cacheable = is_str && is_ascii && size > 0 && size <= STRING_CACHE_MAX_STRING_LENGTH;
    if (MS_UNLIKELY(!cacheable)) {
        return json_decode_dict_key_fallback(self, view, size, is_ascii, type, path);
    }

    uint32_t hash = murmur2(view, size);
    uint32_t index = hash % STRING_CACHE_SIZE;
    PyObject *existing = string_cache[index];

```

Excerpt shortened; the complete reviewed range 18021–18061 is in `data/cases.json`.

Closing lines 18056–18061 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18056-L18061))

```
    string_cache[index] = new;
    return new;
#else
    return json_decode_dict_key_fallback(self, view, size, is_ascii, type, path);
#endif
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1114: ms_decode_decimal

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:12018–12035`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 12018–12035 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L12018-L12035))

```
ms_decode_decimal(
    const char *view, Py_ssize_t size, bool is_ascii, PathNode *path, MsgspecState *mod
) {
    PyObject *str;

    if (MS_LIKELY(is_ascii)) {
        str = PyUnicode_New(size, 127);
        if (str == NULL) return NULL;
        memcpy(ascii_get_buffer(str), view, size);
    }
    else {
        str = PyUnicode_DecodeUTF8(view, size, NULL);
        if (str == NULL) return NULL;
    }
    PyObject *out = ms_decode_decimal_from_pystr(str, path, mod);
    Py_DECREF(str);
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1115: json_float_hook

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:12396–12409`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 12396–12409 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L12396-L12409))

```
json_float_hook(
    const char *buf, Py_ssize_t size, PathNode *path, PyObject *float_hook
) {
    PyObject *str = PyUnicode_New(size, 127);
    if (str == NULL) return NULL;
    memcpy(ascii_get_buffer(str), buf, size);
    PyObject *out = PyObject_CallOneArg(float_hook, str);
    Py_DECREF(str);
    if (out == NULL) {
        ms_maybe_wrap_validation_error(path);
        return NULL;
    }
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1116: json_decode_string

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:17908–17960`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 17908–17925 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17908-L17925))

```
json_decode_string(JSONDecoderState *self, TypeNode *type, PathNode *path) {
    char *view = NULL;
    bool is_ascii = true;
    Py_ssize_t size = json_decode_string_view(self, &view, &is_ascii);
    if (size < 0) return NULL;

    if (MS_LIKELY(type->types & (MS_TYPE_STR | MS_TYPE_ANY))) {
        PyObject *out;
        if (MS_LIKELY(is_ascii)) {
            out = PyUnicode_New(size, 127);
            memcpy(ascii_get_buffer(out), view, size);
        }
        else {
            out = PyUnicode_DecodeUTF8(view, size, NULL);
        }
        return ms_check_str_constraints(out, type, path);
    }
    else if (MS_UNLIKELY(!self->strict)) {
```

Excerpt shortened; the complete reviewed range 17908–17960 is in `data/cases.json`.

Closing lines 17955–17960 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17955-L17960))

```
    }
    else if (MS_UNLIKELY(type->types & (MS_TYPE_ENUM | MS_TYPE_STRLITERAL))) {
        return ms_decode_str_enum_or_literal(view, size, type, path);
    }
    return ms_validation_error("str", type, path);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1117: json_decode_dict_key_fallback

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:17963–18018`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 17963–17980 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L17963-L17980))

```
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
        return ms_check_str_constraints(out, type, path);
```

Excerpt shortened; the complete reviewed range 17963–18018 is in `data/cases.json`.

Closing lines 18013–18018 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L18013-L18018))

```
        return json_decode_binary(view, size, type, path);
    }
    else {
        return ms_validation_error("str", type, path);
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1118: to_builtins_binary

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:20174–20181`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 20174–20181 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L20174-L20181))

```
to_builtins_binary(ToBuiltinsState *self, const char *buf, Py_ssize_t size) {
    Py_ssize_t output_size = ms_encode_base64_size(self->mod, size);
    if (output_size < 0) return NULL;
    PyObject *out = PyUnicode_New(output_size, 127);
    if (out == NULL) return NULL;
    ms_encode_base64(buf, size, ascii_get_buffer(out));
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1119: to_builtins_datetime

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:20184–20191`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 20184–20191 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L20184-L20191))

```
to_builtins_datetime(ToBuiltinsState *self, PyObject *obj) {
    char buf[32];
    int size = ms_encode_datetime(self->mod, obj, buf);
    if (size < 0) return NULL;
    PyObject *out = PyUnicode_New(size, 127);
    memcpy(ascii_get_buffer(out), buf, size);
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1120: to_builtins_date

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:20194–20199`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 20194–20199 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L20194-L20199))

```
to_builtins_date(ToBuiltinsState *self, PyObject *obj) {
    PyObject *out = PyUnicode_New(10, 127);
    if (out == NULL) return NULL;
    ms_encode_date(obj, ascii_get_buffer(out));
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1121: to_builtins_time

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:20202–20209`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 20202–20209 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L20202-L20209))

```
to_builtins_time(ToBuiltinsState *self, PyObject *obj) {
    char buf[21];
    int size = ms_encode_time(self->mod, obj, buf);
    if (size < 0) return NULL;
    PyObject *out = PyUnicode_New(size, 127);
    memcpy(ascii_get_buffer(out), buf, size);
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1122: to_builtins_timedelta

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:20212–20218`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 20212–20218 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L20212-L20218))

```
to_builtins_timedelta(ToBuiltinsState *self, PyObject *obj) {
    char buf[26];
    int size = ms_encode_timedelta(obj, buf);
    PyObject *out = PyUnicode_New(size, 127);
    memcpy(ascii_get_buffer(out), buf, size);
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.

## L1123: to_builtins_uuid

**Classification:** direct layout dependency; project_source; `output_mutation_via_layout_helper`.

**Purpose:** Write new Unicode outputs with memcpy/date/base64/UUID encoders into ascii_get_buffer.

**Migration effect:** A helper update reaches all these output-only consumers; they were outside prior input-read count.

**Fields / layout:** ASCII header+1, new ASCII payload. Types: PyASCIIObject.

**Source:** `msgspec-0.22.0/src/msgspec/_core.c:20221–20228`. SHA-256 `83b0fef8973a212310447e3891ec62a704a8e11d4be1fe942f5326f6e2c9179c`.

**Activation / context:** Direct layout occurs centrally in ascii_get_buffer; these are traced activations of that shared address helper, not extra named-token occurrences.

Lines 20221–20228 ([verified immutable source](https://github.com/msgspec/msgspec/blob/6d3443f2dae8413a1a56640290c09a6f486f30c2/src/msgspec/_core.c#L20221-L20228))

```
to_builtins_uuid(ToBuiltinsState *self, PyObject *obj) {
    PyObject *out = PyUnicode_New(36, 127);
    if (out == NULL) return NULL;
    if (ms_encode_uuid(self->mod, obj, ascii_get_buffer(out), true) < 0) {
        Py_CLEAR(out);
    }
    return out;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d0/e6/6dcf9306ff3c5e486578f3bf29ed11dfbdbbc2a8bf0caf7e07d392887fda/msgspec-0.22.0.tar.gz); archive SHA-256 `0a13624a4969159fe35d8c2a3d377b2b61bbd8585e327440d5e52725affcce38`.
