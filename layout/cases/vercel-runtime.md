# vercel-runtime 0.23.2

0 confirmed layout regions; 4 reviewed regions including non-direct context.

## L1035: escape_unicode_kind1

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Parameter is typed PyUnicodeObject*, while payload and length are obtained exclusively through PyUnicode_1BYTE_DATA/PyUnicode_GET_LENGTH APIs.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `vercel_runtime-0.23.2/src/vercel_runtime/_vendor/markupsafe/_speedups.c:75–98`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 75–80 (immutable GitHub mapping unavailable in saved verification evidence)

```
escape_unicode_kind1(PyUnicodeObject *in)
{
	Py_UCS1 *inp = PyUnicode_1BYTE_DATA(in);
	Py_UCS1 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS1 *outp;
	PyObject *out;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/35/d6/c689033a2b3a2d69caf39e39f17ac0aba3f0d7570af0d22fc01eb0b367ca/vercel_runtime-0.23.2.tar.gz); archive SHA-256 `252e517b6b7aadbd3edf5faac7bc387adde32b3801c1d5cfeb118ea29e89cb8a`.

## L1036: escape_unicode_kind2

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Parameter is typed PyUnicodeObject*, while payload and length are obtained exclusively through PyUnicode_2BYTE_DATA/PyUnicode_GET_LENGTH APIs.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `vercel_runtime-0.23.2/src/vercel_runtime/_vendor/markupsafe/_speedups.c:101–123`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 101–106 (immutable GitHub mapping unavailable in saved verification evidence)

```
escape_unicode_kind2(PyUnicodeObject *in)
{
	Py_UCS2 *inp = PyUnicode_2BYTE_DATA(in);
	Py_UCS2 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS2 *outp;
	PyObject *out;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/35/d6/c689033a2b3a2d69caf39e39f17ac0aba3f0d7570af0d22fc01eb0b367ca/vercel_runtime-0.23.2.tar.gz); archive SHA-256 `252e517b6b7aadbd3edf5faac7bc387adde32b3801c1d5cfeb118ea29e89cb8a`.

## L1037: escape_unicode_kind4

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Parameter is typed PyUnicodeObject*, while payload and length are obtained exclusively through PyUnicode_4BYTE_DATA/PyUnicode_GET_LENGTH APIs.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `vercel_runtime-0.23.2/src/vercel_runtime/_vendor/markupsafe/_speedups.c:127–149`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 127–132 (immutable GitHub mapping unavailable in saved verification evidence)

```
escape_unicode_kind4(PyUnicodeObject *in)
{
	Py_UCS4 *inp = PyUnicode_4BYTE_DATA(in);
	Py_UCS4 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS4 *outp;
	PyObject *out;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/35/d6/c689033a2b3a2d69caf39e39f17ac0aba3f0d7570af0d22fc01eb0b367ca/vercel_runtime-0.23.2.tar.gz); archive SHA-256 `252e517b6b7aadbd3edf5faac7bc387adde32b3801c1d5cfeb118ea29e89cb8a`.

## L1038: escape_unicode typed dispatcher

**Classification:** non-direct context; project_source; `typed_api_only`.

**Purpose:** Casts an opaque input pointer to PyUnicodeObject* for the typed API helper calls; KIND controls dispatch.

**Migration effect:** The type annotation/cast itself does not inspect struct fields or assume header size. DATA/KIND API representation dependencies belong to the separate API survey; replacing an exposed struct type may still require an annotation change.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `vercel_runtime-0.23.2/src/vercel_runtime/_vendor/markupsafe/_speedups.c:151–171`. SHA-256 `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

Lines 161–168 (immutable GitHub mapping unavailable in saved verification evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/35/d6/c689033a2b3a2d69caf39e39f17ac0aba3f0d7570af0d22fc01eb0b367ca/vercel_runtime-0.23.2.tar.gz); archive SHA-256 `252e517b6b7aadbd3edf5faac7bc387adde32b3801c1d5cfeb118ea29e89cb8a`.
