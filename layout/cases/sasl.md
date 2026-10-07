# sasl 0.3.1

2 confirmed layout regions; 3 reviewed regions including non-direct context.

## L0223: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `sasl-0.3.1/sasl/saslwrapper.cpp:437–437`. SHA-256 `d8108d00f60af57e0c52c7baaa2a5449dce2071e0abce8ab7d92a7724e9ab6f0`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 429–445 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/df/ae/d8dda9ef1636f548935c271910d3b35afbf1782df582fda88a13ea48de53/sasl-0.3.1.tar.gz); archive SHA-256 `0695030b23faa65aab2b462ce6f067d61caeb406de22d1ca7f9253fd9ebe127e`.

## L0809: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `sasl-0.3.1/sasl/saslwrapper.cpp:4284–4313`. SHA-256 `d8108d00f60af57e0c52c7baaa2a5449dce2071e0abce8ab7d92a7724e9ab6f0`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 4282–4298 (immutable GitHub mapping unavailable in saved verification evidence)

```
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/df/ae/d8dda9ef1636f548935c271910d3b35afbf1782df582fda88a13ea48de53/sasl-0.3.1.tar.gz); archive SHA-256 `0695030b23faa65aab2b462ce6f067d61caeb406de22d1ca7f9253fd9ebe127e`.

## L0905: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `sasl-0.3.1/sasl/saslwrapper.cpp:501–501`. SHA-256 `d8108d00f60af57e0c52c7baaa2a5449dce2071e0abce8ab7d92a7724e9ab6f0`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 493–509 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/df/ae/d8dda9ef1636f548935c271910d3b35afbf1782df582fda88a13ea48de53/sasl-0.3.1.tar.gz); archive SHA-256 `0695030b23faa65aab2b462ce6f067d61caeb406de22d1ca7f9253fd9ebe127e`.
