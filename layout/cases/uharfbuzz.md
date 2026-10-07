# uharfbuzz 0.56.2

7 confirmed layout regions; 7 reviewed regions including non-direct context.

## L0202: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz.cpp:901–901`. SHA-256 `6eec900978010513f41ea3de91b065cd13723ead15303e66dde63608b562ed64`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 893–909 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
#define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#if CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStrWithError(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
static CYTHON_INLINE PyObject * __Pyx_PyDict_GetItemStr(PyObject *dict, PyObject *name) {
    PyObject *res = __Pyx_PyDict_GetItemStrWithError(dict, name);
    if (res == NULL && PyErr_Occurred()) {
        PyErr_WriteUnraisable(NULL);
    }
    return res;
}
#elif !CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07020000
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.

## L0203: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz_test.cpp:894–894`. SHA-256 `3cf3bfd46b15e6f51cb8535ea7c1c449d3a63ad0f95587f8ad103bb5e504f86b`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 886–902 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
#define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#if CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStrWithError(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
static CYTHON_INLINE PyObject * __Pyx_PyDict_GetItemStr(PyObject *dict, PyObject *name) {
    PyObject *res = __Pyx_PyDict_GetItemStrWithError(dict, name);
    if (res == NULL && PyErr_Occurred()) {
        PyErr_WriteUnraisable(NULL);
    }
    return res;
}
#elif !CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07020000
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.

## L0404: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz.cpp:974–974`. SHA-256 `6eec900978010513f41ea3de91b065cd13723ead15303e66dde63608b562ed64`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 966–982 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_KIND(u)         ((int)PyUnicode_KIND(u))
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, (Py_UCS4) ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
  static CYTHON_INLINE int __Pyx_PyUnicode_KIND_04(PyObject *o) {
      return __Pyx_PyUnicode_KIND(o) - (int) !!PyUnicode_IS_ASCII(o);
  }
#endif
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.

## L0405: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz_test.cpp:967–967`. SHA-256 `3cf3bfd46b15e6f51cb8535ea7c1c449d3a63ad0f95587f8ad103bb5e504f86b`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 959–975 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_KIND(u)         ((int)PyUnicode_KIND(u))
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, (Py_UCS4) ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
  static CYTHON_INLINE int __Pyx_PyUnicode_KIND_04(PyObject *o) {
      return __Pyx_PyUnicode_KIND(o) - (int) !!PyUnicode_IS_ASCII(o);
  }
#endif
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.

## L0640: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz.cpp:97416–97482`. SHA-256 `6eec900978010513f41ea3de91b065cd13723ead15303e66dde63608b562ed64`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 97417–97434 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 97417–97467 is in `data/cases.json`.

Closing lines 97462–97467 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.

## L0793: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz.cpp:98005–98044`. SHA-256 `6eec900978010513f41ea3de91b065cd13723ead15303e66dde63608b562ed64`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 98025–98041 (immutable GitHub mapping unavailable in saved verification evidence)

```
            return NULL; // BaseException
        }
    }
    __PYX_UPDATE_DICT_CACHE(__pyx_mstate_global->__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return result;
    }
#else
    result = _PyDict_GetItem_KnownHash(__pyx_mstate_global->__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_mstate_global->__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyObject *exc = PyErr_Occurred();
    if (unlikely(exc) && !__Pyx_IgnoreGivenException(exc, PyExc_Exception)) {
        return NULL; // BaseException
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.

## L0867: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Class namespace assignment passes private cached name hash to _PyDict_SetItem_KnownHash.

**Migration effect:** Private metadata coupling; regeneration can select normal dictionary API. Does not require codepoint layout.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `uharfbuzz-0.56.2/src/uharfbuzz/_harfbuzz.cpp:3616–3617`. SHA-256 `6eec900978010513f41ea3de91b065cd13723ead15303e66dde63608b562ed64`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000; Python3.13+ generated branch uses PyDict_SetItem.

Lines 3609–3625 (immutable GitHub mapping unavailable in saved verification evidence)

```

/* GetNameInClass.proto */
#define __Pyx_GetNameInClass(var, nmspace, name)  (var) = __Pyx__GetNameInClass(nmspace, name)
static PyObject *__Pyx__GetNameInClass(PyObject *nmspace, PyObject *name);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* CLineInTraceback.proto (used by AddTraceback) */
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/cb/b87e1e470e43c6d0b8edd9b5ed968c4465c3de5391a0f253edb0df1a9f18/uharfbuzz-0.56.2.tar.gz); archive SHA-256 `303cd60c329bc4d88053ca03eb752476b51ca023944051c33710534dbc4fdac6`.
