# bitarray 3.11.0

1 confirmed layout regions; 1 reviewed regions including non-direct context.

## L0036: PyUnstable_Unicode_GET_CACHED_HASH

**Classification:** direct layout dependency; compatibility_header; `compatibility_api_implementation_cached_hash`.

**Purpose:** Vendored compatibility implementation of PyUnstable_Unicode_GET_CACHED_HASH returns private cached hash without computing it.

**Migration effect:** Compatibility/API implementation rather than a package algorithm. Modern API call can replace this implementation as target headers gain it; private cached-hash metadata does not require FSR.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `bitarray-3.11.0/bitarray/pythoncapi_compat.h:2663–2673`. SHA-256 `7e7872c3b4566b3a95a5dbb3576b05060dfc9af6e8c5b6eb042d751c0df1fbb6`.

**Activation / context:** PY_VERSION_HEX<0x030F00A1; PyPy returns -1; Python>=3 uses PyASCIIObject.hash; Python2 branch uses PyUnicodeObject.hash.

Lines 2661–2678 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 2661–2679 is in `data/cases.json`.

Closing lines 2679–2679 (immutable GitHub mapping unavailable in saved verification evidence)

```
// immortal objects are primarily needed for free-threading, this API is implemented
```

[Frozen source distribution](https://files.pythonhosted.org/packages/04/f7/6765577df59e2345036e435f7e983e1c291d67b7d76a51918eff04ad1494/bitarray-3.11.0.tar.gz); archive SHA-256 `bf19437ec00ec3d40aef82eaeedc14cf4000be9b635c4f5049796506e6630dd8`.
