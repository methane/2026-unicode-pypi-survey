# frozendict 2.4.7

98 confirmed layout regions; 103 reviewed regions including non-direct context.

## L0927: _PyDict_CheckConsistency

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c:431–498`. SHA-256 `e3d6d3f04dfad62332dac09457c007102bf83db42ee05663f766d4e1eb3caadd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 431–448 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L431-L448))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
#define CHECK(expr) \
    do { if (!(expr)) { _PyObject_ASSERT_FAILED_MSG(op, Py_STRINGIFY(expr)); } } while (0)

    assert(op != NULL);
    CHECK(PyAnyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    CHECK(0 <= mp->ma_used && mp->ma_used <= usable);
    CHECK(IS_POWER_OF_2(keys->dk_size));
    CHECK(0 <= keys->dk_usable && keys->dk_usable <= usable);
    CHECK(0 <= keys->dk_nentries && keys->dk_nentries <= usable);
    CHECK(keys->dk_usable + keys->dk_nentries <= usable);
```

Excerpt shortened; the complete reviewed range 431–498 is in `data/cases.json`.

Closing lines 493–498 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L493-L498))

```
        }
    }
    return 1;

#undef CHECK
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0928: dict_subscript

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c:946–980`. SHA-256 `e3d6d3f04dfad62332dac09457c007102bf83db42ee05663f766d4e1eb3caadd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 946–963 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L946-L963))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyAnyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 946–980 is in `data/cases.json`.

Closing lines 975–980 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L975-L980))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0929: dict___contains__

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c:1015–1035`. SHA-256 `e3d6d3f04dfad62332dac09457c007102bf83db42ee05663f766d4e1eb3caadd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1015–1032 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L1015-L1032))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 1015–1035 is in `data/cases.json`.

Closing lines 1033–1035 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L1033-L1035))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0930: dict_get_impl

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c:1048–1069`. SHA-256 `e3d6d3f04dfad62332dac09457c007102bf83db42ee05663f766d4e1eb3caadd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1048–1065 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L1048-L1065))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 1048–1069 is in `data/cases.json`.

Closing lines 1066–1069 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L1066-L1069))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0931: d_PyDict_GetItemWithError

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c:1845–1869`. SHA-256 `e3d6d3f04dfad62332dac09457c007102bf83db42ee05663f766d4e1eb3caadd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1845–1862 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L1845-L1862))

```
d_PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyAnyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1845–1869 is in `data/cases.json`.

Closing lines 1864–1869 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject.c#L1864-L1869))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0932: _PyDict_CheckConsistency

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:495–562`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 495–512 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L495-L512))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
#define CHECK(expr) \
    do { if (!(expr)) { _PyObject_ASSERT_FAILED_MSG(op, Py_STRINGIFY(expr)); } } while (0)

    assert(op != NULL);
    CHECK(PyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    CHECK(0 <= mp->ma_used && mp->ma_used <= usable);
    CHECK(IS_POWER_OF_2(keys->dk_size));
    CHECK(0 <= keys->dk_usable && keys->dk_usable <= usable);
    CHECK(0 <= keys->dk_nentries && keys->dk_nentries <= usable);
    CHECK(keys->dk_usable + keys->dk_nentries <= usable);
```

Excerpt shortened; the complete reviewed range 495–562 is in `data/cases.json`.

Closing lines 557–562 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L557-L562))

```
        }
    }
    return 1;

#undef CHECK
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0933: PyDict_GetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1398–1438`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1398–1415 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1398-L1415))

```
PyDict_GetItem(PyObject *op, PyObject *key)
{
    if (!PyDict_Check(op)) {
        return NULL;
    }
    PyDictObject *mp = (PyDictObject *)op;

    Py_hash_t hash;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            PyErr_Clear();
            return NULL;
        }
    }

```

Excerpt shortened; the complete reviewed range 1398–1438 is in `data/cases.json`.

Closing lines 1433–1438 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1433-L1438))

```

    if (ix < 0) {
        return NULL;
    }
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0934: _PyDict_GetItemHint

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1441–1476`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1441–1458 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1441-L1458))

```
_PyDict_GetItemHint(PyDictObject *mp, PyObject *key,
                    Py_ssize_t hint, PyObject **value)
{
    assert(*value == NULL);
    assert(PyDict_CheckExact((PyObject*)mp));
    assert(PyUnicode_CheckExact(key));

    if (hint >= 0 && hint < mp->ma_keys->dk_nentries) {
        PyObject *res = NULL;

        PyDictKeyEntry *ep = DK_ENTRIES(mp->ma_keys) + (size_t)hint;
        if (ep->me_key == key) {
            if (mp->ma_keys->dk_lookup == lookdict_split) {
                assert(mp->ma_values != NULL);
                res = mp->ma_values[(size_t)hint];
            }
            else {
                res = ep->me_value;
```

Excerpt shortened; the complete reviewed range 1441–1476 is in `data/cases.json`.

Closing lines 1471–1476 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1471-L1476))

```
            return -1;
        }
    }

    return (mp->ma_keys->dk_lookup)(mp, key, hash, value);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0935: PyDict_GetItemWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1506–1530`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1506–1523 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1506-L1523))

```
PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1506–1530 is in `data/cases.json`.

Closing lines 1525–1530 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1525-L1530))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0936: _PyDict_GetItemIdWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1533–1542`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1533–1542 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1533-L1542))

```
_PyDict_GetItemIdWithError(PyObject *dp, struct _Py_Identifier *key)
{
    PyObject *kv;
    kv = _PyUnicode_FromId(key); /* borrowed */
    if (kv == NULL)
        return NULL;
    Py_hash_t hash = ((PyASCIIObject *) kv)->hash;
    assert (hash != -1);  /* interned strings have their hash value initialised */
    return _PyDict_GetItem_KnownHash(dp, kv, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0937: _PyDict_LoadGlobal

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1565–1591`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1565–1582 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1565-L1582))

```
_PyDict_LoadGlobal(PyDictObject *globals, PyDictObject *builtins, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }

    /* namespace 1: globals */
    ix = globals->ma_keys->dk_lookup(globals, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
```

Excerpt shortened; the complete reviewed range 1565–1591 is in `data/cases.json`.

Closing lines 1586–1591 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1586-L1591))

```
    /* namespace 2: builtins */
    ix = builtins->ma_keys->dk_lookup(builtins, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0938: PyDict_SetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1600–1624`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1600–1617 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1600-L1617))

```
PyDict_SetItem(PyObject *op, PyObject *key, PyObject *value)
{
    PyDictObject *mp;
    Py_hash_t hash;
    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    assert(key);
    assert(value);
    mp = (PyDictObject *)op;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }
```

Excerpt shortened; the complete reviewed range 1600–1624 is in `data/cases.json`.

Closing lines 1619–1624 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1619-L1624))

```
    if (mp->ma_keys == Py_EMPTY_KEYS) {
        return insert_to_emptydict(mp, key, hash, value);
    }
    /* insertdict() handles any resizing that might be necessary */
    return insertdict(mp, key, hash, value);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0939: PyDict_DelItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1674–1686`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1674–1686 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1674-L1686))

```
PyDict_DelItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    assert(key);
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }

    return _PyDict_DelItem_KnownHash(op, key, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0940: _PyDict_Pop

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:1944–1963`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1944–1961 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1944-L1961))

```
_PyDict_Pop(PyObject *dict, PyObject *key, PyObject *deflt)
{
    Py_hash_t hash;

    if (((PyDictObject *)dict)->ma_used == 0) {
        if (deflt) {
            Py_INCREF(deflt);
            return deflt;
        }
        _PyErr_SetKeyError(key);
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1944–1963 is in `data/cases.json`.

Closing lines 1962–1963 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L1962-L1963))

```
    return _PyDict_Pop_KnownHash(dict, key, hash, deflt);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0941: dict_subscript

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:2183–2217`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2183–2200 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L2183-L2200))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 2183–2217 is in `data/cases.json`.

Closing lines 2212–2217 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L2212-L2217))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0942: dict___contains__

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:2964–2984`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2964–2981 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L2964-L2981))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 2964–2984 is in `data/cases.json`.

Closing lines 2982–2984 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L2982-L2984))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0943: dict_get_impl

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:2997–3018`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2997–3014 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L2997-L3014))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 2997–3018 is in `data/cases.json`.

Closing lines 3015–3018 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L3015-L3018))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0944: PyDict_SetDefault

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:3021–3109`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 3021–3038 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L3021-L3038))

```
PyDict_SetDefault(PyObject *d, PyObject *key, PyObject *defaultobj)
{
    PyDictObject *mp = (PyDictObject *)d;
    PyObject *value;
    Py_hash_t hash;

    if (!PyDict_Check(d)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    if (mp->ma_keys == Py_EMPTY_KEYS) {
```

Excerpt shortened; the complete reviewed range 3021–3109 is in `data/cases.json`.

Closing lines 3104–3109 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L3104-L3109))

```
        mp->ma_version_tag = DICT_NEXT_VERSION();
    }

    ASSERT_CONSISTENT(mp);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0945: update

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c:3338–3528`. SHA-256 `05a05bee018d64d8f4369d818a0aaa9888ddf561377ab68e0f157d8da13dfcfd`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 3338–3355 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L3338-L3355))

```
"D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\n\
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\n\
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\n\
In either case, this is followed by: for k in F:  D[k] = F[k]");

PyDoc_STRVAR(clear__doc__,
"D.clear() -> None.  Remove all items from D.");

PyDoc_STRVAR(copy__doc__,
"D.copy() -> a shallow copy of D");

/* Forward */
static PyObject *dictkeys_new(PyObject *, PyObject *);
static PyObject *dictitems_new(PyObject *, PyObject *);
static PyObject *dictvalues_new(PyObject *, PyObject *);

PyDoc_STRVAR(keys__doc__,
             "D.keys() -> a set-like object providing a view on D's keys");
```

Excerpt shortened; the complete reviewed range 3338–3528 is in `data/cases.json`.

Closing lines 3523–3528 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/dictobject_original.c#L3523-L3528))

```
PyDoc_STRVAR(dictionary_doc,
"dict() -> new empty dictionary\n"
"dict(mapping) -> new dictionary initialized from a mapping object's\n"
"    (key, value) pairs\n"
"dict(iterable) -> new dictionary initialized as if via:\n"
"    d = {}\n"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0946: unicode_eq

**Classification:** non-direct context; project_source; `standard_unicode_api_types_only`.

**Purpose:** Aliases a/b are never accessed through -> members, sizeof or offsetof; only standard PyUnicode_GET_LENGTH/KIND/1BYTE_DATA macros consume them. Character/storage API dependency exists, but named struct here is solely type annotation/API cast.

**Migration effect:** Can change local variables to PyObject* without relying on Unicode struct members; changes to DATA/KIND APIs remain separate from named struct layout.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/cpython_src/Objects/stringlib/eq.h:7–25`. SHA-256 `c4fdd9e41f8748397cd3c0c5d5ecf77662b6c66c1cdd020d50b77fe9ddd1163c`.

**Activation / context:** Copied CPython helper in each version tree; included by adapted dictobject.c when that variant is selected.

Lines 7–24 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/stringlib/eq.h#L7-L24))

```
unicode_eq(PyObject *aa, PyObject *bb)
{
    assert(PyUnicode_Check(aa));
    assert(PyUnicode_Check(bb));
    assert(PyUnicode_IS_READY(aa));
    assert(PyUnicode_IS_READY(bb));

    PyUnicodeObject *a = (PyUnicodeObject *)aa;
    PyUnicodeObject *b = (PyUnicodeObject *)bb;

    if (PyUnicode_GET_LENGTH(a) != PyUnicode_GET_LENGTH(b))
        return 0;
    if (PyUnicode_GET_LENGTH(a) == 0)
        return 1;
    if (PyUnicode_KIND(a) != PyUnicode_KIND(b))
        return 0;
    return memcmp(PyUnicode_1BYTE_DATA(a), PyUnicode_1BYTE_DATA(b),
                  PyUnicode_GET_LENGTH(a) * PyUnicode_KIND(a)) == 0;
```

Excerpt shortened; the complete reviewed range 7–25 is in `data/cases.json`.

Closing lines 25–25 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/cpython_src/Objects/stringlib/eq.h#L25-L25))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0947: frozendict_setitem

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/frozendictobject.c:143–161`. SHA-256 `bfd0a550ee69bb5406e9a14bef64472aa82cbbcc906af217ddd515bad150a7d8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 143–160 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/frozendictobject.c#L143-L160))

```
static int frozendict_setitem(PyObject *op, 
                              PyObject *key, 
                              PyObject *value, 
                              int empty) {
    Py_hash_t hash;

    assert(key);
    assert(value);

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);

        if (hash == -1) {
            return -1;
        }
    }
    return frozendict_insert((PyDictObject*) op, key, hash, value, empty);
```

Excerpt shortened; the complete reviewed range 143–161 is in `data/cases.json`.

Closing lines 161–161 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/frozendictobject.c#L161-L161))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0948: dict_get_index

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_10/frozendictobject.c:877–888`. SHA-256 `bfd0a550ee69bb5406e9a14bef64472aa82cbbcc906af217ddd515bad150a7d8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 877–888 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_10/frozendictobject.c#L877-L888))

```
static Py_ssize_t dict_get_index(PyDictObject *self, PyObject *key) {
    Py_hash_t hash;
    PyObject* val;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return DKIX_ERROR;
    }
    return (self->ma_keys->dk_lookup) (self, key, hash, &val);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0949: _PyDict_CheckConsistency

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c:442–506`. SHA-256 `5fbe7e48171ad5ba8e1ad8922351b257c0212f6dbbfe14ac17eb2da29599b422`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 442–459 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L442-L459))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
    assert(op != NULL);
    assert(PyAnyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    assert(0 <= mp->ma_used && mp->ma_used <= usable);
    assert(IS_POWER_OF_2(keys->dk_size));
    assert(0 <= keys->dk_usable
           && keys->dk_usable <= usable);
    assert(0 <= keys->dk_nentries
           && keys->dk_nentries <= usable);
    assert(keys->dk_usable + keys->dk_nentries <= usable);

```

Excerpt shortened; the complete reviewed range 442–506 is in `data/cases.json`.

Closing lines 501–506 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L501-L506))

```
                assert(mp->ma_values[i] != NULL);
            }
        }
    }
    return 1;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0950: dict_subscript

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c:984–1021`. SHA-256 `5fbe7e48171ad5ba8e1ad8922351b257c0212f6dbbfe14ac17eb2da29599b422`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 984–1001 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L984-L1001))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    PyObject *v;
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject **value_addr;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value_addr, NULL);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || *value_addr == NULL) {
        if (!PyAnyDict_CheckExact(mp)) {
```

Excerpt shortened; the complete reviewed range 984–1021 is in `data/cases.json`.

Closing lines 1016–1021 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L1016-L1021))

```
        return NULL;
    }
    v = *value_addr;
    Py_INCREF(v);
    return v;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0951: dict___contains__

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c:1056–1076`. SHA-256 `5fbe7e48171ad5ba8e1ad8922351b257c0212f6dbbfe14ac17eb2da29599b422`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1056–1073 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L1056-L1073))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject **value_addr;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value_addr, NULL);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || *value_addr == NULL)
```

Excerpt shortened; the complete reviewed range 1056–1076 is in `data/cases.json`.

Closing lines 1074–1076 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L1074-L1076))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0952: dict_get

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c:1079–1108`. SHA-256 `5fbe7e48171ad5ba8e1ad8922351b257c0212f6dbbfe14ac17eb2da29599b422`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1079–1096 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L1079-L1096))

```
dict_get(PyDictObject *self, PyObject *args)
{
    PyObject *key;
    PyObject *default_value = Py_None;
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject **value_addr;

    if (!PyArg_UnpackTuple(args, "get", 1, 2, &key, &default_value))
        return NULL;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1079–1108 is in `data/cases.json`.

Closing lines 1103–1108 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L1103-L1108))

```
    else {
        val = *value_addr;
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0953: d_PyDict_GetItemWithError

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c:2031–2055`. SHA-256 `5fbe7e48171ad5ba8e1ad8922351b257c0212f6dbbfe14ac17eb2da29599b422`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 2031–2048 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L2031-L2048))

```
d_PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject **value_addr;

    if (!PyAnyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 2031–2055 is in `data/cases.json`.

Closing lines 2050–2055 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject.c#L2050-L2055))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value_addr, NULL);
    if (ix < 0)
        return NULL;
    return *value_addr;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0954: _PyDict_CheckConsistency

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:443–505`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 443–460 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L443-L460))

```
_PyDict_CheckConsistency(PyDictObject *mp)
{
    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);
#ifdef DEBUG_PYDICT
    PyDictKeyEntry *entries = DK_ENTRIES(keys);
    Py_ssize_t i;
#endif

    assert(0 <= mp->ma_used && mp->ma_used <= usable);
    assert(IS_POWER_OF_2(keys->dk_size));
    assert(0 <= keys->dk_usable
           && keys->dk_usable <= usable);
    assert(0 <= keys->dk_nentries
           && keys->dk_nentries <= usable);
    assert(keys->dk_usable + keys->dk_nentries <= usable);

```

Excerpt shortened; the complete reviewed range 443–505 is in `data/cases.json`.

Closing lines 500–505 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L500-L505))

```
        }
    }
#endif

    return 1;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0955: PyDict_GetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:1403–1447`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1403–1420 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1403-L1420))

```
PyDict_GetItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    Py_ssize_t ix;
    PyDictObject *mp = (PyDictObject *)op;
    PyThreadState *tstate;
    PyObject **value_addr;

    if (!PyDict_Check(op))
        return NULL;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            PyErr_Clear();
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1403–1447 is in `data/cases.json`.

Closing lines 1442–1447 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1442-L1447))

```
            PyErr_Clear();
            return NULL;
        }
    }
    return *value_addr;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0956: PyDict_GetItemWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:1477–1501`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1477–1494 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1477-L1494))

```
PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject **value_addr;

    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1477–1501 is in `data/cases.json`.

Closing lines 1496–1501 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1496-L1501))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value_addr, NULL);
    if (ix < 0)
        return NULL;
    return *value_addr;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0957: _PyDict_LoadGlobal

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:1521–1547`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1521–1538 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1521-L1538))

```
_PyDict_LoadGlobal(PyDictObject *globals, PyDictObject *builtins, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject **value_addr;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }

    /* namespace 1: globals */
    ix = globals->ma_keys->dk_lookup(globals, key, hash, &value_addr, NULL);
    if (ix == DKIX_ERROR)
        return NULL;
```

Excerpt shortened; the complete reviewed range 1521–1547 is in `data/cases.json`.

Closing lines 1542–1547 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1542-L1547))

```
    /* namespace 2: builtins */
    ix = builtins->ma_keys->dk_lookup(builtins, key, hash, &value_addr, NULL);
    if (ix < 0)
        return NULL;
    return *value_addr;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0958: PyDict_SetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:1556–1577`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1556–1573 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1556-L1573))

```
PyDict_SetItem(PyObject *op, PyObject *key, PyObject *value)
{
    PyDictObject *mp;
    Py_hash_t hash;
    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    assert(key);
    assert(value);
    mp = (PyDictObject *)op;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }
```

Excerpt shortened; the complete reviewed range 1556–1577 is in `data/cases.json`.

Closing lines 1574–1577 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1574-L1577))

```

    /* insertdict() handles any resizing that might be necessary */
    return insertdict(mp, key, hash, value);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0959: PyDict_DelItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:1623–1635`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1623–1635 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1623-L1635))

```
PyDict_DelItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    assert(key);
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }

    return _PyDict_DelItem_KnownHash(op, key, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0960: _PyDict_Pop

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:1893–1912`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1893–1910 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1893-L1910))

```
_PyDict_Pop(PyObject *dict, PyObject *key, PyObject *deflt)
{
    Py_hash_t hash;

    if (((PyDictObject *)dict)->ma_used == 0) {
        if (deflt) {
            Py_INCREF(deflt);
            return deflt;
        }
        _PyErr_SetKeyError(key);
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1893–1912 is in `data/cases.json`.

Closing lines 1911–1912 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L1911-L1912))

```
    return _PyDict_Pop_KnownHash(dict, key, hash, deflt);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0961: dict_subscript

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:2125–2162`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2125–2142 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2125-L2142))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    PyObject *v;
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject **value_addr;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value_addr, NULL);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || *value_addr == NULL) {
        if (!PyDict_CheckExact(mp)) {
```

Excerpt shortened; the complete reviewed range 2125–2162 is in `data/cases.json`.

Closing lines 2157–2162 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2157-L2162))

```
        return NULL;
    }
    v = *value_addr;
    Py_INCREF(v);
    return v;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0962: dict___contains__

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:2803–2823`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2803–2820 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2803-L2820))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=b852b2a19b51ab24]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject **value_addr;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value_addr, NULL);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || *value_addr == NULL)
```

Excerpt shortened; the complete reviewed range 2803–2823 is in `data/cases.json`.

Closing lines 2821–2823 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2821-L2823))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0963: dict_get

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:2826–2853`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2826–2843 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2826-L2843))

```
dict_get(PyDictObject *mp, PyObject *args)
{
    PyObject *key;
    PyObject *failobj = Py_None;
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject **value_addr;

    if (!PyArg_UnpackTuple(args, "get", 1, 2, &key, &failobj))
        return NULL;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 2826–2853 is in `data/cases.json`.

Closing lines 2848–2853 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2848-L2853))

```
        val = failobj;
    else
        val = *value_addr;
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0964: PyDict_SetDefault

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:2856–2941`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2856–2873 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2856-L2873))

```
PyDict_SetDefault(PyObject *d, PyObject *key, PyObject *defaultobj)
{
    PyDictObject *mp = (PyDictObject *)d;
    PyObject *value;
    Py_hash_t hash;
    Py_ssize_t hashpos, ix;
    PyObject **value_addr;

    if (!PyDict_Check(d)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
```

Excerpt shortened; the complete reviewed range 2856–2941 is in `data/cases.json`.

Closing lines 2936–2941 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L2936-L2941))

```
        value = *value_addr;
    }

    assert(_PyDict_CheckConsistency(mp));
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0965: update

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c:3129–3275`. SHA-256 `e711bce02d0db5bfffa7b3153c36142e4c9363f991d8fa673dd88698c0ab763b`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 3129–3146 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L3129-L3146))

```
"D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\n\
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\n\
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\n\
In either case, this is followed by: for k in F:  D[k] = F[k]");

PyDoc_STRVAR(clear__doc__,
"D.clear() -> None.  Remove all items from D.");

PyDoc_STRVAR(copy__doc__,
"D.copy() -> a shallow copy of D");

/* Forward */
static PyObject *dictkeys_new(PyObject *);
static PyObject *dictitems_new(PyObject *);
static PyObject *dictvalues_new(PyObject *);

PyDoc_STRVAR(keys__doc__,
             "D.keys() -> a set-like object providing a view on D's keys");
```

Excerpt shortened; the complete reviewed range 3129–3275 is in `data/cases.json`.

Closing lines 3270–3275 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/dictobject_original.c#L3270-L3275))

```
PyDoc_STRVAR(dictionary_doc,
"dict() -> new empty dictionary\n"
"dict(mapping) -> new dictionary initialized from a mapping object's\n"
"    (key, value) pairs\n"
"dict(iterable) -> new dictionary initialized as if via:\n"
"    d = {}\n"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0966: unicode_eq

**Classification:** non-direct context; project_source; `standard_unicode_api_types_only`.

**Purpose:** Aliases a/b are never accessed through -> members, sizeof or offsetof; only standard PyUnicode_GET_LENGTH/KIND/1BYTE_DATA macros consume them. Character/storage API dependency exists, but named struct here is solely type annotation/API cast.

**Migration effect:** Can change local variables to PyObject* without relying on Unicode struct members; changes to DATA/KIND APIs remain separate from named struct layout.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/cpython_src/Objects/stringlib/eq.h:7–25`. SHA-256 `a4a6edf00d3150dc61a980708568d2de394aa5749a99e3b320428cd334ee4ef0`.

**Activation / context:** Copied CPython helper in each version tree; included by adapted dictobject.c when that variant is selected.

Lines 7–24 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/stringlib/eq.h#L7-L24))

```
unicode_eq(PyObject *aa, PyObject *bb)
{
    assert(PyUnicode_Check(aa));
    assert(PyUnicode_Check(bb));
    assert(! PyUnicode_READY(aa));
    assert(! PyUnicode_READY(bb));
    
    PyUnicodeObject *a = (PyUnicodeObject *)aa;
    PyUnicodeObject *b = (PyUnicodeObject *)bb;

    if (PyUnicode_GET_LENGTH(a) != PyUnicode_GET_LENGTH(b))
        return 0;
    if (PyUnicode_GET_LENGTH(a) == 0)
        return 1;
    if (PyUnicode_KIND(a) != PyUnicode_KIND(b))
        return 0;
    return memcmp(PyUnicode_1BYTE_DATA(a), PyUnicode_1BYTE_DATA(b),
                  PyUnicode_GET_LENGTH(a) * PyUnicode_KIND(a)) == 0;
```

Excerpt shortened; the complete reviewed range 7–25 is in `data/cases.json`.

Closing lines 25–25 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/cpython_src/Objects/stringlib/eq.h#L25-L25))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0967: frozendict_setitem

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/frozendictobject.c:154–172`. SHA-256 `b7acef0f45832277519517a0c1755a03369c8a46ad3acc202706bc288adbb879`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 154–171 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/frozendictobject.c#L154-L171))

```
static int frozendict_setitem(PyObject *op, 
                              PyObject *key, 
                              PyObject *value, 
                              int empty) {
    Py_hash_t hash;

    assert(key);
    assert(value);

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);

        if (hash == -1) {
            return -1;
        }
    }
    return frozendict_insert((PyDictObject*) op, key, hash, value, empty);
```

Excerpt shortened; the complete reviewed range 154–172 is in `data/cases.json`.

Closing lines 172–172 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/frozendictobject.c#L172-L172))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0968: dict_get_index

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_6/frozendictobject.c:889–900`. SHA-256 `b7acef0f45832277519517a0c1755a03369c8a46ad3acc202706bc288adbb879`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 889–900 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_6/frozendictobject.c#L889-L900))

```
static Py_ssize_t dict_get_index(PyDictObject *self, PyObject *key) {
    Py_hash_t hash;
    PyObject** val;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return DKIX_ERROR;
    }
    return (self->ma_keys->dk_lookup) (self, key, hash, &val, NULL);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0969: _PyDict_CheckConsistency

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c:440–504`. SHA-256 `f0582bce07a2f43533ec90b484f561fd5960a6a5b2eb297c22d1e283fb8502a5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 440–457 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L440-L457))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
    assert(op != NULL);
    assert(PyAnyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    assert(0 <= mp->ma_used && mp->ma_used <= usable);
    assert(IS_POWER_OF_2(keys->dk_size));
    assert(0 <= keys->dk_usable
           && keys->dk_usable <= usable);
    assert(0 <= keys->dk_nentries
           && keys->dk_nentries <= usable);
    assert(keys->dk_usable + keys->dk_nentries <= usable);

```

Excerpt shortened; the complete reviewed range 440–504 is in `data/cases.json`.

Closing lines 499–504 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L499-L504))

```
                assert(mp->ma_values[i] != NULL);
            }
        }
    }
    return 1;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0970: dict_subscript

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c:970–1005`. SHA-256 `f0582bce07a2f43533ec90b484f561fd5960a6a5b2eb297c22d1e283fb8502a5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 970–987 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L970-L987))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyAnyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 970–1005 is in `data/cases.json`.

Closing lines 1000–1005 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L1000-L1005))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0971: dict___contains__

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c:1040–1060`. SHA-256 `f0582bce07a2f43533ec90b484f561fd5960a6a5b2eb297c22d1e283fb8502a5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1040–1057 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L1040-L1057))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 1040–1060 is in `data/cases.json`.

Closing lines 1058–1060 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L1058-L1060))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0972: dict_get_impl

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c:1073–1094`. SHA-256 `f0582bce07a2f43533ec90b484f561fd5960a6a5b2eb297c22d1e283fb8502a5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1073–1090 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L1073-L1090))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 1073–1094 is in `data/cases.json`.

Closing lines 1091–1094 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L1091-L1094))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0973: d_PyDict_GetItemWithError

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c:1997–2021`. SHA-256 `f0582bce07a2f43533ec90b484f561fd5960a6a5b2eb297c22d1e283fb8502a5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1997–2014 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L1997-L2014))

```
d_PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyAnyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1997–2021 is in `data/cases.json`.

Closing lines 2016–2021 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject.c#L2016-L2021))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0974: _PyDict_CheckConsistency

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:440–502`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 440–457 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L440-L457))

```
_PyDict_CheckConsistency(PyDictObject *mp)
{
    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);
#ifdef DEBUG_PYDICT
    PyDictKeyEntry *entries = DK_ENTRIES(keys);
    Py_ssize_t i;
#endif

    assert(0 <= mp->ma_used && mp->ma_used <= usable);
    assert(IS_POWER_OF_2(keys->dk_size));
    assert(0 <= keys->dk_usable
           && keys->dk_usable <= usable);
    assert(0 <= keys->dk_nentries
           && keys->dk_nentries <= usable);
    assert(keys->dk_usable + keys->dk_nentries <= usable);

```

Excerpt shortened; the complete reviewed range 440–502 is in `data/cases.json`.

Closing lines 497–502 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L497-L502))

```
        }
    }
#endif

    return 1;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0975: PyDict_GetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:1290–1334`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1290–1307 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1290-L1307))

```
PyDict_GetItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    Py_ssize_t ix;
    PyDictObject *mp = (PyDictObject *)op;
    PyThreadState *tstate;
    PyObject *value;

    if (!PyDict_Check(op))
        return NULL;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            PyErr_Clear();
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1290–1334 is in `data/cases.json`.

Closing lines 1329–1334 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1329-L1334))

```
            PyErr_Clear();
            return NULL;
        }
    }
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0976: PyDict_GetItemWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:1364–1388`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1364–1381 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1364-L1381))

```
PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1364–1388 is in `data/cases.json`.

Closing lines 1383–1388 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1383-L1388))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0977: _PyDict_LoadGlobal

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:1408–1434`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1408–1425 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1408-L1425))

```
_PyDict_LoadGlobal(PyDictObject *globals, PyDictObject *builtins, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }

    /* namespace 1: globals */
    ix = globals->ma_keys->dk_lookup(globals, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
```

Excerpt shortened; the complete reviewed range 1408–1434 is in `data/cases.json`.

Closing lines 1429–1434 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1429-L1434))

```
    /* namespace 2: builtins */
    ix = builtins->ma_keys->dk_lookup(builtins, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0978: PyDict_SetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:1443–1464`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1443–1460 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1443-L1460))

```
PyDict_SetItem(PyObject *op, PyObject *key, PyObject *value)
{
    PyDictObject *mp;
    Py_hash_t hash;
    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    assert(key);
    assert(value);
    mp = (PyDictObject *)op;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }
```

Excerpt shortened; the complete reviewed range 1443–1464 is in `data/cases.json`.

Closing lines 1461–1464 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1461-L1464))

```

    /* insertdict() handles any resizing that might be necessary */
    return insertdict(mp, key, hash, value);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0979: PyDict_DelItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:1511–1523`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1511–1523 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1511-L1523))

```
PyDict_DelItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    assert(key);
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }

    return _PyDict_DelItem_KnownHash(op, key, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0980: _PyDict_Pop

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:1781–1800`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1781–1798 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1781-L1798))

```
_PyDict_Pop(PyObject *dict, PyObject *key, PyObject *deflt)
{
    Py_hash_t hash;

    if (((PyDictObject *)dict)->ma_used == 0) {
        if (deflt) {
            Py_INCREF(deflt);
            return deflt;
        }
        _PyErr_SetKeyError(key);
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1781–1800 is in `data/cases.json`.

Closing lines 1799–1800 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L1799-L1800))

```
    return _PyDict_Pop_KnownHash(dict, key, hash, deflt);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0981: dict_subscript

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:2013–2048`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2013–2030 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2013-L2030))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 2013–2048 is in `data/cases.json`.

Closing lines 2043–2048 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2043-L2048))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0982: dict___contains__

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:2725–2745`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2725–2742 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2725-L2742))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 2725–2745 is in `data/cases.json`.

Closing lines 2743–2745 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2743-L2745))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0983: dict_get_impl

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:2758–2779`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2758–2775 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2758-L2775))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 2758–2779 is in `data/cases.json`.

Closing lines 2776–2779 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2776-L2779))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0984: PyDict_SetDefault

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:2782–2861`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2782–2799 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2782-L2799))

```
PyDict_SetDefault(PyObject *d, PyObject *key, PyObject *defaultobj)
{
    PyDictObject *mp = (PyDictObject *)d;
    PyObject *value;
    Py_hash_t hash;

    if (!PyDict_Check(d)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }

```

Excerpt shortened; the complete reviewed range 2782–2861 is in `data/cases.json`.

Closing lines 2856–2861 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L2856-L2861))

```
        mp->ma_version_tag = DICT_NEXT_VERSION();
    }

    assert(_PyDict_CheckConsistency(mp));
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0985: update

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c:3053–3197`. SHA-256 `fd7d64f8ee6d263cec98f289afa920709b1c5f0344e0c8f8c37fa407a373eeb5`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 3053–3070 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L3053-L3070))

```
"D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\n\
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\n\
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\n\
In either case, this is followed by: for k in F:  D[k] = F[k]");

PyDoc_STRVAR(clear__doc__,
"D.clear() -> None.  Remove all items from D.");

PyDoc_STRVAR(copy__doc__,
"D.copy() -> a shallow copy of D");

/* Forward */
static PyObject *dictkeys_new(PyObject *);
static PyObject *dictitems_new(PyObject *);
static PyObject *dictvalues_new(PyObject *);

PyDoc_STRVAR(keys__doc__,
             "D.keys() -> a set-like object providing a view on D's keys");
```

Excerpt shortened; the complete reviewed range 3053–3197 is in `data/cases.json`.

Closing lines 3192–3197 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/dictobject_original.c#L3192-L3197))

```
PyDoc_STRVAR(dictionary_doc,
"dict() -> new empty dictionary\n"
"dict(mapping) -> new dictionary initialized from a mapping object's\n"
"    (key, value) pairs\n"
"dict(iterable) -> new dictionary initialized as if via:\n"
"    d = {}\n"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0986: unicode_eq

**Classification:** non-direct context; project_source; `standard_unicode_api_types_only`.

**Purpose:** Aliases a/b are never accessed through -> members, sizeof or offsetof; only standard PyUnicode_GET_LENGTH/KIND/1BYTE_DATA macros consume them. Character/storage API dependency exists, but named struct here is solely type annotation/API cast.

**Migration effect:** Can change local variables to PyObject* without relying on Unicode struct members; changes to DATA/KIND APIs remain separate from named struct layout.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/cpython_src/Objects/stringlib/eq.h:7–25`. SHA-256 `a4a6edf00d3150dc61a980708568d2de394aa5749a99e3b320428cd334ee4ef0`.

**Activation / context:** Copied CPython helper in each version tree; included by adapted dictobject.c when that variant is selected.

Lines 7–24 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/stringlib/eq.h#L7-L24))

```
unicode_eq(PyObject *aa, PyObject *bb)
{
    assert(PyUnicode_Check(aa));
    assert(PyUnicode_Check(bb));
    assert(! PyUnicode_READY(aa));
    assert(! PyUnicode_READY(bb));
    
    PyUnicodeObject *a = (PyUnicodeObject *)aa;
    PyUnicodeObject *b = (PyUnicodeObject *)bb;

    if (PyUnicode_GET_LENGTH(a) != PyUnicode_GET_LENGTH(b))
        return 0;
    if (PyUnicode_GET_LENGTH(a) == 0)
        return 1;
    if (PyUnicode_KIND(a) != PyUnicode_KIND(b))
        return 0;
    return memcmp(PyUnicode_1BYTE_DATA(a), PyUnicode_1BYTE_DATA(b),
                  PyUnicode_GET_LENGTH(a) * PyUnicode_KIND(a)) == 0;
```

Excerpt shortened; the complete reviewed range 7–25 is in `data/cases.json`.

Closing lines 25–25 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/cpython_src/Objects/stringlib/eq.h#L25-L25))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0987: frozendict_setitem

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/frozendictobject.c:149–167`. SHA-256 `24a6db969aa920b148c645857c42d7f7fd1f7fd19f5a4f78739fd971285410af`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 149–166 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/frozendictobject.c#L149-L166))

```
static int frozendict_setitem(PyObject *op, 
                              PyObject *key, 
                              PyObject *value, 
                              int empty) {
    Py_hash_t hash;

    assert(key);
    assert(value);

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);

        if (hash == -1) {
            return -1;
        }
    }
    return frozendict_insert((PyDictObject*) op, key, hash, value, empty);
```

Excerpt shortened; the complete reviewed range 149–167 is in `data/cases.json`.

Closing lines 167–167 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/frozendictobject.c#L167-L167))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0988: dict_get_index

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_7/frozendictobject.c:883–894`. SHA-256 `24a6db969aa920b148c645857c42d7f7fd1f7fd19f5a4f78739fd971285410af`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 883–894 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_7/frozendictobject.c#L883-L894))

```
static Py_ssize_t dict_get_index(PyDictObject *self, PyObject *key) {
    Py_hash_t hash;
    PyObject* val;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return DKIX_ERROR;
    }
    return (self->ma_keys->dk_lookup) (self, key, hash, &val);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0989: _PyDict_CheckConsistency

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c:439–506`. SHA-256 `018d83ebb8308e61287b3b7c28ec1367cb9bcabc5f9514030dd58647a095a88e`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 439–456 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L439-L456))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
#define CHECK(expr) \
    do { if (!(expr)) { _PyObject_ASSERT_FAILED_MSG(op, Py_STRINGIFY(expr)); } } while (0)

    assert(op != NULL);
    CHECK(PyAnyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    CHECK(0 <= mp->ma_used && mp->ma_used <= usable);
    CHECK(IS_POWER_OF_2(keys->dk_size));
    CHECK(0 <= keys->dk_usable && keys->dk_usable <= usable);
    CHECK(0 <= keys->dk_nentries && keys->dk_nentries <= usable);
    CHECK(keys->dk_usable + keys->dk_nentries <= usable);
```

Excerpt shortened; the complete reviewed range 439–506 is in `data/cases.json`.

Closing lines 501–506 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L501-L506))

```
        }
    }
    return 1;

#undef CHECK
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0990: dict_subscript

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c:971–1006`. SHA-256 `018d83ebb8308e61287b3b7c28ec1367cb9bcabc5f9514030dd58647a095a88e`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 971–988 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L971-L988))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyAnyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 971–1006 is in `data/cases.json`.

Closing lines 1001–1006 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1001-L1006))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0991: dict___contains__

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c:1041–1061`. SHA-256 `018d83ebb8308e61287b3b7c28ec1367cb9bcabc5f9514030dd58647a095a88e`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1041–1058 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1041-L1058))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 1041–1061 is in `data/cases.json`.

Closing lines 1059–1061 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1059-L1061))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0992: dict_get_impl

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c:1074–1095`. SHA-256 `018d83ebb8308e61287b3b7c28ec1367cb9bcabc5f9514030dd58647a095a88e`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1074–1091 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1074-L1091))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 1074–1095 is in `data/cases.json`.

Closing lines 1092–1095 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1092-L1095))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0993: d_PyDict_GetItemWithError

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c:1869–1893`. SHA-256 `018d83ebb8308e61287b3b7c28ec1367cb9bcabc5f9514030dd58647a095a88e`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1869–1886 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1869-L1886))

```
d_PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyAnyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1869–1893 is in `data/cases.json`.

Closing lines 1888–1893 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject.c#L1888-L1893))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0994: _PyDict_CheckConsistency

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:460–527`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 460–477 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L460-L477))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
#define CHECK(expr) \
    do { if (!(expr)) { _PyObject_ASSERT_FAILED_MSG(op, Py_STRINGIFY(expr)); } } while (0)

    assert(op != NULL);
    CHECK(PyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    CHECK(0 <= mp->ma_used && mp->ma_used <= usable);
    CHECK(IS_POWER_OF_2(keys->dk_size));
    CHECK(0 <= keys->dk_usable && keys->dk_usable <= usable);
    CHECK(0 <= keys->dk_nentries && keys->dk_nentries <= usable);
    CHECK(keys->dk_usable + keys->dk_nentries <= usable);
```

Excerpt shortened; the complete reviewed range 460–527 is in `data/cases.json`.

Closing lines 522–527 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L522-L527))

```
        }
    }
    return 1;

#undef CHECK
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0995: PyDict_GetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:1356–1400`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1356–1373 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1356-L1373))

```
PyDict_GetItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    Py_ssize_t ix;
    PyDictObject *mp = (PyDictObject *)op;
    PyThreadState *tstate;
    PyObject *value;

    if (!PyDict_Check(op))
        return NULL;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            PyErr_Clear();
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1356–1400 is in `data/cases.json`.

Closing lines 1395–1400 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1395-L1400))

```
            PyErr_Clear();
            return NULL;
        }
    }
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0996: PyDict_GetItemWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:1430–1454`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1430–1447 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1430-L1447))

```
PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1430–1454 is in `data/cases.json`.

Closing lines 1449–1454 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1449-L1454))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0997: _PyDict_LoadGlobal

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:1487–1513`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1487–1504 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1487-L1504))

```
_PyDict_LoadGlobal(PyDictObject *globals, PyDictObject *builtins, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }

    /* namespace 1: globals */
    ix = globals->ma_keys->dk_lookup(globals, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
```

Excerpt shortened; the complete reviewed range 1487–1513 is in `data/cases.json`.

Closing lines 1508–1513 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1508-L1513))

```
    /* namespace 2: builtins */
    ix = builtins->ma_keys->dk_lookup(builtins, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0998: PyDict_SetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:1522–1546`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1522–1539 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1522-L1539))

```
PyDict_SetItem(PyObject *op, PyObject *key, PyObject *value)
{
    PyDictObject *mp;
    Py_hash_t hash;
    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    assert(key);
    assert(value);
    mp = (PyDictObject *)op;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }
```

Excerpt shortened; the complete reviewed range 1522–1546 is in `data/cases.json`.

Closing lines 1541–1546 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1541-L1546))

```
    if (mp->ma_keys == Py_EMPTY_KEYS) {
        return insert_to_emptydict(mp, key, hash, value);
    }
    /* insertdict() handles any resizing that might be necessary */
    return insertdict(mp, key, hash, value);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L0999: PyDict_DelItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:1596–1608`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1596–1608 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1596-L1608))

```
PyDict_DelItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    assert(key);
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }

    return _PyDict_DelItem_KnownHash(op, key, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1000: _PyDict_Pop

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:1866–1885`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1866–1883 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1866-L1883))

```
_PyDict_Pop(PyObject *dict, PyObject *key, PyObject *deflt)
{
    Py_hash_t hash;

    if (((PyDictObject *)dict)->ma_used == 0) {
        if (deflt) {
            Py_INCREF(deflt);
            return deflt;
        }
        _PyErr_SetKeyError(key);
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1866–1885 is in `data/cases.json`.

Closing lines 1884–1885 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L1884-L1885))

```
    return _PyDict_Pop_KnownHash(dict, key, hash, deflt);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1001: dict_subscript

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:2098–2133`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2098–2115 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2098-L2115))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 2098–2133 is in `data/cases.json`.

Closing lines 2128–2133 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2128-L2133))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1002: dict___contains__

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:2821–2841`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2821–2838 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2821-L2838))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 2821–2841 is in `data/cases.json`.

Closing lines 2839–2841 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2839-L2841))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1003: dict_get_impl

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:2854–2875`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2854–2871 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2854-L2871))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 2854–2875 is in `data/cases.json`.

Closing lines 2872–2875 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2872-L2875))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1004: PyDict_SetDefault

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:2878–2963`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2878–2895 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2878-L2895))

```
PyDict_SetDefault(PyObject *d, PyObject *key, PyObject *defaultobj)
{
    PyDictObject *mp = (PyDictObject *)d;
    PyObject *value;
    Py_hash_t hash;

    if (!PyDict_Check(d)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    if (mp->ma_keys == Py_EMPTY_KEYS) {
```

Excerpt shortened; the complete reviewed range 2878–2963 is in `data/cases.json`.

Closing lines 2958–2963 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L2958-L2963))

```
        mp->ma_version_tag = DICT_NEXT_VERSION();
    }

    ASSERT_CONSISTENT(mp);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1005: update

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c:3178–3321`. SHA-256 `0687e8ddecead09574714dfee176badda140bc23f0298bd57b73b280c6e70846`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 3178–3195 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L3178-L3195))

```
"D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\n\
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\n\
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\n\
In either case, this is followed by: for k in F:  D[k] = F[k]");

PyDoc_STRVAR(clear__doc__,
"D.clear() -> None.  Remove all items from D.");

PyDoc_STRVAR(copy__doc__,
"D.copy() -> a shallow copy of D");

/* Forward */
static PyObject *dictkeys_new(PyObject *, PyObject *);
static PyObject *dictitems_new(PyObject *, PyObject *);
static PyObject *dictvalues_new(PyObject *, PyObject *);

PyDoc_STRVAR(keys__doc__,
             "D.keys() -> a set-like object providing a view on D's keys");
```

Excerpt shortened; the complete reviewed range 3178–3321 is in `data/cases.json`.

Closing lines 3316–3321 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/dictobject_original.c#L3316-L3321))

```
PyDoc_STRVAR(dictionary_doc,
"dict() -> new empty dictionary\n"
"dict(mapping) -> new dictionary initialized from a mapping object's\n"
"    (key, value) pairs\n"
"dict(iterable) -> new dictionary initialized as if via:\n"
"    d = {}\n"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1006: unicode_eq

**Classification:** non-direct context; project_source; `standard_unicode_api_types_only`.

**Purpose:** Aliases a/b are never accessed through -> members, sizeof or offsetof; only standard PyUnicode_GET_LENGTH/KIND/1BYTE_DATA macros consume them. Character/storage API dependency exists, but named struct here is solely type annotation/API cast.

**Migration effect:** Can change local variables to PyObject* without relying on Unicode struct members; changes to DATA/KIND APIs remain separate from named struct layout.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/cpython_src/Objects/stringlib/eq.h:7–25`. SHA-256 `a4a6edf00d3150dc61a980708568d2de394aa5749a99e3b320428cd334ee4ef0`.

**Activation / context:** Copied CPython helper in each version tree; included by adapted dictobject.c when that variant is selected.

Lines 7–24 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/stringlib/eq.h#L7-L24))

```
unicode_eq(PyObject *aa, PyObject *bb)
{
    assert(PyUnicode_Check(aa));
    assert(PyUnicode_Check(bb));
    assert(! PyUnicode_READY(aa));
    assert(! PyUnicode_READY(bb));
    
    PyUnicodeObject *a = (PyUnicodeObject *)aa;
    PyUnicodeObject *b = (PyUnicodeObject *)bb;

    if (PyUnicode_GET_LENGTH(a) != PyUnicode_GET_LENGTH(b))
        return 0;
    if (PyUnicode_GET_LENGTH(a) == 0)
        return 1;
    if (PyUnicode_KIND(a) != PyUnicode_KIND(b))
        return 0;
    return memcmp(PyUnicode_1BYTE_DATA(a), PyUnicode_1BYTE_DATA(b),
                  PyUnicode_GET_LENGTH(a) * PyUnicode_KIND(a)) == 0;
```

Excerpt shortened; the complete reviewed range 7–25 is in `data/cases.json`.

Closing lines 25–25 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/cpython_src/Objects/stringlib/eq.h#L25-L25))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1007: frozendict_setitem

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/frozendictobject.c:149–167`. SHA-256 `57e831f8b2f8329f7467871e2bdf3446cbb23823d44a115d6979ea0aa37f8fde`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 149–166 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/frozendictobject.c#L149-L166))

```
static int frozendict_setitem(PyObject *op, 
                              PyObject *key, 
                              PyObject *value, 
                              int empty) {
    Py_hash_t hash;

    assert(key);
    assert(value);

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);

        if (hash == -1) {
            return -1;
        }
    }
    return frozendict_insert((PyDictObject*) op, key, hash, value, empty);
```

Excerpt shortened; the complete reviewed range 149–167 is in `data/cases.json`.

Closing lines 167–167 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/frozendictobject.c#L167-L167))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1008: dict_get_index

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_8/frozendictobject.c:883–894`. SHA-256 `57e831f8b2f8329f7467871e2bdf3446cbb23823d44a115d6979ea0aa37f8fde`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 883–894 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_8/frozendictobject.c#L883-L894))

```
static Py_ssize_t dict_get_index(PyDictObject *self, PyObject *key) {
    Py_hash_t hash;
    PyObject* val;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return DKIX_ERROR;
    }
    return (self->ma_keys->dk_lookup) (self, key, hash, &val);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1009: _PyDict_CheckConsistency

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c:443–510`. SHA-256 `09dbf28862a342ede84fc4774c67e086a57388fa104b32bbf85daa5d692005f0`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 443–460 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L443-L460))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
#define CHECK(expr) \
    do { if (!(expr)) { _PyObject_ASSERT_FAILED_MSG(op, Py_STRINGIFY(expr)); } } while (0)

    assert(op != NULL);
    CHECK(PyAnyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    CHECK(0 <= mp->ma_used && mp->ma_used <= usable);
    CHECK(IS_POWER_OF_2(keys->dk_size));
    CHECK(0 <= keys->dk_usable && keys->dk_usable <= usable);
    CHECK(0 <= keys->dk_nentries && keys->dk_nentries <= usable);
    CHECK(keys->dk_usable + keys->dk_nentries <= usable);
```

Excerpt shortened; the complete reviewed range 443–510 is in `data/cases.json`.

Closing lines 505–510 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L505-L510))

```
        }
    }
    return 1;

#undef CHECK
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1010: dict_subscript

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c:978–1012`. SHA-256 `09dbf28862a342ede84fc4774c67e086a57388fa104b32bbf85daa5d692005f0`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 978–995 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L978-L995))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyAnyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 978–1012 is in `data/cases.json`.

Closing lines 1007–1012 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1007-L1012))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1011: dict___contains__

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c:1047–1067`. SHA-256 `09dbf28862a342ede84fc4774c67e086a57388fa104b32bbf85daa5d692005f0`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1047–1064 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1047-L1064))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 1047–1067 is in `data/cases.json`.

Closing lines 1065–1067 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1065-L1067))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1012: dict_get_impl

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c:1080–1101`. SHA-256 `09dbf28862a342ede84fc4774c67e086a57388fa104b32bbf85daa5d692005f0`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1080–1097 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1080-L1097))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 1080–1101 is in `data/cases.json`.

Closing lines 1098–1101 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1098-L1101))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1013: d_PyDict_GetItemWithError

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c:1877–1901`. SHA-256 `09dbf28862a342ede84fc4774c67e086a57388fa104b32bbf85daa5d692005f0`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 1877–1894 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1877-L1894))

```
d_PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyAnyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1877–1901 is in `data/cases.json`.

Closing lines 1896–1901 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject.c#L1896-L1901))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1014: _PyDict_CheckConsistency

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:469–536`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline. Hash field occurs in check_content branch; DEBUG_PYDICT enables content assertions, normal ASSERT_CONSISTENT passes0, NDEBUG can remove assertion callers.

Lines 469–486 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L469-L486))

```
_PyDict_CheckConsistency(PyObject *op, int check_content)
{
#define CHECK(expr) \
    do { if (!(expr)) { _PyObject_ASSERT_FAILED_MSG(op, Py_STRINGIFY(expr)); } } while (0)

    assert(op != NULL);
    CHECK(PyDict_Check(op));
    PyDictObject *mp = (PyDictObject *)op;

    PyDictKeysObject *keys = mp->ma_keys;
    int splitted = _PyDict_HasSplitTable(mp);
    Py_ssize_t usable = USABLE_FRACTION(keys->dk_size);

    CHECK(0 <= mp->ma_used && mp->ma_used <= usable);
    CHECK(IS_POWER_OF_2(keys->dk_size));
    CHECK(0 <= keys->dk_usable && keys->dk_usable <= usable);
    CHECK(0 <= keys->dk_nentries && keys->dk_nentries <= usable);
    CHECK(keys->dk_usable + keys->dk_nentries <= usable);
```

Excerpt shortened; the complete reviewed range 469–536 is in `data/cases.json`.

Closing lines 531–536 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L531-L536))

```
        }
    }
    return 1;

#undef CHECK
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1015: PyDict_GetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1382–1426`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1382–1399 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1382-L1399))

```
PyDict_GetItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    Py_ssize_t ix;
    PyDictObject *mp = (PyDictObject *)op;
    PyThreadState *tstate;
    PyObject *value;

    if (!PyDict_Check(op))
        return NULL;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            PyErr_Clear();
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1382–1426 is in `data/cases.json`.

Closing lines 1421–1426 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1421-L1426))

```
            PyErr_Clear();
            return NULL;
        }
    }
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1016: PyDict_GetItemWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1456–1480`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1456–1473 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1456-L1473))

```
PyDict_GetItemWithError(PyObject *op, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyDictObject*mp = (PyDictObject *)op;
    PyObject *value;

    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1) {
            return NULL;
        }
```

Excerpt shortened; the complete reviewed range 1456–1480 is in `data/cases.json`.

Closing lines 1475–1480 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1475-L1480))

```

    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1017: _PyDict_GetItemIdWithError

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1483–1492`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1483–1492 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1483-L1492))

```
_PyDict_GetItemIdWithError(PyObject *dp, struct _Py_Identifier *key)
{
    PyObject *kv;
    kv = _PyUnicode_FromId(key); /* borrowed */
    if (kv == NULL)
        return NULL;
    Py_hash_t hash = ((PyASCIIObject *) kv)->hash;
    assert (hash != -1);  /* interned strings have their hash value initialised */
    return _PyDict_GetItem_KnownHash(dp, kv, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1018: _PyDict_LoadGlobal

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1515–1541`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1515–1532 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1515-L1532))

```
_PyDict_LoadGlobal(PyDictObject *globals, PyDictObject *builtins, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }

    /* namespace 1: globals */
    ix = globals->ma_keys->dk_lookup(globals, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
```

Excerpt shortened; the complete reviewed range 1515–1541 is in `data/cases.json`.

Closing lines 1536–1541 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1536-L1541))

```
    /* namespace 2: builtins */
    ix = builtins->ma_keys->dk_lookup(builtins, key, hash, &value);
    if (ix < 0)
        return NULL;
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1019: PyDict_SetItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1550–1574`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1550–1567 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1550-L1567))

```
PyDict_SetItem(PyObject *op, PyObject *key, PyObject *value)
{
    PyDictObject *mp;
    Py_hash_t hash;
    if (!PyDict_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    assert(key);
    assert(value);
    mp = (PyDictObject *)op;
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1)
    {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }
```

Excerpt shortened; the complete reviewed range 1550–1574 is in `data/cases.json`.

Closing lines 1569–1574 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1569-L1574))

```
    if (mp->ma_keys == Py_EMPTY_KEYS) {
        return insert_to_emptydict(mp, key, hash, value);
    }
    /* insertdict() handles any resizing that might be necessary */
    return insertdict(mp, key, hash, value);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1020: PyDict_DelItem

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1624–1636`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1624–1636 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1624-L1636))

```
PyDict_DelItem(PyObject *op, PyObject *key)
{
    Py_hash_t hash;
    assert(key);
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return -1;
    }

    return _PyDict_DelItem_KnownHash(op, key, hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1021: _PyDict_Pop

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:1894–1913`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 1894–1911 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1894-L1911))

```
_PyDict_Pop(PyObject *dict, PyObject *key, PyObject *deflt)
{
    Py_hash_t hash;

    if (((PyDictObject *)dict)->ma_used == 0) {
        if (deflt) {
            Py_INCREF(deflt);
            return deflt;
        }
        _PyErr_SetKeyError(key);
        return NULL;
    }
    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1894–1913 is in `data/cases.json`.

Closing lines 1912–1913 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L1912-L1913))

```
    return _PyDict_Pop_KnownHash(dict, key, hash, deflt);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1022: dict_subscript

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:2131–2165`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2131–2148 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2131-L2148))

```
dict_subscript(PyDictObject *mp, PyObject *key)
{
    Py_ssize_t ix;
    Py_hash_t hash;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL) {
        if (!PyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
```

Excerpt shortened; the complete reviewed range 2131–2165 is in `data/cases.json`.

Closing lines 2160–2165 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2160-L2165))

```
        _PyErr_SetKeyError(key);
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1023: dict___contains__

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:2861–2881`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2861–2878 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2861-L2878))

```
dict___contains__(PyDictObject *self, PyObject *key)
/*[clinic end generated code: output=a3d03db709ed6e6b input=fe1cb42ad831e820]*/
{
    register PyDictObject *mp = self;
    Py_hash_t hash;
    Py_ssize_t ix;
    PyObject *value;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (mp->ma_keys->dk_lookup)(mp, key, hash, &value);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || value == NULL)
```

Excerpt shortened; the complete reviewed range 2861–2881 is in `data/cases.json`.

Closing lines 2879–2881 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2879-L2881))

```
        Py_RETURN_FALSE;
    Py_RETURN_TRUE;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1024: dict_get_impl

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:2894–2915`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2894–2911 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2894-L2911))

```
dict_get_impl(PyDictObject *self, PyObject *key, PyObject *default_value)
/*[clinic end generated code: output=bba707729dee05bf input=279ddb5790b6b107]*/
{
    PyObject *val = NULL;
    Py_hash_t hash;
    Py_ssize_t ix;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    ix = (self->ma_keys->dk_lookup) (self, key, hash, &val);
    if (ix == DKIX_ERROR)
        return NULL;
    if (ix == DKIX_EMPTY || val == NULL) {
        val = default_value;
```

Excerpt shortened; the complete reviewed range 2894–2915 is in `data/cases.json`.

Closing lines 2912–2915 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2912-L2915))

```
    }
    Py_INCREF(val);
    return val;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1025: PyDict_SetDefault

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:2918–3003`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 2918–2935 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2918-L2935))

```
PyDict_SetDefault(PyObject *d, PyObject *key, PyObject *defaultobj)
{
    PyDictObject *mp = (PyDictObject *)d;
    PyObject *value;
    Py_hash_t hash;

    if (!PyDict_Check(d)) {
        PyErr_BadInternalCall();
        return NULL;
    }

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return NULL;
    }
    if (mp->ma_keys == Py_EMPTY_KEYS) {
```

Excerpt shortened; the complete reviewed range 2918–3003 is in `data/cases.json`.

Closing lines 2998–3003 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L2998-L3003))

```
        mp->ma_version_tag = DICT_NEXT_VERSION();
    }

    ASSERT_CONSISTENT(mp);
    return value;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1026: update

**Classification:** direct layout dependency; copied_cpython_core; `cpython_reference_cached_hash`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c:3231–3412`. SHA-256 `1aab71cf56e99afd61a7948f29a253be4acc3ef9ae6f11111918693adaf809a8`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation. This original CPython reference copy is not named by retained native include directives; standalone compilation/activation is unverified and excluded from native implementation headline.

Lines 3231–3248 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L3231-L3248))

```
"D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\n\
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\n\
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\n\
In either case, this is followed by: for k in F:  D[k] = F[k]");

PyDoc_STRVAR(clear__doc__,
"D.clear() -> None.  Remove all items from D.");

PyDoc_STRVAR(copy__doc__,
"D.copy() -> a shallow copy of D");

/* Forward */
static PyObject *dictkeys_new(PyObject *, PyObject *);
static PyObject *dictitems_new(PyObject *, PyObject *);
static PyObject *dictvalues_new(PyObject *, PyObject *);

PyDoc_STRVAR(keys__doc__,
             "D.keys() -> a set-like object providing a view on D's keys");
```

Excerpt shortened; the complete reviewed range 3231–3412 is in `data/cases.json`.

Closing lines 3407–3412 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/dictobject_original.c#L3407-L3412))

```
PyDoc_STRVAR(dictionary_doc,
"dict() -> new empty dictionary\n"
"dict(mapping) -> new dictionary initialized from a mapping object's\n"
"    (key, value) pairs\n"
"dict(iterable) -> new dictionary initialized as if via:\n"
"    d = {}\n"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1027: unicode_eq

**Classification:** non-direct context; project_source; `standard_unicode_api_types_only`.

**Purpose:** Aliases a/b are never accessed through -> members, sizeof or offsetof; only standard PyUnicode_GET_LENGTH/KIND/1BYTE_DATA macros consume them. Character/storage API dependency exists, but named struct here is solely type annotation/API cast.

**Migration effect:** Can change local variables to PyObject* without relying on Unicode struct members; changes to DATA/KIND APIs remain separate from named struct layout.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/cpython_src/Objects/stringlib/eq.h:7–25`. SHA-256 `c4fdd9e41f8748397cd3c0c5d5ecf77662b6c66c1cdd020d50b77fe9ddd1163c`.

**Activation / context:** Copied CPython helper in each version tree; included by adapted dictobject.c when that variant is selected.

Lines 7–24 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/stringlib/eq.h#L7-L24))

```
unicode_eq(PyObject *aa, PyObject *bb)
{
    assert(PyUnicode_Check(aa));
    assert(PyUnicode_Check(bb));
    assert(PyUnicode_IS_READY(aa));
    assert(PyUnicode_IS_READY(bb));

    PyUnicodeObject *a = (PyUnicodeObject *)aa;
    PyUnicodeObject *b = (PyUnicodeObject *)bb;

    if (PyUnicode_GET_LENGTH(a) != PyUnicode_GET_LENGTH(b))
        return 0;
    if (PyUnicode_GET_LENGTH(a) == 0)
        return 1;
    if (PyUnicode_KIND(a) != PyUnicode_KIND(b))
        return 0;
    return memcmp(PyUnicode_1BYTE_DATA(a), PyUnicode_1BYTE_DATA(b),
                  PyUnicode_GET_LENGTH(a) * PyUnicode_KIND(a)) == 0;
```

Excerpt shortened; the complete reviewed range 7–25 is in `data/cases.json`.

Closing lines 25–25 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/cpython_src/Objects/stringlib/eq.h#L25-L25))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1028: frozendict_setitem

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/frozendictobject.c:149–167`. SHA-256 `a265a5255cf09b1c19741cf1fc60e0e11734e0b3bd81128fb0434c1ce010c0a9`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 149–166 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/frozendictobject.c#L149-L166))

```
static int frozendict_setitem(PyObject *op, 
                              PyObject *key, 
                              PyObject *value, 
                              int empty) {
    Py_hash_t hash;

    assert(key);
    assert(value);

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);

        if (hash == -1) {
            return -1;
        }
    }
    return frozendict_insert((PyDictObject*) op, key, hash, value, empty);
```

Excerpt shortened; the complete reviewed range 149–167 is in `data/cases.json`.

Closing lines 167–167 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/frozendictobject.c#L167-L167))

```
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.

## L1029: dict_get_index

**Classification:** direct layout dependency; adopted_cpython_variant_activation_unknown; `cached_unicode_hash_read`.

**Purpose:** Read exact Unicode key cached hash for dict lookup/update/consistency, falling back to PyObject_Hash when -1; repeated version copies retain this direct cached-field fast path.

**Migration effect:** Cached hash does not require fixed-width characters, but assumes named header field and offset. Switch to appropriate cached-hash API or maintain metadata prefix; reference/inactive copies are not independently active consumers.

**Fields / layout:** PyASCIIObject.hash. Types: PyASCIIObject.

**Source:** `frozendict-2.4.7/src/frozendict/c_src/3_9/frozendictobject.c:883–894`. SHA-256 `a265a5255cf09b1c19741cf1fc60e0e11734e0b3bd81128fb0434c1ce010c0a9`.

**Activation / context:** Versioned native source tree; frozendictobject.c explicitly includes adapted dictobject.c, not dictobject_original.c. Only selected build variant is compiled; saved corpus lacks setup.py variant-selection logic so do not claim all3.6–3.10 copies run simultaneously or current-interpreter activation.

Lines 883–894 ([verified immutable source](https://github.com/Marco-Sulla/python-frozendict/blob/d4ee7590e2b507fd68124cd8a593778ce3c1158b/src/frozendict/c_src/3_9/frozendictobject.c#L883-L894))

```
static Py_ssize_t dict_get_index(PyDictObject *self, PyObject *key) {
    Py_hash_t hash;
    PyObject* val;

    if (!PyUnicode_CheckExact(key) ||
        (hash = ((PyASCIIObject *) key)->hash) == -1) {
        hash = PyObject_Hash(key);
        if (hash == -1)
            return DKIX_ERROR;
    }
    return (self->ma_keys->dk_lookup) (self, key, hash, &val);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/90/b2/2a3d1374b7780999d3184e171e25439a8358c47b481f68be883c14086b4c/frozendict-2.4.7.tar.gz); archive SHA-256 `e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd`.
