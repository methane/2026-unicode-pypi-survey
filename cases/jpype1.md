# jpype1 — non-simple Unicode reads

[All packages](README.md)

Version: 1.7.1. **22 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`JPConversionAsChar::convert`](#case-001)
- [`JPCharType::setArrayRange`](#case-002)
- [`JPPyString::asCharUTF16`](#case-003)
- [`ord`](#case-004)
- [`fromJPChar`](#case-005)
- [`PyJPChar_new`](#case-006)
- [`PyJPChar_str`](#case-007)
- [`PyJPChar_index`](#case-008)
- [`PyJPChar_float`](#case-009)
- [`PyJPChar_abs`](#case-010)
- [`apply`](#case-011)
- [`PyJPChar_add`](#case-012)
- [`PyJPChar_neg`](#case-013)
- [`PyJPChar_pos`](#case-014)
- [`PyJPChar_inv`](#case-015)
- [`PyJPJChar_compare`](#case-016)
- [`PyJPChar_bool`](#case-017)
- [`PyJPClass_getattro`](#case-018)
- [`PyJPClass_setattro`](#case-019)
- [`PyJPModule_collect`](#case-020)
- [`PyJPValue_getattro`](#case-021)
- [`PyJPValue_setattro`](#case-022)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `JPConversionAsChar::convert`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Calls asCharUTF16 on original Python object, reading codepoint0 for Java char conversion.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=helper_consumer; Java array index start/step do not describe Python Unicode character traversal.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/common/jp_chartype.cpp`, lines 89–94. Member SHA-256: `edf5847b6d7a52292ca50ea7cd9cb5ce75573c70e4ffae40b49c94ed61404b0e`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/common/jp_chartype.cpp#L89-L94).

### Read sites

- Site 1: lines 92–92; derived read; index expression `res.c = JPPyString::asCharUTF16(match.object);`. Resolved scalar conversion reader

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/common/jp_chartype.cpp`, lines 89–94. Member SHA-256: `edf5847b6d7a52292ca50ea7cd9cb5ce75573c70e4ffae40b49c94ed61404b0e`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/common/jp_chartype.cpp#L89-L94).

```cpp
	jvalue convert(JPMatch &match) override
	{
		jvalue res;
		res.c = JPPyString::asCharUTF16(match.object);
		return res;
	}
```

### Callee analysis

- `JPPyString::asCharUTF16` in `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–282: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ/ReadChar codepoint0

Available source context:
Omitted from `jpype1-1.7.1/native/python/jp_pythontypes.cpp`: lines 224–232, 242, 252–261, 277–279. The original contextual region was lines 220–282.

- [`JPPyString::asCharUTF16`](#helper-001) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–223).
- [`JPPyString::asCharUTF16`](#helper-002) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 233–241).
- [`JPPyString::asCharUTF16`](#helper-003) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 243–251).
- [`JPPyString::asCharUTF16`](#helper-004) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 262–276).
- [`JPPyString::asCharUTF16`](#helper-005) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 280–282).

<a id="case-002"></a>

## 2. `JPCharType::setArrayRange`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Loops through Python sequence of individual Unicode strings and calls asCharUTF16 on each, fixed codepoint0 per input. Sequence indices are not Unicode offsets.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=helper_consumer; Java array index start/step do not describe Python Unicode character traversal.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/common/jp_chartype.cpp`, lines 210–230. Member SHA-256: `edf5847b6d7a52292ca50ea7cd9cb5ce75573c70e4ffae40b49c94ed61404b0e`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/common/jp_chartype.cpp#L210-L230).

### Read sites

- Site 1: lines 224–224; derived read; index expression `jchar v = JPPyString::asCharUTF16(seq[i].get());`. Resolved scalar conversion reader

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/common/jp_chartype.cpp`, lines 210–230. Member SHA-256: `edf5847b6d7a52292ca50ea7cd9cb5ce75573c70e4ffae40b49c94ed61404b0e`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/common/jp_chartype.cpp#L210-L230).

```cpp
void JPCharType::setArrayRange(JPJavaFrame& frame, jarray a,
		jsize start, jsize length, jsize step,
		PyObject* sequence)
{
	JP_TRACE_IN("JPCharType::setArrayRange");

	JPPrimitiveArrayAccessor<array_t, type_t*> accessor(frame, a,
			&JPJavaFrame::GetCharArrayElements, &JPJavaFrame::ReleaseCharArrayElements);

	type_t* val = accessor.get();
	JPPySequence seq = JPPySequence::use(sequence);
	jsize index = start;
	for (Py_ssize_t i = 0; i < length; ++i, index += step)
	{
		jchar v = JPPyString::asCharUTF16(seq[i].get());
		JP_PY_CHECK();
		val[index] = (type_t) v;
	}
	accessor.commit();
	JP_TRACE_OUT;
}
```

### Callee analysis

- `JPPyString::asCharUTF16` in `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–282: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ/ReadChar codepoint0

Available source context:
Omitted from `jpype1-1.7.1/native/python/jp_pythontypes.cpp`: lines 224–232, 242, 252–261, 277–279. The original contextual region was lines 220–282.

- [`JPPyString::asCharUTF16`](#helper-001) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–223).
- [`JPPyString::asCharUTF16`](#helper-002) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 233–241).
- [`JPPyString::asCharUTF16`](#helper-003) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 243–251).
- [`JPPyString::asCharUTF16`](#helper-004) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 262–276).
- [`JPPyString::asCharUTF16`](#helper-005) (`jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 280–282).

<a id="case-003"></a>

## 3. `JPPyString::asCharUTF16`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Extracts codepoint at fixed index 0 for Java char conversion (length>1 rejected); no loop.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Rejects values >0xffff. Adjacent surrogate semantics are irrelevant to single-char requirement.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–282. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L220-L282).

### Read sites

- Site 1: lines 242–253; derived read; index expression `0`. READ_CHAR CPython branch
- Site 2: lines 266–277; derived read; index expression `0`. ReadChar alternative branch

### Contextual source excerpts

Omitted from `jpype1-1.7.1/native/python/jp_pythontypes.cpp`: lines 224–237, 253–261, 277–279. The original contextual region was lines 220–282.

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–223. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L220-L223).

```cpp
jchar JPPyString::asCharUTF16(PyObject* pyobj)
{
	if (PyIndex_Check(pyobj))
	{
```

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 238–252. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L238-L252).

```cpp
		if (PyErr_Occurred())
			JP_RAISE_PYTHON();
		return c;
	}
	if (PyUnicode_Check(pyobj))
	{
		if (PyUnicode_GetLength(pyobj) > 1)
			JP_RAISE(PyExc_ValueError, "Char must be length 1");

		PyUnicode_READY(pyobj);
		Py_UCS4 value = PyUnicode_READ_CHAR(pyobj, 0);
		if (value > 0xffff)
		{
			JP_RAISE(PyExc_ValueError, "Unable to pack 4 byte unicode into Java char");
		}
```

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 262–276. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L262-L276).

```cpp
		jchar c = PyBytes_AsString(pyobj)[0];
		JP_PY_CHECK();
		return c;
	}
	if (PyUnicode_Check(pyobj))
	{
		if (PyUnicode_GetLength(pyobj) > 1)
			JP_RAISE(PyExc_ValueError, "Char must be length 1");

		PyUnicode_READY(pyobj);
		Py_UCS4 value = PyUnicode_ReadChar(pyobj, 0);
		if (value > 0xffff)
		{
			JP_RAISE(PyExc_ValueError, "Unable to pack 4 byte unicode into Java char");
		}
```

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 280–282. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L280-L282).

```cpp
	PyErr_Format(PyExc_TypeError, "Unable to convert '%s' to Java char", Py_TYPE(pyobj)->tp_name);
	JP_RAISE_PYTHON();
}
```


<a id="case-004"></a>

## 4. `ord`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive helper.

Reads index0 only after verifying Python unicode length is exactly1.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L40-L53).

### Read sites

- Site 1: lines 42–47; derived read; index expression `0`. Fixed single-codepoint access

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L40-L53).

```cpp
static Py_UCS4 ord(PyObject *c)
{
	if (PyUnicode_Check(c))
	{
		if (PyUnicode_READY(c) == -1)
			return -1;
		if (PyUnicode_GET_LENGTH(c) == 1)
			return PyUnicode_READ_CHAR(c, 0);
	} else if (PyBytes_Check(c) && PyBytes_GET_SIZE(c) == 1)
		return (Py_UCS4) ((unsigned char) *PyBytes_AS_STRING(c));
	else if (PyByteArray_Check(c) &&  PyByteArray_GET_SIZE(c))
		return (Py_UCS4) ((unsigned char) *PyByteArray_AS_STRING(c));
	return (Py_UCS4) - 1;
}
```


<a id="case-005"></a>

## 5. `fromJPChar`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive helper.

Reads first codepoint directly from compact ASCII/1-byte/2-byte layout of JPype Unicode subclass.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L173-L187).

### Read sites

- Site 1: lines 175–186; derived read; index expression `data[0]`. Direct-layout fixed index

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L173-L187).

```cpp
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


<a id="case-006"></a>

## 6. `PyJPChar_new`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 189–240. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L189-L240).

### Read sites

- Site 1: lines 209–209; derived read; index expression `Py_UCS4 cv = ord(in);`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Omitted from `jpype1-1.7.1/native/python/pyjp_char.cpp`: lines 193–204, 214–237. The original contextual region was lines 189–240.

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 189–192. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L189-L192).

```cpp
static PyObject * PyJPChar_new(PyTypeObject *type, PyObject *pyargs, PyObject * kwargs)
{
	JP_PY_TRY("PyJPChar_new");
	// Get the Java class from the type.
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 205–213. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L205-L213).

```cpp
	}

	JPValue jv;
	PyObject *in = PyTuple_GetItem(pyargs, 0);
	Py_UCS4 cv = ord(in);

	JPJavaFrame frame = JPJavaFrame::outer();
	if (cv != (Py_UCS4) - 1)
	{
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 238–240. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L238-L240).

```cpp
	return self;
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-007"></a>

## 7. `PyJPChar_str`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 242–256. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L242-L256).

### Read sites

- Site 1: lines 254–254; derived read; index expression `return PyUnicode_FromOrdinal(fromJPChar(self));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 242–256. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L242-L256).

```cpp
static PyObject *PyJPChar_str(PyJPChar *self)
{
	JP_PY_TRY("PyJPChar_str");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (javaSlot == nullptr)
	{  // GCOVR_EXCL_START
		// A slot is required
		PyErr_SetString(PyExc_TypeError, "Java slot is not set on Java char");
		return nullptr;
	}  // GCOVR_EXCL_STOP
	if (isNull(javaSlot))
		return JPPyString::fromStringUTF8("None").keep();
	return PyUnicode_FromOrdinal(fromJPChar(self));
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-008"></a>

## 8. `PyJPChar_index`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 274–282. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L274-L282).

### Read sites

- Site 1: lines 280–280; derived read; index expression `return PyLong_FromLong(fromJPChar(self));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 274–282. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L274-L282).

```cpp
static PyObject *PyJPChar_index(PyJPChar *self)
{
	JP_PY_TRY("PyJPChar_index");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (assertNotNull(javaSlot))
		return nullptr;
	return PyLong_FromLong(fromJPChar(self));
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-009"></a>

## 9. `PyJPChar_float`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 284–292. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L284-L292).

### Read sites

- Site 1: lines 290–290; derived read; index expression `return PyFloat_FromDouble(fromJPChar(self));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 284–292. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L284-L292).

```cpp
static PyObject *PyJPChar_float(PyJPChar *self)
{
	JP_PY_TRY("PyJPChar_float");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (assertNotNull(javaSlot))
		return nullptr;
	return PyFloat_FromDouble(fromJPChar(self));
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-010"></a>

## 10. `PyJPChar_abs`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 294–305. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L294-L305).

### Read sites

- Site 1: lines 302–302; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 294–305. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L294-L305).

```cpp
static PyObject *PyJPChar_abs(PyJPChar *self)
{
	JP_PY_TRY("PyJPChar_nop");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (assertNotNull(javaSlot))
		return nullptr;

	// Promote to int as per Java rules
	JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));
	return PyLong_Type.tp_as_number->nb_absolute(v.get());
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-011"></a>

## 11. `apply`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 317–348. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L317-L348).

### Read sites

- Site 1: lines 327–327; derived read; index expression `JPPyObject v1 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));`. Scalar input helper reads original codepoint0
- Site 2: lines 328–328; derived read; index expression `JPPyObject v2 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));`. Scalar input helper reads original codepoint0
- Site 3: lines 336–336; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));`. Scalar input helper reads original codepoint0
- Site 4: lines 344–344; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 317–348. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L317-L348).

```cpp
static PyObject *apply(PyObject *first, PyObject *second, PyObject* (*func)(PyObject*, PyObject*))
{
	JPValue *slot0 = PyJPValue_getJavaSlot(first);
	JPValue *slot1 = PyJPValue_getJavaSlot(second);
	if (slot0 != nullptr && slot1 != nullptr)
	{
		if (assertNotNull(slot0))
			return nullptr;
		if (assertNotNull(slot1))
			return nullptr;
		JPPyObject v1 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));
		JPPyObject v2 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));
		return func(v1.get(), v2.get());
	}
	else if (slot0 != nullptr)
	{
		if (assertNotNull(slot0))
			return nullptr;
		// Promote to int as per Java rules
		JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));
		return func(v.get(), second);
	}
	else if (slot1 != nullptr)
	{
		if (assertNotNull(slot1))
			return nullptr;
		// Promote to int as per Java rules
		JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));
		return func(first, v.get());
	}
	return notSupported();
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-012"></a>

## 12. `PyJPChar_add`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 372–411. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L372-L411).

### Read sites

- Site 1: lines 383–383; derived read; index expression `JPPyObject v1 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));`. Scalar input helper reads original codepoint0
- Site 2: lines 384–384; derived read; index expression `JPPyObject v2 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));`. Scalar input helper reads original codepoint0
- Site 3: lines 395–395; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));`. Scalar input helper reads original codepoint0
- Site 4: lines 406–406; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Omitted from `jpype1-1.7.1/native/python/pyjp_char.cpp`: lines 376–378, 389–390, 400–401. The original contextual region was lines 372–411.

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 372–375. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L372-L375).

```cpp
static  PyObject *PyJPChar_add(PyObject *first, PyObject *second)
{
	JP_PY_TRY("PyJPChar_add");
	JPValue *slot0 = PyJPValue_getJavaSlot(first);
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 379–388. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L379-L388).

```cpp
		if (assertNotNull(slot0))
			return nullptr;
		if (assertNotNull(slot1))
			return nullptr;
		JPPyObject v1 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));
		JPPyObject v2 = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));
		return PyNumber_Add(v1.get(), v2.get());
	}
	else if (slot0 != nullptr)
	{
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 391–399. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L391-L399).

```cpp
		if (PyUnicode_Check(second))
			return PyUnicode_Concat(first, second);

		// Promote to int as per Java rules
		JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)first)));
		return PyNumber_Add(v.get(), second);
	}
	else if (slot1 != nullptr)
	{
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 402–411. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L402-L411).

```cpp
		if (PyUnicode_Check(first))
			return PyUnicode_Concat(first, second);

		// Promote to int as per Java rules
		JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*)second)));
		return PyNumber_Add(first, v.get());
	}
	return notSupported();
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-013"></a>

## 13. `PyJPChar_neg`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 456–466. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L456-L466).

### Read sites

- Site 1: lines 463–463; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 456–466. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L456-L466).

```cpp
static PyObject *PyJPChar_neg(PyJPChar *self)
{
	JP_PY_TRY("PyJPChar_neg");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (assertNotNull(javaSlot))
		return nullptr;
	// Promote to int as per Java rules
	JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));
	return PyNumber_Negative(v.get());
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-014"></a>

## 14. `PyJPChar_pos`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 468–478. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L468-L478).

### Read sites

- Site 1: lines 475–475; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 468–478. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L468-L478).

```cpp
static PyObject *PyJPChar_pos(PyJPChar *self)
{
	JP_PY_TRY("PyJPChar_pos");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (assertNotNull(javaSlot))
		return nullptr;
	// Promote to int as per Java rules
	JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));
	return PyNumber_Positive(v.get());
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-015"></a>

## 15. `PyJPChar_inv`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 480–490. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L480-L490).

### Read sites

- Site 1: lines 487–487; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 480–490. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L480-L490).

```cpp
static PyObject *PyJPChar_inv(PyJPChar *self)
{
	JP_PY_TRY("PyJPObject_neg");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (assertNotNull(javaSlot))
		return nullptr;
	// Promote to int as per Java rules
	JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar(self)));
	return PyNumber_Invert(v.get());
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-016"></a>

## 16. `PyJPJChar_compare`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 492–554. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L492-L554).

### Read sites

- Site 1: lines 521–521; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*) self)));`. Scalar input helper reads original codepoint0
- Site 2: lines 530–530; derived read; index expression `JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*) self)));`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Omitted from `jpype1-1.7.1/native/python/pyjp_char.cpp`: lines 496–516, 535–551. The original contextual region was lines 492–554.

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 492–495. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L492-L495).

```cpp
static PyObject *PyJPJChar_compare(PyObject *self, PyObject *other, int op)
{
	JP_PY_TRY("PyJPJChar_compare");
	JPValue *javaSlot1 = PyJPValue_getJavaSlot(other);
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 517–534. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L517-L534).

```cpp
		return PyUnicode_Type.tp_richcompare(self, other, op);
	}
	if (PyFloat_Check(other))
	{
		JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*) self)));
		if (op < 2)
			op += 4;
		else if (op > 3)
			op -= 4;
		return PyFloat_Type.tp_richcompare(other, v.get(), op);
	}
	if (PyNumber_Check(other))
	{
		JPPyObject v = JPPyObject::call(PyLong_FromLong(fromJPChar((PyJPChar*) self)));
		return PyLong_Type.tp_richcompare(v.get(), other, op);
	}
	if (javaSlot1 != nullptr)
	{
```

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 552–554. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L552-L554).

```cpp
	return out;
	JP_PY_CATCH(nullptr);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-017"></a>

## 17. `PyJPChar_bool`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Owning conversion/arithmetic/comparison operation invokes ord/fromJPChar to read fixed codepoint0 of original Python Unicode or JPype Unicode-char subclass; no full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Role=owning_consumer; arithmetic wrappers merely passing objects onward to apply are separately excluded, not recursively duplicated.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 566–574. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L566-L574).

### Read sites

- Site 1: lines 572–572; derived read; index expression `return fromJPChar(self) != 0;`. Scalar input helper reads original codepoint0

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 566–574. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L566-L574).

```cpp
static int PyJPChar_bool(PyJPChar *self)
{
	JP_PY_TRY("PyJPObject_bool");
	JPValue *javaSlot = PyJPValue_getJavaSlot((PyObject*) self);
	if (isNull(javaSlot))
		return 0;
	return fromJPChar(self) != 0;
	JP_PY_CATCH(0);  // GCOVR_EXCL_LINE
}
```

### Callee analysis

- `ord` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ_CHAR(obj,0) after length1 check
- `fromJPChar` in `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187: Exact frozen sdist source recovered and manually inspected B direct compact/1/2byte data[0]

Available source context:

- [`ord`](#helper-006) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53).
- [`fromJPChar`](#helper-007) (`jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187).

<a id="case-018"></a>

## 18. `PyJPClass_getattro`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Single fixed character inspection, not full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 437–470. Member SHA-256: `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L437-L470).

### Read sites

- Site 1: lines 455–455; derived read; index expression `0`. ReadChar selector

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 437–470. Member SHA-256: `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L437-L470).

```cpp
PyObject *PyJPClass_getattro(PyObject *obj, PyObject *name)
{
	JP_PY_TRY("PyJPClass_getattro");
	if (!PyUnicode_Check(name))
	{
		PyErr_Format(PyExc_TypeError,
				"attribute name must be string, not '%.200s'",
				Py_TYPE(name)->tp_name);
		return nullptr;
	}

	// Private members are accessed directly
	PyObject* pyattr = PyType_Type.tp_getattro(obj, name);
	if (pyattr == nullptr)
		return nullptr;
	JPPyObject attr = JPPyObject::claim(pyattr);

	// Private members go regardless
	if (PyUnicode_GetLength(name) && PyUnicode_ReadChar(name, 0) == '_')
		return attr.keep();

	// Methods
	if (Py_TYPE(attr.get()) == PyJPMethod_Type)
		return attr.keep();

	// Don't allow properties to be rewritten
	if (!PyObject_IsInstance(attr.get(), (PyObject*) & PyProperty_Type))
		return attr.keep();

	const char *name_str = PyUnicode_AsUTF8(name);
	PyErr_Format(PyExc_AttributeError, "Field '%s' is static", name_str);
	return nullptr;
	JP_PY_CATCH(nullptr);
}
```


<a id="case-019"></a>

## 19. `PyJPClass_setattro`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Single fixed character inspection, not full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 472–507. Member SHA-256: `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L472-L507).

### Read sites

- Site 1: lines 485–485; derived read; index expression `0`. ReadChar selector

### Contextual source excerpts

Omitted from `jpype1-1.7.1/native/python/pyjp_class.cpp`: lines 476–480, 490–504. The original contextual region was lines 472–507.

Archive member `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 472–475. Member SHA-256: `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L472-L475).

```cpp
int PyJPClass_setattro(PyObject *self, PyObject *attr_name, PyObject *v)
{
	JP_PY_TRY("PyJPClass_setattro");
	PyJPModule_getContext();
```

Archive member `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 481–489. Member SHA-256: `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L481-L489).

```cpp
		return -1;
	}

	// Private members are accessed directly
	if (PyUnicode_GetLength(attr_name) && PyUnicode_ReadChar(attr_name, 0) == '_')
		return PyType_Type.tp_setattro(self, attr_name, v);

	JPPyObject f = JPPyObject::accept(PyJP_GetAttrDescriptor((PyTypeObject*) self, attr_name));
	if (f.isNull())
```

Archive member `jpype1-1.7.1/native/python/pyjp_class.cpp`, lines 505–507. Member SHA-256: `eef21a4a870f32eefdd21e75348e43d9bdcc6d199c708ff6b534b65774e9dea3`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_class.cpp#L505-L507).

```cpp
	return -1;
	JP_PY_CATCH(-1);
}
```


<a id="case-020"></a>

## 20. `PyJPModule_collect`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Single fixed character inspection, not full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_module.cpp`, lines 582–601. Member SHA-256: `fb9bf08fab6e3360d64344a003ab620314e8eee2d991eec7cf50b416b2e70cb4`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_module.cpp#L582-L601).

### Read sites

- Site 1: lines 593–593; derived read; index expression `2`. ReadChar selector

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_module.cpp`, lines 582–601. Member SHA-256: `fb9bf08fab6e3360d64344a003ab620314e8eee2d991eec7cf50b416b2e70cb4`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_module.cpp#L582-L601).

```cpp
PyObject *PyJPModule_collect(PyObject* module, PyObject *obj)
{
	JPContext* context = JPContext_global;
	if (!context->isRunning())
		Py_RETURN_NONE;
	PyObject *a1 = PyTuple_GetItem(obj, 0);
	if (!PyUnicode_Check(a1))
	{
		PyErr_SetString(PyExc_TypeError, "Bad callback argument");
		return nullptr;
	}
	if (PyUnicode_ReadChar(a1, 2) == 'a')
	{
		context->m_GC->onStart();
	} else
	{
		context->m_GC->onEnd();
	}
	Py_RETURN_NONE;
}
```


<a id="case-021"></a>

## 21. `PyJPValue_getattro`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Single fixed character inspection, not full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_value.cpp`, lines 190–222. Member SHA-256: `033dc39e9780b86520c3fcb1567b05822d62f4b7258906229e789adc655be83e`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_value.cpp#L190-L222).

### Read sites

- Site 1: lines 208–208; derived read; index expression `0`. ReadChar selector

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_value.cpp`, lines 190–222. Member SHA-256: `033dc39e9780b86520c3fcb1567b05822d62f4b7258906229e789adc655be83e`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_value.cpp#L190-L222).

```cpp
PyObject *PyJPValue_getattro(PyObject *obj, PyObject *name)
{
	JP_PY_TRY("PyJPObject_getattro");
	if (!PyUnicode_Check(name))
	{
		PyErr_Format(PyExc_TypeError,
				"attribute name must be string, not '%.200s'",
				Py_TYPE(name)->tp_name);
		return nullptr;
	}

	// Private members are accessed directly
	PyObject* pyattr = PyBaseObject_Type.tp_getattro(obj, name);
	if (pyattr == nullptr)
		return nullptr;
	JPPyObject attr = JPPyObject::accept(pyattr);

	// Private members go regardless
	if (PyUnicode_GetLength(name) && PyUnicode_ReadChar(name, 0) == '_')
		return attr.keep();

	// Methods
	if (Py_TYPE(attr.get()) == (PyTypeObject*) PyJPMethod_Type)
		return attr.keep();

	// Don't allow properties to be rewritten
	if (!PyObject_IsInstance(attr.get(), (PyObject*) & PyProperty_Type))
		return attr.keep();

	PyErr_Format(PyExc_AttributeError, "Field '%U' is static", name);
	return nullptr;
	JP_PY_CATCH(nullptr);
}
```


<a id="case-022"></a>

## 22. `PyJPValue_setattro`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Single fixed character inspection, not full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/48/a2/5d27e81d24eef64668bf702bfe0e091cc48388b4666f36e025243eb9d827/jpype1-1.7.1.tar.gz). Archive SHA-256: `3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2`.

**Function source:** `jpype1-1.7.1/native/python/pyjp_value.cpp`, lines 224–246. Member SHA-256: `033dc39e9780b86520c3fcb1567b05822d62f4b7258906229e789adc655be83e`.

[Verified immutable function link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_value.cpp#L224-L246).

### Read sites

- Site 1: lines 229–229; derived read; index expression `0`. ReadChar selector

### Contextual source excerpts

Archive member `jpype1-1.7.1/native/python/pyjp_value.cpp`, lines 224–246. Member SHA-256: `033dc39e9780b86520c3fcb1567b05822d62f4b7258906229e789adc655be83e`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_value.cpp#L224-L246).

```cpp
int PyJPValue_setattro(PyObject *self, PyObject *name, PyObject *value)
{
	JP_PY_TRY("PyJPObject_setattro");

	// Private members are accessed directly
	if (PyUnicode_GetLength(name) && PyUnicode_ReadChar(name, 0) == '_')
		return PyObject_GenericSetAttr(self, name, value);
	JPPyObject f = JPPyObject::accept(PyJP_GetAttrDescriptor(Py_TYPE(self), name));
	if (f.isNull())
	{
		PyErr_Format(PyExc_AttributeError, "Field '%U' is not found", name);
		return -1;
	}
	descrsetfunc desc = Py_TYPE(f.get())->tp_descr_set;
	if (desc != nullptr)
		return desc(f.get(), self, value);

	// Not a descriptor
	PyErr_Format(PyExc_AttributeError,
			"Field '%U' is not settable on Java '%s' object", name, Py_TYPE(self)->tp_name);
	return -1;
	JP_PY_CATCH(-1);
}
```


<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `JPPyString::asCharUTF16`

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 220–223. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L220-L223).

```cpp
jchar JPPyString::asCharUTF16(PyObject* pyobj)
{
	if (PyIndex_Check(pyobj))
	{
```

<a id="helper-002"></a>

### 2. `JPPyString::asCharUTF16`

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 233–241. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L233-L241).

```cpp
		int sz = PyBytes_Size(pyobj);
		if (sz != 1)
			JP_RAISE(PyExc_ValueError, "Char must be length 1");

		jchar c = PyBytes_AsString(pyobj)[0];
		if (PyErr_Occurred())
			JP_RAISE_PYTHON();
		return c;
	}
```

<a id="helper-003"></a>

### 3. `JPPyString::asCharUTF16`

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 243–251. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L243-L251).

```cpp
	{
		if (PyUnicode_GetLength(pyobj) > 1)
			JP_RAISE(PyExc_ValueError, "Char must be length 1");

		PyUnicode_READY(pyobj);
		Py_UCS4 value = PyUnicode_READ_CHAR(pyobj, 0);
		if (value > 0xffff)
		{
			JP_RAISE(PyExc_ValueError, "Unable to pack 4 byte unicode into Java char");
```

<a id="helper-004"></a>

### 4. `JPPyString::asCharUTF16`

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 262–276. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L262-L276).

```cpp
		jchar c = PyBytes_AsString(pyobj)[0];
		JP_PY_CHECK();
		return c;
	}
	if (PyUnicode_Check(pyobj))
	{
		if (PyUnicode_GetLength(pyobj) > 1)
			JP_RAISE(PyExc_ValueError, "Char must be length 1");

		PyUnicode_READY(pyobj);
		Py_UCS4 value = PyUnicode_ReadChar(pyobj, 0);
		if (value > 0xffff)
		{
			JP_RAISE(PyExc_ValueError, "Unable to pack 4 byte unicode into Java char");
		}
```

<a id="helper-005"></a>

### 5. `JPPyString::asCharUTF16`

Archive member `jpype1-1.7.1/native/python/jp_pythontypes.cpp`, lines 280–282. Member SHA-256: `b7b442a1c22f5a792371dd96a6d8b7a62e78754ae02ae66a3443ad94e995bd61`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/jp_pythontypes.cpp#L280-L282).

```cpp
	PyErr_Format(PyExc_TypeError, "Unable to convert '%s' to Java char", Py_TYPE(pyobj)->tp_name);
	JP_RAISE_PYTHON();
}
```

<a id="helper-006"></a>

### 6. `ord`

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 40–53. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L40-L53).

```cpp
static Py_UCS4 ord(PyObject *c)
{
	if (PyUnicode_Check(c))
	{
		if (PyUnicode_READY(c) == -1)
			return -1;
		if (PyUnicode_GET_LENGTH(c) == 1)
			return PyUnicode_READ_CHAR(c, 0);
	} else if (PyBytes_Check(c) && PyBytes_GET_SIZE(c) == 1)
		return (Py_UCS4) ((unsigned char) *PyBytes_AS_STRING(c));
	else if (PyByteArray_Check(c) &&  PyByteArray_GET_SIZE(c))
		return (Py_UCS4) ((unsigned char) *PyByteArray_AS_STRING(c));
	return (Py_UCS4) - 1;
}
```

<a id="helper-007"></a>

### 7. `fromJPChar`

Archive member `jpype1-1.7.1/native/python/pyjp_char.cpp`, lines 173–187. Member SHA-256: `452af5b51013e887457cbb936db15cbfb1908c939c6db4110a6d4ec09b13becf`. [Verified immutable source link](https://github.com/jpype-project/jpype/blob/6b63aca75b8273f5aeb7e82b696418679b07b60a/native/python/pyjp_char.cpp#L173-L187).

```cpp
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
