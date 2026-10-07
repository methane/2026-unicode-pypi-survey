# marisa-trie 1.4.1

5 confirmed layout regions; 5 reviewed regions including non-direct context.

## L0183: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:791–791`. SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 783–799 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L783-L799))

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
    if (res == NULL) PyErr_Clear();
    return res;
}
#elif !CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07020000
#define __Pyx_PyDict_GetItemStrWithError  PyDict_GetItemWithError
#define __Pyx_PyDict_GetItemStr           PyDict_GetItem
```

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.

## L0385: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:861–861`. SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 853–869 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L853-L869))

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
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.

## L0498: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:35822–35893`. SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 35846–35863 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L35846-L35863))

```
        if (unlikely(length2 < 0)) return -1;
        #endif
        if (length != length2) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
            goto return_ne;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.

## L0628: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:36366–36432`. SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 36367–36384 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L36367-L36384))

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

Excerpt shortened; the complete reviewed range 36367–36417 is in `data/cases.json`.

Closing lines 36412–36417 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L36412-L36417))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.

## L0774: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `marisa_trie-1.4.1/src/marisa_trie.cpp:36964–36994`. SHA-256 `be54802a9e50288939c63f807909c1bab68d376e7f15b05ecf933e7294428f46`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 36978–36994 ([verified immutable source](https://github.com/pytries/marisa-trie/blob/3d3bc808248fa863f262f253590e74022736663e/src/marisa_trie.cpp#L36978-L36994))

```
    PyErr_Clear();
#elif CYTHON_AVOID_BORROWED_REFS || CYTHON_AVOID_THREAD_UNSAFE_BORROWED_REFS
    if (unlikely(__Pyx_PyDict_GetItemRef(__pyx_mstate_global->__pyx_d, name, &result) == -1)) PyErr_Clear();
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
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/77/5d/e235921b5b74818cb65b557fa05cc6201c2c1612d4866ff75c835bcf808d/marisa_trie-1.4.1.tar.gz); archive SHA-256 `44ce3bdbeb7c950d463e460184fc3e18702df9ef0edb826bac672fd789fb1d20`.
