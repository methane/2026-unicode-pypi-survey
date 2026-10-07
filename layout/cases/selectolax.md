# selectolax 0.4.13

9 confirmed layout regions; 9 reviewed regions including non-direct context.

## L0166: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/lexbor.c:1075–1075`. SHA-256 `0b7e83b888d1e804856f7ee33103687f81ebf35902e2bbe08cb0e6f8ce93d813`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 1067–1083 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0167: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/parser.c:998–998`. SHA-256 `1b5a2765c6e9fde9d69a710adb257cce926cdc584e4e37c45fc7543e4d2248c6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 990–1006 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0368: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `selectolax-0.4.13/selectolax/lexbor.c:1148–1148`. SHA-256 `0b7e83b888d1e804856f7ee33103687f81ebf35902e2bbe08cb0e6f8ce93d813`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 1140–1156 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0369: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `selectolax-0.4.13/selectolax/parser.c:1071–1071`. SHA-256 `1b5a2765c6e9fde9d69a710adb257cce926cdc584e4e37c45fc7543e4d2248c6`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 1063–1079 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0624: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/lexbor.c:56876–56942`. SHA-256 `0b7e83b888d1e804856f7ee33103687f81ebf35902e2bbe08cb0e6f8ce93d813`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 56877–56894 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 56877–56927 is in `data/cases.json`.

Closing lines 56922–56927 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0625: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/parser.c:43679–43745`. SHA-256 `1b5a2765c6e9fde9d69a710adb257cce926cdc584e4e37c45fc7543e4d2248c6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 43680–43697 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 43680–43730 is in `data/cases.json`.

Closing lines 43725–43730 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0761: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/lexbor.c:57421–57460`. SHA-256 `0b7e83b888d1e804856f7ee33103687f81ebf35902e2bbe08cb0e6f8ce93d813`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 57441–57457 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0762: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/parser.c:44627–44666`. SHA-256 `1b5a2765c6e9fde9d69a710adb257cce926cdc584e4e37c45fc7543e4d2248c6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 44647–44663 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.

## L0859: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Class namespace assignment passes private cached name hash to _PyDict_SetItem_KnownHash.

**Migration effect:** Private metadata coupling; regeneration can select normal dictionary API. Does not require codepoint layout.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `selectolax-0.4.13/selectolax/lexbor.c:3476–3477`. SHA-256 `0b7e83b888d1e804856f7ee33103687f81ebf35902e2bbe08cb0e6f8ce93d813`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000; Python3.13+ generated branch uses PyDict_SetItem.

Lines 3469–3485 (immutable GitHub mapping unavailable in saved verification evidence)

```
                                         PyObject *qualname, PyObject *closure,
                                         PyObject *module, PyObject *globals,
                                         PyObject *code);
static PyTypeObject *__Pyx_Get_FusedFunction_Type(void);

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

[Frozen source distribution](https://files.pythonhosted.org/packages/49/3a/3c56859df452fddb6d94d30ff8b6b19088a09b542a01f211cd147ccca39a/selectolax-0.4.13.tar.gz); archive SHA-256 `261116b1b13efbec5cc0252baeca3a85098e96ef5c088bf3ef8cfbe15d3a8ea3`.
