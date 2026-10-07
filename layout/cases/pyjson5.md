# pyjson5 2.0.1

12 confirmed layout regions; 13 reviewed regions including non-direct context.

## L0170: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:774–774`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 766–782 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L0372: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:844–844`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 836–852 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L0493: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:108262–108333`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 108286–108303 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L0627: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:108806–108872`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 108807–108824 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 108807–108857 is in `data/cases.json`.

Closing lines 108852–108857 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L0765: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:110388–110418`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 110402–110418 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L0919: struct AsciiObject embeds PyASCIIObject

**Classification:** direct layout dependency; generated_distribution_code; `manual_unicode_output_layout_construction`.

**Purpose:** Project encoder constructs ASCII Unicode from raw reallocatable allocation: embeds PyASCIIObject header to calculate payload offset; sets length/state fields and initializes hash/legacy wchar readiness through typed templates.

**Migration effect:** Strong raw allocation/header/payload-offset coupling. Output bytes are ASCII (already UTF8), but this relies on exact object size/state/ownership and must use supported construction or a deliberately preserved ABI.

**Fields / layout:** embedded_base. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:1826–1835`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** Project-generated encode implementation. reset_hash uses field-detection template; reset_wstr/state.ready write only when corresponding member exists; modern absent members select no-op.

Lines 1821–1837 (immutable GitHub mapping unavailable in saved verification evidence)

```
 *     PyASCIIObject base
 *     char data[1]
*/

#line 204 "src/_imports.pyx"
struct __pyx_t_7pyjson5_AsciiObject {

#line 204 "src/_imports.pyx"
  PyASCIIObject base;

#line 204 "src/_imports.pyx"
  char data[1];

#line 204 "src/_imports.pyx"
};

/* "src/_raise_decoder.pyx":1
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L0920: __pyx_pf_7pyjson5_14encode output header construction region

**Classification:** direct layout dependency; generated_distribution_code; `manual_unicode_output_layout_construction`.

**Purpose:** Project encoder constructs ASCII Unicode from raw reallocatable allocation: embeds PyASCIIObject header to calculate payload offset; sets length/state fields and initializes hash/legacy wchar readiness through typed templates.

**Migration effect:** Strong raw allocation/header/payload-offset coupling. Output bytes are ASCII (already UTF8), but this relies on exact object size/state/ownership and must use supported construction or a deliberately preserved ABI.

**Fields / layout:** hash, length, state.ascii, state.compact, state.interned, state.kind, state.ready, wstr. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/pyjson5.cpp:98301–98783`. SHA-256 `b6ec1f35080bc26083218fa6389250c7f5650c1c92e4361ccfdb796d9509e0de`.

**Activation / context:** Project-generated encode implementation. reset_hash uses field-detection template; reset_wstr/state.ready write only when corresponding member exists; modern absent members select no-op.

Lines 98378–98394 (immutable GitHub mapping unavailable in saved verification evidence)

```
#line 289 "src/_exports.pyx"
__Pyx_RefNannySetupContext("encode", 0);

/* "src/_exports.pyx":331
 *     cdef object result
 *     cdef Py_ssize_t start = (
 *         <Py_ssize_t> <void*> &(<AsciiObject*> NULL).data[0]             # <<<<<<<<<<<<<<
 *     )
 *     cdef Py_ssize_t length
*/

#line 331 "src/_exports.pyx"
__pyx_v_start = ((Py_ssize_t)((void *)(&(((__pyx_t_7pyjson5_AsciiObject *)NULL)->data[0]))));

/* "src/_exports.pyx":334
 *     )
 *     cdef Py_ssize_t length
```

Lines 98588–98605 (immutable GitHub mapping unavailable in saved verification evidence)

```
/* "src/_exports.pyx":354
 *             return u''
 * 
 *         temp = ObjectRealloc(writer.obj, writer.position + 1)             # <<<<<<<<<<<<<<
 *         if temp is not NULL:
 *             writer.obj = temp
*/

#line 354 "src/_exports.pyx"
__pyx_v_temp = PyObject_Realloc(__pyx_v_writer.obj, (__pyx_v_writer.position + 1));

/* "src/_exports.pyx":355
 * 
 *         temp = ObjectRealloc(writer.obj, writer.position + 1)
 *         if temp is not NULL:             # <<<<<<<<<<<<<<
 *             writer.obj = temp
 *         (<char*> writer.obj)[writer.position] = 0
*/
```

Excerpt shortened; the complete reviewed range 98588–98664 is in `data/cases.json`.

Closing lines 98659–98664 (immutable GitHub mapping unavailable in saved verification evidence)

```

#line 359 "src/_exports.pyx"
__pyx_v_result = __pyx_t_1;

#line 359 "src/_exports.pyx"
__pyx_t_1 = 0;
```

Lines 98677–98694 (immutable GitHub mapping unavailable in saved verification evidence)

```
/* "src/_exports.pyx":362
 *         writer.obj = NULL
 * 
 *         (<PyASCIIObject*> result).length = length             # <<<<<<<<<<<<<<
 *         reset_hash(<PyASCIIObject*> result)
 *         reset_wstr(<PyASCIIObject*> result)
*/

#line 362 "src/_exports.pyx"
((PyASCIIObject *)__pyx_v_result)->length = __pyx_v_length;

/* "src/_exports.pyx":363
 * 
 *         (<PyASCIIObject*> result).length = length
 *         reset_hash(<PyASCIIObject*> result)             # <<<<<<<<<<<<<<
 *         reset_wstr(<PyASCIIObject*> result)
 *         (<PyASCIIObject*> result).state.interned = SSTATE_NOT_INTERNED
*/
```

Excerpt shortened; the complete reviewed range 98677–98780 is in `data/cases.json`.

Closing lines 98775–98780 (immutable GitHub mapping unavailable in saved verification evidence)

```

#line 371 "src/_exports.pyx"
__Pyx_INCREF(__pyx_v_result);

#line 371 "src/_exports.pyx"
__pyx_r = __pyx_v_result;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L1050: PyASCIIObject external Cython declaration

**Classification:** non-direct context; project_source; `binding_declaration`.

**Purpose:** Declare header fields from Python.h for Cython access; this alone is not an object dereference or allocation.

**Migration effect:** Exposes field names for encode construction; affected field accesses are recorded in encode and native helper cases. External Cython declarations do not themselves prove a runtime layout read.

**Fields / layout:** length, hash, wstr, state.interned, state.kind, state.compact, state.ascii, state.ready. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/src/_imports.pyx:173–184`. SHA-256 `5c41ef9c67c2fdebda15cd0cd1c294e35b1ca1e637d2231a7538f129e2758aa2`.

Lines 173–184 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_imports.pyx#L173-L184))

```
    ctypedef struct __ascii_object_state:
        uint8_t interned
        uint8_t kind
        boolean compact
        boolean ascii
        boolean ready

    ctypedef struct PyASCIIObject:
        Py_ssize_t length
        Py_hash hash
        wchar_t *wstr
        __ascii_object_state state
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L1051: AsciiObject declaration

**Classification:** direct layout dependency; project_source; `layout_embedding`.

**Purpose:** Define an ASCII header followed by character storage; encode takes the data member offset as its reserved output prefix.

**Migration effect:** Requires the ASCII inline layout to match CPython; sizeof/offset changes propagate into output allocation and writes.

**Fields / layout:** base, data[1]. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/src/_imports.pyx:204–206`. SHA-256 `5c41ef9c67c2fdebda15cd0cd1c294e35b1ca1e637d2231a7538f129e2758aa2`.

Lines 204–206 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_imports.pyx#L204-L206))

```
ctypedef struct AsciiObject:
    PyASCIIObject base
    char data[1]
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L1052: encode

**Classification:** direct layout dependency; project_source; `custom_unicode_construction`.

**Purpose:** Write ASCII JSON5 output into a reallocatable allocation with header-size prefix, then initialize it as str and set Unicode header fields directly.

**Migration effect:** Depends on ASCII header-prefix/payload placement and field initialization, not merely on Unicode construction APIs. UTF-8 migration needs a supported adoption/writer mechanism or adaptation of this custom construction path.

**Fields / layout:** offsetof-like AsciiObject.data[0], length, hash, wstr, state.interned, state.kind, state.compact, state.ready, state.ascii. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/src/_exports.pyx:289–374`. SHA-256 `d687310af5345a2e5dfc7cb90433739f8873fb55c33ad4da14094061350edb8a`.

Lines 328–345 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_exports.pyx#L328-L345))

```
    cdef void *temp
    cdef object result
    cdef Py_ssize_t start = (
        <Py_ssize_t> <void*> &(<AsciiObject*> NULL).data[0]
    )
    cdef Py_ssize_t length
    cdef object opts = _to_options(options, options_kw)
    cdef WriterReallocatable writer = WriterReallocatable(
        Writer(
            _WriterReallocatable_reserve,
            _WriterReallocatable_append_c,
            _WriterReallocatable_append_s,
            <PyObject*> opts,
        ),
        start, 0, NULL,
    )

    try:
```

Excerpt shortened; the complete reviewed range 328–374 is in `data/cases.json`.

Closing lines 369–374 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_exports.pyx#L369-L374))

```
        (<PyASCIIObject*> result).state.ascii = True

        return result
    finally:
        if writer.obj is not NULL:
            ObjectFree(writer.obj)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L1053: ResetHash_<T,false,true>::reset and hash trait

**Classification:** direct layout dependency; project_source; `direct_field_write`.

**Purpose:** SFINAE detects hash member and reset_hash(PyASCIIObject*) sets it to -1. The neighboring ob_shash path serves another structure; field choice is established by traits, not misleading comments.

**Migration effect:** Removing/renaming hash requires adapting this template specialization or replacing the direct reset with supported construction.

**Fields / layout:** decltype(C.hash), hash. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/src/native.hpp:116–138`. SHA-256 `37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085`.

Lines 116–133 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L116-L133))

```
template <typename T>
struct has_hash {
    template <typename C> static std::uint8_t test(typename VoidT_<decltype((std::declval<C>().hash, true))>::Value);
    template <typename C> static std::uint64_t test(...);
    enum { value = sizeof(test<T>(0)) == sizeof(std::uint8_t) };
};

template<class T, bool ob_shash = has_ob_shash<T>::value, bool hash = has_hash<T>::value>
struct ResetHash_;

template<class T>
struct ResetHash_ <T, true, false> {
    static inline void reset(T *obj) {
        obj->ob_shash = -1;  // CPython: str
    }
};

template<class T>
```

Excerpt shortened; the complete reviewed range 116–138 is in `data/cases.json`.

Closing lines 134–138 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L134-L138))

```
struct ResetHash_ <T, false, true> {
    static inline void reset(T *obj) {
        obj->hash = -1;  // CPython: bytes
    }
};
```

Lines 147–150 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L147-L150))

```
template <class T>
static inline void reset_hash(T *obj) {
    ResetHash_<T>::reset(obj);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L1054: ResetWstr_<T,true>::reset and wstr trait

**Classification:** direct layout dependency; project_source; `conditional_direct_field_write`.

**Purpose:** If T has wstr, reset_wstr writes nullptr; absent-field versions use a no-op specialization.

**Migration effect:** The existing SFINAE adapts to removed wstr in3.12+, but any retained wide-string field semantics still require agreement with Unicode initialization.

**Fields / layout:** decltype(C.wstr), wstr. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/src/native.hpp:153–180`. SHA-256 `37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085`.

Lines 153–170 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L153-L170))

```
template <typename T>
struct has_wstr {
    template <typename C> static std::uint8_t test(typename VoidT_<decltype((std::declval<C>().wstr, true))>::Value);
    template <typename C> static std::uint64_t test(...);
    enum { value = sizeof(test<T>(0)) == sizeof(std::uint8_t) };
};

template<class T, bool hash = has_wstr<T>::value>
struct ResetWstr_;

template<class T>
struct ResetWstr_ <T, true> {
    static inline void reset(T *obj) {
        obj->wstr = nullptr;  // CPython >= 3.12: absent
    }
};

template<class T>
```

Excerpt shortened; the complete reviewed range 153–180 is in `data/cases.json`.

Closing lines 175–180 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L175-L180))

```
};

template <class T>
static inline void reset_wstr(T *obj) {
    ResetWstr_<T>::reset(obj);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

## L1055: SetReady_<T,true>::set and ready trait

**Classification:** direct layout dependency; project_source; `conditional_direct_field_write`.

**Purpose:** If T has state.ready, set_ready writes true; absent-field versions use a no-op specialization.

**Migration effect:** The existing SFINAE handles removed ready flag; other state flags in encode remain direct layout dependencies.

**Fields / layout:** decltype(C.state.ready), state.ready. Types: PyASCIIObject.

**Source:** `pyjson5-2.0.1/src/native.hpp:182–209`. SHA-256 `37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085`.

Lines 182–199 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L182-L199))

```
template <typename T>
struct has_ready {
    template <typename C> static std::uint8_t test(typename VoidT_<decltype((std::declval<C>().state.ready, true))>::Value);
    template <typename C> static std::uint64_t test(...);
    enum { value = sizeof(test<T>(0)) == sizeof(std::uint8_t) };
};

template<class T, bool hash = has_ready<T>::value>
struct SetReady_;

template<class T>
struct SetReady_ <T, true> {
    static inline void set(T *obj) {
        obj->state.ready = true;  // CPython >= 3.12: absent
    }
};

template<class T>
```

Excerpt shortened; the complete reviewed range 182–209 is in `data/cases.json`.

Closing lines 204–209 ([verified immutable source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L204-L209))

```
};

template <class T>
static inline void set_ready(T *obj) {
    SetReady_<T>::set(obj);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA-256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.
