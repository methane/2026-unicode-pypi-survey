# gensim 4.4.0

32 confirmed layout regions; 42 reviewed regions including non-direct context.

## L0171: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/_matutils.c:563–563`. SHA-256 `100f18c06810b5c9c63fbd81f9cf2a03c28006d585d1f0dbfb3429e6872ad022`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 555–571 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0172: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/corpora/_mmreader.c:563–563`. SHA-256 `d80e20e7dab9eee3483240fc973bc7361428b327d05d424d0ed85ea3c24a1108`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 555–571 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0173: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_corpusfile.cpp:590–590`. SHA-256 `b149ce9f0f3f80e0c4408fa6af3897132ac32b5ab3aad03dc989d5cf0f4344f4`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 582–598 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0174: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_inner.cpp:589–589`. SHA-256 `c16c2cd5dda89a75b10aa9589934b0fa569479dadd1efbbf54d63970f5452872`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 581–597 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0175: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_corpusfile.cpp:590–590`. SHA-256 `34185bdeaa14ff05aeb57a17c6ba8d939bdee23ebdc3b5df5b6c8d778f1513d6`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 582–598 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0176: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_inner.c:569–569`. SHA-256 `9353c181221c9f127d63b0b2627c548d18a22d274a1abe8cdbde8f85c7f21782`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 561–577 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0177: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/nmf_pgd.c:563–563`. SHA-256 `65f297f065520f950b8b6c6e8d2bd2443aef40889e97a5b1df793cbc32d4ba1d`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 555–571 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0178: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_corpusfile.cpp:590–590`. SHA-256 `0049a8085a443352018629656ec36dd3e5fe50aee24ea4c7c19f4eccf122ef75`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 582–598 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0179: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_inner.c:568–568`. SHA-256 `45896b768dba6d43a38733ecf91a1a17ee6b97f7d2455c641d2dafa85d284c61`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 560–576 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0180: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/similarities/fastss.c:563–563`. SHA-256 `2eb5b61b6d28d317e8141fbd2304a88ceb056abcd99cf2d7f64d9356898fc7a7`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 555–571 (immutable GitHub mapping unavailable in saved verification evidence)

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
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0373: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/_matutils.c:584–584`. SHA-256 `100f18c06810b5c9c63fbd81f9cf2a03c28006d585d1f0dbfb3429e6872ad022`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 576–592 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0374: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/corpora/_mmreader.c:584–584`. SHA-256 `d80e20e7dab9eee3483240fc973bc7361428b327d05d424d0ed85ea3c24a1108`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 576–592 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0375: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_corpusfile.cpp:611–611`. SHA-256 `b149ce9f0f3f80e0c4408fa6af3897132ac32b5ab3aad03dc989d5cf0f4344f4`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 603–619 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0376: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_inner.cpp:610–610`. SHA-256 `c16c2cd5dda89a75b10aa9589934b0fa569479dadd1efbbf54d63970f5452872`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 602–618 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0377: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_corpusfile.cpp:611–611`. SHA-256 `34185bdeaa14ff05aeb57a17c6ba8d939bdee23ebdc3b5df5b6c8d778f1513d6`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 603–619 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0378: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_inner.c:590–590`. SHA-256 `9353c181221c9f127d63b0b2627c548d18a22d274a1abe8cdbde8f85c7f21782`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 582–598 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0379: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/nmf_pgd.c:584–584`. SHA-256 `65f297f065520f950b8b6c6e8d2bd2443aef40889e97a5b1df793cbc32d4ba1d`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 576–592 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0380: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_corpusfile.cpp:611–611`. SHA-256 `0049a8085a443352018629656ec36dd3e5fe50aee24ea4c7c19f4eccf122ef75`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 603–619 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0381: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_inner.c:589–589`. SHA-256 `45896b768dba6d43a38733ecf91a1a17ee6b97f7d2455c641d2dafa85d284c61`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 581–597 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0382: __Pyx_PyUnicode_IS_TRUE macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_wstr_metadata_read`.

**Purpose:** Older non-ready Unicode truth test reads wstr_length when ready fixed-width length is unavailable.

**Migration effect:** Only old wchar/not-ready compatibility logic. No active modern Python3.12+ layout use in this named-field branch; replacing legacy conversion requires metadata accessor.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gensim-4.4.0/gensim/similarities/fastss.c:584–584`. SHA-256 `2eb5b61b6d28d317e8141fbd2304a88ceb056abcd99cf2d7f64d9356898fc7a7`.

**Activation / context:** Not limited API; Python<3.12 branch; CPython>=3.9 special case; non-ready Unicode only. Ready strings use PyUnicode_GET_LENGTH.

Lines 576–592 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0494: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/_matutils.c:24041–24140`. SHA-256 `100f18c06810b5c9c63fbd81f9cf2a03c28006d585d1f0dbfb3429e6872ad022`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 24077–24094 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 24077–24097 is in `data/cases.json`.

Closing lines 24095–24097 (immutable GitHub mapping unavailable in saved verification evidence)

```
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0495: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/nmf_pgd.c:18282–18381`. SHA-256 `65f297f065520f950b8b6c6e8d2bd2443aef40889e97a5b1df793cbc32d4ba1d`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 18318–18335 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 18318–18338 is in `data/cases.json`.

Closing lines 18336–18338 (immutable GitHub mapping unavailable in saved verification evidence)

```
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0496: __Pyx_PyUnicode_Equals

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Unicode equality rejects mismatched already-known hashes before length/kind/data comparison.

**Migration effect:** Private metadata offset dependency. Named hash fields do not themselves require FSR payload; later generic DATA/READ comparison is a separate algorithm.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/similarities/fastss.c:5197–5296`. SHA-256 `2eb5b61b6d28d317e8141fbd2304a88ceb056abcd99cf2d7f64d9356898fc7a7`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS. PyASCIIObject branch under CYTHON_PEP393_ENABLED; PyUnicodeObject hash fallback only non-PEP393/Python2 legacy layout.

Lines 5233–5250 (immutable GitHub mapping unavailable in saved verification evidence)

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

Excerpt shortened; the complete reviewed range 5233–5253 is in `data/cases.json`.

Closing lines 5251–5253 (immutable GitHub mapping unavailable in saved verification evidence)

```
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0766: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/_matutils.c:22816–22845`. SHA-256 `100f18c06810b5c9c63fbd81f9cf2a03c28006d585d1f0dbfb3429e6872ad022`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 22814–22830 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0767: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/corpora/_mmreader.c:7542–7571`. SHA-256 `d80e20e7dab9eee3483240fc973bc7361428b327d05d424d0ed85ea3c24a1108`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 7540–7556 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0768: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_inner.cpp:10785–10814`. SHA-256 `c16c2cd5dda89a75b10aa9589934b0fa569479dadd1efbbf54d63970f5452872`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 10783–10799 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0769: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_inner.c:10316–10345`. SHA-256 `9353c181221c9f127d63b0b2627c548d18a22d274a1abe8cdbde8f85c7f21782`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 10314–10330 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0770: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/nmf_pgd.c:18615–18644`. SHA-256 `65f297f065520f950b8b6c6e8d2bd2443aef40889e97a5b1df793cbc32d4ba1d`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 18613–18629 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0771: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_corpusfile.cpp:11279–11308`. SHA-256 `0049a8085a443352018629656ec36dd3e5fe50aee24ea4c7c19f4eccf122ef75`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 11277–11293 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0772: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_inner.c:12088–12117`. SHA-256 `45896b768dba6d43a38733ecf91a1a17ee6b97f7d2455c641d2dafa85d284c61`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 12086–12102 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0773: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Module-global fallback looks up global Unicode name using private cached hash.

**Migration effect:** Private metadata field coupling only, not a fixed-width codepoint buffer requirement; update generated runtime once and regenerate copies.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/similarities/fastss.c:6034–6063`. SHA-256 `2eb5b61b6d28d317e8141fbd2304a88ceb056abcd99cf2d7f64d9356898fc7a7`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; direct global lookup fallback.

Lines 6032–6048 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0862: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Class namespace assignment passes private cached name hash to _PyDict_SetItem_KnownHash.

**Migration effect:** Private metadata coupling; regeneration can select normal dictionary API. Does not require codepoint layout.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gensim-4.4.0/gensim/similarities/fastss.c:1510–1511`. SHA-256 `2eb5b61b6d28d317e8141fbd2304a88ceb056abcd99cf2d7f64d9356898fc7a7`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000; Python3.13+ generated branch uses PyDict_SetItem.

Lines 1503–1519 (immutable GitHub mapping unavailable in saved verification evidence)

```
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* CalculateMetaclass.proto */
```

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0883: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/_matutils.c:635–635`. SHA-256 `100f18c06810b5c9c63fbd81f9cf2a03c28006d585d1f0dbfb3429e6872ad022`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 627–643 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0884: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/corpora/_mmreader.c:635–635`. SHA-256 `d80e20e7dab9eee3483240fc973bc7361428b327d05d424d0ed85ea3c24a1108`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 627–643 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0885: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_corpusfile.cpp:662–662`. SHA-256 `b149ce9f0f3f80e0c4408fa6af3897132ac32b5ab3aad03dc989d5cf0f4344f4`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 654–670 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0886: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/doc2vec_inner.cpp:661–661`. SHA-256 `c16c2cd5dda89a75b10aa9589934b0fa569479dadd1efbbf54d63970f5452872`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 653–669 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0887: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_corpusfile.cpp:662–662`. SHA-256 `34185bdeaa14ff05aeb57a17c6ba8d939bdee23ebdc3b5df5b6c8d778f1513d6`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 654–670 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0888: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/fasttext_inner.c:641–641`. SHA-256 `9353c181221c9f127d63b0b2627c548d18a22d274a1abe8cdbde8f85c7f21782`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 633–649 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0889: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/nmf_pgd.c:635–635`. SHA-256 `65f297f065520f950b8b6c6e8d2bd2443aef40889e97a5b1df793cbc32d4ba1d`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 627–643 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0890: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_corpusfile.cpp:662–662`. SHA-256 `0049a8085a443352018629656ec36dd3e5fe50aee24ea4c7c19f4eccf122ef75`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 654–670 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0891: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/models/word2vec_inner.c:640–640`. SHA-256 `45896b768dba6d43a38733ecf91a1a17ee6b97f7d2455c641d2dafa85d284c61`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 632–648 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.

## L0892: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `gensim-4.4.0/gensim/similarities/fastss.c:635–635`. SHA-256 `2eb5b61b6d28d317e8141fbd2304a88ceb056abcd99cf2d7f64d9356898fc7a7`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 627–643 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/1a/80/fe9d2e1ace968041814dbcfce4e8499a643a36c41267fa4b6c4f54cce420/gensim-4.4.0.tar.gz); archive SHA-256 `a3f5b626da5518e79a479140361c663089fe7998df8ba52d56e1ded71ac5bdf5`.
