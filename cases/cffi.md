# cffi — non-simple Unicode reads

[All packages](README.md)

Version: 2.1.1. **7 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`_convert_to_char16_t`](#case-001)
- [`_convert_to_char32_t`](#case-002)
- [`convert_array_from_object`](#case-003)
- [`cast_to_integer_or_char`](#case-004)
- [`check_bytes_for_float_compatible`](#case-005)
- [`_my_PyUnicode_AsSingleChar16`](#case-006)
- [`_my_PyUnicode_AsSingleChar32`](#case-007)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `_convert_to_char16_t`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Unicode branch invokes validated single-character helper at index0; other branches consume external CData/bytes/numbers.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Direct helper consumer; not all transitive callers counted.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1250–1272. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1250-L1272).

### Read sites

- Site 1: lines 1255–1258; scalar helper; index expression `0`. Delegates to _my_PyUnicode_AsSingleChar16/32.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1255–1258. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1255-L1258).

```c
    if (PyUnicode_Check(init)) {
        cffi_char16_t ordinal;
        if (_my_PyUnicode_AsSingleChar16(init, &ordinal, err_got) == 0)
            return ordinal;
```

### Callee analysis

- `_my_PyUnicode_AsSingleChar16/32` in `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89: length1 guard and READ_CHAR(unicode,0). B scalar

Available source context:

- [`_my_PyUnicode_AsSingleChar16/32`](#helper-001) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89).

<a id="case-002"></a>

## 2. `_convert_to_char32_t`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Unicode branch invokes validated single-character helper at index0; other branches consume external CData/bytes/numbers.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Direct helper consumer; not all transitive callers counted.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1274–1296. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1274-L1296).

### Read sites

- Site 1: lines 1279–1282; scalar helper; index expression `0`. Delegates to _my_PyUnicode_AsSingleChar16/32.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1279–1282. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1279-L1282).

```c
    if (PyUnicode_Check(init)) {
        cffi_char32_t ordinal;
        if (_my_PyUnicode_AsSingleChar32(init, &ordinal, err_got) == 0)
            return ordinal;
```

### Callee analysis

- `_my_PyUnicode_AsSingleChar16/32` in `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89: length1 guard and READ_CHAR(unicode,0). B scalar

Available source context:

- [`_my_PyUnicode_AsSingleChar16/32`](#helper-001) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89).

<a id="case-003"></a>

## 3. `convert_array_from_object`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Unicode char16 array path first counts expanded UTF16 length then invokes conversion helper which restarts at zero. char32 path bulk materializes UCS4.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1476–1571. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1476-L1571).

### Read sites

- Site 1: lines 1528–1552; two helpers; index expression `SizeAsChar16 then AsChar16: both start0`. Sizing pass then conversion pass; char32 instead uses AsUCS4.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1476–1482. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1476-L1482).

```c
convert_array_from_object(char *data, CTypeDescrObject *ct, PyObject *init)
{
    /* used by convert_from_object(), and also to decode lists/tuples/unicodes
       passed as function arguments.  'ct' is an CT_ARRAY in the first case
       and a CT_POINTER in the second case. */
    const char *expected;
    CTypeDescrObject *ctitem = ct->ct_itemdescr;
```

Archive member `cffi-2.1.1/src/c/_cffi_backend.c`, lines 1528–1552. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L1528-L1552).

```c
        else {
            Py_ssize_t n;
            if (!PyUnicode_Check(init)) {
                expected = "unicode or list or tuple";
                goto cannot_convert;
            }

            if (ctitem->ct_size == 4)
                n = _my_PyUnicode_SizeAsChar32(init);
            else
                n = _my_PyUnicode_SizeAsChar16(init);

            if (ct->ct_length >= 0 && n > ct->ct_length) {
                PyErr_Format(PyExc_IndexError,
                             "initializer unicode is too long for '%s' "
                             "(got %zd characters)", ct->ct_name, n);
                return -1;
            }
            if (n != ct->ct_length)
                n++;
            if (ctitem->ct_size == 4)
                return _my_PyUnicode_AsChar32(init, (cffi_char32_t *)data, n);
            else
                return _my_PyUnicode_AsChar16(init, (cffi_char16_t *)data, n);
        }
```

### Callee analysis

- `_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16` in `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 91–140: Each scans i=0 through full Unicode length. B two passes

Available source context:
Omitted from `cffi-2.1.1/src/c/wchar_helper_3.h`: lines 106–109, 119, 133–137. The original contextual region was lines 91–140.

- [`_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`](#helper-002) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 91–105).
- [`_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`](#helper-003) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 110–118).
- [`_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`](#helper-004) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 120–132).
- [`_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`](#helper-005) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 138–140).

<a id="case-004"></a>

## 4. `cast_to_integer_or_char`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Unicode branch invokes validated single-character helper at index0; other branches consume external CData/bytes/numbers.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Direct helper consumer; not all transitive callers counted.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/_cffi_backend.c`, lines 4020–4081. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L4020-L4081).

### Read sites

- Site 1: lines 4030–4046; scalar helper; index expression `0`. Delegates to _my_PyUnicode_AsSingleChar16/32.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/_cffi_backend.c`, lines 4030–4046. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L4030-L4046).

```c
    else if (PyUnicode_Check(ob)) {
        char err_buf[80];
        cffi_char32_t ordinal;
        if (_my_PyUnicode_AsSingleChar32(ob, &ordinal, err_buf) < 0) {
            PyErr_Format(PyExc_TypeError,
                         "cannot cast %s to ctype '%s'", err_buf, ct->ct_name);
            return NULL;
        }
        /* the types char16_t and char32_t are both unsigned.  However,
           wchar_t might be signed.  In theory it does not matter,
           because 'ordinal' comes from a regular Python unicode. */
#ifdef HAVE_WCHAR_H
        if (ct->ct_flags & CT_IS_SIGNED_WCHAR)
            value = (wchar_t)ordinal;
        else
#endif
            value = ordinal;
```

### Callee analysis

- `_my_PyUnicode_AsSingleChar16/32` in `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89: length1 guard and READ_CHAR(unicode,0). B scalar

Available source context:

- [`_my_PyUnicode_AsSingleChar16/32`](#helper-001) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89).

<a id="case-005"></a>

## 5. `check_bytes_for_float_compatible`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Unicode branch invokes validated single-character helper at index0; other branches consume external CData/bytes/numbers.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Direct helper consumer; not all transitive callers counted.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/_cffi_backend.c`, lines 4084–4110. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L4084-L4110).

### Read sites

- Site 1: lines 4092–4101; scalar helper; index expression `0`. Delegates to _my_PyUnicode_AsSingleChar16/32.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/_cffi_backend.c`, lines 4092–4101. Member SHA-256: `335899c93f88c53939fa8121502fb7129f34b9b8bdd97563d33346e0e91f9964`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/_cffi_backend.c#L4092-L4101).

```c
    else if (PyUnicode_Check(io)) {
        char ignored[80];
        cffi_char32_t ordinal;
        if (_my_PyUnicode_AsSingleChar32(io, &ordinal, ignored) < 0)
            goto error;
        /* the signness of the 32-bit version of wide chars should not
         * matter here, because 'ordinal' comes from a normal Python
         * unicode string */
        *out_value = ordinal;
        return 1;
```

### Callee analysis

- `_my_PyUnicode_AsSingleChar16/32` in `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89: length1 guard and READ_CHAR(unicode,0). B scalar

Available source context:

- [`_my_PyUnicode_AsSingleChar16/32`](#helper-001) (`cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89).

<a id="case-006"></a>

## 6. `_my_PyUnicode_AsSingleChar16`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Read index 0 only after requiring length exactly 1; scalar conversion, not full-loop traversal.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 58–76. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L58-L76).

### Read sites

- Site 1: lines 62–74; scalar; index expression `0`. Single-character char16_t conversion rejects codepoints >0xffff.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 58–76. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L58-L76).

```c
_my_PyUnicode_AsSingleChar16(PyObject *unicode, cffi_char16_t *result,
                             char *err_got)
{
    cffi_char32_t ch;
    if (PyUnicode_GET_LENGTH(unicode) != 1) {
        sprintf(err_got, "unicode string of length %zd",
                PyUnicode_GET_LENGTH(unicode));
        return -1;
    }
    ch = PyUnicode_READ_CHAR(unicode, 0);

    if (ch > 0xFFFF)
    {
        sprintf(err_got, "larger-than-0xFFFF character");
        return -1;
    }
    *result = (cffi_char16_t)ch;
    return 0;
}
```


<a id="case-007"></a>

## 7. `_my_PyUnicode_AsSingleChar32`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Read index 0 only after requiring length exactly 1; scalar conversion.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz). Archive SHA-256: `dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be`.

**Function source:** `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 79–89. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`.

[Verified immutable function link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L79-L89).

### Read sites

- Site 1: lines 82–87; scalar; index expression `0`. Single-character char32_t conversion.

### Contextual source excerpts

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 79–89. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L79-L89).

```c
_my_PyUnicode_AsSingleChar32(PyObject *unicode, cffi_char32_t *result,
                             char *err_got)
{
    if (PyUnicode_GET_LENGTH(unicode) != 1) {
        sprintf(err_got, "unicode string of length %zd",
                PyUnicode_GET_LENGTH(unicode));
        return -1;
    }
    *result = PyUnicode_READ_CHAR(unicode, 0);
    return 0;
}
```


<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `_my_PyUnicode_AsSingleChar16/32`

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 57–89. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L57-L89).

```c
static int
_my_PyUnicode_AsSingleChar16(PyObject *unicode, cffi_char16_t *result,
                             char *err_got)
{
    cffi_char32_t ch;
    if (PyUnicode_GET_LENGTH(unicode) != 1) {
        sprintf(err_got, "unicode string of length %zd",
                PyUnicode_GET_LENGTH(unicode));
        return -1;
    }
    ch = PyUnicode_READ_CHAR(unicode, 0);

    if (ch > 0xFFFF)
    {
        sprintf(err_got, "larger-than-0xFFFF character");
        return -1;
    }
    *result = (cffi_char16_t)ch;
    return 0;
}

static int
_my_PyUnicode_AsSingleChar32(PyObject *unicode, cffi_char32_t *result,
                             char *err_got)
{
    if (PyUnicode_GET_LENGTH(unicode) != 1) {
        sprintf(err_got, "unicode string of length %zd",
                PyUnicode_GET_LENGTH(unicode));
        return -1;
    }
    *result = PyUnicode_READ_CHAR(unicode, 0);
    return 0;
}
```

<a id="helper-002"></a>

### 2. `_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 91–105. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L91-L105).

```c
static Py_ssize_t _my_PyUnicode_SizeAsChar16(PyObject *unicode)
{
    Py_ssize_t length = PyUnicode_GET_LENGTH(unicode);
    Py_ssize_t result = length;
    unsigned int kind = PyUnicode_KIND(unicode);

    if (kind == PyUnicode_4BYTE_KIND)
    {
        Py_UCS4 *data = PyUnicode_4BYTE_DATA(unicode);
        Py_ssize_t i;
        for (i = 0; i < length; i++) {
            if (data[i] > 0xFFFF)
                result++;
        }
    }
```

<a id="helper-003"></a>

### 3. `_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 110–118. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L110-L118).

```c
{
    return PyUnicode_GET_LENGTH(unicode);
}

static int _my_PyUnicode_AsChar16(PyObject *unicode,
                                  cffi_char16_t *result,
                                  Py_ssize_t resultlen)
{
    Py_ssize_t len = PyUnicode_GET_LENGTH(unicode);
```

<a id="helper-004"></a>

### 4. `_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 120–132. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L120-L132).

```c
    void *data = PyUnicode_DATA(unicode);
    Py_ssize_t i;

    for (i = 0; i < len; i++) {
        cffi_char32_t ordinal = PyUnicode_READ(kind, data, i);
        if (ordinal > 0xFFFF) {
            if (ordinal > 0x10FFFF) {
                PyErr_Format(PyExc_ValueError,
                             "unicode character out of range for "
                             "conversion to char16_t: 0x%x", (int)ordinal);
                return -1;
            }
            ordinal -= 0x10000;
```

<a id="helper-005"></a>

### 5. `_my_PyUnicode_SizeAsChar16 / _my_PyUnicode_AsChar16`

Archive member `cffi-2.1.1/src/c/wchar_helper_3.h`, lines 138–140. Member SHA-256: `956749dc021ca76c36952ba00ab5180120eda2d05b1145f71ca1a283f3fc9247`. [Verified immutable source link](https://github.com/python-cffi/cffi/blob/fd33e7700f0ebafe6f30bd5053f13327221b77a2/src/c/wchar_helper_3.h#L138-L140).

```c
    }
    return 0;
}
```
