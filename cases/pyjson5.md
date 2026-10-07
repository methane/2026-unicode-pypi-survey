# pyjson5 — non-simple Unicode reads

[All packages](README.md)

Version: 2.0.1. **20 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`_skip_single_line`](#case-001)
- [`_skip_multiline_comment`](#case-002)
- [`_skip_to_data_sub`](#case-003)
- [`_skip_to_data`](#case-004)
- [`_get_hex_character`](#case-005)
- [`_get_escape_sequence`](#case-006)
- [`_decode_string_sub`](#case-007)
- [`_decode_string`](#case-008)
- [`_decode_number_leading_zero`](#case-009)
- [`_decode_number_any`](#case-010)
- [`_decode_number`](#case-011)
- [`_skip_comma`](#case-012)
- [`_decode_identifier_name`](#case-013)
- [`_accept_string`](#case-014)
- [`_encode_unicode_impl`](#case-015)
- [`_encode_unicode`](#case-016)
- [`_encode_nested_key`](#case-017)
- [`_encode_datetime`](#case-018)
- [`_reader_ucs_get`](#case-019)
- [`EscapeDct::find_unescaped_range`](#case-020)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `_skip_single_line`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 5–12. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L5-L12).

### Read sites

- Site 1: lines 5–12; sequential parser range; index expression `_reader_get(reader) at lines 8`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 5–12. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L5-L12).

```cython
cdef boolean _skip_single_line(ReaderRef reader) except False:
    cdef uint32_t c0
    while _reader_good(reader):
        c0 = _reader_get(reader)
        if _is_line_terminator(c0):
            break

    return True
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-002"></a>

## 2. `_skip_multiline_comment`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 15–33. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L15-L33).

### Read sites

- Site 1: lines 15–33; sequential parser range; index expression `_reader_get(reader) at lines 24`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 15–33. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L15-L33).

```cython
cdef boolean _skip_multiline_comment(ReaderRef reader) except False:
    cdef uint32_t c0
    cdef boolean seen_asterisk = False
    cdef Py_ssize_t comment_start = _reader_tell(reader)

    while True:
        if expect(not _reader_good(reader), False):
            break

        c0 = _reader_get(reader)
        if c0 == b'*':
            seen_asterisk = True
        elif seen_asterisk:
            if c0 == b'/':
                return True
            seen_asterisk = False

    _raise_unclosed(b'comment', comment_start)
    return False
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-003"></a>

## 3. `_skip_to_data_sub`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 39–72. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L39-L72).

### Read sites

- Site 1: lines 39–72; sequential parser range; index expression `_reader_get(reader) at lines 67`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 39–72. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L39-L72).

```cython
cdef int32_t _skip_to_data_sub(ReaderRef reader, uint32_t c0) except -2:
    cdef int32_t c1 = 0  # silence warning
    cdef boolean seen_slash

    seen_slash = False
    while True:
        if c0 == b'/':
            if seen_slash:
                _skip_single_line(reader)
                seen_slash = False
            else:
                seen_slash = True
        elif c0 == b'*':
            if expect(not seen_slash, False):
                _raise_stray_character('asterisk', _reader_tell(reader))

            _skip_multiline_comment(reader)
            seen_slash = False
        elif not _is_ws_zs(c0):
            c1 = cast_to_int32(c0)
            break
        elif expect(seen_slash, False):
            _raise_stray_character('slash', _reader_tell(reader))

        if not _reader_good(reader):
            c1 = -1
            break

        c0 = _reader_get(reader)

    if expect(seen_slash, False):
        _raise_stray_character('slash', _reader_tell(reader))

    return c1
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-004"></a>

## 4. `_skip_to_data`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 78–86. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L78-L86).

### Read sites

- Site 1: lines 78–86; sequential parser range; index expression `_reader_get(reader) at lines 82`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 78–86. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L78-L86).

```cython
cdef int32_t _skip_to_data(ReaderRef reader) except -2:
    cdef uint32_t c0
    cdef int32_t c1
    if _reader_good(reader):
        c0 = _reader_get(reader)
        c1 = _skip_to_data_sub(reader, c0)
    else:
        c1 = -1
    return c1
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-005"></a>

## 5. `_get_hex_character`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 89–115. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L89-L115).

### Read sites

- Site 1: lines 89–115; sequential parser range; index expression `_reader_get(reader) at lines 102`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 89–115. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L89-L115).

```cython
cdef int32_t _get_hex_character(ReaderRef reader, Py_ssize_t length) except -1:
    cdef Py_ssize_t start
    cdef uint32_t c0
    cdef uint32_t result
    cdef Py_ssize_t index

    start = _reader_tell(reader)
    result = 0
    for index in range(length):
        result <<= 4
        if expect(not _reader_good(reader), False):
            _raise_unclosed(b'escape sequence', start)

        c0 = _reader_get(reader)
        if b'0' <= c0 <= b'9':
            result |= c0 - <uint32_t> b'0'
        elif b'a' <= c0 <= b'f':
            result |= c0 - <uint32_t> b'a' + 10
        elif b'A' <= c0 <= b'F':
            result |= c0 - <uint32_t> b'A' + 10
        else:
            _raise_expected_s('hexadecimal character', start, c0)

    if expect(result > 0x10ffff, False):
        _raise_expected_s('Unicode code point', start, result)

    return cast_to_int32(result)
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-006"></a>

## 6. `_get_escape_sequence`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 141–182. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L141-L182).

### Read sites

- Site 1: lines 141–182; sequential parser range; index expression `_reader_get(reader) at lines 145,176`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_decoder.pyx`: lines 150–171. The original contextual region was lines 141–182.

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 141–149. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L141-L149).

```cython
cdef int32_t _get_escape_sequence(ReaderRef reader,
                                  Py_ssize_t start) except 0x7ffffff:
    cdef uint32_t c0

    c0 = _reader_get(reader)
    if expect(not _reader_good(reader), False):
        _raise_unclosed(b'string', start)

    if c0 == b'b':
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 172–182. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L172-L182).

```cython
    elif _is_line_terminator(c0):
        if c0 != 0x000D:
            return -1

        c0 = _reader_get(reader)
        if c0 == 0x000A:
            return -1

        return -cast_to_int32(c0 + 1)
    else:
        return cast_to_int32(c0)
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-007"></a>

## 7. `_decode_string_sub`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 185–220. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L185-L220).

### Read sites

- Site 1: lines 185–220; sequential parser range; index expression `_reader_get(reader) at lines 202,214`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_decoder.pyx`: lines 195–197, 207–209. The original contextual region was lines 185–220.

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 185–194. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L185-L194).

```cython
cdef object _decode_string_sub(ReaderRef reader, uint32_t delim,
                               Py_ssize_t start, uint32_t c0):
    cdef int32_t c1
    cdef StackHeapString[uint32_t] buf

    while True:
        if expect(c0 == delim, False):
            break

        if expect(not _reader_good(reader), False):
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 198–206. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L198-L206).

```cython
            if expect(c0 in (0xA, 0xD), False):
                _raise_unclosed(b'string', start)

            buf.push_back(c0)
            c0 = _reader_get(reader)
            continue

        c1 = _get_escape_sequence(reader, start)
        if c1 >= -1:
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 210–220. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L210-L220).

```cython
            if c1 >= 0:
                c0 = cast_to_uint32(c1)
                buf.push_back(c0)

            c0 = _reader_get(reader)
        else:
            c0 = cast_to_uint32(-(c1 + 1))

    return PyUnicode_FromKindAndData(
        PyUnicode_4BYTE_KIND, buf.data(), buf.size(),
    )
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-008"></a>

## 8. `_decode_string`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 223–241. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L223-L241).

### Read sites

- Site 1: lines 223–241; sequential parser range; index expression `_reader_get(reader) at lines 237`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 223–241. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L223-L241).

```cython
cdef object _decode_string(ReaderRef reader, int32_t *c_in_out):
    cdef uint32_t delim
    cdef uint32_t c0
    cdef int32_t c1
    cdef Py_ssize_t start
    cdef object result

    c1 = c_in_out[0]
    delim = cast_to_uint32(c1)
    start = _reader_tell(reader)

    if expect(not _reader_good(reader), False):
        _raise_unclosed(b'string', start)

    c0 = _reader_get(reader)
    result = _decode_string_sub(reader, delim, start, c0)

    c_in_out[0] = NO_EXTRA_DATA
    return result
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-009"></a>

## 9. `_decode_number_leading_zero`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 256–330. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L256-L330).

### Read sites

- Site 1: lines 256–330; sequential parser range; index expression `_reader_get(reader) at lines 265,272,295,316`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_decoder.pyx`: lines 284–290, 321–324. The original contextual region was lines 256–330.

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 256–283. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L256-L283).

```cython
cdef object _decode_number_leading_zero(ReaderRef reader, StackHeapString[char] &buf,
                                        int32_t *c_in_out, Py_ssize_t start):
    cdef uint32_t c0
    cdef int32_t c1 = 0  # silence warning

    if not _reader_good(reader):
        c_in_out[0] = -1
        return 0

    c0 = _reader_get(reader)
    if _is_x(c0):
        while True:
            if not _reader_good(reader):
                c1 = -1
                break

            c0 = _reader_get(reader)
            if _is_hexadecimal(c0):
                buf.push_back(<char> <unsigned char> c0)
            elif c0 != b'_':
                c1 = cast_to_int32(c0)
                break

        c_in_out[0] = c1

        buf.push_back(b'\0')
        try:
            return PyLong_FromString(buf.data(), NULL, 16)
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 291–320. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L291-L320).

```cython
            if not _reader_good(reader):
                c1 = -1
                break

            c0 = _reader_get(reader)
            if _is_in_float_representation(c0):
                buf.push_back(<char> <unsigned char> c0)
            elif c0 != b'_':
                c1 = cast_to_int32(c0)
                break

        c_in_out[0] = c1

        if buf.data()[buf.size() - 1] == b'.':
            (<char*> buf.data())[buf.size() - 1] = b'\0'
        else:
            buf.push_back(b'\0')

        return _decode_double(buf, start)
    elif _is_e(c0):
        while True:
            if not _reader_good(reader):
                c1 = -1
                break

            c0 = _reader_get(reader)
            if _is_in_float_representation(c0):
                pass
            elif c0 == b'_':
                pass
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 325–330. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L325-L330).

```cython
        c_in_out[0] = c1
        return 0.0
    else:
        c1 = cast_to_int32(c0)
        c_in_out[0] = c1
        return 0
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-010"></a>

## 10. `_decode_number_any`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 333–391. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L333-L391).

### Read sites

- Site 1: lines 333–391; sequential parser range; index expression `_reader_get(reader) at lines 375`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_decoder.pyx`: lines 354–370, 382–388. The original contextual region was lines 333–391.

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 333–353. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L333-L353).

```cython
cdef object _decode_number_any(ReaderRef reader, StackHeapString[char] &buf,
                               int32_t *c_in_out, Py_ssize_t start):
    cdef uint32_t c0
    cdef int32_t c1
    cdef boolean is_float = False
    cdef boolean was_point = False
    cdef boolean leading_point = False

    c1 = c_in_out[0]
    c0 = cast_to_uint32(c1)

    if c0 == b'.':
        buf.push_back(b'0')
        is_float = True
        leading_point = True

    while True:
        if _is_decimal(c0):
            pass
        elif _is_in_float_representation(c0):
            is_float = True
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 371–381. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L371-L381).

```cython
        if not _reader_good(reader):
            c1 = -1
            break

        c0 = _reader_get(reader)

    c_in_out[0] = c1

    if leading_point and buf.size() == 1:  # single '.'
        _raise_unclosed('NumericLiteral', start)

```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 389–391. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L389-L391).

```cython
        _raise_unclosed('NumericLiteral', start)
    else:
        return _decode_double(buf, start)
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-011"></a>

## 11. `_decode_number`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 394–437. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L394-L437).

### Read sites

- Site 1: lines 394–437; sequential parser range; index expression `_reader_get(reader) at lines 407,420`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_decoder.pyx`: lines 415, 425–431. The original contextual region was lines 394–437.

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 394–414. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L394-L414).

```cython
cdef object _decode_number(ReaderRef reader, int32_t *c_in_out):
    cdef uint32_t c0
    cdef int32_t c1
    cdef Py_ssize_t start = _reader_tell(reader)
    cdef StackHeapString[char] buf

    c1 = c_in_out[0]
    c0 = cast_to_uint32(c1)

    if c0 == b'+':
        if expect(not _reader_good(reader), False):
            _raise_unclosed(b'number', start)

        c0 = _reader_get(reader)
        if c0 == b'I':
            _accept_string(reader, b'nfinity')
            c_in_out[0] = NO_EXTRA_DATA
            return CONST_POS_INF
        elif c0 == b'N':
            _accept_string(reader, b'aN')
            c_in_out[0] = NO_EXTRA_DATA
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 416–424. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L416-L424).

```cython
    elif c0 == b'-':
        if expect(not _reader_good(reader), False):
            _raise_unclosed(b'number', start)

        c0 = _reader_get(reader)
        if c0 == b'I':
            _accept_string(reader, b'nfinity')
            c_in_out[0] = NO_EXTRA_DATA
            return CONST_NEG_INF
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 432–437. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L432-L437).

```cython
    if c0 == b'0':
        return _decode_number_leading_zero(reader, buf, c_in_out, start)
    else:
        c1 = cast_to_int32(c0)
        c_in_out[0] = c1
        return _decode_number_any(reader, buf, c_in_out, start)
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-012"></a>

## 12. `_skip_comma`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 443–483. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L443-L483).

### Read sites

- Site 1: lines 443–483; sequential parser range; index expression `_reader_get(reader) at lines 479`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 443–483. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L443-L483).

```cython
cdef uint32_t _skip_comma(ReaderRef reader, Py_ssize_t start,
                          uint32_t terminator, const char *what,
                          int32_t *c_in_out) except -1:
    cdef int32_t c0
    cdef uint32_t c1
    cdef boolean needs_comma
    cdef uint32_t done

    c0 = c_in_out[0]
    c1 = cast_to_uint32(c0)

    needs_comma = True
    while True:
        c0 = _skip_to_data_sub(reader, c1)
        if c0 < 0:
            break

        c1 = cast_to_uint32(c0)
        if c1 == terminator:
            c_in_out[0] = NO_EXTRA_DATA
            return 1

        if c1 != b',':
            if expect(needs_comma, False):
                _raise_expected_sc(
                    'comma', terminator, _reader_tell(reader), c1,
                )
            c_in_out[0] = c0
            return 0

        if expect(not needs_comma, False):
            _raise_stray_character('comma', _reader_tell(reader))

        if expect(not _reader_good(reader), False):
            break

        c1 = _reader_get(reader)
        needs_comma = False

    _raise_unclosed(what, start)
    return -1
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-013"></a>

## 13. `_decode_identifier_name`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 486–527. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L486-L527).

### Read sites

- Site 1: lines 486–527; sequential parser range; index expression `_reader_get(reader) at lines 505,519`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_decoder.pyx`: lines 510–514. The original contextual region was lines 486–527.

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 486–509. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L486-L509).

```cython
cdef unicode _decode_identifier_name(ReaderRef reader, int32_t *c_in_out):
    cdef int32_t c0
    cdef uint32_t c1
    cdef Py_ssize_t start
    cdef StackHeapString[uint32_t] buf

    start = _reader_tell(reader)

    c0 = c_in_out[0]
    c1 = cast_to_uint32(c0)
    if expect(not _is_identifier_start(c1), False):
        _raise_expected_s('IdentifierStart', _reader_tell(reader), c1)

    while True:
        if expect(c1 == b'\\', False):
            if not _reader_good(reader):
                _raise_unclosed('IdentifierName', start)
                break

            c1 = _reader_get(reader)
            if c1 == b'u':
                c1 = cast_to_uint32(_get_escaped_unicode_maybe_surrogate(reader, _reader_tell(reader)))
            elif c1 == b'U':
                c1 = cast_to_uint32(_get_hex_character(reader, 8))
```

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 515–527. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L515-L527).

```cython
        if not _reader_good(reader):
            c0 = -1
            break

        c1 = _reader_get(reader)
        if not _is_identifier_part(c1):
            c0 = cast_to_int32(c1)
            break

    c_in_out[0] = c0
    return PyUnicode_FromKindAndData(
        PyUnicode_4BYTE_KIND, buf.data(), buf.size(),
    )
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-014"></a>

## 14. `_accept_string`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Consumes current reader cursor as a sequential parser continuation. Caller has already consumed preceding syntax; each _reader_get advances exactly one source codepoint. Function reads a selected syntactic range and may stop or reject before end of whole input.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator continuation; no random-access view required by this access pattern.

**Offsets and character semantics:** ReaderUCS position/error locations count codepoints; parsed syntax has scalar lookahead variables but no reread of source.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_decoder.pyx`, lines 631–650. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L631-L650).

### Read sites

- Site 1: lines 631–650; sequential parser range; index expression `_reader_get(reader) at lines 646`. Monotonic read stream, no seek/reset/peek in implementation.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_decoder.pyx`, lines 631–650. Member SHA-256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L631-L650).

```cython
cdef boolean _accept_string(ReaderRef reader, const char *string) except False:
    cdef uint32_t c0
    cdef uint32_t c1
    cdef Py_ssize_t start

    start = _reader_tell(reader)
    while True:
        c0 = string[0]
        string += 1
        if not c0:
            break

        if expect(not _reader_good(reader), False):
            _raise_unclosed(b'literal', start)

        c1 = _reader_get(reader)
        if expect(c0 != c1, False):
            _raise_expected_c(c0, start, c1)

    return True
```

### Callee analysis

- `_reader_get -> _reader_ucs_get` in `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59: Typed pointer only moves forward by one each get. B continuation relative to original source; iterator migration feasible.

Available source context:

- [`_reader_get -> _reader_ucs_get`](#helper-001) (`pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59).

<a id="case-015"></a>

## 15. `_encode_unicode_impl`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, caller-provided start or range, multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

FSR input is walked in escaped/unescaped runs: find_unescaped_range scans a prefix then unescaped prefix is copied again. Consumes advancing data pointer/data[0]; additionally reads options quotationmark[0] twice.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** UCSString element offsets count codepoints; 1-byte unescaped output cast to ASCII. Surrogates escaped independently as \uXXXX; supplementary scalar becomes explicit JSON escape pair.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_encoder.pyx`, lines 1–83. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L1-L83).

### Read sites

- Site 1: lines 10–40; typed run scan and copy; index expression `data += unescaped_length; data[index]; data[0]`. Scan ranges then copy same unescaped characters.
- Site 2: lines 75–81; scalar index; index expression `quotationmark[0]`. Fixed index configuration string read twice.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_encoder.pyx`: lines 5–7, 18–20, 30–33, 44–70. The original contextual region was lines 1–83.

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 1–4. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L1-L4).

```cython
cdef int _encode_unicode_impl(WriterRef writer, UCSString data, Py_ssize_t length) except -1:
    cdef char buf[32]
    cdef uint32_t c
    cdef uint32_t s1, s2
```

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 8–17. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L8-L17).

```cython
    cdef Py_ssize_t sublength

    if length > 0:
        writer.reserve(writer, 2 + length)
        writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
        while True:
            if UCSString is UCS1String:
                sublength = length
            else:
                sublength = min(length, <Py_ssize_t> sizeof(buf))
```

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 21–29. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L21-L29).

```cython
                if UCSString is UCS1String:
                    writer.append_s(writer, <const char*> data, unescaped_length)
                else:
                    for index in range(unescaped_length):
                        buf[index] = <const char> data[index]
                    writer.append_s(writer, buf, unescaped_length)

                data += unescaped_length
                length -= unescaped_length
```

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 34–43. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L34-L43).

```cython
                    continue

            c = data[0]
            if (UCSString is UCS1String) or (c < 0x100):
                escaped_length = ESCAPE_DCT.items[c][0]
                escaped_string = &ESCAPE_DCT.items[c][1]
                writer.append_s(writer, escaped_string, escaped_length)
            elif (UCSString is UCS2String) or (c <= 0xffff):
                buf[0] = b'\\';
                buf[1] = b'u';
```

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 71–83. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L71-L83).

```cython
                buf[0xc] = 0;

                writer.append_s(writer, buf, 12);

            data += 1
            length -= 1
            if length <= 0:
                break
        writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
    else:
        writer.append_s(writer, b'""', 2)

    return True
```

### Callee analysis

- `EscapeDct::find_unescaped_range` in `pyjson5-2.0.1/src/native.hpp`, lines 81–87: index=0; start[index] until first escaped char. B run prefix; then encoder re-copies source prefix.

Available source context:

- [`EscapeDct::find_unescaped_range`](#helper-002) (`pyjson5-2.0.1/src/native.hpp`, lines 81–87).

<a id="case-016"></a>

## 16. `_encode_unicode`

**Classification:** B. **Subtypes:** multiple passes, caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

DATA dispatch forwards full source to _encode_unicode_impl, which scans/copies runs and performs fixed quotationmark reads.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_encoder.pyx`, lines 86–104. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L86-L104).

### Read sites

- Site 1: lines 86–104; typed handoff; index expression `1/2/4BYTE_DATA, GET_LENGTH`. Known in-file callee performs scan+copy.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 86–104. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L86-L104).

```cython
cdef int _encode_unicode(WriterRef writer, object data) except -1:
    cdef Py_ssize_t length
    cdef int kind

    PyUnicode_READY(data)

    length = PyUnicode_GET_LENGTH(data)
    kind = PyUnicode_KIND(data)

    if kind == PyUnicode_1BYTE_KIND:
        _encode_unicode_impl(writer, PyUnicode_1BYTE_DATA(data), length)
    elif kind == PyUnicode_2BYTE_KIND:
        _encode_unicode_impl(writer, PyUnicode_2BYTE_DATA(data), length)
    elif kind == PyUnicode_4BYTE_KIND:
        _encode_unicode_impl(writer, PyUnicode_4BYTE_DATA(data), length)
    else:
        pass  # impossible

    return True
```

### Callee analysis

- `_encode_unicode_impl` in `pyjson5-2.0.1/src/_encoder.pyx`, lines 1–83: Advancing pointer and run scanner followed by copies. B scan+copy and fixed config indexing.
- `EscapeDct::find_unescaped_range` in `pyjson5-2.0.1/src/native.hpp`, lines 81–87: index=0; start[index] until first escaped char. B run prefix; then encoder re-copies source prefix.

Available source context:
Omitted from `pyjson5-2.0.1/src/_encoder.pyx`: lines 7–8, 18–20, 30–40, 50–56, 66–74. The original contextual region was lines 1–83.

- [`_encode_unicode_impl`](#helper-003) (`pyjson5-2.0.1/src/_encoder.pyx`, lines 1–6).
- [`_encode_unicode_impl`](#helper-004) (`pyjson5-2.0.1/src/_encoder.pyx`, lines 9–17).
- [`_encode_unicode_impl`](#helper-005) (`pyjson5-2.0.1/src/_encoder.pyx`, lines 21–29).
- [`_encode_unicode_impl`](#helper-006) (`pyjson5-2.0.1/src/_encoder.pyx`, lines 41–49).
- [`_encode_unicode_impl`](#helper-007) (`pyjson5-2.0.1/src/_encoder.pyx`, lines 57–65).
- [`_encode_unicode_impl`](#helper-008) (`pyjson5-2.0.1/src/_encoder.pyx`, lines 75–83).
- [`EscapeDct::find_unescaped_range`](#helper-002) (`pyjson5-2.0.1/src/native.hpp`, lines 81–87).

<a id="case-017"></a>

## 17. `_encode_nested_key`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads quotationmark[0] twice. Main loop reads owned serialized sub_writer.obj byte buffer rather than original Python FSR input.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Quotationmark ASCII codepoint/byte; nested-key serialized string uses byte indices, separate buffer.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_encoder.pyx`, lines 107–142. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L107-L142).

### Read sites

- Site 1: lines 130–137; scalar index; index expression `quotationmark[0]`. Repeated fixed configuration character.

### Contextual source excerpts

Omitted from `pyjson5-2.0.1/src/_encoder.pyx`: lines 111–125. The original contextual region was lines 107–142.

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 107–110. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L107-L110).

```cython
cdef int _encode_nested_key(WriterRef writer, object data) except -1:
    cdef const char *string
    cdef char c
    cdef Py_ssize_t index, length
```

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 126–142. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L126-L142).

```cython

        length = sub_writer.position
        string = <char*> sub_writer.obj

        writer.reserve(writer, 2 + length)
        writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
        for index in range(length):
            c = string[index]
            if c in b'\\"':
                writer.append_c(writer, b'\\')
            writer.append_c(writer, c)
        writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
    finally:
        if sub_writer.obj is not NULL:
            ObjectFree(sub_writer.obj)

    return True
```


<a id="case-018"></a>

## 18. `_encode_datetime`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads quotationmark[0] before and after appending strict UTF-8 isoformat bytes; fixed config index, not FSR traversal of datetime output.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Quote is ASCII; isoformat string strict UTF-8 length is bytes.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_encoder.pyx`, lines 269–286. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L269-L286).

### Read sites

- Site 1: lines 277–284; scalar index; index expression `quotationmark[0] twice`. Single-character configuration consumed twice.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 269–286. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L269-L286).

```cython
cdef int _encode_datetime(WriterRef writer, object data) except -1:
    cdef object stringified
    cdef Py_ssize_t length
    cdef const char *string

    if not isinstance(data, DATETIME_CLASSES):
        return False

    stringified = data.isoformat()
    length = 0
    string = PyUnicode_AsUTF8AndSize(stringified, &length)

    writer.reserve(writer, 2 + length)
    writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
    writer.append_s(writer, string, length)
    writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])

    return True
```


<a id="case-019"></a>

## 19. `_reader_ucs_get`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads one element from current stream cursor and increments cursor. Standalone invocation starts wherever caller reader currently is; across whole Unicode decode calls are strictly forward from0.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

Codepoint iterator primitive; avoid classifying this B range-continuation as needing FSR/random access.

**Offsets and character semantics:** Pointer advances by typed FSR element; position/remaining count codepoints in UCS1/2/4 specializations.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Sequential iterator primitive, not random-access need.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59. Member SHA-256: `20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_reader_ucs.pyx#L52-L59).

### Read sites

- Site 1: lines 52–59; sequential cursor; index expression `self.string[0]; string+=1`. Exactly one current codepoint consumed, no random seek or lookahead.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59. Member SHA-256: `20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_reader_ucs.pyx#L52-L59).

```cython
cdef inline uint32_t _reader_ucs_get(ReaderUCSRef self) noexcept nogil:
    cdef int32_t c = self.string[0]

    self.string += 1
    self.base.remaining -= 1
    self.base.position += 1

    return cast_to_uint32(c)
```


<a id="case-020"></a>

## 20. `EscapeDct::find_unescaped_range`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts index0 relative to caller-supplied current pointer, scans until escaped character or sublength. Caller pointer may already be inside original Unicode.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Typed S element indexes count FSR codepoints.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Iterator-compatible scan when fused with output; existing implementation rereads copied run.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz). Archive SHA-256: `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

**Function source:** `pyjson5-2.0.1/src/native.hpp`, lines 81–87. Member SHA-256: `37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085`.

[Verified immutable function link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L81-L87).

### Read sites

- Site 1: lines 81–87; typed prefix scan; index expression `start[index]; index=0..length until is_escaped`. Prefix scan; returned unescaped span copied again by encoder.

### Contextual source excerpts

Archive member `pyjson5-2.0.1/src/native.hpp`, lines 81–87. Member SHA-256: `37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L81-L87).

```cpp
    static inline std::size_t find_unescaped_range(const S *start, Py_ssize_t length) {
        Py_ssize_t index = 0;
        while ((index < length) && !is_escaped(start[index])) {
            ++index;
        }
        return index;
    }
```


<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `_reader_get -> _reader_ucs_get`

Archive member `pyjson5-2.0.1/src/_reader_ucs.pyx`, lines 52–59. Member SHA-256: `20899d35bd6ce53461eed29ff0a1257b444f817c12af9708af6b6383224562a0`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_reader_ucs.pyx#L52-L59).

```cython
cdef inline uint32_t _reader_ucs_get(ReaderUCSRef self) noexcept nogil:
    cdef int32_t c = self.string[0]

    self.string += 1
    self.base.remaining -= 1
    self.base.position += 1

    return cast_to_uint32(c)
```

<a id="helper-002"></a>

### 2. `EscapeDct::find_unescaped_range`

Archive member `pyjson5-2.0.1/src/native.hpp`, lines 81–87. Member SHA-256: `37f48f8c4e342490ed840b5e0d66f8ced7f80390d911d14796fe03c09e587085`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/native.hpp#L81-L87).

```cpp
    static inline std::size_t find_unescaped_range(const S *start, Py_ssize_t length) {
        Py_ssize_t index = 0;
        while ((index < length) && !is_escaped(start[index])) {
            ++index;
        }
        return index;
    }
```

<a id="helper-003"></a>

### 3. `_encode_unicode_impl`

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 1–6. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L1-L6).

```cython
cdef int _encode_unicode_impl(WriterRef writer, UCSString data, Py_ssize_t length) except -1:
    cdef char buf[32]
    cdef uint32_t c
    cdef uint32_t s1, s2
    cdef const char *escaped_string
    cdef Py_ssize_t escaped_length
```

<a id="helper-004"></a>

### 4. `_encode_unicode_impl`

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 9–17. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L9-L17).

```cython

    if length > 0:
        writer.reserve(writer, 2 + length)
        writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
        while True:
            if UCSString is UCS1String:
                sublength = length
            else:
                sublength = min(length, <Py_ssize_t> sizeof(buf))
```

<a id="helper-005"></a>

### 5. `_encode_unicode_impl`

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 21–29. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L21-L29).

```cython
                if UCSString is UCS1String:
                    writer.append_s(writer, <const char*> data, unescaped_length)
                else:
                    for index in range(unescaped_length):
                        buf[index] = <const char> data[index]
                    writer.append_s(writer, buf, unescaped_length)

                data += unescaped_length
                length -= unescaped_length
```

<a id="helper-006"></a>

### 6. `_encode_unicode_impl`

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 41–49. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L41-L49).

```cython
            elif (UCSString is UCS2String) or (c <= 0xffff):
                buf[0] = b'\\';
                buf[1] = b'u';
                buf[2] = HEX[(c >> (4*3)) & 0xf];
                buf[3] = HEX[(c >> (4*2)) & 0xf];
                buf[4] = HEX[(c >> (4*1)) & 0xf];
                buf[5] = HEX[(c >> (4*0)) & 0xf];
                buf[6] = 0;

```

<a id="helper-007"></a>

### 7. `_encode_unicode_impl`

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 57–65. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L57-L65).

```cython
                buf[0x0] = b'\\';
                buf[0x1] = b'u';
                buf[0x2] = HEX[(s1 >> (4*3)) & 0xf];
                buf[0x3] = HEX[(s1 >> (4*2)) & 0xf];
                buf[0x4] = HEX[(s1 >> (4*1)) & 0xf];
                buf[0x5] = HEX[(s1 >> (4*0)) & 0xf];

                buf[0x6] = b'\\';
                buf[0x7] = b'u';
```

<a id="helper-008"></a>

### 8. `_encode_unicode_impl`

Archive member `pyjson5-2.0.1/src/_encoder.pyx`, lines 75–83. Member SHA-256: `2227b86c27b02b24d24d26531e024f6401076fa19f162a5b8daaab03830b66ad`. [Verified immutable source link](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_encoder.pyx#L75-L83).

```cython
            data += 1
            length -= 1
            if length <= 0:
                break
        writer.append_c(writer, <char> PyUnicode_1BYTE_DATA((<Options> writer.options).quotationmark)[0])
    else:
        writer.append_s(writer, b'""', 2)

    return True
```
