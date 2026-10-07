# editdistance 0.8.1

3 confirmed layout regions; 4 reviewed regions including non-direct context.

## L0182: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `editdistance-0.8.1/src/editdistance/bycython.cpp:925–925`. SHA-256 `03ed3fed26b3d613515da088e80ac2ab8e4aba1533c752745b88fdba314b88da`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 917–933 ([verified immutable source](https://github.com/roy-ht/editdistance/blob/9e05bc645062f68a5c329ea64a1c31cd142bd185/src/editdistance/bycython.cpp#L917-L933))

```
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX > 0x030600B4 && PY_VERSION_HEX < 0x030d0000 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStrWithError(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
static CYTHON_INLINE PyObject * __Pyx_PyDict_GetItemStr(PyObject *dict, PyObject *name) {
    PyObject *res = __Pyx_PyDict_GetItemStrWithError(dict, name);
    if (res == NULL) PyErr_Clear();
    return res;
}
#elif PY_MAJOR_VERSION >= 3 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07020000)
#define __Pyx_PyDict_GetItemStrWithError  PyDict_GetItemWithError
#define __Pyx_PyDict_GetItemStr           PyDict_GetItem
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d5/18/9f4f975ca87a390832b1c22478f3702fcdf739f83211e24d054b7551270d/editdistance-0.8.1.tar.gz); archive SHA-256 `d1cdf80a5d5014b0c9126a69a42ce55a457b457f6986ff69ca98e4fe4d2d8fed`.

## L0384: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `editdistance-0.8.1/src/editdistance/bycython.cpp:1005–1005`. SHA-256 `03ed3fed26b3d613515da088e80ac2ab8e4aba1533c752745b88fdba314b88da`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 997–1013 ([verified immutable source](https://github.com/roy-ht/editdistance/blob/9e05bc645062f68a5c329ea64a1c31cd142bd185/src/editdistance/bycython.cpp#L997-L1013))

```
  #define __Pyx_PyUnicode_KIND(u)         ((int)PyUnicode_KIND(u))
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, (Py_UCS4) ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d5/18/9f4f975ca87a390832b1c22478f3702fcdf739f83211e24d054b7551270d/editdistance-0.8.1.tar.gz); archive SHA-256 `d1cdf80a5d5014b0c9126a69a42ce55a457b457f6986ff69ca98e4fe4d2d8fed`.

## L0497: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `editdistance-0.8.1/src/editdistance/bycython.cpp:3384–3483`. SHA-256 `03ed3fed26b3d613515da088e80ac2ab8e4aba1533c752745b88fdba314b88da`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 3420–3437 ([verified immutable source](https://github.com/roy-ht/editdistance/blob/9e05bc645062f68a5c329ea64a1c31cd142bd185/src/editdistance/bycython.cpp#L3420-L3437))

```
        length = __Pyx_PyUnicode_GET_LENGTH(s1);
        if (length != __Pyx_PyUnicode_GET_LENGTH(s2)) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
        #if CYTHON_PEP393_ENABLED
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
        #else
            hash1 = ((PyUnicodeObject*)s1)->hash;
            hash2 = ((PyUnicodeObject*)s2)->hash;
        #endif
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
```

Excerpt shortened; the complete reviewed range 3420–3440 is in `data/cases.json`.

Closing lines 3438–3440 ([verified immutable source](https://github.com/roy-ht/editdistance/blob/9e05bc645062f68a5c329ea64a1c31cd142bd185/src/editdistance/bycython.cpp#L3438-L3440))

```
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d5/18/9f4f975ca87a390832b1c22478f3702fcdf739f83211e24d054b7551270d/editdistance-0.8.1.tar.gz); archive SHA-256 `d1cdf80a5d5014b0c9126a69a42ce55a457b457f6986ff69ca98e4fe4d2d8fed`.

## L0894: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `editdistance-0.8.1/src/editdistance/bycython.cpp:1060–1060`. SHA-256 `03ed3fed26b3d613515da088e80ac2ab8e4aba1533c752745b88fdba314b88da`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 1052–1068 ([verified immutable source](https://github.com/roy-ht/editdistance/blob/9e05bc645062f68a5c329ea64a1c31cd142bd185/src/editdistance/bycython.cpp#L1052-L1068))

```
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
```

[Frozen source distribution](https://files.pythonhosted.org/packages/d5/18/9f4f975ca87a390832b1c22478f3702fcdf739f83211e24d054b7551270d/editdistance-0.8.1.tar.gz); archive SHA-256 `d1cdf80a5d5014b0c9126a69a42ce55a457b457f6986ff69ca98e4fe4d2d8fed`.
