# numba 0.68.0

1 confirmed layout regions; 1 reviewed regions including non-direct context.

## L0926: numba_extract_unicode layout guards and cached hash

**Classification:** direct layout dependency; project_source; `layout_guard_and_cached_hash_read`.

**Purpose:** sizeof/offsetof guards prove nesting/common hash offset, then cached hash is read directly without computing.

**Migration effect:** UTF8 representation itself does not invalidate cached-hash semantics, but named members/types/nesting offsets are compiled ABI/source dependencies. Different headers can fail compilation; mismatching checked layouts return NULL rather than compute hash. Preserved common prefix/hash layout can keep this part working. DATA/KIND uses are separate API dependencies.

**Fields / layout:** PyCompactUnicodeObject._base, PyUnicodeObject._base, _base.hash, _base._base.hash, PyASCIIObject.hash. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `numba-0.68.0/numba/_helperlib.c:1140–1170`. SHA-256 `b30132af3313c175b639ab2b205b681848634afd5540e578f99af83a9d5c8076`.

**Activation / context:** On successful READY branch; guard intended compile-time constant. Requires concrete CPython type definitions. Noncomputing hash read is intentional.

Lines 1140–1157 ([verified immutable source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/_helperlib.c#L1140-L1157))

```
#define MEMBER_SIZE(structure, member) sizeof(((structure *)0)->member)

NUMBA_EXPORT_FUNC(void *)
numba_extract_unicode(PyObject *obj, Py_ssize_t *length, int *kind,
                      unsigned int *ascii, Py_ssize_t *hash) {
    if (!PyUnicode_READY(obj)) {
        *length = PyUnicode_GET_LENGTH(obj);
        *kind = PyUnicode_KIND(obj);
        /* could also use PyUnicode_IS_ASCII but it is not publicly advertised in https://docs.python.org/3/c-api/unicode.html */
        *ascii = (unsigned int)(PyUnicode_MAX_CHAR_VALUE(obj) == (0x7f));
        /* this is here as a crude check for safe casting of all unicode string
         * structs to a PyASCIIObject */
        if (MEMBER_SIZE(PyCompactUnicodeObject, _base) == sizeof(PyASCIIObject)             &&
            MEMBER_SIZE(PyUnicodeObject, _base) == sizeof(PyCompactUnicodeObject)           &&
            offsetof(PyCompactUnicodeObject, _base) == 0                                    &&
            offsetof(PyUnicodeObject, _base) == 0                                           &&
            offsetof(PyCompactUnicodeObject, _base.hash) == offsetof(PyASCIIObject, hash)   &&
            offsetof(PyUnicodeObject, _base._base.hash) == offsetof(PyASCIIObject, hash)
```

Excerpt shortened; the complete reviewed range 1140–1166 is in `data/cases.json`.

Closing lines 1161–1166 ([verified immutable source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/_helperlib.c#L1161-L1166))

```
        }
        else {
            /* cast is not safe, fail */
            return NULL;
        }
        return PyUnicode_DATA(obj);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA-256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
