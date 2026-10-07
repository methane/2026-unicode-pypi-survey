# simplejson — non-simple Unicode reads

[All packages](README.md)

Version: 4.1.2. **11 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`ascii_escape_unicode[Python>=3.14]`](#case-001)
- [`ascii_escape_unicode[Python<3.14]`](#case-002)
- [`scanstring_unicode[Python>=3.14]`](#case-003)
- [`scanstring_unicode[Python<3.14]`](#case-004)
- [`escape_unicode_noascii[Python>=3.14]`](#case-005)
- [`escape_unicode_noascii[Python<3.14]`](#case-006)
- [`encoder_encode_decimal`](#case-007)
- [`_match_number_unicode`](#case-008)
- [`_parse_object_unicode`](#case-009)
- [`_parse_array_unicode`](#case-010)
- [`scan_once_unicode`](#case-011)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `ascii_escape_unicode[Python>=3.14]`

**Classification:** B. **Subtypes:** multiple passes, caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Scalar inspection is a simple full forward pass, but WriteSubstring rereads already inspected safe runs for bulk output copying. The complete function is scan plus range copy, not exactly one input read per codepoint.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Cached data survives writer creation/write operations; some WriteSubstring implementation could request representation from same input. Stable pointer contract needed for migration.

- Source calls this single-pass because output size prepass was removed; classification includes subsequent range-copy reads. Conditional implementations are separate source function definitions.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 865–909. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L865-L909).

### Read sites

- Site 1: lines 880–896; scalar loop; index expression `i=0; i<input_chars; i++`. Forward scalar inspection.
- Site 2: lines 885–888; bulk reread; index expression `run_start,i`. Previously inspected codepoint ranges copied by writer.
- Site 3: lines 898–901; bulk reread; index expression `run_start,i`. Previously inspected codepoint ranges copied by writer.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 869–875, 906. The original contextual region was lines 865–909.

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 865–868. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L865-L868).

```c
ascii_escape_unicode(PyObject *pystr)
{
    /* Single-pass implementation using PyUnicodeWriter (Python 3.14+).
     * Writes runs of safe characters via WriteSubstring and escape
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 876–905. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L876-L905).

```c
    if (writer == NULL)
        return NULL;
    if (PyUnicodeWriter_WriteChar(writer, '"') < 0)
        goto bail;
    for (i = 0; i < input_chars; i++) {
        JSON_UNICHR c = PyUnicode_READ(kind, data, i);
        if (S_CHAR(c))
            continue;
        /* Flush run of safe characters */
        if (i > run_start) {
            if (PyUnicodeWriter_WriteSubstring(writer, pystr, run_start, i) < 0)
                goto bail;
        }
        /* Write escape sequence */
        {
            char buf[12];
            Py_ssize_t len = ascii_escape_char(c, buf, 0);
            if (PyUnicodeWriter_WriteUTF8(writer, buf, len) < 0)
                goto bail;
        }
        run_start = i + 1;
    }
    /* Flush remaining safe characters */
    if (i > run_start) {
        if (PyUnicodeWriter_WriteSubstring(writer, pystr, run_start, i) < 0)
            goto bail;
    }
    if (PyUnicodeWriter_WriteChar(writer, '"') < 0)
        goto bail;
    return PyUnicodeWriter_Finish(writer);
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 907–909. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L907-L909).

```c
    PyUnicodeWriter_Discard(writer);
    return NULL;
}
```


<a id="case-002"></a>

## 2. `ascii_escape_unicode[Python<3.14]`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

First full pass computes exact output size; second starts i=0 and rereads every codepoint to produce escapes.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Output rval DATA/KIND are write-only; included ranges separate input reads from output writes.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 912–955. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L912-L955).

### Read sites

- Site 1: lines 925–932; scalar loop; index expression `i=0; i<input_chars; i++`. Sizing pass.
- Site 2: lines 949–951; scalar loop; index expression `i=0; i<input_chars; i++ again`. Output-fill pass rereads whole input.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 916–920, 937–944. The original contextual region was lines 912–955.

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 912–915. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L912-L915).

```c
ascii_escape_unicode(PyObject *pystr)
{
    /* Two-pass implementation: calculate exact output size, then fill. */
    Py_ssize_t i;
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 921–936. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L921-L936).

```c
    PyObject *rval;
    char *output;

    output_size = 2;
    for (i = 0; i < input_chars; i++) {
        Py_ssize_t charsize = ascii_char_size(PyUnicode_READ(kind, data, i));
        if (output_size > PY_SSIZE_T_MAX - charsize) {
            PyErr_SetString(PyExc_OverflowError, "string is too long to escape");
            return NULL;
        }
        output_size += charsize;
    }
#if PY_MAJOR_VERSION >= 3
    rval = PyUnicode_New(output_size, 127);
    if (rval == NULL) {
        return NULL;
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 945–955. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L945-L955).

```c
    output = PyString_AS_STRING(rval);
#endif
    chars = 0;
    output[chars++] = '"';
    for (i = 0; i < input_chars; i++) {
        chars = ascii_escape_char(PyUnicode_READ(kind, data, i), output, chars);
    }
    output[chars++] = '"';
    assert(chars == output_size);
    return rval;
}
```


<a id="case-003"></a>

## 3. `scanstring_unicode[Python>=3.14]`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Caller end starts scanning inside JSON input; scans to quote/backslash, reads escape digits/lookahead next+1, and rewinds six codepoints on invalid low surrogate. Literal source chunks are recopied.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Error offsets are Python codepoint indexes, not UTF-8 byte offsets. Existing JSON escape high+low pair normalization is parser behavior; adjacent literal surrogate codepoints remain independent.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 1486–1671. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1486-L1671).

### Read sites

- Site 1: lines 1493–1535; scalar range; index expression `next=end (caller); next<len`. Interior string scan; stop at quote/escape.
- Site 2: lines 1544–1639; lookahead and rewind; index expression `next; next+1; next+=2; end-=6; next=end`. Unicode escape probing with rewind; range-copy reread.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 1502–1514, 1524–1529. The original contextual region was lines 1486–1535.
Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 1558–1578, 1588–1600, 1614–1624, 1634–1639. The original contextual region was lines 1541–1642.
Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 1588–1599, 1614–1624, 1634–1636. The original contextual region was lines 1573–1639.

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1486–1501. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1486-L1501).

```c
scanstring_unicode(_speedups_state *state, PyObject *pystr, Py_ssize_t end,
                   int strict, Py_ssize_t *next_end_ptr)
{
    /* Python 3.14+: use PyUnicodeWriter instead of a chunks list.
     * The writer is lazily created on the first escape sequence so that
     * the common no-escape path returns a cheap PyUnicode_Substring. */
    PyObject *rval;
    Py_ssize_t begin = end - 1;
    Py_ssize_t next = begin;
    int kind = PyUnicode_KIND(pystr);
    Py_ssize_t len = PyUnicode_GET_LENGTH(pystr);
    void *buf = PyUnicode_DATA(pystr);
    PyUnicodeWriter *writer = NULL;
    Py_ssize_t literal_start;

    if (len == end) {
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1515–1523. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1515-L1523).

```c
    while (1) {
        /* Find the end of the string or the next escape */
        JSON_UNICHR c = 0;
        for (next = end; next < len; next++) {
            c = PyUnicode_READ(kind, buf, next);
            if (c == '"' || c == '\\') {
                break;
            }
            else if (strict && c <= 0x1f) {
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1530–1535. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1530-L1535).

```c
            goto bail;
        }
        next++;
        if (c == '"') {
            end = next;
            break;
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1541–1557. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1541-L1557).

```c
            if (writer == NULL)
                goto bail;
        }
        if (next - 1 > literal_start) {
            if (PyUnicodeWriter_WriteSubstring(writer, pystr,
                                               literal_start, next - 1) < 0)
                goto bail;
        }
        if (next == len) {
            raise_errmsg(state, ERR_STRING_UNTERMINATED, pystr, begin);
            goto bail;
        }
        c = PyUnicode_READ(kind, buf, next);
        if (c != 'u') {
            /* Non-unicode backslash escapes */
            end = next + 1;
            switch (c) {
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1579–1587. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1579-L1587).

```c
                goto bail;
            }
            /* Decode 4 hex digits */
            for (; next < end; next++) {
                JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
                c <<= 4;
                switch (hex_digit) {
                    case '0': case '1': case '2': case '3': case '4':
                    case '5': case '6': case '7': case '8': case '9':
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1601–1613. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1601-L1613).

```c
            if ((c & 0xfc00) == 0xd800) {
                JSON_UNICHR c2 = 0;
                if (end + 6 <= len &&
                    PyUnicode_READ(kind, buf, next) == '\\' &&
                    PyUnicode_READ(kind, buf, next + 1) == 'u') {
                    end += 6;
                    /* Decode 4 hex digits */
                    for (next += 2; next < end; next++) {
                        JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
                        c2 <<= 4;
                        switch (hex_digit) {
                        case '0': case '1': case '2': case '3': case '4':
                        case '5': case '6': case '7': case '8': case '9':
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1625–1633. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1625-L1633).

```c
                    }
                    if ((c2 & 0xfc00) != 0xdc00) {
                        /* not a low surrogate, rewind */
                        end -= 6;
                        next = end;
                    }
                    else {
                        c = 0x10000 + (((c - 0xd800) << 10) | (c2 - 0xdc00));
                    }
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1640–1642. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1640-L1642).

```c
    }

    /* Finalize */
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1544–1569. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1544-L1569).

```c
        if (next - 1 > literal_start) {
            if (PyUnicodeWriter_WriteSubstring(writer, pystr,
                                               literal_start, next - 1) < 0)
                goto bail;
        }
        if (next == len) {
            raise_errmsg(state, ERR_STRING_UNTERMINATED, pystr, begin);
            goto bail;
        }
        c = PyUnicode_READ(kind, buf, next);
        if (c != 'u') {
            /* Non-unicode backslash escapes */
            end = next + 1;
            switch (c) {
                case '"': break;
                case '\\': break;
                case '/': break;
                case 'b': c = '\b'; break;
                case 'f': c = '\f'; break;
                case 'n': c = '\n'; break;
                case 'r': c = '\r'; break;
                case 't': c = '\t'; break;
                default: c = 0;
            }
            if (c == 0) {
                raise_errmsg(state, ERR_STRING_ESC1, pystr, end - 1);
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1573–1587. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1573-L1587).

```c
        else {
            c = 0;
            next++;
            end = next + 4;
            if (end > len) {
                raise_errmsg(state, ERR_STRING_ESC4, pystr, next - 2);
                goto bail;
            }
            /* Decode 4 hex digits */
            for (; next < end; next++) {
                JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
                c <<= 4;
                switch (hex_digit) {
                    case '0': case '1': case '2': case '3': case '4':
                    case '5': case '6': case '7': case '8': case '9':
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1600–1613. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1600-L1613).

```c
            /* Surrogate pair */
            if ((c & 0xfc00) == 0xd800) {
                JSON_UNICHR c2 = 0;
                if (end + 6 <= len &&
                    PyUnicode_READ(kind, buf, next) == '\\' &&
                    PyUnicode_READ(kind, buf, next + 1) == 'u') {
                    end += 6;
                    /* Decode 4 hex digits */
                    for (next += 2; next < end; next++) {
                        JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
                        c2 <<= 4;
                        switch (hex_digit) {
                        case '0': case '1': case '2': case '3': case '4':
                        case '5': case '6': case '7': case '8': case '9':
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1625–1633. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1625-L1633).

```c
                    }
                    if ((c2 & 0xfc00) != 0xdc00) {
                        /* not a low surrogate, rewind */
                        end -= 6;
                        next = end;
                    }
                    else {
                        c = 0x10000 + (((c - 0xd800) << 10) | (c2 - 0xdc00));
                    }
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1637–1639. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1637-L1639).

```c
        if (PyUnicodeWriter_WriteChar(writer, c) < 0)
            goto bail;
        literal_start = end;
```


<a id="case-004"></a>

## 4. `scanstring_unicode[Python<3.14]`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Caller end starts scanning inside JSON input; scans to quote/backslash, reads escape digits/lookahead next+1, and rewinds six codepoints on invalid low surrogate. Literal source chunks are recopied.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Error offsets are Python codepoint indexes, not UTF-8 byte offsets. Existing JSON escape high+low pair normalization is parser behavior; adjacent literal surrogate codepoints remain independent.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 1674–1860. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1674-L1860).

### Read sites

- Site 1: lines 1685–1738; scalar range; index expression `next=end (caller); next<len`. Interior string scan; stop at quote/escape.
- Site 2: lines 1740–1835; lookahead and rewind; index expression `next; next+1; next+=2; end-=6; next=end`. Unicode escape probing with rewind; range-copy reread.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 1678–1682, 1695–1705, 1715–1724. The original contextual region was lines 1674–1738.
Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 1749–1791, 1802–1816, 1826. The original contextual region was lines 1737–1838.
Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 1779–1791, 1806–1816, 1826. The original contextual region was lines 1772–1835.

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1674–1677. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1674-L1677).

```c
scanstring_unicode(_speedups_state *state, PyObject *pystr, Py_ssize_t end,
                   int strict, Py_ssize_t *next_end_ptr)
{
    /* Read the JSON string from PyUnicode pystr.
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1683–1694. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1683-L1694).

```c
    Return value is a new PyUnicode
    */
    PyObject *rval;
    Py_ssize_t begin = end - 1;
    Py_ssize_t next = begin;
    PY2_UNUSED int kind = PyUnicode_KIND(pystr);
    Py_ssize_t len = PyUnicode_GET_LENGTH(pystr);
    void *buf = PyUnicode_DATA(pystr);
    PyObject *chunks = NULL;
    PyObject *chunk = NULL;

    if (len == end) {
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1706–1714. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1706-L1714).

```c
    while (1) {
        /* Find the end of the string or the next escape */
        JSON_UNICHR c = 0;
        for (next = end; next < len; next++) {
            c = PyUnicode_READ(kind, buf, next);
            if (c == '"' || c == '\\') {
                break;
            }
            else if (strict && c <= 0x1f) {
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1725–1738. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1725-L1738).

```c
            APPEND_OLD_CHUNK
#if PY_MAJOR_VERSION < 3
            chunk = PyUnicode_FromUnicode(&((const Py_UNICODE *)buf)[end], next - end);
#else
            chunk = PyUnicode_Substring(pystr, end, next);
#endif
            if (chunk == NULL) {
                goto bail;
            }
        }
        next++;
        if (c == '"') {
            end = next;
            break;
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1737–1748. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1737-L1748).

```c
            end = next;
            break;
        }
        if (next == len) {
            raise_errmsg(state, ERR_STRING_UNTERMINATED, pystr, begin);
            goto bail;
        }
        c = PyUnicode_READ(kind, buf, next);
        if (c != 'u') {
            /* Non-unicode backslash escapes */
            end = next + 1;
            switch (c) {
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1792–1801. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1792-L1801).

```c
            /* Surrogate pair */
            if ((c & 0xfc00) == 0xd800) {
                JSON_UNICHR c2 = 0;
                if (end + 6 <= len &&
                    PyUnicode_READ(kind, buf, next) == '\\' &&
                    PyUnicode_READ(kind, buf, next + 1) == 'u') {
                    end += 6;
                    /* Decode 4 hex digits */
                    for (next += 2; next < end; next++) {
                        JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1817–1825. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1817-L1825).

```c
                    }
                    if ((c2 & 0xfc00) != 0xdc00) {
                        /* not a low surrogate, rewind */
                        end -= 6;
                        next = end;
                    }
                    else {
                        c = 0x10000 + (((c - 0xd800) << 10) | (c2 - 0xdc00));
                    }
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1827–1838. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1827-L1838).

```c
            }
#endif
        }
        APPEND_OLD_CHUNK
        chunk = PyUnicode_FromOrdinal(c);
        if (chunk == NULL) {
            goto bail;
        }
    }

    if (chunks == NULL) {
        if (chunk != NULL)
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1740–1769. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1740-L1769).

```c
        if (next == len) {
            raise_errmsg(state, ERR_STRING_UNTERMINATED, pystr, begin);
            goto bail;
        }
        c = PyUnicode_READ(kind, buf, next);
        if (c != 'u') {
            /* Non-unicode backslash escapes */
            end = next + 1;
            switch (c) {
                case '"': break;
                case '\\': break;
                case '/': break;
                case 'b': c = '\b'; break;
                case 'f': c = '\f'; break;
                case 'n': c = '\n'; break;
                case 'r': c = '\r'; break;
                case 't': c = '\t'; break;
                default: c = 0;
            }
            if (c == 0) {
                raise_errmsg(state, ERR_STRING_ESC1, pystr, end - 1);
                goto bail;
            }
        }
        else {
            c = 0;
            next++;
            end = next + 4;
            if (end > len) {
                raise_errmsg(state, ERR_STRING_ESC4, pystr, next - 2);
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1772–1778. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1772-L1778).

```c
            /* Decode 4 hex digits */
            for (; next < end; next++) {
                JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
                c <<= 4;
                switch (hex_digit) {
                    case '0': case '1': case '2': case '3': case '4':
                    case '5': case '6': case '7': case '8': case '9':
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1792–1805. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1792-L1805).

```c
            /* Surrogate pair */
            if ((c & 0xfc00) == 0xd800) {
                JSON_UNICHR c2 = 0;
                if (end + 6 <= len &&
                    PyUnicode_READ(kind, buf, next) == '\\' &&
                    PyUnicode_READ(kind, buf, next + 1) == 'u') {
                    end += 6;
                    /* Decode 4 hex digits */
                    for (next += 2; next < end; next++) {
                        JSON_UNICHR hex_digit = PyUnicode_READ(kind, buf, next);
                        c2 <<= 4;
                        switch (hex_digit) {
                        case '0': case '1': case '2': case '3': case '4':
                        case '5': case '6': case '7': case '8': case '9':
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1817–1825. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1817-L1825).

```c
                    }
                    if ((c2 & 0xfc00) != 0xdc00) {
                        /* not a low surrogate, rewind */
                        end -= 6;
                        next = end;
                    }
                    else {
                        c = 0x10000 + (((c - 0xd800) << 10) | (c2 - 0xdc00));
                    }
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1827–1835. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1827-L1835).

```c
            }
#endif
        }
        APPEND_OLD_CHUNK
        chunk = PyUnicode_FromOrdinal(c);
        if (chunk == NULL) {
            goto bail;
        }
    }
```


<a id="case-005"></a>

## 5. `escape_unicode_noascii[Python>=3.14]`

**Classification:** B. **Subtypes:** multiple passes, caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Scalar inspection is a simple full forward pass, but WriteSubstring rereads already inspected safe runs for bulk output copying. The complete function is scan plus range copy, not exactly one input read per codepoint.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Cached data survives writer creation/write operations; some WriteSubstring implementation could request representation from same input. Stable pointer contract needed for migration.

- Source calls this single-pass because output size prepass was removed; classification includes subsequent range-copy reads. Conditional implementations are separate source function definitions.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 1998–2054. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1998-L2054).

### Read sites

- Site 1: lines 2011–2042; scalar loop; index expression `i=0; i<input_chars; i++`. Forward scalar inspection.
- Site 2: lines 2016–2019; bulk reread; index expression `run_start,i`. Previously inspected codepoint ranges copied by writer.
- Site 3: lines 2044–2046; bulk reread; index expression `run_start,i`. Previously inspected codepoint ranges copied by writer.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 2002–2006, 2051. The original contextual region was lines 1998–2054.

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 1998–2001. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L1998-L2001).

```c
escape_unicode_noascii(PyObject *pystr)
{
    /* Single-pass using PyUnicodeWriter (Python 3.14+). */
    Py_ssize_t i;
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2007–2050. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2007-L2050).

```c
    if (writer == NULL)
        return NULL;
    if (PyUnicodeWriter_WriteChar(writer, '"') < 0)
        goto bail;
    for (i = 0; i < input_chars; i++) {
        JSON_UNICHR c = PyUnicode_READ(kind, data, i);
        if (!NEEDS_ESCAPE(c))
            continue;
        /* Flush run of safe characters */
        if (i > run_start) {
            if (PyUnicodeWriter_WriteSubstring(writer, pystr, run_start, i) < 0)
                goto bail;
        }
        {
            char buf[6]; /* longest escape: \u00XX */
            Py_ssize_t len = 0;
            buf[len++] = '\\';
            switch (c) {
                case '\\': buf[len++] = '\\'; break;
                case '"':  buf[len++] = '"'; break;
                case '\b': buf[len++] = 'b'; break;
                case '\f': buf[len++] = 'f'; break;
                case '\n': buf[len++] = 'n'; break;
                case '\r': buf[len++] = 'r'; break;
                case '\t': buf[len++] = 't'; break;
                default:
                    buf[len++] = 'u';
                    buf[len++] = '0';
                    buf[len++] = '0';
                    buf[len++] = "0123456789abcdef"[(c >> 4) & 0xf];
                    buf[len++] = "0123456789abcdef"[(c     ) & 0xf];
            }
            if (PyUnicodeWriter_WriteUTF8(writer, buf, len) < 0)
                goto bail;
        }
        run_start = i + 1;
    }
    if (i > run_start) {
        if (PyUnicodeWriter_WriteSubstring(writer, pystr, run_start, i) < 0)
            goto bail;
    }
    if (PyUnicodeWriter_WriteChar(writer, '"') < 0)
        goto bail;
    return PyUnicodeWriter_Finish(writer);
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2052–2054. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2052-L2054).

```c
    PyUnicodeWriter_Discard(writer);
    return NULL;
}
```


<a id="case-006"></a>

## 6. `escape_unicode_noascii[Python<3.14]`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

First full pass computes exact output size; second starts i=0 and rereads every codepoint to produce escapes.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Output rval DATA/KIND are write-only; included ranges separate input reads from output writes.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 2057–2126. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2057-L2126).

### Read sites

- Site 1: lines 2067–2076; scalar loop; index expression `i=0; i<input_chars; i++`. Sizing pass.
- Site 2: lines 2093–2104; scalar loop; index expression `i=0; i<input_chars; i++ again`. Output-fill pass rereads whole input.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups.c`: lines 2061–2062, 2073–2088, 2107–2123. The original contextual region was lines 2057–2126.

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2057–2060. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2057-L2060).

```c
escape_unicode_noascii(PyObject *pystr)
{
    /* Two-pass: compute size, then fill. */
    Py_ssize_t i;
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2063–2072. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2063-L2072).

```c
    void *data = PyUnicode_DATA(pystr);
    Py_ssize_t output_size = 2; /* opening and closing quotes */
    PyObject *rval;

    for (i = 0; i < input_chars; i++) {
        JSON_UNICHR c = PyUnicode_READ(kind, data, i);
        Py_ssize_t charsize = escape_char_noascii_size(c);
        if (output_size > PY_SSIZE_T_MAX - charsize) {
            PyErr_SetString(PyExc_OverflowError,
                            "string is too long to escape");
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2089–2106. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2089-L2106).

```c
        int out_kind = PyUnicode_KIND(rval);
        void *out_data = PyUnicode_DATA(rval);
        Py_ssize_t chars = 0;
        PyUnicode_WRITE(out_kind, out_data, chars++, '"');
        for (i = 0; i < input_chars; i++) {
            JSON_UNICHR c = PyUnicode_READ(kind, data, i);
            if (!NEEDS_ESCAPE(c)) {
                PyUnicode_WRITE(out_kind, out_data, chars++, c);
            }
            else {
                JSON_UNICHR buf[6];
                Py_ssize_t j, n = escape_char_noascii(c, buf, 0);
                for (j = 0; j < n; j++)
                    PyUnicode_WRITE(out_kind, out_data, chars++, buf[j]);
            }
        }
        PyUnicode_WRITE(out_kind, out_data, chars++, '"');
        assert(chars == output_size);
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2124–2126. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2124-L2126).

```c
#endif
    return rval;
}
```


<a id="case-007"></a>

## 7. `encoder_encode_decimal`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Checks sign at index 0 and first significant character at index negative?1:0 of PyObject_Str decimal result; no iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offset 0/1; expected ASCII Decimal repr; whole str then emitted unchanged.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups.c`, lines 2841–2893. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2841-L2893).

### Read sites

- Site 1: lines 2863–2876; scalar index; index expression `0 and negative?1:0`. Distinguish finite Decimal digits from NaN/Infinity.

### Contextual source excerpts

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2841–2852. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2841-L2852).

```c
encoder_encode_decimal(PyEncoderObject *s, PyObject *obj)
{
    /* Return the JSON representation of a Decimal. Finite Decimals are
       stringified as-is (preserving precision and trailing zeros); non-finite
       Decimals (NaN, sNaN, Infinity) are routed through the same
       allow_nan/ignore_nan handling as floats so they never emit invalid
       JSON. See https://github.com/simplejson/simplejson/issues/149

       str(Decimal) carries a leading '-' sign at most (never '+'); a finite
       value's first significant character is always a digit while a non-finite
       value's is a letter ('N'/'s' for [s]NaN, 'I' for Infinity). So a single
       str() plus a one/two character check distinguishes the two. */
```

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2863–2893. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2863-L2893).

```c
    if (str == NULL)
        return NULL;
#if PY_MAJOR_VERSION >= 3
    if (PyUnicode_READY(str)) {
        Py_DECREF(str);
        return NULL;
    }
    len = PyUnicode_GET_LENGTH(str);
    kind = PyUnicode_KIND(str);
    data = PyUnicode_DATA(str);
    negative = (len > 0 && PyUnicode_READ(kind, data, 0) == '-');
    c = (JSON_UNICHR)0;
    if (len > (negative ? 1 : 0))
        c = PyUnicode_READ(kind, data, negative ? 1 : 0);
#else
    len = PyString_GET_SIZE(str);
    data = PyString_AS_STRING(str);
    negative = (len > 0 && data[0] == '-');
    c = (JSON_UNICHR)0;
    if (len > (negative ? 1 : 0))
        c = (unsigned char)data[negative ? 1 : 0];
#endif
    if (IS_DIGIT(c)) {
        /* First significant character is a digit: finite Decimal, emit as-is. */
        return str;
    }
    /* Non-finite Decimal; use the same allow_nan/ignore_nan path as floats
       without creating a temporary float. */
    Py_DECREF(str);
    return encoder_encode_nonfinite(s, c == 'I' ? (negative ? -1 : 1) : 0);
}
```


<a id="case-008"></a>

## 8. `_match_number_unicode`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts caller start; probes idx+1 for fraction, idx-1 to validate exponent; resets idx=e_start on absent exponent digits; copies parsed range.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Offsets index original Python codepoints; constant token lookahead is scalar/codepoint distance, not UTF-8 byte distance.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Recursive scan_once/parser calls reacquire DATA on the same pystr while caller caches str; scalar/parser callbacks may also retain cached pointer across nested calls. Any future FSR eviction must respect these outstanding views.

- SKIP_WHITESPACE macro at header lines66-70 uses JSON_SCAN_READ(idx) and can leave delimiter read to be repeated. Its sites are attributed to each consuming function, not counted as a separate synthetic function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 73–169. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L73-L169).

### Read sites

- Site 1: lines 73–109; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.
- Site 2: lines 116–148; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups_scan.h`: lines 77–101. The original contextual region was lines 73–109.

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 73–76. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L73-L76).

```c
JSON_SCAN_FN(_match_number)(PyScannerObject *s, PyObject *pystr,
                            Py_ssize_t start, Py_ssize_t *next_idx_ptr)
{
    /* Read a JSON number from pystr.
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 102–109. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L102-L109).

```c
        idx++;
    }
    else if (IS_DIGIT(c)) {
        idx++;
        while (idx <= end_idx && IS_DIGIT(JSON_SCAN_READ(idx))) {
            idx++;
        }
    }
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 116–148. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L116-L148).

```c
    /* if the next char is '.' followed by a digit then read all float digits */
    if (idx < end_idx &&
        JSON_SCAN_READ(idx) == '.' &&
        IS_DIGIT(JSON_SCAN_READ(idx + 1))) {
        is_float = 1;
        idx += 2;
        while (idx <= end_idx && IS_DIGIT(JSON_SCAN_READ(idx))) idx++;
    }

    /* if the next char is 'e' or 'E' then maybe read the exponent (or backtrack) */
    if (idx < end_idx &&
        (JSON_SCAN_READ(idx) == 'e' || JSON_SCAN_READ(idx) == 'E')) {
        Py_ssize_t e_start = idx;
        idx++;

        /* read an exponent sign if present */
        if (idx < end_idx &&
            (JSON_SCAN_READ(idx) == '-' || JSON_SCAN_READ(idx) == '+')) idx++;

        /* read all digits */
        while (idx <= end_idx && IS_DIGIT(JSON_SCAN_READ(idx))) idx++;

        /* if we got a digit, then parse as float. if not, backtrack */
        if (IS_DIGIT(JSON_SCAN_READ(idx - 1))) {
            is_float = 1;
        }
        else {
            idx = e_start;
        }
    }

    /* copy the section we determined to be a number */
    numstr = JSON_SCAN_NUMSTR_CREATE(start, idx);
```

### Callee analysis

- `JSON_SCAN_DATA_INIT/READ` in `simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283: Unicode macro binding selects DATA/KIND/READ; included once for Unicode. Native handwritten source template, not Cython-generated expansion.

Available source context:

- [`JSON_SCAN_DATA_INIT/READ`](#helper-001) (`simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283).

<a id="case-009"></a>

## 9. `_parse_object_unicode`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts caller idx after opening brace; whitespace helper rechecks boundary chars; nested parser calls advance idx to next_idx; punctuation is probed multiple times.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Offsets index original Python codepoints; constant token lookahead is scalar/codepoint distance, not UTF-8 byte distance.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Recursive scan_once/parser calls reacquire DATA on the same pystr while caller caches str; scalar/parser callbacks may also retain cached pointer across nested calls. Any future FSR eviction must respect these outstanding views.

- SKIP_WHITESPACE macro at header lines66-70 uses JSON_SCAN_READ(idx) and can leave delimiter read to be repeated. Its sites are attributed to each consuming function, not counted as a separate synthetic function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 172–332. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L172-L332).

### Read sites

- Site 1: lines 172–238; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.
- Site 2: lines 260–303; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups_scan.h`: lines 176–203, 213–235. The original contextual region was lines 172–238.
Omitted from `simplejson-4.1.2/simplejson/_speedups_scan.h`: lines 264–277, 287–290, 300. The original contextual region was lines 260–303.

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 63–70. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L63-L70).

```c
/* Advance idx past any JSON whitespace (space, tab, CR, LF). The
 * idx <= end_idx guard matches the parser's convention that end_idx
 * is the index of the LAST valid byte (i.e. length - 1). */
#define SKIP_WHITESPACE() \
    do { \
        while (idx <= end_idx && IS_WHITESPACE(JSON_SCAN_READ(idx))) \
            idx++; \
    } while (0)
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 172–175. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L172-L175).

```c
JSON_SCAN_FN(_parse_object)(PyScannerObject *s, PyObject *pystr,
                            Py_ssize_t idx, Py_ssize_t *next_idx_ptr)
{
    /* Read a JSON object from pystr.
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 204–212. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L204-L212).

```c
    /* only loop if the object is non-empty */
    if (idx <= end_idx && JSON_SCAN_READ(idx) != '}') {
        int trailing_delimiter = 0;
        Py_ssize_t comma_idx = 0;
        while (idx <= end_idx) {
            trailing_delimiter = 0;

            /* read key */
            if (JSON_SCAN_READ(idx) != '"') {
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 236–238. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L236-L238).

```c

            /* read any JSON term */
            val = JSON_SCAN_FN(scan_once)(s, pystr, idx, &next_idx);
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 260–263. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L260-L263).

```c
            idx = next_idx;

            /* skip whitespace before } or , */
            SKIP_WHITESPACE();
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 278–286. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L278-L286).

```c
            /* skip whitespace after , delimiter */
            SKIP_WHITESPACE();
            trailing_delimiter = 1;

            /* check for trailing comma before } */
            if (idx <= end_idx && JSON_SCAN_READ(idx) == '}') {
                raise_errmsg(state, ERR_TRAILING_COMMA_OBJECT, pystr, comma_idx);
                goto bail;
            }
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 291–299. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L291-L299).

```c
            goto bail;
        }
    }

    /* verify that idx < end_idx, str[idx] should be '}' */
    if (idx > end_idx || JSON_SCAN_READ(idx) != '}') {
        if (did_parse) {
            raise_errmsg(state, ERR_OBJECT_DELIMITER, pystr, idx);
        } else {
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 301–303. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L301-L303).

```c
        }
        goto bail;
    }
```

### Callee analysis

- `JSON_SCAN_DATA_INIT/READ` in `simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283: Unicode macro binding selects DATA/KIND/READ; included once for Unicode. Native handwritten source template, not Cython-generated expansion.

Available source context:

- [`JSON_SCAN_DATA_INIT/READ`](#helper-001) (`simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283).

<a id="case-010"></a>

## 10. `_parse_array_unicode`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts caller idx after opening bracket, invokes nested scanner, then repeatedly reads punctuation after whitespace runs and on final delimiter check.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Offsets index original Python codepoints; constant token lookahead is scalar/codepoint distance, not UTF-8 byte distance.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Recursive scan_once/parser calls reacquire DATA on the same pystr while caller caches str; scalar/parser callbacks may also retain cached pointer across nested calls. Any future FSR eviction must respect these outstanding views.

- SKIP_WHITESPACE macro at header lines66-70 uses JSON_SCAN_READ(idx) and can leave delimiter read to be repeated. Its sites are attributed to each consuming function, not counted as a separate synthetic function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 335–427. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L335-L427).

### Read sites

- Site 1: lines 335–363; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.
- Site 2: lines 369–411; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups_scan.h`: lines 373–385, 395–398, 408. The original contextual region was lines 369–411.

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 63–70. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L63-L70).

```c
/* Advance idx past any JSON whitespace (space, tab, CR, LF). The
 * idx <= end_idx guard matches the parser's convention that end_idx
 * is the index of the LAST valid byte (i.e. length - 1). */
#define SKIP_WHITESPACE() \
    do { \
        while (idx <= end_idx && IS_WHITESPACE(JSON_SCAN_READ(idx))) \
            idx++; \
    } while (0)
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 335–363. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L335-L363).

```c
JSON_SCAN_FN(_parse_array)(PyScannerObject *s, PyObject *pystr,
                           Py_ssize_t idx, Py_ssize_t *next_idx_ptr)
{
    /* Read a JSON array from pystr.
       idx is the index of the first character after the opening brace.
       *next_idx_ptr is a return-by-reference index to the first character
       after the closing brace. */
    _speedups_state *state = get_speedups_state(s->module_ref);
    JSON_SCAN_DATA_INIT(pystr);
    PyObject *val = NULL;
    PyObject *rval = PyList_New(0);
    Py_ssize_t next_idx;
    if (rval == NULL)
        return NULL;

    /* skip whitespace after [ */
    SKIP_WHITESPACE();

    /* only loop if the array is non-empty */
    if (idx <= end_idx && JSON_SCAN_READ(idx) != ']') {
        int trailing_delimiter = 0;
        Py_ssize_t comma_idx = 0;
        while (idx <= end_idx) {
            trailing_delimiter = 0;
            /* read any JSON term and de-tuplefy the (rval, idx) */
            val = JSON_SCAN_FN(scan_once)(s, pystr, idx, &next_idx);
            if (val == NULL) {
                goto bail;
            }
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 369–372. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L369-L372).

```c
            idx = next_idx;

            /* skip whitespace between term and , */
            SKIP_WHITESPACE();
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 386–394. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L386-L394).

```c
            /* skip whitespace after , */
            SKIP_WHITESPACE();
            trailing_delimiter = 1;

            /* check for trailing comma before ] */
            if (idx <= end_idx && JSON_SCAN_READ(idx) == ']') {
                raise_errmsg(state, ERR_TRAILING_COMMA_ARRAY, pystr, comma_idx);
                goto bail;
            }
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 399–407. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L399-L407).

```c
            goto bail;
        }
    }

    /* verify that idx < end_idx, str[idx] should be ']' */
    if (idx > end_idx || JSON_SCAN_READ(idx) != ']') {
        if (PyList_GET_SIZE(rval)) {
            raise_errmsg(state, ERR_ARRAY_DELIMITER, pystr, idx);
        } else {
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 409–411. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L409-L411).

```c
        }
        goto bail;
    }
```

### Callee analysis

- `JSON_SCAN_DATA_INIT/READ` in `simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283: Unicode macro binding selects DATA/KIND/READ; included once for Unicode. Native handwritten source template, not Cython-generated expansion.

Available source context:

- [`JSON_SCAN_DATA_INIT/READ`](#helper-001) (`simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283).

<a id="case-011"></a>

## 11. `scan_once_unicode`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads caller idx term start and hard-coded lookahead idx+1..idx+8 for named tokens; dispatches caller subrange to recursive parser.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Offsets index original Python codepoints; constant token lookahead is scalar/codepoint distance, not UTF-8 byte distance.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Recursive scan_once/parser calls reacquire DATA on the same pystr while caller caches str; scalar/parser callbacks may also retain cached pointer across nested calls. Any future FSR eviction must respect these outstanding views.

- SKIP_WHITESPACE macro at header lines66-70 uses JSON_SCAN_READ(idx) and can leave delimiter read to be repeated. Its sites are attributed to each consuming function, not counted as a separate synthetic function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz). Archive SHA-256: `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

**Function source:** `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 430–556. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`.

[Verified immutable function link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L430-L556).

### Read sites

- Site 1: lines 430–472; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.
- Site 2: lines 480–554; macro instantiated scalar; index expression `JSON_SCAN_READ -> PyUnicode_READ(kind,str,index)`. Templated body bound to Unicode DATA/KIND by _speedups.c lines2265-2283.

### Contextual source excerpts

Omitted from `simplejson-4.1.2/simplejson/_speedups_scan.h`: lines 434–448, 466–469. The original contextual region was lines 430–472.
Omitted from `simplejson-4.1.2/simplejson/_speedups_scan.h`: lines 484–547. The original contextual region was lines 480–554.

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 430–433. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L430-L433).

```c
JSON_SCAN_FN(scan_once)(PyScannerObject *s, PyObject *pystr,
                        Py_ssize_t idx, Py_ssize_t *next_idx_ptr)
{
    /* Read one JSON term (of any kind) from pystr.
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 449–465. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L449-L465).

```c
            rval = JSON_SCAN_SCANSTRING_CALL(idx + 1, next_idx_ptr);
            break;
        case '{':
            /* object */
            if (Py_EnterRecursiveCall(" while decoding a JSON object "
                                      "from a string"))
                return NULL;
            rval = JSON_SCAN_FN(_parse_object)(s, pystr, idx + 1, next_idx_ptr);
            Py_LeaveRecursiveCall();
            break;
        case '[':
            /* array */
            if (Py_EnterRecursiveCall(" while decoding a JSON array "
                                      "from a string"))
                return NULL;
            rval = JSON_SCAN_FN(_parse_array)(s, pystr, idx + 1, next_idx_ptr);
            Py_LeaveRecursiveCall();
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 470–472. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L470-L472).

```c
                && JSON_SCAN_READ(idx + 1) == 'u'
                && JSON_SCAN_READ(idx + 2) == 'l'
                && JSON_SCAN_READ(idx + 3) == 'l') {
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 480–483. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L480-L483).

```c
        case 't':
            /* true */
            if ((idx + 3 < length)
                && JSON_SCAN_READ(idx + 1) == 'r'
```

Archive member `simplejson-4.1.2/simplejson/_speedups_scan.h`, lines 548–554. Member SHA-256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L548-L554).

```c
        default:
            fallthrough = 1;
    }
    /* Didn't find a string, object, array, or named constant.
       Look for a number. */
    if (fallthrough)
        rval = JSON_SCAN_FN(_match_number)(s, pystr, idx, next_idx_ptr);
```

### Callee analysis

- `JSON_SCAN_DATA_INIT/READ` in `simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283: Unicode macro binding selects DATA/KIND/READ; included once for Unicode. Native handwritten source template, not Cython-generated expansion.

Available source context:

- [`JSON_SCAN_DATA_INIT/READ`](#helper-001) (`simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `JSON_SCAN_DATA_INIT/READ`

Archive member `simplejson-4.1.2/simplejson/_speedups.c`, lines 2265–2283. Member SHA-256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`. [Verified immutable source link](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2265-L2283).

```c
#define JSON_SCAN_SUFFIX _unicode
#define JSON_SCAN_DATA_INIT(p) \
    PY2_UNUSED int kind = PyUnicode_KIND(p); \
    void *str = PyUnicode_DATA(p); \
    Py_ssize_t end_idx = PyUnicode_GET_LENGTH(p) - 1
#define JSON_SCAN_READ(i) PyUnicode_READ(kind, str, (i))
#define JSON_SCAN_SCANSTRING_CALL(pos, nextp) \
    scanstring_unicode(state, pystr, (pos), s->strict, (nextp))
#if PY_MAJOR_VERSION >= 3
#define JSON_SCAN_NUMSTR_CREATE(sidx, eidx) \
    PyUnicode_Substring(pystr, (sidx), (eidx))
#else
#define JSON_SCAN_NUMSTR_CREATE(sidx, eidx) \
    PyUnicode_FromUnicode(&((Py_UNICODE *)str)[(sidx)], (eidx) - (sidx))
#endif
#define JSON_SCAN_PARSE_FLOAT_FAST(ns) _match_number_float_fast_unicode(ns)
#define JSON_SCAN_PARSE_INT_FAST(ns)   _match_number_int_fast_unicode(s, ns)
#define JSON_SPEEDUPS_SCAN_INCLUDING 1
#include "_speedups_scan.h"
```
