# numba: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#numba)

Unbox emits numba_extract_unicode on original Python str and creates new NRT MemInfo retaining owner/data. Separate boundary crossings create separate native ownership scopes; cheap native getitem can follow. Repeated native operations on one live unboxed value share that same view and must not be counted as separate rematerializations.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## unicode.py: 177–197

Actual UnicodeType unbox captures data and attaches retained PyObject to native MemInfo.

Archive member: `numba-0.68.0/numba/cpython/unicode.py`

Member SHA256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`

[Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

[Verified permanent source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L177-L197).

```
@unbox(types.UnicodeType)
def unbox_unicode_str(typ, obj, c):
    """
    Convert a unicode str object to a native unicode structure.
    """
    ok, data, length, kind, is_ascii, hashv = \
        c.pyapi.string_as_string_size_and_kind(obj)
    uni_str = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    uni_str.data = data
    uni_str.length = length
    uni_str.kind = kind
    uni_str.is_ascii = is_ascii
    uni_str.hash = hashv
    uni_str.meminfo = c.pyapi.nrt_meminfo_new_from_pyobject(
        data,  # the borrowed data pointer
        obj,   # the owner pyobject; the call will incref it.
    )
    uni_str.parent = obj

    is_error = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(uni_str._getvalue(), is_error=is_error)
```

## _helperlib.c: 1143–1160

Native extraction getter returns DATA plus length/kind/hash.

Archive member: `numba-0.68.0/numba/_helperlib.c`

Member SHA256: `b30132af3313c175b639ab2b205b681848634afd5540e578f99af83a9d5c8076`

[Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

[Verified permanent source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/_helperlib.c#L1143-L1160).

```
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
           ) {
            /* Grab the hash from the type object cache, do not compute it. */
            *hash = ((PyASCIIObject *)(obj))->hash;
```

## unicode.py: 1821–1831

Native getitem_char reads one normalized caller index.

Archive member: `numba-0.68.0/numba/cpython/unicode.py`

Member SHA256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`

[Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

[Verified permanent source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1821-L1831).

```
            def getitem_char(s, idx):
                idx = normalize_str_idx(idx, len(s))
                cp = _get_code_point(s, idx)
                kind = _codepoint_to_kind(cp)
                if kind == s._kind:
                    return _get_str_slice_view(s, idx, 1)
                else:
                    is_ascii = _codepoint_is_ascii(cp)
                    ret = _empty_string(kind, 1, is_ascii)
                    _set_code_point(ret, 0, cp)
                    return ret
```

## _helperlib.c: 1160–1170

Native extraction getter returns DATA plus length/kind/hash.

Archive member: `numba-0.68.0/numba/_helperlib.c`

Member SHA256: `b30132af3313c175b639ab2b205b681848634afd5540e578f99af83a9d5c8076`

[Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

[Verified permanent source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/_helperlib.c#L1160-L1170).

```
            *hash = ((PyASCIIObject *)(obj))->hash;
        }
        else {
            /* cast is not safe, fail */
            return NULL;
        }
        return PyUnicode_DATA(obj);
    } else {
        return NULL;
    }
}
```

## _nrt_python.c: 18–36

MemInfo acquires owner; destructor releases owner at native lifetime end.

Archive member: `numba-0.68.0/numba/core/runtime/_nrt_python.c`

Member SHA256: `53334b5db0e22f1b00fc0b73426176561b746bb8c3a0779a210c440225835a8e`

[Frozen sdist](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
 * Create a NRT MemInfo for data owned by a PyObject.
 */

static void
pyobject_dtor(void *ptr, size_t size, void* info) {
    PyGILState_STATE gstate;
    PyObject *ownerobj = info;

    gstate = PyGILState_Ensure();   /* ensure the GIL */
    Py_DECREF(ownerobj);            /* release the python object */
    PyGILState_Release(gstate);     /* release the GIL */
}

NUMBA_EXPORT_FUNC(NRT_MemInfo *)
NRT_meminfo_new_from_pyobject(void *data, PyObject *ownerobj) {
    size_t dummy_size = 0;
    Py_INCREF(ownerobj);
    return NRT_MemInfo_new(data, dummy_size, pyobject_dtor, ownerobj);
}
```
