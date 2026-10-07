# pyobjc-core 12.2.2

3 confirmed layout regions; 3 reviewed regions including non-direct context.

## L1056: PyObjCUnicodeObject declaration

**Classification:** direct layout dependency; project_source; `subclass_embedding`.

**Purpose:** Embed full noncompact Unicode base ahead of Objective-C proxy metadata.

**Migration effect:** Changing the Unicode base size/layout changes subclass extension offsets and allocation; subclass is constructed manually rather than using standard str.__new__.

**Fields / layout:** base, weakrefs, nsstr, py_nsstr. Types: PyUnicodeObject.

**Source:** `pyobjc_core-12.2.2/Modules/objc/pyobjc_unicode.m:21–27`. SHA-256 `332a31079cc98704ed0e97227d0d24e3566cef9d4713afb10d57498935cb9d9c`.

Lines 21–27 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L21-L27))

```
typedef struct {
    PyUnicodeObject base;
    PyObject* _Nullable weakrefs;
    id nsstr;
    PyObject* _Nullable py_nsstr;

} PyObjCUnicodeObject;
```

Lines 128–145 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L128-L145))

```
static PyMemberDef unic_members[] = {
    {
        .name   = "__weaklistoffset__",
        .type   = T_PYSSIZET,
        .offset = offsetof(PyObjCUnicodeObject, weakrefs),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyType_Slot unic_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&unic_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&unic_getattro},
    {.slot = Py_tp_doc, .pfunc = (void*)&unic_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&unic_methods},
    {.slot = Py_tp_members, .pfunc = (void*)&unic_members},
    {.slot = Py_tp_getset, .pfunc = (void*)&unic_getset},
```

Excerpt shortened; the complete reviewed range 128–156 is in `data/cases.json`.

Closing lines 151–156 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L151-L156))

```
    .basicsize = sizeof(PyObjCUnicodeObject),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .slots = unic_slots,
};
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz); archive SHA-256 `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.

## L1057: unic_spec / weakref offset

**Classification:** direct layout dependency; project_source; `subclass_size`.

**Purpose:** Expose subclass weakref offset and allocate full Unicode base plus Objective-C metadata.

**Migration effect:** A Unicode structure layout/size change requires compatible subclass allocation and updated extension offsets.

**Fields / layout:** offsetof(PyObjCUnicodeObject,weakrefs), sizeof(PyObjCUnicodeObject). Types: PyUnicodeObject.

**Source:** `pyobjc_core-12.2.2/Modules/objc/pyobjc_unicode.m:128–156`. SHA-256 `332a31079cc98704ed0e97227d0d24e3566cef9d4713afb10d57498935cb9d9c`.

Lines 128–145 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L128-L145))

```
static PyMemberDef unic_members[] = {
    {
        .name   = "__weaklistoffset__",
        .type   = T_PYSSIZET,
        .offset = offsetof(PyObjCUnicodeObject, weakrefs),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};

static PyType_Slot unic_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&unic_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&unic_getattro},
    {.slot = Py_tp_doc, .pfunc = (void*)&unic_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&unic_methods},
    {.slot = Py_tp_members, .pfunc = (void*)&unic_members},
    {.slot = Py_tp_getset, .pfunc = (void*)&unic_getset},
```

Excerpt shortened; the complete reviewed range 128–156 is in `data/cases.json`.

Closing lines 151–156 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L151-L156))

```
    .basicsize = sizeof(PyObjCUnicodeObject),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .slots = unic_slots,
};
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz); archive SHA-256 `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.

## L1058: PyObjCUnicode_New

**Classification:** direct layout dependency; project_source; `custom_unicode_construction`.

**Purpose:** Allocate a Unicode subclass, initialize noncompact header directly, choose one/two/four-byte FSR from NSString data, allocate/reuse external character storage, and set UTF8/wide aliases.

**Migration effect:** Requires a supported noncompact/subclass construction contract or substantial adaptation under UTF-8 internals. A cached FSR read view does not cover ownership and direct writes to header/data union; destructor expects CPython Unicode ownership rules.

**Fields / layout:** sizeof(PyObjCUnicodeObject), hash, wstr, length, state.compact, state.ready, state.interned, state.statically_allocated, state.ascii, state.kind, utf8, utf8_length, wstr_length, base.data.any, base.data.latin1, base.data.ucs2, base.data.ucs4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `pyobjc_core-12.2.2/Modules/objc/pyobjc_unicode.m:177–434`. SHA-256 `332a31079cc98704ed0e97227d0d24e3566cef9d4713afb10d57498935cb9d9c`.

Lines 220–237 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L220-L237))

```
    // Using PyObject_Malloc instead of PyObject_New matches the
    // implementation of PyUnicode_New
    result = PyObject_Malloc(sizeof(PyObjCUnicodeObject));
    if (unlikely(result == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(characters);
        characters = NULL;

        return NULL;
        // LCOV_EXCL_STOP
    }
    (void)PyObject_Init((PyObject*)result, (PyTypeObject*)PyObjCUnicode_Type);

    result->weakrefs = NULL;
    result->py_nsstr = NULL;
    result->nsstr    = [value retain];

    ascii   = (PyASCIIObject*)result;
```

Excerpt shortened; the complete reviewed range 220–262 is in `data/cases.json`.

Closing lines 257–262 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L257-L262))

```
    compact->utf8        = NULL;
#if PY_VERSION_HEX < 0x030c0000
    compact->wstr_length = 0;
#endif

    result->base.data.any = NULL;
```

Lines 285–302 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L285-L302))

```
    if (maxchar <= 128) {
        ascii->state.ascii = 1;
        ascii->state.kind  = PyUnicode_1BYTE_KIND;

    } else if (maxchar <= 255) {
        ascii->state.ascii = 0;
        ascii->state.kind  = PyUnicode_1BYTE_KIND;

    } else if (maxchar <= 0xFFFF) {
        ascii->state.ascii = 0;
        ascii->state.kind  = PyUnicode_2BYTE_KIND;

    } else {
        ascii->state.ascii = 0;
        ascii->state.kind  = PyUnicode_4BYTE_KIND;
    }

    /* Create storage for the code points and copy the data */
```

Excerpt shortened; the complete reviewed range 285–340 is in `data/cases.json`.

Closing lines 335–340 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L335-L340))

```
            /* No surrogates and 2BYTE_KIND, this means the unichar buffer
             * can be reused as storage for the python unicode string
             */
            ascii->length          = length;
            result->base.data.ucs2 = (Py_UCS2*)characters;
            characters             = NULL;
```

Lines 349–366 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L349-L366))

```
            result->base.data.ucs2 =
                PyMem_Malloc(sizeof(Py_UCS2) * (length + 1 - nr_surrogates));
            if (unlikely(result->base.data.ucs2 == NULL)) // LCOV_BR_EXCL_LINE
                goto error;                               // LCOV_EXCL_LINE

            ucs2_cur = result->base.data.ucs2;
            for (i = 0; i < length; i++) {
                if (Py_UNICODE_IS_HIGH_SURROGATE(characters[i]) && (i < length - 1)
                    && (Py_UNICODE_IS_LOW_SURROGATE(characters[i + 1]))) {
                    Py_UCS4 ch =
                        Py_UNICODE_JOIN_SURROGATES(characters[i], characters[i + 1]);
                    *ucs2_cur++ = (Py_UCS2)ch;
                    i++;
                } else {
                    *ucs2_cur++ = (Py_UCS2)characters[i];
                }
            }
            ascii->length = length - nr_surrogates;
```

Excerpt shortened; the complete reviewed range 349–417 is in `data/cases.json`.

Closing lines 412–417 ([verified immutable source](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/pyobjc_unicode.m#L412-L417))

```
#endif

        ascii->wstr          = (wchar_t*)result->base.data.ucs4;
        compact->wstr_length = ascii->length;
#endif
    } // LCOV_BR_EXCL_LINE
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz); archive SHA-256 `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.
