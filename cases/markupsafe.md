# markupsafe — non-simple Unicode reads

[All packages](README.md)

Version: 3.0.3. **3 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`escape_unicode_kind1`](#case-001)
- [`escape_unicode_kind2`](#case-002)
- [`escape_unicode_kind4`](#case-003)

<a id="case-001"></a>

## 1. `escape_unicode_kind1`

**Classification:** B. **Subtypes:** multiple passes, reset or backtracking. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

GET_DELTA consumes the full input, then inp resets to its initial DATA pointer and DO_ESCAPE traverses it again; DO_ESCAPE also bulk-copies earlier runs using inp-ncopy.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Pointer inp_end from first getter is retained across a second DATA call; a new fallible FSR materializer must specify stability. Current same-representation getter does not invalidate it.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz). Archive SHA-256: `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

**Function source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 75–98. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

[Verified immutable function link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L75-L98).

### Read sites

- Site 1: lines 77–84; derived read; index expression `*inp++`. First full pass, GET_DELTA macro
- Site 2: lines 94–96; derived read; index expression `*inp; inp-ncopy`. Second pass after pointer reset and copies of already inspected spans

### Contextual source excerpts

Omitted from `markupsafe-3.0.3/src/markupsafe/_speedups.c`: lines 9–16, 26–69. The original contextual region was lines 3–72.

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 3–8. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L3-L8).

```c
#define GET_DELTA(inp, inp_end, delta) \
	while (inp < inp_end) { \
		switch (*inp++) { \
		case '"': \
		case '\'': \
		case '&': \
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 17–25. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L17-L25).

```c

#define DO_ESCAPE(inp, inp_end, outp) \
	{ \
		Py_ssize_t ncopy = 0; \
		while (inp < inp_end) { \
			switch (*inp) { \
			case '"': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 70–72. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L70-L72).

```c
		} \
		memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
	}
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 75–98. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L75-L98).

```c
escape_unicode_kind1(PyUnicodeObject *in)
{
	Py_UCS1 *inp = PyUnicode_1BYTE_DATA(in);
	Py_UCS1 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS1 *outp;
	PyObject *out;
	Py_ssize_t delta = 0;

	GET_DELTA(inp, inp_end, delta);
	if (!delta) {
		Py_INCREF(in);
		return (PyObject*)in;
	}

	out = PyUnicode_New(PyUnicode_GET_LENGTH(in) + delta,
						PyUnicode_IS_ASCII(in) ? 127 : 255);
	if (!out)
		return NULL;

	inp = PyUnicode_1BYTE_DATA(in);
	outp = PyUnicode_1BYTE_DATA(out);
	DO_ESCAPE(inp, inp_end, outp);
	return out;
}
```


<a id="case-002"></a>

## 2. `escape_unicode_kind2`

**Classification:** B. **Subtypes:** multiple passes, reset or backtracking. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

GET_DELTA consumes the full input, then inp resets to its initial DATA pointer and DO_ESCAPE traverses it again; DO_ESCAPE also bulk-copies earlier runs using inp-ncopy.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Pointer inp_end from first getter is retained across a second DATA call; a new fallible FSR materializer must specify stability. Current same-representation getter does not invalidate it.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz). Archive SHA-256: `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

**Function source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 101–123. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

[Verified immutable function link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L101-L123).

### Read sites

- Site 1: lines 103–110; derived read; index expression `*inp++`. First full pass, GET_DELTA macro
- Site 2: lines 119–121; derived read; index expression `*inp; inp-ncopy`. Second pass after pointer reset and copies of already inspected spans

### Contextual source excerpts

Omitted from `markupsafe-3.0.3/src/markupsafe/_speedups.c`: lines 9–16, 26–69. The original contextual region was lines 3–72.

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 3–8. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L3-L8).

```c
#define GET_DELTA(inp, inp_end, delta) \
	while (inp < inp_end) { \
		switch (*inp++) { \
		case '"': \
		case '\'': \
		case '&': \
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 17–25. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L17-L25).

```c

#define DO_ESCAPE(inp, inp_end, outp) \
	{ \
		Py_ssize_t ncopy = 0; \
		while (inp < inp_end) { \
			switch (*inp) { \
			case '"': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 70–72. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L70-L72).

```c
		} \
		memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
	}
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 101–123. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L101-L123).

```c
escape_unicode_kind2(PyUnicodeObject *in)
{
	Py_UCS2 *inp = PyUnicode_2BYTE_DATA(in);
	Py_UCS2 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS2 *outp;
	PyObject *out;
	Py_ssize_t delta = 0;

	GET_DELTA(inp, inp_end, delta);
	if (!delta) {
		Py_INCREF(in);
		return (PyObject*)in;
	}

	out = PyUnicode_New(PyUnicode_GET_LENGTH(in) + delta, 65535);
	if (!out)
		return NULL;

	inp = PyUnicode_2BYTE_DATA(in);
	outp = PyUnicode_2BYTE_DATA(out);
	DO_ESCAPE(inp, inp_end, outp);
	return out;
}
```


<a id="case-003"></a>

## 3. `escape_unicode_kind4`

**Classification:** B. **Subtypes:** multiple passes, reset or backtracking. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

GET_DELTA consumes the full input, then inp resets to its initial DATA pointer and DO_ESCAPE traverses it again; DO_ESCAPE also bulk-copies earlier runs using inp-ncopy.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Pointer inp_end from first getter is retained across a second DATA call; a new fallible FSR materializer must specify stability. Current same-representation getter does not invalidate it.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz). Archive SHA-256: `722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698`.

**Function source:** `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 127–149. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`.

[Verified immutable function link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L127-L149).

### Read sites

- Site 1: lines 129–136; derived read; index expression `*inp++`. First full pass, GET_DELTA macro
- Site 2: lines 145–147; derived read; index expression `*inp; inp-ncopy`. Second pass after pointer reset and copies of already inspected spans

### Contextual source excerpts

Omitted from `markupsafe-3.0.3/src/markupsafe/_speedups.c`: lines 9–16, 26–69. The original contextual region was lines 3–72.

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 3–8. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L3-L8).

```c
#define GET_DELTA(inp, inp_end, delta) \
	while (inp < inp_end) { \
		switch (*inp++) { \
		case '"': \
		case '\'': \
		case '&': \
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 17–25. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L17-L25).

```c

#define DO_ESCAPE(inp, inp_end, outp) \
	{ \
		Py_ssize_t ncopy = 0; \
		while (inp < inp_end) { \
			switch (*inp) { \
			case '"': \
				memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
				outp += ncopy; ncopy = 0; \
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 70–72. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L70-L72).

```c
		} \
		memcpy(outp, inp-ncopy, sizeof(*outp)*ncopy); \
	}
```

Archive member `markupsafe-3.0.3/src/markupsafe/_speedups.c`, lines 127–149. Member SHA-256: `b77b42ea8555efe6e6294aaf08ee69552932f86f000885e958c689c2436d2638`. [Verified immutable source link](https://github.com/pallets/markupsafe/blob/297fc8e356e6836a62087949245d09a28e9f1b13/src/markupsafe/_speedups.c#L127-L149).

```c
escape_unicode_kind4(PyUnicodeObject *in)
{
	Py_UCS4 *inp = PyUnicode_4BYTE_DATA(in);
	Py_UCS4 *inp_end = inp + PyUnicode_GET_LENGTH(in);
	Py_UCS4 *outp;
	PyObject *out;
	Py_ssize_t delta = 0;

	GET_DELTA(inp, inp_end, delta);
	if (!delta) {
		Py_INCREF(in);
		return (PyObject*)in;
	}

	out = PyUnicode_New(PyUnicode_GET_LENGTH(in) + delta, 1114111);
	if (!out)
		return NULL;

	inp = PyUnicode_4BYTE_DATA(in);
	outp = PyUnicode_4BYTE_DATA(out);
	DO_ESCAPE(inp, inp_end, outp);
	return out;
}
```
