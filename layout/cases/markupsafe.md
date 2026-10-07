# markupsafe 3.0.3

0 confirmed layout regions; 4 reviewed regions including non-direct context.

## L1031: escape_unicode_kind1

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Parameter is typed PyUnicodeObject*, while payload and length are obtained exclusively through PyUnicode_1BYTE_DATA/PyUnicode_GET_LENGTH APIs.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c:75–98`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 75–80 ([verified immutable source](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L75-L80))

```
escape_unicode_kind1(PyUnicodeObject *in)
{
	Py_UCS1 *inp = PyUnicode_1BYTE_DATA(in);
	Py_UCS1 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS1 *outp;
	PyObject *out;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz); archive SHA-256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

## L1032: escape_unicode_kind2

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Parameter is typed PyUnicodeObject*, while payload and length are obtained exclusively through PyUnicode_2BYTE_DATA/PyUnicode_GET_LENGTH APIs.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c:101–123`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 101–106 ([verified immutable source](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L101-L106))

```
escape_unicode_kind2(PyUnicodeObject *in)
{
	Py_UCS2 *inp = PyUnicode_2BYTE_DATA(in);
	Py_UCS2 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS2 *outp;
	PyObject *out;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz); archive SHA-256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

## L1033: escape_unicode_kind4

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Parameter is typed PyUnicodeObject*, while payload and length are obtained exclusively through PyUnicode_4BYTE_DATA/PyUnicode_GET_LENGTH APIs.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c:127–149`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 127–132 ([verified immutable source](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L127-L132))

```
escape_unicode_kind4(PyUnicodeObject *in)
{
	Py_UCS4 *inp = PyUnicode_4BYTE_DATA(in);
	Py_UCS4 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS4 *outp;
	PyObject *out;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz); archive SHA-256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

## L1034: escape_unicode typed dispatcher

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Casts an opaque input pointer to PyUnicodeObject* for the typed API helper calls; KIND controls dispatch.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c:151–171`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 161–168 ([verified immutable source](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L161-L168))

```
	switch (PyUnicode_KIND(s)) {
	case PyUnicode_1BYTE_KIND:
		return escape_unicode_kind1((PyUnicodeObject*) s);
	case PyUnicode_2BYTE_KIND:
		return escape_unicode_kind2((PyUnicodeObject*) s);
	case PyUnicode_4BYTE_KIND:
		return escape_unicode_kind4((PyUnicodeObject*) s);
	}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz); archive SHA-256 `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.
