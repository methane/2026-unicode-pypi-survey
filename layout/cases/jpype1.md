# jpype1 1.7.1

5 confirmed layout regions; 5 reviewed regions including non-direct context.

## L1045: PyJPChar declaration

**Classification:** direct layout dependency; project_source; `subclass_embedding`.

**Purpose:** Embed a compact Unicode header and reserve four trailing bytes for a Java UTF16 code unit and terminator.

**Migration effect:** Changes to compact header size and one/two-byte payload placement require redesigning the custom JChar representation.

**Fields / layout:** m_Obj, m_Data[4]. Types: PyCompactUnicodeObject.

**Source:** `jpype1-1.7.1/native/python/pyjp_char.cpp:28–32`. SHA-256 `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

Lines 28–38 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L28-L38))

```
struct PyJPChar
{
	PyCompactUnicodeObject m_Obj;
	char m_Data[4];
} ;

#define _PyUnicode_LENGTH(op) (((PyASCIIObject *)(op))->length)
#define _PyUnicode_STATE(op) (((PyASCIIObject *)(op))->state)
#define _PyUnicode_HASH(op) (((PyASCIIObject *)(op))->hash)
#define _PyUnicode_WSTR(op) (((PyASCIIObject*)(op))->wstr)
#define _PyUnicode_WSTR_LENGTH(op)  (((PyCompactUnicodeObject*)(op))->wstr_length)
```

Lines 619–635 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L619-L635))

```
static PyType_Spec charSpec = {
	"_jpype._JChar",
	sizeof (PyJPChar),
	0,
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, // | Py_TPFLAGS_HAVE_GC,
	charSlots
};

#ifdef __cplusplus
}
#endif

void PyJPChar_initType(PyObject* module)
{
	// We will inherit from str and JObject
	JPPyObject bases = JPPyTuple_Pack(&PyUnicode_Type, PyJPObject_Type);
	PyJPChar_Type = (PyTypeObject*) PyJPClass_FromSpecWithBases(&charSpec, bases.get());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz); archive SHA-256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

## L1046: _PyUnicode_* local layout macros

**Classification:** direct layout dependency; project_source; `direct_field_alias`.

**Purpose:** Define local macros for direct Unicode header fields; used by custom JChar constructor/reader.

**Migration effect:** These macros bypass public constructors/accessors and must be adapted if fields or header layout change.

**Fields / layout:** length, state, hash, wstr, wstr_length. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `jpype1-1.7.1/native/python/pyjp_char.cpp:34–38`. SHA-256 `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

Lines 34–38 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L34-L38))

```
#define _PyUnicode_LENGTH(op) (((PyASCIIObject *)(op))->length)
#define _PyUnicode_STATE(op) (((PyASCIIObject *)(op))->state)
#define _PyUnicode_HASH(op) (((PyASCIIObject *)(op))->hash)
#define _PyUnicode_WSTR(op) (((PyASCIIObject*)(op))->wstr)
#define _PyUnicode_WSTR_LENGTH(op)  (((PyCompactUnicodeObject*)(op))->wstr_length)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz); archive SHA-256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

## L1047: PyJPChar_Create

**Classification:** direct layout dependency; project_source; `custom_unicode_construction`.

**Purpose:** Initialize a str-derived Java char by writing Unicode header fields and placing data immediately after ASCII/compact header; use one-byte or two-byte forms and set legacy wide-string aliases conditionally.

**Migration effect:** An FSR compatibility buffer alone does not make these direct header writes valid. The constructor needs supported subclass allocation/initialization or a revised representation contract under UTF-8 internals.

**Fields / layout:** length, hash, state.compact, state.interned, state.ready, state.ascii, state.kind, wstr, wstr_length, utf8, utf8_length, payload after header. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `jpype1-1.7.1/native/python/pyjp_char.cpp:80–154`. SHA-256 `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

Lines 80–97 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L80-L97))

```
PyObject *PyJPChar_Create(PyTypeObject *type, Py_UCS2 p)
{
	// Allocate a new string type (derived from UNICODE)
	PyJPChar  *self = (PyJPChar*) PyJPValue_alloc(type, 0);
	if (self == nullptr)
		return nullptr;

	// Set up a wide char with value of zero
	self->m_Data[0] = 0;
	self->m_Data[1] = 0;
	self->m_Data[2] = 0;
	self->m_Data[3] = 0;

	// Values taken from internal/cpython/unicode.h

	// Mark the type in unicode
	_PyUnicode_LENGTH(self) = 1;
	_PyUnicode_HASH(self) = -1;
```

Excerpt shortened; the complete reviewed range 80–154 is in `data/cases.json`.

Closing lines 149–154 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L149-L154))

```
		self->m_Obj.utf8 = nullptr;
		self->m_Obj.utf8_length = 0;
	}

	return (PyObject*) self;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz); archive SHA-256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

## L1048: fromJPChar

**Classification:** direct layout dependency; project_source; `header_payload_offset_read`.

**Purpose:** Read index0 from payload computed as PyASCIIObject+1 or PyCompactUnicodeObject+1 according to direct header flags.

**Migration effect:** Must replace fixed FSR payload offsets/width selection with supported scalar access or an explicit stable representation.

**Fields / layout:** state.ascii, state.kind, payload after header. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `jpype1-1.7.1/native/python/pyjp_char.cpp:173–187`. SHA-256 `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

Lines 173–187 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L173-L187))

```
Py_UCS2 fromJPChar(PyJPChar *self)
{
	if (_PyUnicode_STATE(self).ascii == 1)
	{
		auto *data = (Py_UCS1*) (((PyASCIIObject*) self) + 1);
		return data[0];
	}
	if (_PyUnicode_STATE(self).kind == PyUnicode_1BYTE_KIND)
	{
		auto *data = (Py_UCS1*) ( ((PyCompactUnicodeObject*) self) + 1);
		return data[0];
	}
	auto *data = (Py_UCS2*) ( ((PyCompactUnicodeObject*) self) + 1);
	return data[0];
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz); archive SHA-256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

## L1049: charSpec

**Classification:** direct layout dependency; project_source; `subclass_size`.

**Purpose:** Allocate the Java char subclass using the size of the header-plus-inline-buffer structure.

**Migration effect:** Changing compact header/payload assumptions changes subclass allocation size and compatibility with str allocation.

**Fields / layout:** sizeof(PyJPChar), m_Obj, m_Data. Types: PyCompactUnicodeObject.

**Source:** `jpype1-1.7.1/native/python/pyjp_char.cpp:619–625`. SHA-256 `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

Lines 28–32 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L28-L32))

```
struct PyJPChar
{
	PyCompactUnicodeObject m_Obj;
	char m_Data[4];
} ;
```

Lines 619–635 ([verified immutable source](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L619-L635))

```
static PyType_Spec charSpec = {
	"_jpype._JChar",
	sizeof (PyJPChar),
	0,
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, // | Py_TPFLAGS_HAVE_GC,
	charSlots
};

#ifdef __cplusplus
}
#endif

void PyJPChar_initType(PyObject* module)
{
	// We will inherit from str and JObject
	JPPyObject bases = JPPyTuple_Pack(&PyUnicode_Type, PyJPObject_Type);
	PyJPChar_Type = (PyTypeObject*) PyJPClass_FromSpecWithBases(&charSpec, bases.get());
```

[Frozen source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz); archive SHA-256 `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.
