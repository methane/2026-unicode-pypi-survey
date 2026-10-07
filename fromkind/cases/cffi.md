# cffi 2.1.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0134: _my_PyUnicode_FromChar32

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `w` — external C data or local C scalar. cffi_char32_t is uint32_t; size counts 32-bit elements. No UTF-8 bytes or Python FSR pointer is passed at observed callers.

**Length:** `size`; 32-bit codepoint elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/wchar_helper_3.h:10–18) Modern header selection; alternative legacy implementation otherwise (cffi-2.1.1/src/c/_cffi_backend.c:382–386)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Only active when PyUnicode_KIND is defined; provider API invocation counted once, observed caller invocations listed separately.

**Source:** `cffi-2.1.1/src/c/wchar_helper_3.h:14–18`; SHA-256 `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`.

`cffi-2.1.1/src/c/wchar_helper_3.h` lines 10–18 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L10-L18))

```
typedef uint16_t cffi_char16_t;
typedef uint32_t cffi_char32_t;


static PyObject *
_my_PyUnicode_FromChar32(const cffi_char32_t *w, Py_ssize_t size)
{
    return PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, w, size);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0135: _my_PyUnicode_FromChar16

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `w` — external C data or local C scalar. cffi_char16_t is uint16_t. Pair scan excludes valid high/low surrogate pairs from this constructor branch. Each remaining unit, including lone surrogate, is one output codepoint. Pair-containing input uses a separate PyUnicode_New/write path.

**Length:** `size`; 16-bit elements; codepoints on this branch.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/wchar_helper_3.h:10–11) Exact retained source snippet included (cffi-2.1.1/src/c/wchar_helper_3.h:21–55) Modern header selection; alternative legacy implementation otherwise (cffi-2.1.1/src/c/_cffi_backend.c:382–386)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Fixed2 constructor branch taken only when count_surrogates == 0.

**Source:** `cffi-2.1.1/src/c/wchar_helper_3.h:21–55`; SHA-256 `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`.

`cffi-2.1.1/src/c/wchar_helper_3.h` lines 10–11 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L10-L11))

```
typedef uint16_t cffi_char16_t;
typedef uint32_t cffi_char32_t;
```

`cffi-2.1.1/src/c/wchar_helper_3.h` lines 21–36 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L21-L36))

```
_my_PyUnicode_FromChar16(const cffi_char16_t *w, Py_ssize_t size)
{
    /* are there any surrogate pairs, and if so, how many? */
    Py_ssize_t i, count_surrogates = 0;
    for (i = 0; i < size - 1; i++) {
        if (0xD800 <= w[i] && w[i] <= 0xDBFF &&
                0xDC00 <= w[i+1] && w[i+1] <= 0xDFFF)
            count_surrogates++;
    }
    if (count_surrogates == 0) {
        /* no, fast path */
        return PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, w, size);
    }
    else
    {
        PyObject *result = PyUnicode_New(size - count_surrogates, 0x10FFFF);
```

Closing lines 50–55 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L50-L55))

```
            }
            *data++ = ch;
        }
        return result;
    }
}
```

Original reviewed range 21–55 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0136: convert_to_object

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `(cffi_char16_t *)data` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 16-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:1162–1171)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:1168–1168`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 1162–1171 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1162-L1171))

```
    else if (ct->ct_flags & CT_PRIMITIVE_CHAR) {
        /*READ(data, ct->ct_size)*/
        switch (ct->ct_size) {
        case sizeof(char):
            return PyBytes_FromStringAndSize(data, 1);
        case 2:
            return _my_PyUnicode_FromChar16((cffi_char16_t *)data, 1);
        case 4:
            return _my_PyUnicode_FromChar32((cffi_char32_t *)data, 1);
        }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0137: convert_to_object

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `(cffi_char32_t *)data` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 32-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:1162–1171)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:1170–1170`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 1162–1171 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1162-L1171))

```
    else if (ct->ct_flags & CT_PRIMITIVE_CHAR) {
        /*READ(data, ct->ct_size)*/
        switch (ct->ct_size) {
        case sizeof(char):
            return PyBytes_FromStringAndSize(data, 1);
        case 2:
            return _my_PyUnicode_FromChar16((cffi_char16_t *)data, 1);
        case 4:
            return _my_PyUnicode_FromChar32((cffi_char32_t *)data, 1);
        }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0138: b_string

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `start` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `length`; 16-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:6804–6823)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:6822–6822`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 6804–6819 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6804-L6819))

```
        else if (cd->c_type->ct_itemdescr->ct_flags & CT_PRIMITIVE_CHAR) {
            switch (cd->c_type->ct_itemdescr->ct_size) {
            case 2: {
                const cffi_char16_t *start = (cffi_char16_t *)cd->c_data;
                if (length < 0) {
                    /*READ(start, 2)*/
                    length = 0;
                    while (start[length])
                        length++;
                    /*READ(start, 2 * length)*/
                }
                else {
                    /*READ(start, 2 * length)*/
                    maxlen = length;
                    length = 0;
                    while (length < maxlen && start[length])
```

Closing lines 6820–6823 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6820-L6823))

```
                        length++;
                }
                return _my_PyUnicode_FromChar16(start, length);
            }
```

Original reviewed range 6804–6823 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0139: b_string

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `start` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `length`; 32-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:6824–6841)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:6840–6840`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 6824–6839 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6824-L6839))

```
            case 4: {
                const cffi_char32_t *start = (cffi_char32_t *)cd->c_data;
                if (length < 0) {
                    /*READ(start, 4)*/
                    length = 0;
                    while (start[length])
                        length++;
                    /*READ(start, 4 * length)*/
                }
                else {
                    /*READ(start, 4 * length)*/
                    maxlen = length;
                    length = 0;
                    while (length < maxlen && start[length])
                        length++;
                }
```

Closing lines 6840–6841 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6840-L6841))

```
                return _my_PyUnicode_FromChar32(start, length);
            }
```

Original reviewed range 6824–6841 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0140: b_string

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `(cffi_char16_t *)cd->c_data` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 16-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:6851–6863)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:6860–6860`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 6851–6863 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6851-L6863))

```
    else if (cd->c_type->ct_flags & (CT_PRIMITIVE_CHAR |
                                     CT_PRIMITIVE_SIGNED |
                                     CT_PRIMITIVE_UNSIGNED)) {
        /*READ(cd->c_data, cd->c_type->ct_size)*/
        if (cd->c_type->ct_size == sizeof(char))
            return PyBytes_FromStringAndSize(cd->c_data, 1);
        else if (cd->c_type->ct_flags & CT_PRIMITIVE_CHAR) {
            switch (cd->c_type->ct_size) {
            case 2:
                return _my_PyUnicode_FromChar16((cffi_char16_t *)cd->c_data, 1);
            case 4:
                return _my_PyUnicode_FromChar32((cffi_char32_t *)cd->c_data, 1);
            }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0141: b_string

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `(cffi_char32_t *)cd->c_data` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 32-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:6851–6863)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:6862–6862`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 6851–6863 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6851-L6863))

```
    else if (cd->c_type->ct_flags & (CT_PRIMITIVE_CHAR |
                                     CT_PRIMITIVE_SIGNED |
                                     CT_PRIMITIVE_UNSIGNED)) {
        /*READ(cd->c_data, cd->c_type->ct_size)*/
        if (cd->c_type->ct_size == sizeof(char))
            return PyBytes_FromStringAndSize(cd->c_data, 1);
        else if (cd->c_type->ct_flags & CT_PRIMITIVE_CHAR) {
            switch (cd->c_type->ct_size) {
            case 2:
                return _my_PyUnicode_FromChar16((cffi_char16_t *)cd->c_data, 1);
            case 4:
                return _my_PyUnicode_FromChar32((cffi_char32_t *)cd->c_data, 1);
            }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0142: b_unpack

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `(cffi_char16_t *)cd->c_data` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `length`; 16-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:6881–6916)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:6913–6913`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 6881–6896 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6881-L6896))

```
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O!n:unpack", keywords,
                                     &CData_Type, &cd, &length))
        return NULL;

    if (!(cd->c_type->ct_flags & (CT_ARRAY|CT_POINTER))) {
        PyErr_Format(PyExc_TypeError,
                     "expected a pointer or array, got '%s'",
                     cd->c_type->ct_name);
        return NULL;
    }
    if (length < 0) {
        PyErr_SetString(PyExc_ValueError, "'length' cannot be negative");
        return NULL;
    }
    if (cd->c_data == NULL) {
        PyObject *s = cdata_repr(cd);
```

Closing lines 6911–6916 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6911-L6916))

```
            return PyBytes_FromStringAndSize(cd->c_data, length);
        case 2:
            return _my_PyUnicode_FromChar16((cffi_char16_t *)cd->c_data,length);
        case 4:
            return _my_PyUnicode_FromChar32((cffi_char32_t *)cd->c_data,length);
        }
```

Original reviewed range 6881–6916 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0143: b_unpack

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `(cffi_char32_t *)cd->c_data` — external C data. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `length`; 32-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:6881–6916)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:6915–6915`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 6881–6896 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6881-L6896))

```
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O!n:unpack", keywords,
                                     &CData_Type, &cd, &length))
        return NULL;

    if (!(cd->c_type->ct_flags & (CT_ARRAY|CT_POINTER))) {
        PyErr_Format(PyExc_TypeError,
                     "expected a pointer or array, got '%s'",
                     cd->c_type->ct_name);
        return NULL;
    }
    if (length < 0) {
        PyErr_SetString(PyExc_ValueError, "'length' cannot be negative");
        return NULL;
    }
    if (cd->c_data == NULL) {
        PyObject *s = cdata_repr(cd);
```

Closing lines 6911–6916 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L6911-L6916))

```
            return PyBytes_FromStringAndSize(cd->c_data, length);
        case 2:
            return _my_PyUnicode_FromChar16((cffi_char16_t *)cd->c_data,length);
        case 4:
            return _my_PyUnicode_FromChar32((cffi_char32_t *)cd->c_data,length);
        }
```

Original reviewed range 6881–6916 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0144: _cffi_from_c_wchar_t

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `&input` — constructed local scalar. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 16-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:7806–7815)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:7809–7809`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 7806–7815 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L7806-L7815))

```
static PyObject *_cffi_from_c_wchar_t(cffi_wchar_t x) {
    if (sizeof(cffi_wchar_t) == 2) {
        cffi_char16_t input = x;
        return _my_PyUnicode_FromChar16(&input, 1);
    }
    else {
        cffi_char32_t input = x;
        return _my_PyUnicode_FromChar32(&input, 1);
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0145: _cffi_from_c_wchar_t

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `&input` — constructed local scalar. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 32-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:7806–7815)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:7813–7813`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 7806–7815 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L7806-L7815))

```
static PyObject *_cffi_from_c_wchar_t(cffi_wchar_t x) {
    if (sizeof(cffi_wchar_t) == 2) {
        cffi_char16_t input = x;
        return _my_PyUnicode_FromChar16(&input, 1);
    }
    else {
        cffi_char32_t input = x;
        return _my_PyUnicode_FromChar32(&input, 1);
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0146: _cffi_from_c_wchar3216_t

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `&input` — constructed local scalar. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 16-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:7823–7832)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:7826–7826`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 7823–7832 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L7823-L7832))

```
static PyObject *_cffi_from_c_wchar3216_t(int x) {
    if (sizeof(cffi_wchar_t) == 4) {
        cffi_char16_t input = x;
        return _my_PyUnicode_FromChar16(&input, 1);
    }
    else {
        cffi_char32_t input = x;
        return _my_PyUnicode_FromChar32(&input, 1);
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

## K0147: _cffi_from_c_wchar3216_t

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `&input` — constructed local scalar. Wrapper passes CData storage or a local scalar. b_string computes bounded/NUL-terminated element count; b_unpack uses exact requested element count including embedded NUL.

**Length:** `1`; 32-bit elements.

**Confirmed:** Exact retained source snippet included (cffi-2.1.1/src/c/_cffi_backend.c:7823–7832)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static wrapper invocation; not an additional direct API invocation. Width follows branch sizeof/ct_size; FromChar16 may use alternate pair-decoding output implementation.

**Source:** `cffi-2.1.1/src/c/_cffi_backend.c:7830–7830`; SHA-256 `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

`cffi-2.1.1/src/c/_cffi_backend.c` lines 7823–7832 ([verified immutable source](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L7823-L7832))

```
static PyObject *_cffi_from_c_wchar3216_t(int x) {
    if (sizeof(cffi_wchar_t) == 4) {
        cffi_char16_t input = x;
        return _my_PyUnicode_FromChar16(&input, 1);
    }
    else {
        cffi_char32_t input = x;
        return _my_PyUnicode_FromChar32(&input, 1);
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz); archive SHA-256 `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.
