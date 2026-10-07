# multidict 7.0.0

4 confirmed layout regions; 4 reviewed regions including non-direct context.

## L0033: PyUnstable_Unicode_GET_CACHED_HASH

**Classification:** direct layout dependency; compatibility_header; `compatibility_api_implementation_cached_hash`.

**Purpose:** Vendored compatibility implementation of PyUnstable_Unicode_GET_CACHED_HASH returns private cached hash without computing it.

**Migration effect:** Compatibility/API implementation rather than a package algorithm. Modern API call can replace this implementation as target headers gain it; private cached-hash metadata does not require FSR.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `multidict-7.0.0/multidict/_multilib/pythoncapi_compat.h:2698–2708`. SHA-256 `b22379bbb744cc459261f3bf3fbf8882cc02bd12a72d15fb7731c0956fc4fff6`.

**Activation / context:** PY_VERSION_HEX<0x030F00A1; PyPy returns -1; Python>=3 uses PyASCIIObject.hash; Python2 branch uses PyUnicodeObject.hash.

Lines 2696–2713 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if PY_VERSION_HEX < 0x030F00A1
static inline Py_hash_t
PyUnstable_Unicode_GET_CACHED_HASH(PyObject *op)
{
#ifdef PYPY_VERSION
    (void)op;  // unused argument
    return -1;
#elif PY_VERSION_HEX >= 0x03000000
    return ((PyASCIIObject *)op)->hash;
#else
    return ((PyUnicodeObject *)op)->hash;
#endif
}
#endif

#if 0x030D0000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x030F00A7 && \
    !defined(PYPY_VERSION)
// Immortal objects were implemented in Python 3.12, however there is no easy
```

Excerpt shortened; the complete reviewed range 2696–2714 is in `data/cases.json`.

Closing lines 2714–2714 (immutable GitHub mapping unavailable in saved verification evidence)

```
// API to make objects immortal until 3.14 which has _Py_SetImmortal(). Since
```

[Frozen source distribution](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz); archive SHA-256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.

## L1039: unicode_hash

**Classification:** direct layout dependency; project_source; `cached_hash_read`.

**Purpose:** Read cached str hash directly, atomically in free-threaded builds, before falling back to str.tp_hash. No character buffer is read.

**Migration effect:** Requires preserving or replacing the exposed PyASCIIObject hash field and atomic access protocol; UTF-8 payload indexing is not involved.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `multidict-7.0.0/multidict/_multilib/htkeys.h:527–545`. SHA-256 `579869824f9fba4a88cbbd4bb717015ac24044f6aa91c6de9524dc6ee70684b4`.

Lines 527–544 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/htkeys.h#L527-L544))

```
static inline Py_hash_t
unicode_hash(PyObject* o)
{
    assert(PyUnicode_CheckExact(o));
    PyASCIIObject* ascii = (PyASCIIObject*)o;
    /* Another thread may be filling in the cached hash concurrently. */
#ifdef Py_GIL_DISABLED
    Py_hash_t hash = atomic_load_ssize_relaxed(&ascii->hash);
#else
    Py_hash_t hash = ascii->hash;
#endif
    if (hash == -1) {
        hash = PyUnicode_Type.tp_hash(o);
        if (hash == -1) {
            return -1;
        }
    }
    return hash;
```

Excerpt shortened; the complete reviewed range 527–545 is in `data/cases.json`.

Closing lines 545–545 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/htkeys.h#L545-L545))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz); archive SHA-256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.

## L1040: istrobject declaration

**Classification:** direct layout dependency; project_source; `subclass_embedding`.

**Purpose:** Embed the complete PyUnicodeObject as the first member of a Unicode subclass and store a canonical lowercase identity after it.

**Migration effect:** Changing PyUnicodeObject size/layout changes the position of canonical and the subclass basic size; construction delegates to str.__new__, so Unicode payload creation can remain in CPython.

**Fields / layout:** str, canonical. Types: PyUnicodeObject.

**Source:** `multidict-7.0.0/multidict/_multilib/istr.h:11–14`. SHA-256 `13509ec863d9a1a80aa505507a0327c0204ed12c0d91b03214a42f34936cbe7b`.

Lines 11–14 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/istr.h#L11-L14))

```
typedef struct {
    PyUnicodeObject str;
    PyObject* canonical;
} istrobject;
```

Lines 29–39 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/istr.h#L29-L39))

```
/* Build the instance once str.__new__() has produced its value. */
static inline PyObject*
_istr_finish(mod_state* state, PyObject* ret)
{
    PyObject* canonical = PyObject_CallMethodNoArgs(ret, state->str_lower);
    if (canonical == NULL) {
        Py_DECREF(ret);
        return NULL;
    }
    ((istrobject*)ret)->canonical = canonical;
    return ret;
```

Lines 61–69 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/istr.h#L61-L69))

```
    if (x != NULL && IStr_CheckExact(state, x)) {
        Py_INCREF(x);
        return x;
    }
    ret = PyUnicode_Type.tp_new(type, args, kwds);
    if (ret == NULL) {
        return NULL;
    }
    return _istr_finish(state, ret);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz); archive SHA-256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.

## L1041: istr_spec

**Classification:** direct layout dependency; project_source; `subclass_size`.

**Purpose:** Type basic size includes the embedded full Unicode base and subclass metadata.

**Migration effect:** A different Unicode base structure size requires recompilation and agreement with str subclass allocation; no custom payload field writes occur here.

**Fields / layout:** sizeof(istrobject), str, canonical. Types: PyUnicodeObject.

**Source:** `multidict-7.0.0/multidict/_multilib/istr.h:182–191`. SHA-256 `13509ec863d9a1a80aa505507a0327c0204ed12c0d91b03214a42f34936cbe7b`.

Lines 11–14 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/istr.h#L11-L14))

```
typedef struct {
    PyUnicodeObject str;
    PyObject* canonical;
} istrobject;
```

Lines 182–191 ([verified immutable source](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/istr.h#L182-L191))

```
static PyType_Spec istr_spec = {
    .name = "multidict._multidict.istr",
    .basicsize = sizeof(istrobject),
    .flags = (Py_TPFLAGS_DEFAULT
#if PY_VERSION_HEX >= 0x030a00f0
              | Py_TPFLAGS_IMMUTABLETYPE
#endif
              | Py_TPFLAGS_UNICODE_SUBCLASS),
    .slots = istr_slots,
};
```

[Frozen source distribution](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz); archive SHA-256 `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.
