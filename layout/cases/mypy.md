# mypy 2.4.0

2 confirmed layout regions; 2 reviewed regions including non-direct context.

## L0034: PyUnstable_Unicode_GET_CACHED_HASH

**Classification:** direct layout dependency; compatibility_header; `compatibility_api_implementation_cached_hash`.

**Purpose:** Vendored compatibility implementation of PyUnstable_Unicode_GET_CACHED_HASH returns private cached hash without computing it.

**Migration effect:** Compatibility/API implementation rather than a package algorithm. Modern API call can replace this implementation as target headers gain it; private cached-hash metadata does not require FSR.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `mypy-2.4.0/mypyc/lib-rt/pythoncapi_compat.h:2664–2674`. SHA-256 `9f585b89c11f16332deee57297a9069eb1cdaec51ea7a2a7c33ddb659a2869c5`.

**Activation / context:** PY_VERSION_HEX<0x030F00A1; PyPy returns -1; Python>=3 uses PyASCIIObject.hash; Python2 branch uses PyUnicodeObject.hash.

Lines 2662–2679 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if PY_VERSION_HEX < 0x030F00A1
static inline Py_hash_t
PyUnstable_Unicode_GET_CACHED_HASH(PyObject *op)
{
#ifdef PYPY_VERSION
    (void)op;  // unused argument
    return -1;
#elif PY_VERSION_HEX >= 0x03000000
    return ((PyASCIIObject*)op)->hash;
#else
    return ((PyUnicodeObject*)op)->hash;
#endif
}
#endif

#if 0x030D0000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x030F00A7 && !defined(PYPY_VERSION)
// Immortal objects were implemented in Python 3.12, however there is no easy API
// to make objects immortal until 3.14 which has _Py_SetImmortal(). Since
```

Excerpt shortened; the complete reviewed range 2662–2680 is in `data/cases.json`.

Closing lines 2680–2680 (immutable GitHub mapping unavailable in saved verification evidence)

```
// immortal objects are primarily needed for free-threading, this API is implemented
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## L0924: _PyUnicode_LENGTH macro and CPyTagged_ShortToStr

**Classification:** direct layout dependency; project_source; `direct_unicode_length_mutation`.

**Purpose:** Allocate ASCII Unicode with MAX_INT_CHARS, write actual digits/NUL into DATA, directly shrink header length using macro lvalue before returning.

**Migration effect:** Direct length field mutation bypasses Unicode API: relies on header location and assumes updating this one length is sufficient for fresh compact ASCII output. UTF8 migration with distinct byte/codepoint length/state needs consistent construction/finalization API or preserved layout invariants. This is output construction, so prior character-read inventory can exclude it while it remains an actual structural dependency.

**Fields / layout:** PyASCIIObject.length. Types: PyASCIIObject.

**Source:** `mypy-2.4.0/mypyc/lib-rt/misc_ops.c:535–585`. SHA-256 `52495418b4abae8fd9ab235446acaf01afeba6644900911dec2fdac0015f4db9`.

**Activation / context:** Unconditional runtime macro; CPyTagged_Str routes tagged small ints to helper. MyPy/LibRT exact same source_sha256, count one shared family.

Lines 535–537 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/misc_ops.c#L535-L537))

```
#define MAX_INT_CHARS 22
#define _PyUnicode_LENGTH(op)                           \
    (((PyASCIIObject *)(op))->length)
```

Lines 570–585 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/misc_ops.c#L570-L585))

```
static PyObject *CPyTagged_ShortToStr(Py_ssize_t n) {
    PyObject *obj = PyUnicode_New(MAX_INT_CHARS, 127);
    if (!obj) return NULL;
    int len = fmt_ssize_t((char *)PyUnicode_1BYTE_DATA(obj), n);
    _PyUnicode_LENGTH(obj) = len;
    return obj;
}

PyObject *CPyTagged_Str(CPyTagged n) {
    if (CPyTagged_CheckShort(n)) {
        return CPyTagged_ShortToStr(CPyTagged_ShortAsSsize_t(n));
    } else {
        return PyObject_Str(CPyTagged_AsObject(n));
    }
}

```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.
