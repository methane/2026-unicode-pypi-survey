# pywinpty 3.0.5

18 confirmed layout regions; 22 reviewed regions including non-direct context.

## L1060: Printer.generate_unicode

**Classification:** direct layout dependency; copied_cpython_core; `code_generator_layout`.

**Purpose:** Vendored CPython tool emits static Unicode structs and designated field initializers; type tokens occur in generated C strings, not comments.

**Migration effect:** CPython deepfreeze generator needs updating with core layout changes; it is not pywinpty runtime business logic or a handwritten package consumer.

**Fields / layout:** _ascii, _compact, _data, length, hash, state.kind, state.compact, state.ascii, state.ready, wstr, wstr_length. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/Tools/scripts/deepfreeze.py:175–236`. SHA-256 `81e2d25f53698a7f029fa316c7ce7f629a63c16520ed6beb5d03a0a6aacc63cb`.

Lines 175–192 (immutable GitHub mapping unavailable in saved verification evidence)

```
    def generate_unicode(self, name: str, s: str) -> str:
        if s in strings:
            return f"&_Py_STR({strings[s]})"
        if s in identifiers:
            return f"&_Py_ID({s})"
        if re.match(r'\A[A-Za-z0-9_]+\Z', s):
            name = f"const_str_{s}"
        kind, ascii = analyze_character_width(s)
        if kind == PyUnicode_1BYTE_KIND:
            datatype = "uint8_t"
        elif kind == PyUnicode_2BYTE_KIND:
            datatype = "uint16_t"
        else:
            datatype = "uint32_t"
        self.write("static")
        with self.indent():
            with self.block("struct"):
                if ascii:
```

Excerpt shortened; the complete reviewed range 175–236 is in `data/cases.json`.

Closing lines 231–236 (immutable GitHub mapping unavailable in saved verification evidence)

```
                if kind == PyUnicode_4BYTE_KIND:
                    self.patchups.append("if (sizeof(wchar_t) == 4) {")
                    self.patchups.append(f"    {name}._compact._base.wstr = (wchar_t *) {name}._data;")
                    self.patchups.append(f"    {name}._compact.wstr_length = {len(s)};")
                    self.patchups.append("}")
                return f"& {name}._compact._base.ob_base"
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1061: generate_global_strings

**Classification:** direct layout dependency; copied_cpython_core; `code_generator_layout`.

**Purpose:** Vendored CPython generator emits static ASCII/Latin1 singleton array layouts.

**Migration effect:** Core global-string generation changes with Unicode layout; keep this vendored core tool separate from extension consumers.

**Fields / layout:** _ascii, _latin1, _data[2]. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/Tools/scripts/generate_global_objects.py:188–221`. SHA-256 `407b01d9dac46418843f9f3b83bda132ef5fb8fe62b554924ee64fec484b9884`.

Lines 188–205 (immutable GitHub mapping unavailable in saved verification evidence)

```
def generate_global_strings(identifiers, strings):
    filename = os.path.join(INTERNAL, 'pycore_global_strings.h')

    # Read the non-generated part of the file.
    with open(filename) as infile:
        orig = infile.read()
    lines = iter(orig.rstrip().splitlines())
    before = '\n'.join(iter_to_marker(lines, START))
    for _ in iter_to_marker(lines, END):
        pass
    after = '\n'.join(lines)

    # Generate the file.
    with open_for_changes(filename, orig) as outfile:
        printer = Printer(outfile)
        printer.write(before)
        printer.write(START)
        with printer.block('struct _Py_global_strings', ';'):
```

Excerpt shortened; the complete reviewed range 188–221 is in `data/cases.json`.

Closing lines 216–221 (immutable GitHub mapping unavailable in saved verification evidence)

```
                printer.write("uint8_t _data[2];")
            with printer.block('struct', ' latin1[128];'):
                printer.write("PyCompactUnicodeObject _latin1;")
                printer.write("uint8_t _data[2];")
        printer.write(END)
        printer.write(after)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1062: generate_runtime_init

**Classification:** direct layout dependency; copied_cpython_core; `code_generator_layout`.

**Purpose:** Emit the initialization table corresponding to static ASCII/Latin1 embedded-header arrays; aliases resolve to retained pycore_runtime_init.h.

**Migration effect:** Core-only generated initialization depends on corresponding header/layout macros; not an independent pywinpty package consumer.

**Fields / layout:** _PyASCIIObject_INIT, _PyUnicode_LATIN1_INIT, ascii[128], latin1[128]. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/Tools/scripts/generate_global_objects.py:224–288`. SHA-256 `407b01d9dac46418843f9f3b83bda132ef5fb8fe62b554924ee64fec484b9884`.

Lines 265–282 (immutable GitHub mapping unavailable in saved verification evidence)

```
                with printer.block('.bytes_characters =', ','):
                    for i in range(256):
                        printer.write(f'_PyBytes_CHAR_INIT({i}),')
                printer.write('')
                # Global strings.
                with printer.block('.strings =', ','):
                    with printer.block('.literals =', ','):
                        for literal, name in sorted(strings.items(), key=lambda x: x[1]):
                            printer.write(f'INIT_STR({name}, "{literal}"),')
                    with printer.block('.identifiers =', ','):
                        for name in sorted(identifiers):
                            assert name.isidentifier(), name
                            printer.write(f'INIT_ID({name}),')
                    with printer.block('.ascii =', ','):
                        for i in range(128):
                            printer.write(f'_PyASCIIObject_INIT("\\x{i:02x}"),')
                    with printer.block('.latin1 =', ','):
                        for i in range(128, 256):
```

Excerpt shortened; the complete reviewed range 265–284 is in `data/cases.json`.

Closing lines 283–284 (immutable GitHub mapping unavailable in saved verification evidence)

```
                            printer.write(f'_PyUnicode_LATIN1_INIT("\\x{i:02x}"),')
                printer.write('')
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1063: STRUCT_FOR_ASCII_STR

**Classification:** direct layout dependency; copied_cpython_core; `layout_embedding`.

**Purpose:** Core macro embeds ASCII header immediately before literal-sized storage; reused for literals and identifiers.

**Migration effect:** Core struct macro must match migrated inline-string allocation/layout; this is vendored CPython implementation.

**Fields / layout:** _ascii, _data[sizeof(LITERAL)]. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/internal/pycore_global_strings.h:16–24`. SHA-256 `98cd0bc1d6a1c93e0204837650210986b9bdfe489614aaca8946ac60fbed5a8f`.

Lines 16–24 (immutable GitHub mapping unavailable in saved verification evidence)

```
#define STRUCT_FOR_ASCII_STR(LITERAL) \
    struct { \
        PyASCIIObject _ascii; \
        uint8_t _data[sizeof(LITERAL)]; \
    }
#define STRUCT_FOR_STR(NAME, LITERAL) \
    STRUCT_FOR_ASCII_STR(LITERAL) _ ## NAME;
#define STRUCT_FOR_ID(NAME) \
    STRUCT_FOR_ASCII_STR(#NAME) _ ## NAME;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1064: ASCII and Latin1 singleton arrays

**Classification:** direct layout dependency; copied_cpython_core; `layout_embedding`.

**Purpose:** Generated core header contains128ASCII and128Latin1 singleton objects as header-plus-two-byte structs.

**Migration effect:** Static objects assume old compact representations and require core-generated updates under UTF8 internals.

**Fields / layout:** _ascii, _latin1, _data[2]. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/internal/pycore_global_strings.h:360–367`. SHA-256 `98cd0bc1d6a1c93e0204837650210986b9bdfe489614aaca8946ac60fbed5a8f`.

Lines 360–367 (immutable GitHub mapping unavailable in saved verification evidence)

```
    struct {
        PyASCIIObject _ascii;
        uint8_t _data[2];
    } ascii[128];
    struct {
        PyCompactUnicodeObject _latin1;
        uint8_t _data[2];
    } latin1[128];
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1065: _PyUnicode_ASCII_BASE_INIT and static Unicode initializers

**Classification:** direct layout dependency; copied_cpython_core; `direct_static_field_initialization`.

**Purpose:** Supporting core initializer macros directly initialize embedded Unicode headers and literal payload storage.

**Migration effect:** Core initialization macros must change with struct/representation invariants; vendored CPython source, not external extension usage.

**Fields / layout:** ob_base, length, hash, state.kind, state.compact, state.ascii, state.ready, _ascii, _latin1._base, _data. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/internal/pycore_runtime_init.h:96–123`. SHA-256 `860b0112848e000a33fb4ec4f12c639562ae7af17b2fad982e3bb1ead2b9c1ba`.

Lines 96–113 (immutable GitHub mapping unavailable in saved verification evidence)

```
#define _PyUnicode_ASCII_BASE_INIT(LITERAL, ASCII) \
    { \
        .ob_base = _PyObject_IMMORTAL_INIT(&PyUnicode_Type), \
        .length = sizeof(LITERAL) - 1, \
        .hash = -1, \
        .state = { \
            .kind = 1, \
            .compact = 1, \
            .ascii = ASCII, \
            .ready = 1, \
        }, \
    }
#define _PyASCIIObject_INIT(LITERAL) \
    { \
        ._ascii = _PyUnicode_ASCII_BASE_INIT(LITERAL, 1), \
        ._data = LITERAL \
    }
#define INIT_STR(NAME, LITERAL) \
```

Excerpt shortened; the complete reviewed range 96–123 is in `data/cases.json`.

Closing lines 118–123 (immutable GitHub mapping unavailable in saved verification evidence)

```
    { \
        ._latin1 = { \
            ._base = _PyUnicode_ASCII_BASE_INIT(LITERAL, 0), \
        }, \
        ._data = LITERAL, \
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1066: PyASCIIObject definition

**Classification:** non-direct context; copied_cpython_core; `core_layout_definition`.

**Purpose:** Vendored CPython defines the PEP393 Unicode structure itself; not an external callsite.

**Migration effect:** These definitions are core implementation to be changed as part of a migration; do not count as a pywinpty handwritten consumer.

**Fields / layout:** PyObject_HEAD, length, hash, state.interned, state.kind, state.compact, state.ascii, state.ready, wstr. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:72–206`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 72–89 (immutable GitHub mapping unavailable in saved verification evidence)

```
typedef struct {
    /* There are 4 forms of Unicode strings:

       - compact ascii:

         * structure = PyASCIIObject
         * test: PyUnicode_IS_COMPACT_ASCII(op)
         * kind = PyUnicode_1BYTE_KIND
         * compact = 1
         * ascii = 1
         * ready = 1
         * (length is the length of the utf8 and wstr strings)
         * (data starts just after the structure)
         * (since ASCII is decoded from UTF-8, the utf8 string are the data)

       - compact:

         * structure = PyCompactUnicodeObject
```

Excerpt shortened; the complete reviewed range 72–206 is in `data/cases.json`.

Closing lines 201–206 (immutable GitHub mapping unavailable in saved verification evidence)

```
        /* Padding to ensure that PyUnicode_DATA() is always aligned to
           4 bytes (see issue #19537 on m68k). */
        unsigned int :24;
    } state;
    wchar_t *wstr;              /* wchar_t representation (null-terminated) */
} PyASCIIObject;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1067: PyCompactUnicodeObject definition

**Classification:** non-direct context; copied_cpython_core; `core_layout_definition`.

**Purpose:** Vendored CPython defines the PEP393 Unicode structure itself; not an external callsite.

**Migration effect:** These definitions are core implementation to be changed as part of a migration; do not count as a pywinpty handwritten consumer.

**Fields / layout:** _base, utf8_length, utf8, wstr_length. Types: PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:211–218`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 211–218 (immutable GitHub mapping unavailable in saved verification evidence)

```
typedef struct {
    PyASCIIObject _base;
    Py_ssize_t utf8_length;     /* Number of bytes in utf8, excluding the
                                 * terminating \0. */
    char *utf8;                 /* UTF-8 representation (null-terminated) */
    Py_ssize_t wstr_length;     /* Number of code points in wstr, possible
                                 * surrogates count as two code points. */
} PyCompactUnicodeObject;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1068: PyUnicodeObject definition

**Classification:** non-direct context; copied_cpython_core; `core_layout_definition`.

**Purpose:** Vendored CPython defines the PEP393 Unicode structure itself; not an external callsite.

**Migration effect:** These definitions are core implementation to be changed as part of a migration; do not count as a pywinpty handwritten consumer.

**Fields / layout:** _base, data.any, data.latin1, data.ucs2, data.ucs4. Types: PyUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:223–231`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 223–231 (immutable GitHub mapping unavailable in saved verification evidence)

```
typedef struct {
    PyCompactUnicodeObject _base;
    union {
        void *any;
        Py_UCS1 *latin1;
        Py_UCS2 *ucs2;
        Py_UCS4 *ucs4;
    } data;                     /* Canonical, smallest-form Unicode buffer */
} PyUnicodeObject;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1069: _PyASCIIObject_CAST/_PyCompactUnicodeObject_CAST/_PyUnicodeObject_CAST

**Classification:** non-direct context; copied_cpython_core; `typed_alias_definition`.

**Purpose:** Core typed-cast macros assert Unicode type and cast pointer; direct field accesses occur in their consumers, recorded separately.

**Migration effect:** Type names change with core definitions; this region itself does not read/write payload or metadata.

**Fields / layout:** none. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:238–246`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 238–246 (immutable GitHub mapping unavailable in saved verification evidence)

```
#define _PyASCIIObject_CAST(op) \
    (assert(PyUnicode_Check(op)), \
     _Py_CAST(PyASCIIObject*, (op)))
#define _PyCompactUnicodeObject_CAST(op) \
    (assert(PyUnicode_Check(op)), \
     _Py_CAST(PyCompactUnicodeObject*, (op)))
#define _PyUnicodeObject_CAST(op) \
    (assert(PyUnicode_Check(op)), \
     _Py_CAST(PyUnicodeObject*, (op)))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1070: PyUnicode_CHECK_INTERNED

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** state.interned. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:259–261`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 259–261 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline unsigned int PyUnicode_CHECK_INTERNED(PyObject *op) {
    return _PyASCIIObject_CAST(op)->state.interned;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1071: PyUnicode_IS_READY

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** state.ready. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:268–270`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 268–270 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline unsigned int PyUnicode_IS_READY(PyObject *op) {
    return _PyASCIIObject_CAST(op)->state.ready;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1072: PyUnicode_IS_ASCII

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** state.ascii. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:278–281`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 278–281 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline unsigned int PyUnicode_IS_ASCII(PyObject *op) {
    assert(PyUnicode_IS_READY(op));
    return _PyASCIIObject_CAST(op)->state.ascii;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1073: PyUnicode_IS_COMPACT

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** state.compact. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:288–290`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 288–290 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline unsigned int PyUnicode_IS_COMPACT(PyObject *op) {
    return _PyASCIIObject_CAST(op)->state.compact;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1074: PyUnicode_IS_COMPACT_ASCII

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** state.ascii. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:297–299`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 297–299 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline int PyUnicode_IS_COMPACT_ASCII(PyObject *op) {
    return (_PyASCIIObject_CAST(op)->state.ascii && PyUnicode_IS_COMPACT(op));
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1075: PyUnicode_KIND

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** state.kind. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:315–318`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 315–318 (immutable GitHub mapping unavailable in saved verification evidence)

```
/* Return one of the PyUnicode_*_KIND values defined above. */
#define PyUnicode_KIND(op) \
    (assert(PyUnicode_IS_READY(op)), \
     _PyASCIIObject_CAST(op)->state.kind)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1076: _PyUnicode_COMPACT_DATA

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** payload after PyASCIIObject/PyCompactUnicodeObject. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:321–326`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 321–326 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline void* _PyUnicode_COMPACT_DATA(PyObject *op) {
    if (PyUnicode_IS_ASCII(op)) {
        return _Py_STATIC_CAST(void*, (_PyASCIIObject_CAST(op) + 1));
    }
    return _Py_STATIC_CAST(void*, (_PyCompactUnicodeObject_CAST(op) + 1));
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1077: _PyUnicode_NONCOMPACT_DATA

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** data.any. Types: PyUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:328–334`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 328–334 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline void* _PyUnicode_NONCOMPACT_DATA(PyObject *op) {
    void *data;
    assert(!PyUnicode_IS_COMPACT(op));
    data = _PyUnicodeObject_CAST(op)->data.any;
    assert(data != NULL);
    return data;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1078: PyUnicode_GET_LENGTH

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** length. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:358–361`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 358–361 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline Py_ssize_t PyUnicode_GET_LENGTH(PyObject *op) {
    assert(PyUnicode_IS_READY(op));
    return _PyASCIIObject_CAST(op)->length;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1079: PyUnicode_WSTR_LENGTH

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** length, wstr_length. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:633–641`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 633–641 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline Py_ssize_t PyUnicode_WSTR_LENGTH(PyObject *op)
{
    if (PyUnicode_IS_COMPACT_ASCII(op)) {
        return _PyASCIIObject_CAST(op)->length;
    }
    else {
        return _PyCompactUnicodeObject_CAST(op)->wstr_length;
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1080: PyUnicode_GET_SIZE

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** wstr. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:652–662`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 652–662 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline Py_ssize_t PyUnicode_GET_SIZE(PyObject *op)
{
    _Py_COMP_DIAG_PUSH
    _Py_COMP_DIAG_IGNORE_DEPR_DECLS
    if (_PyASCIIObject_CAST(op)->wstr == _Py_NULL) {
        (void)PyUnicode_AsUnicode(op);
        assert(_PyASCIIObject_CAST(op)->wstr != _Py_NULL);
    }
    return PyUnicode_WSTR_LENGTH(op);
    _Py_COMP_DIAG_POP
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.

## L1081: PyUnicode_AS_UNICODE

**Classification:** direct layout dependency; copied_cpython_core; `core_accessor_implementation`.

**Purpose:** Vendored CPython API/helper implementation accesses fields via the retained typed-cast macros.

**Migration effect:** Core API implementation may be rewritten forUTF8 while preserving external API contracts; this is not independent external package layout usage.

**Fields / layout:** wstr. Types: PyASCIIObject.

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:685–696`. SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

Lines 685–696 (immutable GitHub mapping unavailable in saved verification evidence)

```
static inline Py_UNICODE* PyUnicode_AS_UNICODE(PyObject *op)
{
    wchar_t *wstr = _PyASCIIObject_CAST(op)->wstr;
    if (wstr != _Py_NULL) {
        return wstr;
    }

    _Py_COMP_DIAG_PUSH
    _Py_COMP_DIAG_IGNORE_DEPR_DECLS
    return PyUnicode_AsUnicode(op);
    _Py_COMP_DIAG_POP
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.
