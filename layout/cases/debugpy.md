# debugpy 1.8.22

16 confirmed layout regions; 17 reviewed regions including non-direct context.

## L0030: Legacy local PyUnicodeObject typedef

**Classification:** non-direct context; project_source; `unused_local_replica_declaration`.

**Purpose:** Declares an old wchar Unicode object shape in process-attachment header. Both package copies have identical SHA. No non-generated use/cast/field read of this typedef found in saved source corpus.

**Migration effect:** Would require update if activated against a new layout; declaration by itself is not an actual consumer or proof that obsolete struct is used.

**Fields / layout:** length, str (wchar_t*), hash. Types: PyUnicodeObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/pydevd_attach_to_process/common/python.h:75–82`. SHA-256 `d6f71bd096cddd23d9e43e174bcc9281f166b8505ee228fc71d76921906135b7`.

**Activation / context:** Comment claims2.4-3.7 compatibility; this is not evidence of PEP393 compatibility. No production use established. Other generated Cython headers delegated separately.

Lines 75–82 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/pydevd_attach_to_process/common/python.h#L75-L82))

```

// 2.4 - 3.7 compatible
typedef struct {
    PyObject_HEAD
    size_t length;      /* Length of raw Unicode data in buffer */
    wchar_t *str;       /* Raw Unicode buffer */
    long hash;          /* Hash value; -1 if not set */
} PyUnicodeObject;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0066: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:776–776`. SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 768–784 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L768-L784))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0067: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:781–781`. SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 773–789 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L773-L789))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0068: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c:776–776`. SHA-256 `612fecb49fc746d832943c20fe9f533feef582d8c885a8ece35358d88320c401`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 768–784 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L768-L784))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0270: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:846–846`. SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 838–854 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L838-L854))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0271: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:851–851`. SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 843–859 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L843-L859))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0272: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c:846–846`. SHA-256 `612fecb49fc746d832943c20fe9f533feef582d8c885a8ece35358d88320c401`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 838–854 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L838-L854))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0456: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:44610–44681`. SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 44634–44651 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L44634-L44651))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0457: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:19309–19380`. SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 19333–19350 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L19333-L19350))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0458: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c:35540–35611`. SHA-256 `612fecb49fc746d832943c20fe9f533feef582d8c885a8ece35358d88320c401`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 35564–35581 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L35564-L35581))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0564: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:45282–45348`. SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 45283–45300 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L45283-L45300))

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

Excerpt shortened; the complete reviewed range 45283–45333 is in `data/cases.json`.

Closing lines 45328–45333 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L45328-L45333))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0565: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:20533–20599`. SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 20534–20551 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L20534-L20551))

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

Excerpt shortened; the complete reviewed range 20534–20584 is in `data/cases.json`.

Closing lines 20579–20584 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L20579-L20584))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0566: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c:36084–36150`. SHA-256 `612fecb49fc746d832943c20fe9f533feef582d8c885a8ece35358d88320c401`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 36085–36102 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L36085-L36102))

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

Excerpt shortened; the complete reviewed range 36085–36135 is in `data/cases.json`.

Closing lines 36130–36135 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L36130-L36135))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0685: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c:45141–45171`. SHA-256 `e5cdcf5b54006888b0edd409f6be4f551b23ce8c36092253b52566e8e66fa1d6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 45155–45171 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_cython.c#L45155-L45171))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0686: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c:19473–19503`. SHA-256 `0b087abafd7fdbfb733e8dddd424e41240d7cf9ab5b5a3bf8a8cc1c06f5a7c51`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 19487–19503 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c#L19487-L19503))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0687: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c:38076–38106`. SHA-256 `612fecb49fc746d832943c20fe9f533feef582d8c885a8ece35358d88320c401`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 38090–38106 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L38090-L38106))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.

## L0835: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Class namespace assignment passes private cached name hash to _PyDict_SetItem_KnownHash.

**Migration effect:** Private metadata coupling; regeneration can select normal dictionary API. Does not require codepoint layout.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `debugpy-1.8.22/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c:2691–2692`. SHA-256 `612fecb49fc746d832943c20fe9f533feef582d8c885a8ece35358d88320c401`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000; Python3.13+ generated branch uses PyDict_SetItem.

Lines 2684–2700 ([verified immutable source](https://github.com/microsoft/debugpy/blob/e2208059db34fa1055c809ff0b303ae1cf1868d7/src/debugpy/_vendored/pydevd/_pydevd_sys_monitoring/_pydevd_sys_monitoring_cython.c#L2684-L2700))

```
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name, PyObject *qualname,
                                           PyObject *mkw, PyObject *modname, PyObject *doc);
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases, PyObject *dict,
                                      PyObject *mkw, int calculate_metaclass, int allow_py2_metaclass);

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

[Frozen source distribution](https://files.pythonhosted.org/packages/44/9d/3cb6693342acf96802dba89934a5b8da43c201d764ebd1f2c0514a3d42bd/debugpy-1.8.22.tar.gz); archive SHA-256 `e489c7268e1c7b41e13b438d9c533d2a7af73fb59bf8cd30fead8286c1c39c4e`.
