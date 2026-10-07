# pylibjpeg-libjpeg 2.4.0

4 confirmed layout regions; 5 reviewed regions including non-direct context.

## L0226: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `pylibjpeg_libjpeg-2.4.0/libjpeg/_libjpeg.cpp:1125–1125`. SHA-256 `8579dc4c67b5a3b93afa5a460dc89a9c02a2aca3d56c6bcac239432ef6f88c55`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 1117–1133 ([verified immutable source](https://github.com/pydicom/pylibjpeg-libjpeg/blob/b5ea88550c6a2ec30c99fc98fc0b3d89fae8f3be/libjpeg/_libjpeg.cpp#L1117-L1133))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/73/2d/50e07dc574183da13bd4ccc3f300072cc47457bb70b5ff3ba5f17f920914/pylibjpeg_libjpeg-2.4.0.tar.gz); archive SHA-256 `2798ca404a8834447efefa89a03563ce93abdbe4146ea35901680f975959f501`.

## L0424: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `pylibjpeg_libjpeg-2.4.0/libjpeg/_libjpeg.cpp:1205–1205`. SHA-256 `8579dc4c67b5a3b93afa5a460dc89a9c02a2aca3d56c6bcac239432ef6f88c55`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 1197–1213 ([verified immutable source](https://github.com/pydicom/pylibjpeg-libjpeg/blob/b5ea88550c6a2ec30c99fc98fc0b3d89fae8f3be/libjpeg/_libjpeg.cpp#L1197-L1213))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/73/2d/50e07dc574183da13bd4ccc3f300072cc47457bb70b5ff3ba5f17f920914/pylibjpeg_libjpeg-2.4.0.tar.gz); archive SHA-256 `2798ca404a8834447efefa89a03563ce93abdbe4146ea35901680f975959f501`.

## L0520: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `pylibjpeg_libjpeg-2.4.0/libjpeg/_libjpeg.cpp:7609–7708`. SHA-256 `8579dc4c67b5a3b93afa5a460dc89a9c02a2aca3d56c6bcac239432ef6f88c55`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 7645–7662 ([verified immutable source](https://github.com/pydicom/pylibjpeg-libjpeg/blob/b5ea88550c6a2ec30c99fc98fc0b3d89fae8f3be/libjpeg/_libjpeg.cpp#L7645-L7662))

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

Excerpt shortened; the complete reviewed range 7645–7665 is in `data/cases.json`.

Closing lines 7663–7665 ([verified immutable source](https://github.com/pydicom/pylibjpeg-libjpeg/blob/b5ea88550c6a2ec30c99fc98fc0b3d89fae8f3be/libjpeg/_libjpeg.cpp#L7663-L7665))

```
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/73/2d/50e07dc574183da13bd4ccc3f300072cc47457bb70b5ff3ba5f17f920914/pylibjpeg_libjpeg-2.4.0.tar.gz); archive SHA-256 `2798ca404a8834447efefa89a03563ce93abdbe4146ea35901680f975959f501`.

## L0812: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `pylibjpeg_libjpeg-2.4.0/libjpeg/_libjpeg.cpp:8002–8039`. SHA-256 `8579dc4c67b5a3b93afa5a460dc89a9c02a2aca3d56c6bcac239432ef6f88c55`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 8000–8016 ([verified immutable source](https://github.com/pydicom/pylibjpeg-libjpeg/blob/b5ea88550c6a2ec30c99fc98fc0b3d89fae8f3be/libjpeg/_libjpeg.cpp#L8000-L8016))

```
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && PY_VERSION_HEX < 0x030d0000
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#elif CYTHON_COMPILING_IN_LIMITED_API
    if (unlikely(!__pyx_m)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/73/2d/50e07dc574183da13bd4ccc3f300072cc47457bb70b5ff3ba5f17f920914/pylibjpeg_libjpeg-2.4.0.tar.gz); archive SHA-256 `2798ca404a8834447efefa89a03563ce93abdbe4146ea35901680f975959f501`.

## L0906: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `pylibjpeg_libjpeg-2.4.0/libjpeg/_libjpeg.cpp:1260–1260`. SHA-256 `8579dc4c67b5a3b93afa5a460dc89a9c02a2aca3d56c6bcac239432ef6f88c55`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 1252–1268 ([verified immutable source](https://github.com/pydicom/pylibjpeg-libjpeg/blob/b5ea88550c6a2ec30c99fc98fc0b3d89fae8f3be/libjpeg/_libjpeg.cpp#L1252-L1268))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/73/2d/50e07dc574183da13bd4ccc3f300072cc47457bb70b5ff3ba5f17f920914/pylibjpeg_libjpeg-2.4.0.tar.gz); archive SHA-256 `2798ca404a8834447efefa89a03563ce93abdbe4146ea35901680f975959f501`.
