# regex 2026.9.29

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0148: build_unicode_value

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** dynamic_1_2_4; expression `kind (switch on buffer_charsize: 1/2/4 -> corresponding PyUnicode_*BYTE_KIND; default1)`.

**Input:** `buffer` — constructed codepoint array. Width switch maps charsize 1/2/4 to the matching kind (fallback1). Observed callers use allocated folding output or local Py_UCS4; length end-start in selected-width elements.

**Length:** `len (= end - start)`; selected-width codepoint elements.

**Confirmed:** Exact retained source snippet included (regex-2026.9.29/src/_regex.c:9577–9602) get_string obtains original Unicode DATA/KIND/length (regex-2026.9.29/src/_regex.c:18223–18247) fold_case source acquisition and typed character-reader selection (regex-2026.9.29/src/_regex.c:26231–26248) Observed wrapper caller (regex-2026.9.29/src/_regex.c:26347–26347) Observed wrapper caller (regex-2026.9.29/src/_regex.c:26382–26382)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** fold_case acquires original input through get_string, dispatches character width/read helper, then writes a separate allocated folded array. Constructor does not directly receive original FSR.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Two static observed wrapper callers: fold_case and get_expand_on_folding.

**Source:** `regex-2026.9.29/src/_regex.c:9577–9602`; SHA-256 `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

`regex-2026.9.29/src/_regex.c` lines 9577–9592 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L9577-L9592))

```
/* Builds a Unicode string. */
Py_LOCAL_INLINE(PyObject*) build_unicode_value(void* buffer, Py_ssize_t start,
  Py_ssize_t end, Py_ssize_t buffer_charsize) {
    Py_ssize_t len;
    int kind;

    buffer = (void*)((uint8_t*)buffer + start * buffer_charsize);
    len = end - start;

    switch (buffer_charsize) {
    case 1:
        kind = PyUnicode_1BYTE_KIND;
        break;
    case 2:
        kind = PyUnicode_2BYTE_KIND;
        break;
```

Closing lines 9597–9602 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L9597-L9602))

```
        kind = PyUnicode_1BYTE_KIND;
        break;
    }

    return PyUnicode_FromKindAndData(kind, buffer, len);
}
```

Original reviewed range 9577–9602 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz); archive SHA-256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

## K0149: fold_case

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** dynamic_1_2_4; expression `forwarded/dynamic; see snippets`.

**Input:** `folded` — constructed codepoint array. folded allocated in element-width bytes and filled by case-fold codepoint setters; expansion caller instead passes table-derived local Py_UCS4 scalar.

**Length:** `folded_len`; codepoint elements.

**Confirmed:** Exact retained source snippet included (regex-2026.9.29/src/_regex.c:26265–26300) Exact retained source snippet included (regex-2026.9.29/src/_regex.c:26316–26354)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** fold_case acquires original input through get_string, dispatches character width/read helper, then writes a separate allocated folded array. Constructor does not directly receive original FSR.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static build_unicode_value wrapper activation; not additional direct constructor API site.

**Source:** `regex-2026.9.29/src/_regex.c:26347–26347`; SHA-256 `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

`regex-2026.9.29/src/_regex.c` lines 26265–26280 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26265-L26280))

```
    folded_charsize = str_info.charsize;

    /* When folding a Unicode string, some codepoints in the range U+00..U+FF
     * are mapped to codepoints in the range U+0100..U+FFFF.
     */
    if (encoding == &unicode_encoding && str_info.charsize == 1)
        folded_charsize = 2;

    /* Get the function for writing to the folded string. */
    switch (folded_charsize) {
    case 1:
        set_char_at = bytes1_set_char_at;
        break;
    case 2:
        set_char_at = bytes2_set_char_at;
        break;
```

Closing lines 26295–26300 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26295-L26300))

```
    else
        buf_size = str_info.length;

    folded = re_alloc((size_t)(buf_size * folded_charsize));
    if (!folded) {
        release_buffer(&str_info);
```

Original reviewed range 26265–26300 is recorded in `data/sites.json`; public excerpts are bounded.

`regex-2026.9.29/src/_regex.c` lines 26316–26331 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26316-L26331))

```
        for (i = 0; i < str_info.length; i++) {
            int count;
            int j;

            count = full_case_fold(&locale_info, char_at(str_info.characters,
              i), codepoints);
            for (j = 0; j < count; j++)
                set_char_at(folded, folded_len + j, codepoints[j]);

            folded_len += count;
        }
    } else {
        /* Simple case-folding. */
        Py_UCS4 (*simple_case_fold)(RE_LocaleInfo* locale_info, Py_UCS4 ch);
        Py_ssize_t i;

```

Closing lines 26349–26354 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26349-L26354))

```
        result = build_bytes_value(folded, 0, folded_len, folded_charsize);

    re_dealloc(folded);

    /* Release the original string's buffer. */
    release_buffer(&str_info);
```

Original reviewed range 26316–26354 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz); archive SHA-256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

## K0150: get_expand_on_folding

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `&codepoint` — constructed local scalar. folded allocated in element-width bytes and filled by case-fold codepoint setters; expansion caller instead passes table-derived local Py_UCS4 scalar.

**Length:** `1`; codepoint elements.

**Confirmed:** Exact retained source snippet included (regex-2026.9.29/src/_regex.c:26361–26400)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Static build_unicode_value wrapper activation; not additional direct constructor API site.

**Source:** `regex-2026.9.29/src/_regex.c:26382–26382`; SHA-256 `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

`regex-2026.9.29/src/_regex.c` lines 26361–26376 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26361-L26376))

```
static PyObject* get_expand_on_folding(PyObject* self, PyObject* unused) {
    int count;
    PyObject* list;
    int i;
    PyObject* result;

    /* How many characters are there? */
    count = sizeof(re_expand_on_folding) / sizeof(re_expand_on_folding[0]);

    /* Put all the characters in a tuple. */
    list = PyList_New(0);
    if (!list)
        return NULL;

    for (i = 0; i < count; i++) {
        Py_UCS4 codepoint;
```

Closing lines 26395–26400 ([verified immutable source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26395-L26400))

```
    return result;

error:
    Py_DECREF(list);
    return NULL;
}
```

Original reviewed range 26361–26400 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz); archive SHA-256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.
