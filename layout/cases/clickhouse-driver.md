# clickhouse-driver 0.2.11

19 confirmed layout regions; 19 reviewed regions including non-direct context.

## L0144: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedreader.c:771–771`. SHA-256 `482cf3b0829b89762ec32a99df1a117a5ac93f2264eb9a2da856e37c866e2221`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 763–779 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedreader.c#L763-L779))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0145: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedwriter.c:758–758`. SHA-256 `fc4601239dc64226a04ad568bd6f9daae2d21e7190d39704323973bb0134e1b6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 750–766 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedwriter.c#L750-L766))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0146: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/columns/largeint.c:758–758`. SHA-256 `aca26a48a74d693b25b1987a843bc781829ccfc24843e5a95e5028c5dd5a2396`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 750–766 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/columns/largeint.c#L750-L766))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0147: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/varint.c:758–758`. SHA-256 `b290991f7523e4373de7f6e34957ad1a99bc7d488377a3bc978699b4a132adb6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 750–766 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/varint.c#L750-L766))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0346: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedreader.c:841–841`. SHA-256 `482cf3b0829b89762ec32a99df1a117a5ac93f2264eb9a2da856e37c866e2221`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 833–849 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedreader.c#L833-L849))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0347: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedwriter.c:828–828`. SHA-256 `fc4601239dc64226a04ad568bd6f9daae2d21e7190d39704323973bb0134e1b6`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 820–836 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedwriter.c#L820-L836))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0348: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/columns/largeint.c:828–828`. SHA-256 `aca26a48a74d693b25b1987a843bc781829ccfc24843e5a95e5028c5dd5a2396`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 820–836 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/columns/largeint.c#L820-L836))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0349: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/varint.c:828–828`. SHA-256 `b290991f7523e4373de7f6e34957ad1a99bc7d488377a3bc978699b4a132adb6`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 820–836 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/varint.c#L820-L836))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0478: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedreader.c:11600–11671`. SHA-256 `482cf3b0829b89762ec32a99df1a117a5ac93f2264eb9a2da856e37c866e2221`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 11624–11641 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedreader.c#L11624-L11641))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0479: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedwriter.c:10457–10528`. SHA-256 `fc4601239dc64226a04ad568bd6f9daae2d21e7190d39704323973bb0134e1b6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 10481–10498 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedwriter.c#L10481-L10498))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0480: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/columns/largeint.c:6805–6876`. SHA-256 `aca26a48a74d693b25b1987a843bc781829ccfc24843e5a95e5028c5dd5a2396`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 6829–6846 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/columns/largeint.c#L6829-L6846))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0481: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/varint.c:4434–4505`. SHA-256 `b290991f7523e4373de7f6e34957ad1a99bc7d488377a3bc978699b4a132adb6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 4458–4475 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/varint.c#L4458-L4475))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0602: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedreader.c:12144–12210`. SHA-256 `482cf3b0829b89762ec32a99df1a117a5ac93f2264eb9a2da856e37c866e2221`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 12145–12162 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedreader.c#L12145-L12162))

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

Excerpt shortened; the complete reviewed range 12145–12195 is in `data/cases.json`.

Closing lines 12190–12195 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedreader.c#L12190-L12195))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0603: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedwriter.c:11001–11067`. SHA-256 `fc4601239dc64226a04ad568bd6f9daae2d21e7190d39704323973bb0134e1b6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 11002–11019 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedwriter.c#L11002-L11019))

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

Excerpt shortened; the complete reviewed range 11002–11052 is in `data/cases.json`.

Closing lines 11047–11052 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedwriter.c#L11047-L11052))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0604: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/columns/largeint.c:7359–7425`. SHA-256 `aca26a48a74d693b25b1987a843bc781829ccfc24843e5a95e5028c5dd5a2396`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 7360–7377 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/columns/largeint.c#L7360-L7377))

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

Excerpt shortened; the complete reviewed range 7360–7410 is in `data/cases.json`.

Closing lines 7405–7410 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/columns/largeint.c#L7405-L7410))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0605: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/varint.c:4988–5054`. SHA-256 `b290991f7523e4373de7f6e34957ad1a99bc7d488377a3bc978699b4a132adb6`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 4989–5006 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/varint.c#L4989-L5006))

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

Excerpt shortened; the complete reviewed range 4989–5039 is in `data/cases.json`.

Closing lines 5034–5039 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/varint.c#L5034-L5039))

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0740: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedreader.c:13017–13047`. SHA-256 `482cf3b0829b89762ec32a99df1a117a5ac93f2264eb9a2da856e37c866e2221`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 13031–13047 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedreader.c#L13031-L13047))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0741: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/bufferedwriter.c:11559–11589`. SHA-256 `fc4601239dc64226a04ad568bd6f9daae2d21e7190d39704323973bb0134e1b6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 11573–11589 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/bufferedwriter.c#L11573-L11589))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.

## L0742: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `clickhouse_driver-0.2.11/clickhouse_driver/columns/largeint.c:8365–8395`. SHA-256 `aca26a48a74d693b25b1987a843bc781829ccfc24843e5a95e5028c5dd5a2396`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 8379–8395 ([verified immutable source](https://github.com/mymarilyn/clickhouse-driver/blob/48bada60b888e2dd92f90cab86d585cfacead059/clickhouse_driver/columns/largeint.c#L8379-L8395))

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

[Frozen source distribution](https://files.pythonhosted.org/packages/da/75/42c6c0f1e0b84213ff096f913ac0ff82037da6f06754bff28685b2d1e23a/clickhouse_driver-0.2.11.tar.gz); archive SHA-256 `1bec70343bde9e9a55c2254c5960d34c682ff7d60256589226d96c67a112f95a`.
