# cython 3.3.0

6 confirmed layout regions; 9 reviewed regions including non-direct context.

## L0021: PyUnicodeObjectPtr _typename and GDB type lookup binding

**Classification:** non-direct context; project_source; `dynamic_type_binding`.

**Purpose:** _typename feeds get_gdb_type lookup_type; Py_UNICODE size supports old surrogate codeunit decoding. Executable type literals are not comments.

**Migration effect:** Retaining/renaming type names affects debugger lookup, but this region does not itself dereference a Unicode field.

**Fields / layout:** GDB PyUnicodeObject type name, Py_UNICODE sizeof. Types: PyUnicodeObject.

**Source:** `cython-3.3.0/Cython/Debugger/libpython.py:1153–1159`. SHA-256 `929b3bb9e3bb70b3e588c4a1c1f73d5ec2c98a77fa0aa0a3394ab6d634d99e85`.

**Activation / context:** Selected for objects with Py_TPFLAGS_UNICODE_SUBCLASS; pretty-printer and get_gdb_type helpers feed this reader.

Lines 1153–1159 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Debugger/libpython.py#L1153-L1159))

```
class PyUnicodeObjectPtr(PyObjectPtr):
    _typename = 'PyUnicodeObject'

    def char_width(self):
        _type_Py_UNICODE = gdb.lookup_type('Py_UNICODE')
        return _type_Py_UNICODE.sizeof

```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0022: PyUnicodeObjectPtr.proxyval

**Classification:** direct layout dependency; project_source; `gdb_dynamic_fields_and_payload`.

**Purpose:** GDB reads inferior object fields by executable string keys; detects PEP393 by data field, picks header-adjacent/raw/wchar payload, reads codepoints and joins UTF16 surrogates.

**Migration effect:** UTF8 internal payload changes kind/byte-length/decoder assumptions. Dynamic GDB field lookup can follow changed offsets automatically only when expected field names and payload semantics survive.

**Fields / layout:** lookup_type(PyUnicodeObject).fields, _base._base, state.ready, state.compact, state.ascii, state.kind, length, wstr, wstr_length, data.any, ascii.address+1, compact.address+1, legacy length/str. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `cython-3.3.0/Cython/Debugger/libpython.py:1160–1229`. SHA-256 `929b3bb9e3bb70b3e588c4a1c1f73d5ec2c98a77fa0aa0a3394ab6d634d99e85`.

**Activation / context:** PEP393 path claimed3.3+ by source; legacy path3.2-. Readiness/wstr branch is not guarded for later removal of fields: already tied to old layouts rather than demonstrated support for every new Python. Underlying GDB field access is direct dereference, not Python string lookup.

Lines 1160–1177 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Debugger/libpython.py#L1160-L1177))

```
    def proxyval(self, visited):
        global _is_pep393
        if _is_pep393 is None:
            fields = gdb.lookup_type('PyUnicodeObject').fields()
            _is_pep393 = 'data' in [f.name for f in fields]
        if _is_pep393:
            # Python 3.3 and newer
            may_have_surrogates = False
            compact = self.field('_base')
            ascii = compact['_base']
            state = ascii['state']
            is_compact_ascii = (int(state['ascii']) and int(state['compact']))
            if not int(state['ready']):
                # string is not ready
                field_length = int(compact['wstr_length'])
                may_have_surrogates = True
                field_str = ascii['wstr']
            else:
```

Excerpt shortened; the complete reviewed range 1160–1204 is in `data/cases.json`.

Closing lines 1199–1204 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Debugger/libpython.py#L1199-L1204))

```
        # UCS-1, UCS-2 or UCS-4 code points:
        if not may_have_surrogates:
            Py_UNICODEs = [int(field_str[i]) for i in safe_range(field_length)]
        else:
            # A more elaborate routine if sizeof(Py_UNICODE) is 2 in the
            # inferior process: we must join surrogate pairs.
```

Lines 1205–1222 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Debugger/libpython.py#L1205-L1222))

```
            Py_UNICODEs = []
            i = 0
            limit = safety_limit(field_length)
            while i < limit:
                ucs = int(field_str[i])
                i += 1
                if ucs < 0xD800 or ucs >= 0xDC00 or i == field_length:
                    Py_UNICODEs.append(ucs)
                    continue
                # This could be a surrogate pair.
                ucs2 = int(field_str[i])
                if ucs2 < 0xDC00 or ucs2 > 0xDFFF:
                    continue
                code = (ucs & 0x03FF) << 10
                code |= ucs2 & 0x03FF
                code += 0x00010000
                Py_UNICODEs.append(code)
                i += 1
```

Excerpt shortened; the complete reviewed range 1205–1229 is in `data/cases.json`.

Closing lines 1224–1229 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Debugger/libpython.py#L1224-L1229))

```
        # Convert the int code points to unicode characters, and generate a
        # local unicode instance.
        # This splits surrogate pairs if sizeof(Py_UNICODE) is 2 here (in gdb).
        result = ''.join([
            (chr(ucs) if ucs <= 0x10ffff else '\ufffd')
            for ucs in Py_UNICODEs])
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0023: pretty_printer_lookup Unicode type dispatch

**Classification:** non-direct context; project_source; `dynamic_type_dispatch`.

**Purpose:** Recognizes GDB pointer target type string and returns PyObjectPtrPrinter; proxyval separately owns actual layout access.

**Migration effect:** Requires a compatible type identity/dispatch route; not itself field access.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `cython-3.3.0/Cython/Debugger/libpython.py:1406–1414`. SHA-256 `929b3bb9e3bb70b3e588c4a1c1f73d5ec2c98a77fa0aa0a3394ab6d634d99e85`.

**Activation / context:** Executable literal comparison, not documentation.

Lines 1406–1414 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Debugger/libpython.py#L1406-L1414))

```
def pretty_printer_lookup(gdbval):
    type = gdbval.type.unqualified()
    if type.code != gdb.TYPE_CODE_PTR:
        return None

    type = type.target().unqualified()
    t = str(type)
    if t in ("PyObject", "PyFrameObject", "PyUnicodeObject", "wrapperobject"):
        return PyObjectPtrPrinter(gdbval)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0024: init_builtin_types str object struct name

**Classification:** non-direct context; project_source; `compiler_type_name_and_cast_configuration`.

**Purpose:** Assigns objstruct_cname for str; BuiltinObjectType stores it and can emit pointer casts via cast_code(to_object_struct=True). No Unicode member offsets/content read here.

**Migration effect:** May require retained type name for generated casts; no independent physical layout or encoding assumption established from the literal.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `cython-3.3.0/Cython/Compiler/Builtin.py:817–854`. SHA-256 `79afb19d876b24fd124498aeb7e99930a480aaa459eee642ca307a1f239f7bc1`.

**Activation / context:** Executed compiler configuration, not a comment despite literal masking.

Lines 817–834 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Compiler/Builtin.py#L817-L834))

```
    global builtin_types

    # Some builtin types are not available by name,
    # so we declare them in a throw-away scope.
    hidden_builtins_scope = BuiltinScope()

    for name, cname, methods in builtin_types_table:
        if name == 'frozenset':
            objstruct_cname = 'PySetObject'
        elif name == 'bytearray':
            objstruct_cname = 'PyByteArrayObject'
        elif name == 'int':
            objstruct_cname = 'PyLongObject'
        elif name == 'str':
            objstruct_cname = 'PyUnicodeObject'
        elif name == 'bool':
            objstruct_cname = 'PyLongObject'
        else:
```

Excerpt shortened; the complete reviewed range 817–854 is in `data/cases.json`.

Closing lines 849–854 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Compiler/Builtin.py#L849-L854))

```
            type_class = PyrexTypes.BuiltinTypeConstructorObjectType
            scope = hidden_builtins_scope
            # Make sure the 'type' base type is declared in the hidden scope.
            if 'type' not in hidden_builtins_scope.entries:
                hidden_builtins_scope.entries['type'] = builtin_scope.lookup('type')

```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0025: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; cython_runtime_source; `cached_hash_field_read`.

**Purpose:** Reads key and interned argument-name cached hashes to gate Unicode keyword equality/duplicate-argument checks.

**Migration effect:** Requires cached hash header field/offset contract or revised accessor; does not itself interpret codepoint payload.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `cython-3.3.0/Cython/Utility/FunctionArguments.c:368–435`. SHA-256 `1eebc86617465886e5f88f93ad311b23f6240a8bac9555a046f2cbb37d5234dd`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS branches; other branch uses public comparisons. Hash -1 triggers PyObject_Hash first.

Lines 368–385 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/FunctionArguments.c#L368-L385))

```
static int __Pyx_MatchKeywordArg_str(
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    // The key hash is probably pre-calculated.
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif

```

Excerpt shortened; the complete reviewed range 368–401 is in `data/cases.json`.

Closing lines 396–401 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/FunctionArguments.c#L396-L401))

```
        }
        #else

        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
```

Lines 413–428 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/FunctionArguments.c#L413-L428))

```

    // Not found in keyword parameters, check for (unlikely) duplicate positional argument.
    name = argnames;
    while (name != first_kw_arg) {
        PyObject *name_str = **name;

        #if CYTHON_USE_UNICODE_INTERNALS
        if (unlikely(key_hash == ((PyASCIIObject*)name_str)->hash)) {
            if (__Pyx_UnicodeKeywordsEqual(name_str, key))
                goto arg_passed_twice;
        }

        #else

        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0026: __Pyx_PyDict_GetItemStrWithError macro

**Classification:** direct layout dependency; cython_runtime_source; `cached_hash_field_read`.

**Purpose:** Feeds cached name hash directly to private known-hash dictionary lookup; wrapper invokes macro.

**Migration effect:** Header/hash ABI dependency; update template/accessor if header changes. No payload decode here.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `cython-3.3.0/Cython/Utility/ModuleSetupCode.c:996–1009`. SHA-256 `a069bbb204c5ceff6729d5ffb0ca4e3daf11f514d5cb70a54c5bfe93fba5f5c1`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS; fallback uses API lookup.

Lines 996–1009 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ModuleSetupCode.c#L996-L1009))

```
#if CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS
// _PyDict_GetItem_KnownHash() existed from CPython 3.5 to 3.12, but it was
// dropping exceptions in 3.5. Since 3.6, exceptions are kept.
#define __Pyx_PyDict_GetItemStrWithError(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
static CYTHON_INLINE PyObject * __Pyx_PyDict_GetItemStr(PyObject *dict, PyObject *name) {
    PyObject *res = __Pyx_PyDict_GetItemStrWithError(dict, name);
    if (res == NULL && PyErr_Occurred()) {
        // Like PyDict_GetItem, this is a bit indiscriminate about catching *all* errors.
        // Recent versions of Python format any unraised exception so do that too here.
        PyErr_WriteUnraisable(NULL);
    }
    return res;
}
#elif !CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07020000
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0027: __Pyx_PyUnicode_IS_TRUE legacy unready branch

**Classification:** direct layout dependency; cython_runtime_source; `legacy_wstr_length_field_read`.

**Purpose:** Uses wchar buffer length only for unready strings while avoiding deprecated Unicode size API.

**Migration effect:** Legacy direct field dependency; modern>=3.12 branch uses length API and never accesses wstr_length.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `cython-3.3.0/Cython/Utility/ModuleSetupCode.c:1065–1105`. SHA-256 `a069bbb204c5ceff6729d5ffb0ca4e3daf11f514d5cb70a54c5bfe93fba5f5c1`.

**Activation / context:** Non-limited API, PY_VERSION_HEX<0x030C0000 and CYTHON_COMPILING_IN_CPYTHON, only when PyUnicode_IS_READY false. Limited API and newer-version branches do not dereference this field.

Lines 1065–1078 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ModuleSetupCode.c#L1065-L1078))

```
#endif

#if CYTHON_COMPILING_IN_LIMITED_API
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_ReadChar(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((void)u, 1114111U)
  #define __Pyx_PyUnicode_KIND(u)         ((void)u, (0))
  #define __Pyx_PyUnicode_KIND_04(u)      __Pyx_PyUnicode_KIND(u)
  // __Pyx_PyUnicode_DATA() and __Pyx_PyUnicode_READ() must go together, e.g. for iteration.
  #define __Pyx_PyUnicode_DATA(u)         ((void*)u)
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)k, PyUnicode_ReadChar((PyObject*)(d), i))
  //#define __Pyx_PyUnicode_WRITE(k, d, i, ch)  /* not available */
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GetLength(u))
#else
```

Lines 1093–1103 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ModuleSetupCode.c#L1093-L1103))

```
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON
    // Avoid calling deprecated C-API functions in Py3.9+ that PEP-623 schedules for removal in Py3.12.
    // https://www.python.org/dev/peps/pep-0623/
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0028: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; cython_runtime_source; `cached_hash_field_read`.

**Purpose:** Uses interned name cached hash for exact dict class namespace assignment.

**Migration effect:** Header/hash ABI dependency, no character payload assumption.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `cython-3.3.0/Cython/Utility/ObjectHandling.c:1546–1557`. SHA-256 `faf3268d038deb49a26b53011e4fa89d457716f02f701447cfb899231cf563bb`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX<0x030d0000;3.13+ CPython branch uses PyDict_SetItem instead.

Lines 1546–1557 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ObjectHandling.c#L1546-L1557))

```
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000
// Identifier names are always interned and have a pre-calculated hash value.
#define __Pyx_SetNameInClass(ns, name, value) \
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value) \
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/////////////// SetNewInClass.proto ///////////////
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.

## L0029: __Pyx__GetModuleGlobalName fallback lookup

**Classification:** direct layout dependency; cython_runtime_source; `cached_hash_field_read`.

**Purpose:** Known-hash lookup reads interned global-name hash in non-limited borrowed-reference branch.

**Migration effect:** Header/hash ABI dependency; does not read flexible Unicode payload.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `cython-3.3.0/Cython/Utility/ObjectHandling.c:1620–1663`. SHA-256 `faf3268d038deb49a26b53011e4fa89d457716f02f701447cfb899231cf563bb`.

**Activation / context:** Excluded by limited API or CYTHON_AVOID_BORROWED_REFS/CYTHON_AVOID_THREAD_UNSAFE_BORROWED_REFS branches. Utility selection and dict-version flags control generated helper availability.

Lines 1620–1637 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ObjectHandling.c#L1620-L1637))

```
/////////////// GetModuleGlobalName ///////////////
//@requires: GetBuiltinName
//@requires: Exceptions.c::IgnoreException
//@substitute: naming

#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if CYTHON_COMPILING_IN_LIMITED_API
    if (unlikely(!$module_cname)) {
        if (!PyErr_Occurred())
            PyErr_SetNone(PyExc_NameError);
        return NULL;
    }
```

Excerpt shortened; the complete reviewed range 1620–1640 is in `data/cases.json`.

Closing lines 1638–1640 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ObjectHandling.c#L1638-L1640))

```
    result = PyObject_GetAttr($module_cname, name);
    if (likely(result)) {
        return result;
```

Lines 1652–1663 ([verified immutable source](https://github.com/cython/cython/blob/bcd04a2966842d80de6ecff4e68e8d892bec5ef7/Cython/Utility/ObjectHandling.c#L1652-L1663))

```
    if (likely(result)) {
        return result;
    }
#else
    // Identifier names are always interned and have a pre-calculated hash value.
    result = _PyDict_GetItem_KnownHash(NAMED_CGLOBAL(moddict_cname), name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(NAMED_CGLOBAL(moddict_cname), result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyObject *exc = PyErr_Occurred();
    if (unlikely(exc) && !__Pyx_IgnoreGivenException(exc, PyExc_Exception)) {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/d8/4981ef716ad0e3ff0d3ef383aefc6b03c4a88dee33b272bf8e0d833001ca/cython-3.3.0.tar.gz); archive SHA-256 `eed0d93fbca7087f143b42c34b05a825849bdf17f101572c2105acfa49aa88b8`.
