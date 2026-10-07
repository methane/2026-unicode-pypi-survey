# regex: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#regex)

Each independent Pattern match/search creates local RE_State, borrows subject DATA and ends state after producing result. Small caller-selected match windows can be cheap on a long non-ASCII subject. Scanner retains RE_State until scanner destruction, so it can retain one lease across calls. A compiled Pattern alone caches pattern state, not every future subject view.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## _regex.c: 18234–18244

Subject capture, local-state finalization and persistent scanner lifetime

Archive member: `regex-2026.9.29/src/_regex.c`

Member SHA256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`

[Frozen sdist](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz); archive SHA256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

[Verified permanent source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18234-L18244).

```
    if (PyUnicode_Check(string)) {
        /* Unicode strings don't always support the buffer interface. */
        if (PyUnicode_READY(string) == -1)
            return false;

        str_info->characters = (void*)PyUnicode_DATA(string);
        str_info->length = PyUnicode_GetLength(string);
        str_info->charsize = PyUnicode_KIND(string);
        str_info->is_unicode = true;
        str_info->should_release = false;
        return true;
```

## _regex.c: 21023–21031

Subject capture, local-state finalization and persistent scanner lifetime

Archive member: `regex-2026.9.29/src/_regex.c`

Member SHA256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`

[Frozen sdist](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz); archive SHA256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

[Verified permanent source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L21023-L21031).

```
static void scanner_dealloc(PyObject* self_) {
    ScannerObject* self;

    self = (ScannerObject*)self_;

    if (self->status != RE_ERROR_INITIALISING)
        state_fini(&self->state);
    Py_DECREF(self->pattern);
    PyObject_DEL(self);
```

## _regex.c: 21622–21636

Subject capture, local-state finalization and persistent scanner lifetime

Archive member: `regex-2026.9.29/src/_regex.c`

Member SHA256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`

[Frozen sdist](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz); archive SHA256 `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

[Verified permanent source](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L21622-L21636).

```
    if (!state_init(&state, self, string, start, end, false, conc, part, false,
      true, match_all, tim))
        return NULL;

    status = do_match(&state, search);

    if (status >= 0 || status == RE_ERROR_PARTIAL)
        /* Create the match object. */
        match = pattern_new_match(self, &state, status);
    else
        match = NULL;

    state_fini(&state);

    return match;
```
