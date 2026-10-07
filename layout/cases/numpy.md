# numpy 2.5.3

3 confirmed layout regions; 3 reviewed regions including non-direct context.

## L0032: PyUnstable_Unicode_GET_CACHED_HASH

**Classification:** direct layout dependency; compatibility_header; `compatibility_api_implementation_cached_hash`.

**Purpose:** Vendored compatibility implementation of PyUnstable_Unicode_GET_CACHED_HASH returns private cached hash without computing it.

**Migration effect:** Compatibility/API implementation rather than a package algorithm. Modern API call can replace this implementation as target headers gain it; private cached-hash metadata does not require FSR.

**Fields / layout:** hash. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `numpy-2.5.3/numpy/_core/src/common/pythoncapi-compat/pythoncapi_compat.h:2649–2659`. SHA-256 `ad22f3f51dba39039457be9cb9c162f10eb348218b93635cd998fe4021bf4631`.

**Activation / context:** PY_VERSION_HEX<0x030F00A1; PyPy returns -1; Python>=3 uses PyASCIIObject.hash; Python2 branch uses PyUnicodeObject.hash.

Lines 2647–2664 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if PY_VERSION_HEX < 0x030F00A1
static inline Py_hash_t
PyUnstable_Unicode_GET_CACHED_HASH(PyObject *op)
{
#ifdef PYPY_VERSION
    (void)op;  // unused argument
    return -1;
#elif PY_VERSION_HEX >= 0x03000000
    return ((PyASCIIObject*)op)->hash;
#else
    return ((PyUnicodeObject*)op)->hash;
#endif
}
#endif

#if 0x030D0000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x030F00A7 && !defined(PYPY_VERSION)
// Immortal objects were implemented in Python 3.12, however there is no easy API
// to make objects immortal until 3.14 which has _Py_SetImmortal(). Since
```

Excerpt shortened; the complete reviewed range 2647–2665 is in `data/cases.json`.

Closing lines 2665–2665 (immutable GitHub mapping unavailable in saved verification evidence)

```
// immortal objects are primarily needed for free-threading, this API is implemented
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## L0923: PyUnicodeScalarObject embedded base

**Classification:** direct layout dependency; project_source; `embedded_unicode_object`.

**Purpose:** Embed full PyUnicodeObject prefix before NumPy-owned cached UCS4 pointer/format fields.

**Migration effect:** Changing size/layout/completeness of PyUnicodeObject changes derived scalar size and private-field offsets; removal/opacity prevents embedding. Rebuild alone may suffice only if complete prefix subtype contract remains valid; prior no-character-read exclusion does not remove ABI dependency.

**Fields / layout:** base, obval, buffer_fmt (NPY feature >=1.20). Types: PyUnicodeObject, PyUnicodeScalarObject.

**Source:** `numpy-2.5.3/numpy/_core/include/numpy/arrayscalars.h:139–148`. SHA-256 `39bc05ddd08ab9f2bd6f8f1f8ac79e542d45aa008de6707a0586831075a17734`.

**Activation / context:** Excluded under Py_LIMITED_API; normal NumPy native/unlimited build uses this concrete scalar layout. Feature >=1.20 adds buffer_fmt.

Lines 139–148 ([verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/include/numpy/arrayscalars.h#L139-L148))

```
#ifndef Py_LIMITED_API
typedef struct {
        /* note that the PyObject_HEAD macro lives right here */
        PyUnicodeObject base;
        Py_UCS4 *obval;
    #if NPY_FEATURE_VERSION >= NPY_1_20_API_VERSION
        char *buffer_fmt;
    #endif
} PyUnicodeScalarObject;
#endif
```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

## L1030: Unicode specialization of Py@Name@ArrType_Type

**Classification:** direct layout dependency; project_source; `derived_unicode_scalar_sizeof`.

**Purpose:** Unicode appears in template Name list; tp_basicsize derives from composite scalar struct with embedded complete Unicode base.

**Migration effect:** Confirms NumPy allocation footprint depends on embedded base size, beyond merely retaining a PyObject reference. Private obval/buffer_fmt accesses use offsets after that base.

**Fields / layout:** PyTypeObject.tp_basicsize, sizeof(PyUnicodeScalarObject). Types: PyUnicodeObject, PyUnicodeScalarObject (Unicode template specialization).

**Source:** `numpy-2.5.3/numpy/_core/src/multiarray/scalartypes.c.src:4299–4320`. SHA-256 `16645b91a059f3c11388cebf86e5a909991dc805d2442816954f26cc749ce38d`.

**Activation / context:** Unicode entry generated from saved .c.src template; no generator execution was performed.

Lines 4299–4316 ([verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/scalartypes.c.src#L4299-L4316))

```
 * #Name = Bool,
 *         Byte, Short, Int, Long, LongLong,
 *         UByte, UShort, UInt, ULong, ULongLong,
 *         Half, Float, Double, LongDouble,
 *         CFloat, CDouble, CLongDouble,
 *         String, Unicode, Void,
 *         Datetime, Timedelta#
 * #NAME = BOOL,
 *         BYTE, SHORT, INT, LONG, LONGLONG,
 *         UBYTE, USHORT, UINT, ULONG, ULONGLONG,
 *         HALF, FLOAT, DOUBLE, LONGDOUBLE,
 *         CFLOAT, CDOUBLE, CLONGDOUBLE,
 *         STRING, UNICODE, VOID,
 *         DATETIME, TIMEDELTA#
 */

NPY_NO_EXPORT PyTypeObject Py@Name@ArrType_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
```

Excerpt shortened; the complete reviewed range 4299–4320 is in `data/cases.json`.

Closing lines 4317–4320 ([verified immutable source](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/scalartypes.c.src#L4317-L4320))

```
    .tp_name = "numpy." NPY_@NAME@_name,
    .tp_basicsize = sizeof(Py@Name@ScalarObject),
};

```

[Frozen source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz); archive SHA-256 `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.
