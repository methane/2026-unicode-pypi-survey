# regex — non-simple Unicode reads

[All packages](README.md)

Version: 2026.9.29. **85 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`bytes1_char_at`](#case-001)
- [`bytes2_char_at`](#case-002)
- [`bytes4_char_at`](#case-003)
- [`ascii_word_left`](#case-004)
- [`ascii_word_right`](#case-005)
- [`ascii_at_line_start`](#case-006)
- [`ascii_at_line_end`](#case-007)
- [`locale_word_left`](#case-008)
- [`locale_word_right`](#case-009)
- [`unicode_word_left`](#case-010)
- [`unicode_word_right`](#case-011)
- [`unicode_at_default_boundary`](#case-012)
- [`unicode_at_grapheme_boundary`](#case-013)
- [`unicode_at_line_start`](#case-014)
- [`unicode_at_line_end`](#case-015)
- [`match_many_ANY`](#case-016)
- [`match_many_ANY_REV`](#case-017)
- [`match_many_ANY_U`](#case-018)
- [`match_many_ANY_U_REV`](#case-019)
- [`match_many_CHARACTER`](#case-020)
- [`match_many_CHARACTER_IGN`](#case-021)
- [`match_many_CHARACTER_IGN_REV`](#case-022)
- [`match_many_CHARACTER_REV`](#case-023)
- [`match_many_PROPERTY`](#case-024)
- [`match_many_PROPERTY_IGN`](#case-025)
- [`match_many_PROPERTY_IGN_REV`](#case-026)
- [`match_many_PROPERTY_REV`](#case-027)
- [`match_many_RANGE`](#case-028)
- [`match_many_RANGE_IGN`](#case-029)
- [`match_many_RANGE_IGN_REV`](#case-030)
- [`match_many_RANGE_REV`](#case-031)
- [`match_many_SET`](#case-032)
- [`match_many_SET_IGN`](#case-033)
- [`match_many_SET_IGN_REV`](#case-034)
- [`match_many_SET_REV`](#case-035)
- [`simple_string_search`](#case-036)
- [`simple_string_search_ign`](#case-037)
- [`simple_string_search_ign_rev`](#case-038)
- [`simple_string_search_rev`](#case-039)
- [`fast_string_search`](#case-040)
- [`fast_string_search_ign`](#case-041)
- [`fast_string_search_ign_rev`](#case-042)
- [`fast_string_search_rev`](#case-043)
- [`string_search_fld`](#case-044)
- [`string_search_fld_rev`](#case-045)
- [`try_match_ANY`](#case-046)
- [`try_match_ANY_REV`](#case-047)
- [`try_match_ANY_U`](#case-048)
- [`try_match_ANY_U_REV`](#case-049)
- [`try_match_CHARACTER`](#case-050)
- [`try_match_CHARACTER_IGN`](#case-051)
- [`try_match_CHARACTER_IGN_REV`](#case-052)
- [`try_match_CHARACTER_REV`](#case-053)
- [`try_match_END_OF_LINE`](#case-054)
- [`try_match_PROPERTY`](#case-055)
- [`try_match_PROPERTY_IGN`](#case-056)
- [`try_match_PROPERTY_IGN_REV`](#case-057)
- [`try_match_PROPERTY_REV`](#case-058)
- [`try_match_RANGE`](#case-059)
- [`try_match_RANGE_IGN`](#case-060)
- [`try_match_RANGE_IGN_REV`](#case-061)
- [`try_match_RANGE_REV`](#case-062)
- [`try_match_SET`](#case-063)
- [`try_match_SET_IGN`](#case-064)
- [`try_match_SET_IGN_REV`](#case-065)
- [`try_match_SET_REV`](#case-066)
- [`try_match_START_OF_LINE`](#case-067)
- [`try_match_STRING`](#case-068)
- [`try_match_STRING_FLD`](#case-069)
- [`try_match_STRING_FLD_REV`](#case-070)
- [`try_match_STRING_IGN`](#case-071)
- [`try_match_STRING_IGN_REV`](#case-072)
- [`try_match_STRING_REV`](#case-073)
- [`search_start_END_OF_LINE`](#case-074)
- [`search_start_END_OF_LINE_rev`](#case-075)
- [`search_start_START_OF_LINE`](#case-076)
- [`search_start_START_OF_LINE_rev`](#case-077)
- [`fuzzy_ext_match`](#case-078)
- [`folded_char_at`](#case-079)
- [`fuzzy_ext_match_group_fld`](#case-080)
- [`partial_string_match`](#case-081)
- [`partial_string_match_ign`](#case-082)
- [`basic_match`](#case-083)
- [`get_string`](#case-084)
- [`state_init_2`](#case-085)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `bytes1_char_at`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive reader.

Reads *((Py_UCS1/2/4*)text + pos), where pos comes from the caller. These are handwritten primitive getters, not compatibility/API definitions.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** No risk was identified in this case.

- Shared primitive reader counted once as a source function; callers count their own access algorithms, not every runtime invocation.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 763–765. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L763-L765).

### Read sites

- Site 1: lines 764–764; typed codepoint pointer read; index expression `pos`. Dereferences caller-supplied codepoint index; dispatch primitive shared by many engine callers.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 763–765. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L763-L765).

```c
static Py_UCS4 bytes1_char_at(void* text, Py_ssize_t pos) {
    return *((Py_UCS1*)text + pos);
}
```


<a id="case-002"></a>

## 2. `bytes2_char_at`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive reader.

Reads *((Py_UCS1/2/4*)text + pos), where pos comes from the caller. These are handwritten primitive getters, not compatibility/API definitions.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** No risk was identified in this case.

- Shared primitive reader counted once as a source function; callers count their own access algorithms, not every runtime invocation.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 778–780. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L778-L780).

### Read sites

- Site 1: lines 779–779; typed codepoint pointer read; index expression `pos`. Dereferences caller-supplied codepoint index; dispatch primitive shared by many engine callers.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 778–780. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L778-L780).

```c
static Py_UCS4 bytes2_char_at(void* text, Py_ssize_t pos) {
    return *((Py_UCS2*)text + pos);
}
```


<a id="case-003"></a>

## 3. `bytes4_char_at`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive reader.

Reads *((Py_UCS1/2/4*)text + pos), where pos comes from the caller. These are handwritten primitive getters, not compatibility/API definitions.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** No risk was identified in this case.

- Shared primitive reader counted once as a source function; callers count their own access algorithms, not every runtime invocation.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 793–795. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L793-L795).

### Read sites

- Site 1: lines 794–794; typed codepoint pointer read; index expression `pos`. Dereferences caller-supplied codepoint index; dispatch primitive shared by many engine callers.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 793–795. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L793-L795).

```c
static Py_UCS4 bytes4_char_at(void* text, Py_ssize_t pos) {
    return *((Py_UCS4*)text + pos);
}
```


<a id="case-004"></a>

## 4. `ascii_word_left`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests the codepoint immediately before caller-provided text_pos (text_pos - 1), guarded against text_start.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 849–852. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L849-L852).

### Read sites

- Site 1: lines 851–851; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 849–852. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L849-L852).

```c
Py_LOCAL_INLINE(bool) ascii_word_left(RE_State* state, Py_ssize_t text_pos) {
    return text_pos > state->text_start && ascii_has_property(RE_PROP_WORD,
      state->char_at(state->text, text_pos - 1));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-005"></a>

## 5. `ascii_word_right`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests the codepoint at caller-provided text_pos, guarded against text_end; right-side boundary probe rather than a full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 855–858. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L855-L858).

### Read sites

- Site 1: lines 857–857; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 855–858. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L855-L858).

```c
Py_LOCAL_INLINE(bool) ascii_word_right(RE_State* state, Py_ssize_t text_pos) {
    return text_pos < state->text_end && ascii_has_property(RE_PROP_WORD,
      state->char_at(state->text, text_pos));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-006"></a>

## 6. `ascii_at_line_start`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

CR/LF boundary test reads text_pos and/or text_pos - 1. Caller-selected boundary can be inside the string; neighboring reads check whether CRLF is a pair.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 899–916. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L899-L916).

### Read sites

- Site 1: lines 905–905; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 2: lines 912–912; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 899–916. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L899-L916).

```c
static bool ascii_at_line_start(RE_State* state, Py_ssize_t text_pos) {
    Py_UCS4 ch;

    if (text_pos <= state->text_start)
        return true;

    ch = state->char_at(state->text, text_pos - 1);

    if (ch == 0x0D) {
        if (text_pos >= state->text_end)
            return true;

        /* No line break inside CRLF. */
        return state->char_at(state->text, text_pos) != 0x0A;
    }

    return 0x0A <= ch && ch <= 0x0D;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-007"></a>

## 7. `ascii_at_line_end`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

CR/LF boundary test reads text_pos and/or text_pos - 1. Caller-selected boundary can be inside the string; neighboring reads check whether CRLF is a pair.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 919–936. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L919-L936).

### Read sites

- Site 1: lines 925–925; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 932–932; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 919–936. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L919-L936).

```c
static bool ascii_at_line_end(RE_State* state, Py_ssize_t text_pos) {
    Py_UCS4 ch;

    if (text_pos >= state->text_end)
        return true;

    ch = state->char_at(state->text, text_pos);

    if (ch == 0x0A) {
        if (text_pos <= state->text_start)
            return true;

        /* No line break inside CRLF. */
        return state->char_at(state->text, text_pos - 1) != 0x0D;
    }

    return 0x0A <= ch && ch <= 0x0D;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-008"></a>

## 8. `locale_word_left`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests the codepoint immediately before caller-provided text_pos (text_pos - 1), guarded against text_start.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1222–1225. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1222-L1225).

### Read sites

- Site 1: lines 1224–1224; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 1222–1225. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1222-L1225).

```c
Py_LOCAL_INLINE(bool) locale_word_left(RE_State* state, Py_ssize_t text_pos) {
    return text_pos > state->text_start && locale_has_property(state->locale_info,
      RE_PROP_WORD, state->char_at(state->text, text_pos - 1));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-009"></a>

## 9. `locale_word_right`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests the codepoint at caller-provided text_pos, guarded against text_end; right-side boundary probe rather than a full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1228–1232. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1228-L1232).

### Read sites

- Site 1: lines 1231–1231; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 1228–1232. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1228-L1232).

```c
Py_LOCAL_INLINE(bool) locale_word_right(RE_State* state, Py_ssize_t text_pos) {
    return text_pos < state->text_end &&
      locale_has_property(state->locale_info, RE_PROP_WORD,
      state->char_at(state->text, text_pos));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-010"></a>

## 10. `unicode_word_left`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests the codepoint immediately before caller-provided text_pos (text_pos - 1), guarded against text_start.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1447–1450. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1447-L1450).

### Read sites

- Site 1: lines 1449–1449; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 1447–1450. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1447-L1450).

```c
Py_LOCAL_INLINE(bool) unicode_word_left(RE_State* state, Py_ssize_t text_pos) {
    return text_pos > state->text_start && unicode_has_property(RE_PROP_WORD,
      state->char_at(state->text, text_pos - 1));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-011"></a>

## 11. `unicode_word_right`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests the codepoint at caller-provided text_pos, guarded against text_end; right-side boundary probe rather than a full-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1453–1457. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1453-L1457).

### Read sites

- Site 1: lines 1456–1456; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 1453–1457. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1453-L1457).

```c
Py_LOCAL_INLINE(bool) unicode_word_right(RE_State* state, Py_ssize_t text_pos)
  {
    return text_pos < state->text_end && unicode_has_property(RE_PROP_WORD,
      state->char_at(state->text, text_pos));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-012"></a>

## 12. `unicode_at_default_boundary`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Unicode word-boundary test reads left_pos=text_pos-1 and right_pos=text_pos, probes left_pos-1/right_pos+1, walks left over Extend/Format/ZWJ, and revisits the left side to count regional indicators.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1531–1749. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1531-L1749).

### Read sites

- Site 1: lines 1553–1553; codepoint read via helper; index expression `left_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 1554–1554; codepoint read via helper; index expression `right_pos`. Exact read expression; access pattern explained at function level.
- Site 3: lines 1599–1599; codepoint read via helper; index expression `left_pos`. Exact read expression; access pattern explained at function level.
- Site 4: lines 1619–1619; codepoint read via helper; index expression `right_pos + 1`. Exact read expression; access pattern explained at function level.
- Site 5: lines 1632–1632; codepoint read via helper; index expression `left_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 6: lines 1650–1650; codepoint read via helper; index expression `right_pos + 1`. Exact read expression; access pattern explained at function level.
- Site 7: lines 1663–1663; codepoint read via helper; index expression `left_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 8: lines 1692–1692; codepoint read via helper; index expression `left_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 9: lines 1706–1706; codepoint read via helper; index expression `right_pos + 1`. Exact read expression; access pattern explained at function level.
- Site 10: lines 1739–1739; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 1535–1548, 1559–1594, 1604–1614, 1624–1627, 1637–1645, 1655–1658, 1668–1687, 1697–1701, 1711–1734, 1744–1746. The original contextual region was lines 1531–1749.

Archive member `regex-2026.9.29/src/_regex.c`, lines 1531–1534. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1531-L1534).

```c
static bool unicode_at_default_boundary(RE_State* state, Py_ssize_t text_pos) {
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    Py_ssize_t left_pos;
    Py_ssize_t right_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1549–1558. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1549-L1558).

```c
    char_at = state->char_at;

    left_pos = text_pos - 1;
    right_pos = text_pos;
    left_char = char_at(state->text, left_pos);
    right_char = char_at(state->text, right_pos);

    /* Do not break within CRLF. */
    /* WB3 */
    left_prop = re_get_word_break(left_char);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1595–1603. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1595-L1603).

```c
      left_prop == RE_WBREAK_ZWJ) {
        if (left_pos <= state->text_start)
            return false;
        --left_pos;
        left_char = char_at(state->text, left_pos);
        left_prop = re_get_word_break(left_char);
    }

    /* Do not break between most letters. */
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1615–1623. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1615-L1623).

```c
    if (right_pos + 1 < state->text_end) {
        Py_UCS4 right_right_char;
        uint32_t right_right_prop;

        right_right_char = char_at(state->text, right_pos + 1);
        right_right_prop = re_get_word_break(right_right_char);

        if (IS_AHLETTER(left_prop) && (right_prop == RE_WBREAK_MIDLETTER ||
          IS_MIDNUMLETQ(right_prop)) && IS_AHLETTER(right_right_prop))
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1628–1636. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1628-L1636).

```c
    if (left_pos - 1 >= state->text_start) {
        Py_UCS4 left_left_char;
        uint32_t left_left_prop;

        left_left_char = char_at(state->text, left_pos - 1);
        left_left_prop = re_get_word_break(left_left_char);

        if (IS_AHLETTER(left_left_prop) && (left_prop == RE_WBREAK_MIDLETTER ||
          IS_MIDNUMLETQ(left_prop)) && IS_AHLETTER(right_prop))
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1646–1654. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1646-L1654).

```c
    if (right_pos + 1 < state->text_end) {
        Py_UCS4 right_right_char;
        uint32_t right_right_prop;

        right_right_char = char_at(state->text, right_pos + 1);
        right_right_prop = re_get_word_break(right_right_char);

        if (left_prop == RE_WBREAK_HEBREWLETTER && right_prop ==
          RE_WBREAK_DOUBLEQUOTE && right_right_prop == RE_WBREAK_HEBREWLETTER)
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1659–1667. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1659-L1667).

```c
    if (left_pos - 1 >= state->text_start) {
        Py_UCS4 left_left_char;
        uint32_t left_left_prop;

        left_left_char = char_at(state->text, left_pos - 1);
        left_left_prop = re_get_word_break(left_left_char);

        if (left_left_prop == RE_WBREAK_HEBREWLETTER && left_prop ==
          RE_WBREAK_DOUBLEQUOTE && right_prop == RE_WBREAK_HEBREWLETTER)
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1688–1696. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1688-L1696).

```c
    if (left_pos - 1 >= state->text_start) {
        Py_UCS4 left_left_char;
        uint32_t left_left_prop;

        left_left_char = char_at(state->text, left_pos - 1);
        left_left_prop = re_get_word_break(left_left_char);

        if (left_left_prop == RE_WBREAK_NUMERIC && (left_prop ==
          RE_WBREAK_MIDNUM || IS_MIDNUMLETQ(left_prop)) && right_prop ==
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1702–1710. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1702-L1710).

```c
    if (right_pos + 1 < state->text_end) {
        Py_UCS4 right_right_char;
        uint32_t right_right_prop;

        right_right_char = char_at(state->text, right_pos + 1);
        right_right_prop = re_get_word_break(right_right_char);

        if (left_prop == RE_WBREAK_NUMERIC && (right_prop == RE_WBREAK_MIDNUM
          || IS_MIDNUMLETQ(right_prop)) && right_right_prop ==
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1735–1743. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1735-L1743).

```c
     */
    /* WB15 and WB16 */
    pos = left_pos;

    while (pos >= state->text_start && re_get_word_break(char_at(state->text, pos)) ==
      RE_WBREAK_REGIONALINDICATOR)
        --pos;

    if ((left_pos - pos) % 2 == 1)
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1747–1749. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1747-L1749).

```c
    /* WB999 */
    return true;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-013"></a>

## 13. `unicode_at_grapheme_boundary`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Grapheme-boundary test probes text_pos-1/text_pos, then independently walks backward through Indic conjuncts, emoji Extend sequences and regional indicators; the same prefix can be revisited.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1786–1933. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1786-L1933).

### Read sites

- Site 1: lines 1810–1810; codepoint read via helper; index expression `left_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 1811–1811; codepoint read via helper; index expression `right_pos`. Exact read expression; access pattern explained at function level.
- Site 3: lines 1877–1877; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 4: lines 1904–1905; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 5: lines 1908–1909; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 6: lines 1922–1923; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 1790–1805, 1816–1872, 1882–1899, 1914–1917, 1928–1930. The original contextual region was lines 1786–1933.

Archive member `regex-2026.9.29/src/_regex.c`, lines 1786–1789. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1786-L1789).

```c
static bool unicode_at_grapheme_boundary(RE_State* state, Py_ssize_t text_pos)
  {
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    Py_ssize_t left_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1806–1815. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1806-L1815).

```c
    char_at = state->char_at;

    left_pos = text_pos - 1;
    right_pos = text_pos;
    left_char = char_at(state->text, left_pos);
    right_char = char_at(state->text, right_pos);

    /* Do not break between a CR and LF. Otherwise, break before and after
     * controls.
     */
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1873–1881. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1873-L1881).

```c
        has_linker = false;
        pos = left_pos;

        do {
            prop = re_get_indic_conjunct_break(char_at(state->text, pos));

            switch (prop) {
            case RE_INCB_LINKER:
                has_linker = true;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1900–1913. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1900-L1913).

```c
    if (left_prop == RE_GBREAK_ZWJ && re_get_extended_pictographic(right_char))
      {
        pos = left_pos - 1;

        while (pos >= state->text_start && re_get_grapheme_cluster_break(char_at(state->text,
          pos)) == RE_GBREAK_EXTEND)
            --pos;

        if (pos >= state->text_start && re_get_extended_pictographic(char_at(state->text,
          pos)))
            return false;
    }

    /* The \p{Extended_Pictographic} values are provided as a part of the Emoji
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1918–1927. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1918-L1927).

```c
    /* GB12 and GB13 */
    if (right_prop == RE_GBREAK_REGIONALINDICATOR) {
        pos = left_pos;

        while (pos >= state->text_start && re_get_grapheme_cluster_break(char_at(state->text,
          pos)) == RE_GBREAK_REGIONALINDICATOR)
            --pos;

        if ((left_pos - pos) % 2 == 1)
            return false;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 1931–1933. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1931-L1933).

```c
    /* GB999 */
    return true;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-014"></a>

## 14. `unicode_at_line_start`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

CR/LF boundary test reads text_pos and/or text_pos - 1. Caller-selected boundary can be inside the string; neighboring reads check whether CRLF is a pair.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1942–1960. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1942-L1960).

### Read sites

- Site 1: lines 1948–1948; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 2: lines 1955–1955; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 1942–1960. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1942-L1960).

```c
static bool unicode_at_line_start(RE_State* state, Py_ssize_t text_pos) {
    Py_UCS4 ch;

    if (text_pos <= state->text_start)
        return true;

    ch = state->char_at(state->text, text_pos - 1);

    if (ch == 0x0D) {
        if (text_pos >= state->text_end)
            return true;

        /* No line break inside CRLF. */
        return state->char_at(state->text, text_pos) != 0x0A;
    }

    return (0x0A <= ch && ch <= 0x0D) || ch == 0x85 || ch == 0x2028 || ch ==
      0x2029;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-015"></a>

## 15. `unicode_at_line_end`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

CR/LF boundary test reads text_pos and/or text_pos - 1. Caller-selected boundary can be inside the string; neighboring reads check whether CRLF is a pair.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 1963–1981. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1963-L1981).

### Read sites

- Site 1: lines 1969–1969; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 1976–1976; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 1963–1981. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1963-L1981).

```c
static bool unicode_at_line_end(RE_State* state, Py_ssize_t text_pos) {
    Py_UCS4 ch;

    if (text_pos >= state->text_end)
        return true;

    ch = state->char_at(state->text, text_pos);

    if (ch == 0x0A) {
        if (text_pos <= state->text_start)
            return true;

        /* No line break inside CRLF. */
        return state->char_at(state->text, text_pos - 1) != 0x0D;
    }

    return (0x0A <= ch && ch <= 0x0D) || ch == 0x85 || ch == 0x2028 || ch ==
      0x2029;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-016"></a>

## 16. `match_many_ANY`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3537–3589. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3537-L3589).

### Read sites

- Site 1: lines 3552–3552; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3566–3566; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3580–3580; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3541–3547, 3557–3561, 3571–3575, 3585–3586. The original contextual region was lines 3537–3589.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3537–3540. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3537-L3540).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_ANY(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3548–3556. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3548-L3556).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] != '\n') == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3562–3570. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3562-L3570).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] != '\n') == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3576–3584. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3576-L3584).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] != '\n') == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3587–3589. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3587-L3589).

```c

    return text_pos;
}
```


<a id="case-017"></a>

## 17. `match_many_ANY_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3592–3644. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3592-L3644).

### Read sites

- Site 1: lines 3607–3607; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3621–3621; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3635–3635; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3596–3602, 3612–3616, 3626–3630, 3640–3641. The original contextual region was lines 3592–3644.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3592–3595. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3592-L3595).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_ANY_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3603–3611. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3603-L3611).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] != '\n') == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3617–3625. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3617-L3625).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] != '\n') == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3631–3639. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3631-L3639).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] != '\n') == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3642–3644. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3642-L3644).

```c

    return text_pos;
}
```


<a id="case-018"></a>

## 18. `match_many_ANY_U`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3647–3722. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3647-L3722).

### Read sites

- Site 1: lines 3665–3665; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3669–3669; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3686–3686; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 3690–3690; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 3707–3707; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 3711–3711; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3651–3660, 3674–3681, 3695–3702, 3716–3719. The original contextual region was lines 3647–3722.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3647–3650. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3647-L3650).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_ANY_U(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3661–3673. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3661-L3673).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_is_line_sep(text_ptr[0]) !=
              match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && ascii_is_line_sep(text_ptr[0]) !=
              match)
                ++text_ptr;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3682–3694. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3682-L3694).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_is_line_sep(text_ptr[0]) !=
              match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && ascii_is_line_sep(text_ptr[0]) !=
              match)
                ++text_ptr;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3703–3715. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3703-L3715).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_is_line_sep(text_ptr[0]) !=
              match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && ascii_is_line_sep(text_ptr[0]) !=
              match)
                ++text_ptr;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3720–3722. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3720-L3722).

```c

    return text_pos;
}
```


<a id="case-019"></a>

## 19. `match_many_ANY_U_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3725–3800. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3725-L3800).

### Read sites

- Site 1: lines 3743–3743; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3747–3747; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3764–3764; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 3768–3768; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 3785–3785; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 3789–3789; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3729–3738, 3752–3759, 3773–3780, 3794–3797. The original contextual region was lines 3725–3800.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3725–3728. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3725-L3728).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_ANY_U_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3739–3751. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3739-L3751).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_is_line_sep(text_ptr[-1]) !=
              match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && ascii_is_line_sep(text_ptr[-1]) !=
              match)
                --text_ptr;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3760–3772. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3760-L3772).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_is_line_sep(text_ptr[-1]) !=
              match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && ascii_is_line_sep(text_ptr[-1]) !=
              match)
                --text_ptr;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3781–3793. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3781-L3793).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_is_line_sep(text_ptr[-1]) !=
              match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && ascii_is_line_sep(text_ptr[-1]) !=
              match)
                --text_ptr;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3798–3800. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3798-L3800).

```c

    return text_pos;
}
```


<a id="case-020"></a>

## 20. `match_many_CHARACTER`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3803–3858. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3803-L3858).

### Read sites

- Site 1: lines 3821–3821; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3835–3835; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3849–3849; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3807–3816, 3826–3830, 3840–3844, 3854–3855. The original contextual region was lines 3803–3858.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3803–3806. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3803-L3806).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_CHARACTER(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    Py_UCS4 ch;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3817–3825. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3817-L3825).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] == ch) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3831–3839. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3831-L3839).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] == ch) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3845–3853. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3845-L3853).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] == ch) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3856–3858. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3856-L3858).

```c

    return text_pos;
}
```


<a id="case-021"></a>

## 21. `match_many_CHARACTER_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3861–3921. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3861-L3921).

### Read sites

- Site 1: lines 3881–3881; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3896–3896; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3911–3911; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3865–3876, 3886–3891, 3901–3906, 3916–3918. The original contextual region was lines 3861–3921.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3861–3864. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3861-L3864).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_CHARACTER_IGN(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    Py_UCS4 cases[RE_MAX_CASES];
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3877–3885. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3877-L3885).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && any_case(text_ptr[0], case_count, cases)
          == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3892–3900. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3892-L3900).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && any_case(text_ptr[0], case_count, cases)
          == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3907–3915. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3907-L3915).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && any_case(text_ptr[0], case_count, cases)
          == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3919–3921. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3919-L3921).

```c

    return text_pos;
}
```


<a id="case-022"></a>

## 22. `match_many_CHARACTER_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3924–3984. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3924-L3984).

### Read sites

- Site 1: lines 3944–3944; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 3959–3959; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 3974–3974; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3928–3939, 3949–3954, 3964–3969, 3979–3981. The original contextual region was lines 3924–3984.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3924–3927. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3924-L3927).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_CHARACTER_IGN_REV(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    Py_UCS4 cases[RE_MAX_CASES];
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3940–3948. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3940-L3948).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && any_case(text_ptr[-1], case_count,
          cases) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3955–3963. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3955-L3963).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && any_case(text_ptr[-1], case_count,
          cases) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3970–3978. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3970-L3978).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && any_case(text_ptr[-1], case_count,
          cases) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 3982–3984. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3982-L3984).

```c

    return text_pos;
}
```


<a id="case-023"></a>

## 23. `match_many_CHARACTER_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 3987–4042. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3987-L4042).

### Read sites

- Site 1: lines 4005–4005; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4019–4019; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4033–4033; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 3991–4000, 4010–4014, 4024–4028, 4038–4039. The original contextual region was lines 3987–4042.

Archive member `regex-2026.9.29/src/_regex.c`, lines 3987–3990. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3987-L3990).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_CHARACTER_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    Py_UCS4 ch;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4001–4009. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4001-L4009).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] == ch) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4015–4023. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4015-L4023).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] == ch) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4029–4037. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4029-L4037).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] == ch) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4040–4042. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4040-L4042).

```c

    return text_pos;
}
```


<a id="case-024"></a>

## 24. `match_many_PROPERTY`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4045–4152. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4045-L4152).

### Read sites

- Site 1: lines 4081–4081; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4085–4085; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4090–4090; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 4107–4107; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 4111–4111; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 4116–4116; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 7: lines 4133–4133; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 8: lines 4137–4137; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 9: lines 4142–4142; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4049–4076, 4095–4102, 4121–4128, 4147–4149. The original contextual region was lines 4045–4152.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4045–4048. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4045-L4048).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_PROPERTY(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4077–4094. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4077-L4094).

```c
        limit_ptr = (Py_UCS1*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_has_property(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr < limit_ptr && ascii_has_property(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && locale_has_property(locale_info,
              property,
                text_ptr[0]) == match)
                ++text_ptr;
        }

        text_pos = text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4103–4120. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4103-L4120).

```c
        limit_ptr = (Py_UCS2*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_has_property(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr < limit_ptr && ascii_has_property(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && locale_has_property(locale_info,
              property,
                text_ptr[0]) == match)
                ++text_ptr;
        }

        text_pos = text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4129–4146. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4129-L4146).

```c
        limit_ptr = (Py_UCS4*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_has_property(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr < limit_ptr && ascii_has_property(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && locale_has_property(locale_info,
              property,
                text_ptr[0]) == match)
                ++text_ptr;
        }

        text_pos = text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4150–4152. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4150-L4152).

```c

    return text_pos;
}
```


<a id="case-025"></a>

## 25. `match_many_PROPERTY_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4155–4262. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4155-L4262).

### Read sites

- Site 1: lines 4191–4191; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4195–4195; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4200–4200; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 4217–4217; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 4221–4221; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 4226–4226; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 7: lines 4243–4243; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 8: lines 4247–4247; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 9: lines 4252–4252; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4159–4186, 4205–4212, 4231–4238, 4257–4259. The original contextual region was lines 4155–4262.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4155–4158. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4155-L4158).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_PROPERTY_IGN(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4187–4204. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4187-L4204).

```c
        limit_ptr = (Py_UCS1*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_has_property_ign(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr < limit_ptr && ascii_has_property_ign(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && locale_has_property_ign(locale_info,
              property,
                text_ptr[0]) == match)
                ++text_ptr;
        }

        text_pos = text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4213–4230. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4213-L4230).

```c
        limit_ptr = (Py_UCS2*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_has_property_ign(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr < limit_ptr && ascii_has_property_ign(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && locale_has_property_ign(locale_info,
              property,
                text_ptr[0]) == match)
                ++text_ptr;
        }

        text_pos = text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4239–4256. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4239-L4256).

```c
        limit_ptr = (Py_UCS4*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr < limit_ptr && unicode_has_property_ign(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr < limit_ptr && ascii_has_property_ign(property,
              text_ptr[0]) == match)
                ++text_ptr;
        } else {
            while (text_ptr < limit_ptr && locale_has_property_ign(locale_info,
              property,
                text_ptr[0]) == match)
                ++text_ptr;
        }

        text_pos = text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4260–4262. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4260-L4262).

```c

    return text_pos;
}
```


<a id="case-026"></a>

## 26. `match_many_PROPERTY_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4265–4372. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4265-L4372).

### Read sites

- Site 1: lines 4301–4301; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4305–4305; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4310–4310; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 4327–4327; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 4331–4331; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 4336–4336; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 7: lines 4353–4353; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 8: lines 4357–4357; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 9: lines 4362–4362; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4269–4296, 4315–4322, 4341–4348, 4367–4369. The original contextual region was lines 4265–4372.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4265–4268. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4265-L4268).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_PROPERTY_IGN_REV(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4297–4314. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4297-L4314).

```c
        limit_ptr = (Py_UCS1*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_has_property_ign(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr > limit_ptr && ascii_has_property_ign(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && locale_has_property_ign(locale_info,
              property,
                text_ptr[-1]) == match)
                --text_ptr;
        }

        text_pos = text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4323–4340. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4323-L4340).

```c
        limit_ptr = (Py_UCS2*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_has_property_ign(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr > limit_ptr && ascii_has_property_ign(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && locale_has_property_ign(locale_info,
              property,
                text_ptr[-1]) == match)
                --text_ptr;
        }

        text_pos = text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4349–4366. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4349-L4366).

```c
        limit_ptr = (Py_UCS4*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_has_property_ign(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr > limit_ptr && ascii_has_property_ign(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && locale_has_property_ign(locale_info,
              property,
                text_ptr[-1]) == match)
                --text_ptr;
        }

        text_pos = text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4370–4372. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4370-L4372).

```c

    return text_pos;
}
```


<a id="case-027"></a>

## 27. `match_many_PROPERTY_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4375–4482. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4375-L4482).

### Read sites

- Site 1: lines 4411–4411; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4415–4415; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4420–4420; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 4437–4437; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 4441–4441; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 4446–4446; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 7: lines 4463–4463; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 8: lines 4467–4467; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 9: lines 4472–4472; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4379–4406, 4425–4432, 4451–4458, 4477–4479. The original contextual region was lines 4375–4482.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4375–4378. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4375-L4378).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_PROPERTY_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4407–4424. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4407-L4424).

```c
        limit_ptr = (Py_UCS1*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_has_property(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr > limit_ptr && ascii_has_property(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && locale_has_property(locale_info,
              property,
                text_ptr[-1]) == match)
                --text_ptr;
        }

        text_pos = text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4433–4450. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4433-L4450).

```c
        limit_ptr = (Py_UCS2*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_has_property(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr > limit_ptr && ascii_has_property(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && locale_has_property(locale_info,
              property,
                text_ptr[-1]) == match)
                --text_ptr;
        }

        text_pos = text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4459–4476. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4459-L4476).

```c
        limit_ptr = (Py_UCS4*)text + limit;

        if (encoding == &unicode_encoding) {
            while (text_ptr > limit_ptr && unicode_has_property(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else if (encoding == &ascii_encoding) {
            while (text_ptr > limit_ptr && ascii_has_property(property,
              text_ptr[-1]) == match)
                --text_ptr;
        } else {
            while (text_ptr > limit_ptr && locale_has_property(locale_info,
              property,
                text_ptr[-1]) == match)
                --text_ptr;
        }

        text_pos = text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4480–4482. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4480-L4482).

```c

    return text_pos;
}
```


<a id="case-028"></a>

## 28. `match_many_RANGE`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4485–4545. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4485-L4545).

### Read sites

- Site 1: lines 4506–4506; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4521–4521; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4536–4536; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4489–4501, 4511–4516, 4526–4531, 4541–4542. The original contextual region was lines 4485–4545.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4485–4488. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4485-L4488).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_RANGE(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4502–4510. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4502-L4510).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && matches_RANGE(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4517–4525. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4517-L4525).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && matches_RANGE(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4532–4540. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4532-L4540).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && matches_RANGE(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4543–4545. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4543-L4545).

```c

    return text_pos;
}
```


<a id="case-029"></a>

## 29. `match_many_RANGE_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4548–4608. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4548-L4608).

### Read sites

- Site 1: lines 4569–4569; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4584–4584; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4599–4599; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4552–4564, 4574–4579, 4589–4594, 4604–4605. The original contextual region was lines 4548–4608.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4548–4551. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4548-L4551).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_RANGE_IGN(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4565–4573. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4565-L4573).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && matches_RANGE_IGN(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4580–4588. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4580-L4588).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && matches_RANGE_IGN(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4595–4603. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4595-L4603).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && matches_RANGE_IGN(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4606–4608. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4606-L4608).

```c

    return text_pos;
}
```


<a id="case-030"></a>

## 30. `match_many_RANGE_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4611–4671. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4611-L4671).

### Read sites

- Site 1: lines 4632–4632; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4647–4647; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4662–4662; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4615–4627, 4637–4642, 4652–4657, 4667–4668. The original contextual region was lines 4611–4671.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4611–4614. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4611-L4614).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_RANGE_IGN_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4628–4636. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4628-L4636).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && matches_RANGE_IGN(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4643–4651. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4643-L4651).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && matches_RANGE_IGN(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4658–4666. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4658-L4666).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && matches_RANGE_IGN(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4669–4671. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4669-L4671).

```c

    return text_pos;
}
```


<a id="case-031"></a>

## 31. `match_many_RANGE_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4674–4734. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4674-L4734).

### Read sites

- Site 1: lines 4695–4695; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4710–4710; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4725–4725; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4678–4690, 4700–4705, 4715–4720, 4730–4731. The original contextual region was lines 4674–4734.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4674–4677. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4674-L4677).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_RANGE_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4691–4699. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4691-L4699).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && matches_RANGE(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4706–4714. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4706-L4714).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && matches_RANGE(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4721–4729. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4721-L4729).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && matches_RANGE(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4732–4734. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4732-L4734).

```c

    return text_pos;
}
```


<a id="case-032"></a>

## 32. `match_many_SET`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4737–4797. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4737-L4797).

### Read sites

- Site 1: lines 4758–4758; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4773–4773; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4788–4788; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4741–4753, 4763–4768, 4778–4783, 4793–4794. The original contextual region was lines 4737–4797.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4737–4740. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4737-L4740).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_SET(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4754–4762. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4754-L4762).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && matches_SET(encoding, locale_info, node,
          text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4769–4777. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4769-L4777).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && matches_SET(encoding, locale_info, node,
          text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4784–4792. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4784-L4792).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && matches_SET(encoding, locale_info, node,
          text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4795–4797. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4795-L4797).

```c

    return text_pos;
}
```


<a id="case-033"></a>

## 33. `match_many_SET_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4800–4860. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4800-L4860).

### Read sites

- Site 1: lines 4821–4821; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4836–4836; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4851–4851; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4804–4816, 4826–4831, 4841–4846, 4856–4857. The original contextual region was lines 4800–4860.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4800–4803. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4800-L4803).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_SET_IGN(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4817–4825. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4817-L4825).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && matches_SET_IGN(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4832–4840. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4832-L4840).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && matches_SET_IGN(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4847–4855. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4847-L4855).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && matches_SET_IGN(encoding, locale_info,
          node, text_ptr[0]) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4858–4860. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4858-L4860).

```c

    return text_pos;
}
```


<a id="case-034"></a>

## 34. `match_many_SET_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4863–4923. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4863-L4923).

### Read sites

- Site 1: lines 4884–4884; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4899–4899; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4914–4914; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4867–4879, 4889–4894, 4904–4909, 4919–4920. The original contextual region was lines 4863–4923.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4863–4866. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4863-L4866).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_SET_IGN_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4880–4888. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4880-L4888).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && matches_SET_IGN(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4895–4903. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4895-L4903).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && matches_SET_IGN(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4910–4918. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4910-L4918).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && matches_SET_IGN(encoding, locale_info,
          node, text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4921–4923. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4921-L4923).

```c

    return text_pos;
}
```


<a id="case-035"></a>

## 35. `match_many_SET_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 4926–4986. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4926-L4986).

### Read sites

- Site 1: lines 4947–4947; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 4962–4962; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 4977–4977; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 4930–4942, 4952–4957, 4967–4972, 4982–4983. The original contextual region was lines 4926–4986.

Archive member `regex-2026.9.29/src/_regex.c`, lines 4926–4929. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4926-L4929).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_SET_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4943–4951. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4943-L4951).

```c
        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && matches_SET(encoding, locale_info, node,
          text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4958–4966. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4958-L4966).

```c
        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && matches_SET(encoding, locale_info, node,
          text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4973–4981. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4973-L4981).

```c
        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && matches_SET(encoding, locale_info, node,
          text_ptr[-1]) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 4984–4986. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4984-L4986).

```c

    return text_pos;
}
```


<a id="case-036"></a>

## 36. `simple_string_search`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Search outer loop advances text_ptr from caller text_pos; each candidate checks text_ptr[0], then text_ptr[s_pos] with s_pos reset to 1. Failed candidates restart comparison at the next position; overlapping input is reread.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 5231–5377. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5231-L5377).

### Read sites

- Site 1: lines 5251–5251; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 5273–5273; typed codepoint pointer read; index expression `s_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 5292–5292; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 5314–5314; typed codepoint pointer read; index expression `s_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 5333–5333; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 5355–5355; typed codepoint pointer read; index expression `s_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 5235–5246, 5256–5268, 5278–5287, 5297–5309, 5319–5328, 5338–5350, 5360–5374. The original contextual region was lines 5231–5377.

Archive member `regex-2026.9.29/src/_regex.c`, lines 5231–5234. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5231-L5234).

```c
Py_LOCAL_INLINE(Py_ssize_t) simple_string_search(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool* is_partial) {
    Py_ssize_t length;
    RE_CODE* values;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5247–5255. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5247-L5255).

```c
        Py_UCS1* text_ptr = text + text_pos;
        Py_UCS1* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (text_ptr[0] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5269–5277. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5269-L5277).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[s_pos], values[s_pos]))
                        break;

                    ++s_pos;
                }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5288–5296. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5288-L5296).

```c
        Py_UCS2* text_ptr = text + text_pos;
        Py_UCS2* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (text_ptr[0] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5310–5318. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5310-L5318).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[s_pos], values[s_pos]))
                        break;

                    ++s_pos;
                }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5329–5337. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5329-L5337).

```c
        Py_UCS4* text_ptr = text + text_pos;
        Py_UCS4* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (text_ptr[0] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5351–5359. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5351-L5359).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[s_pos], values[s_pos]))
                        break;

                    ++s_pos;
                }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5375–5377. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5375-L5377).

```c

    return -1;
}
```


<a id="case-037"></a>

## 37. `simple_string_search_ign`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Search outer loop advances text_ptr from caller text_pos; each candidate checks text_ptr[0], then text_ptr[s_pos] with s_pos reset to 1. Failed candidates restart comparison at the next position; overlapping input is reread.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 5380–5534. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5380-L5534).

### Read sites

- Site 1: lines 5405–5405; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 5427–5427; typed codepoint pointer read; index expression `s_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 5447–5447; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 5469–5469; typed codepoint pointer read; index expression `s_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 5489–5489; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 5511–5511; typed codepoint pointer read; index expression `s_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 5384–5400, 5410–5422, 5432–5442, 5452–5464, 5474–5484, 5494–5506, 5516–5531. The original contextual region was lines 5380–5534.

Archive member `regex-2026.9.29/src/_regex.c`, lines 5380–5383. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5380-L5383).

```c
Py_LOCAL_INLINE(Py_ssize_t) simple_string_search_ign(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool* is_partial) {
    Py_ssize_t length;
    RE_CODE* values;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5401–5409. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5401-L5409).

```c
        Py_UCS1* text_ptr = text + text_pos;
        Py_UCS1* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (any_case(text_ptr[0], case_count, cases)) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5423–5431. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5423-L5431).

```c
                        return -1;

                    }

                    if (!same_char_ign(encoding, locale_info, text_ptr[s_pos],
                      values[s_pos]))
                        break;

                    ++s_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5443–5451. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5443-L5451).

```c
        Py_UCS2* text_ptr = text + text_pos;
        Py_UCS2* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (any_case(text_ptr[0], case_count, cases)) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5465–5473. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5465-L5473).

```c
                        return -1;

                    }

                    if (!same_char_ign(encoding, locale_info, text_ptr[s_pos],
                      values[s_pos]))
                        break;

                    ++s_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5485–5493. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5485-L5493).

```c
        Py_UCS4* text_ptr = text + text_pos;
        Py_UCS4* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (any_case(text_ptr[0], case_count, cases)) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5507–5515. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5507-L5515).

```c
                        return -1;

                    }

                    if (!same_char_ign(encoding, locale_info, text_ptr[s_pos],
                      values[s_pos]))
                        break;

                    ++s_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5532–5534. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5532-L5534).

```c

    return -1;
}
```


<a id="case-038"></a>

## 38. `simple_string_search_ign_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Reverse search outer loop decrements text_ptr from caller text_pos; each candidate checks text_ptr[-1] then text_ptr[-s_pos-1]. Failed candidates restart a reverse comparison, rereading overlapping input.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 5537–5691. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5537-L5691).

### Read sites

- Site 1: lines 5562–5562; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 5584–5585; typed codepoint pointer read; index expression `- s_pos - 1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 5604–5604; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 5626–5627; typed codepoint pointer read; index expression `- s_pos - 1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 5646–5646; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 5668–5669; typed codepoint pointer read; index expression `- s_pos - 1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 5541–5557, 5567–5579, 5590–5599, 5609–5621, 5632–5641, 5651–5663, 5674–5688. The original contextual region was lines 5537–5691.

Archive member `regex-2026.9.29/src/_regex.c`, lines 5537–5540. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5537-L5540).

```c
Py_LOCAL_INLINE(Py_ssize_t) simple_string_search_ign_rev(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, Py_ssize_t limit, bool* is_partial) {
    Py_ssize_t length;
    RE_CODE* values;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5558–5566. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5558-L5566).

```c
        Py_UCS1* text_ptr = text + text_pos;
        Py_UCS1* limit_ptr = text + limit;

        while (text_ptr > limit_ptr) {
            if (any_case(text_ptr[-1], case_count, cases)) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5580–5589. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5580-L5589).

```c
                        return -1;

                    }

                    if (!same_char_ign(encoding, locale_info, text_ptr[- s_pos
                      - 1], values[length - s_pos - 1]))
                        break;

                    ++s_pos;
                }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5600–5608. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5600-L5608).

```c
        Py_UCS2* text_ptr = text + text_pos;
        Py_UCS2* limit_ptr = text + limit;

        while (text_ptr > limit_ptr) {
            if (any_case(text_ptr[-1], case_count, cases)) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5622–5631. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5622-L5631).

```c
                        return -1;

                    }

                    if (!same_char_ign(encoding, locale_info, text_ptr[- s_pos
                      - 1], values[length - s_pos - 1]))
                        break;

                    ++s_pos;
                }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5642–5650. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5642-L5650).

```c
        Py_UCS4* text_ptr = text + text_pos;
        Py_UCS4* limit_ptr = text + limit;

        while (text_ptr > limit_ptr) {
            if (any_case(text_ptr[-1], case_count, cases)) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5664–5673. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5664-L5673).

```c
                        return -1;

                    }

                    if (!same_char_ign(encoding, locale_info, text_ptr[- s_pos
                      - 1], values[length - s_pos - 1]))
                        break;

                    ++s_pos;
                }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5689–5691. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5689-L5691).

```c

    return -1;
}
```


<a id="case-039"></a>

## 39. `simple_string_search_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Reverse search outer loop decrements text_ptr from caller text_pos; each candidate checks text_ptr[-1] then text_ptr[-s_pos-1]. Failed candidates restart a reverse comparison, rereading overlapping input.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 5694–5843. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5694-L5843).

### Read sites

- Site 1: lines 5714–5714; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 5736–5736; typed codepoint pointer read; index expression `- s_pos - 1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 5756–5756; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 5778–5778; typed codepoint pointer read; index expression `- s_pos - 1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 5798–5798; typed codepoint pointer read; index expression `-1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 5820–5820; typed codepoint pointer read; index expression `- s_pos - 1`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 5698–5709, 5719–5731, 5741–5751, 5761–5773, 5783–5793, 5803–5815, 5825–5840. The original contextual region was lines 5694–5843.

Archive member `regex-2026.9.29/src/_regex.c`, lines 5694–5697. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5694-L5697).

```c
Py_LOCAL_INLINE(Py_ssize_t) simple_string_search_rev(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool* is_partial) {
    Py_ssize_t length;
    RE_CODE* values;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5710–5718. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5710-L5718).

```c
        Py_UCS1* text_ptr = text + text_pos;
        Py_UCS1* limit_ptr = text + limit;

        while (text_ptr > limit_ptr) {
            if (text_ptr[-1] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5732–5740. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5732-L5740).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[- s_pos - 1], values[length - s_pos
                      - 1]))
                        break;

                    ++s_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5752–5760. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5752-L5760).

```c
        Py_UCS2* text_ptr = text + text_pos;
        Py_UCS2* limit_ptr = text + limit;

        while (text_ptr > limit_ptr) {
            if (text_ptr[-1] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5774–5782. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5774-L5782).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[- s_pos - 1], values[length - s_pos
                      - 1]))
                        break;

                    ++s_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5794–5802. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5794-L5802).

```c
        Py_UCS4* text_ptr = text + text_pos;
        Py_UCS4* limit_ptr = text + limit;

        while (text_ptr > limit_ptr) {
            if (text_ptr[-1] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5816–5824. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5816-L5824).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[- s_pos - 1], values[length - s_pos
                      - 1]))
                        break;

                    ++s_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5841–5843. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5841-L5843).

```c

    return -1;
}
```


<a id="case-040"></a>

## 40. `fast_string_search`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Boyer-Moore reads text_ptr[last_pos], then scans text_ptr[pos] backward through a candidate. good_suffix_offset[pos] or bad_character_offset[ch & 0xFF] controls a non-unit jump to the next candidate; arbitrary codepoint offset view is needed for existing behavior.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 5846–5953. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5846-L5953).

### Read sites

- Site 1: lines 5877–5877; typed codepoint pointer read; index expression `last_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 5882–5882; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 5905–5905; typed codepoint pointer read; index expression `last_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 5910–5910; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 5933–5933; typed codepoint pointer read; index expression `last_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 5938–5938; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 5850–5872, 5887–5900, 5915–5928, 5943–5950. The original contextual region was lines 5846–5953.

Archive member `regex-2026.9.29/src/_regex.c`, lines 5846–5849. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5846-L5849).

```c
Py_LOCAL_INLINE(Py_ssize_t) fast_string_search(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit) {
    void* text;
    Py_ssize_t length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5873–5886. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5873-L5886).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char(text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5901–5914. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5901-L5914).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char(text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5929–5942. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5929-L5942).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char(text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5951–5953. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5951-L5953).

```c

    return -1;
}
```


<a id="case-041"></a>

## 41. `fast_string_search_ign`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Boyer-Moore reads text_ptr[last_pos], then scans text_ptr[pos] backward through a candidate. good_suffix_offset[pos] or bad_character_offset[ch & 0xFF] controls a non-unit jump to the next candidate; arbitrary codepoint offset view is needed for existing behavior.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 5956–6071. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5956-L6071).

### Read sites

- Site 1: lines 5992–5992; typed codepoint pointer read; index expression `last_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 5998–5998; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 6021–6021; typed codepoint pointer read; index expression `last_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 6027–6027; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 6050–6050; typed codepoint pointer read; index expression `last_pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 6056–6056; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 5960–5987, 6003–6016, 6032–6045, 6061–6068. The original contextual region was lines 5956–6071.

Archive member `regex-2026.9.29/src/_regex.c`, lines 5956–5959. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5956-L5959).

```c
Py_LOCAL_INLINE(Py_ssize_t) fast_string_search_ign(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit) {
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 5988–6002. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5988-L6002).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (any_case(ch, case_count, cases)) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char_ign(encoding, locale_info,
                  text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS1*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6017–6031. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6017-L6031).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (any_case(ch, case_count, cases)) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char_ign(encoding, locale_info,
                  text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS2*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6046–6060. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6046-L6060).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (any_case(ch, case_count, cases)) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char_ign(encoding, locale_info,
                  text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS4*)text;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6069–6071. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6069-L6071).

```c

    return -1;
}
```


<a id="case-042"></a>

## 42. `fast_string_search_ign_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Reverse Boyer-Moore subtracts pattern length from caller text_pos, reads text_ptr[0] then scans text_ptr[pos] forward within a candidate. Shift tables move to earlier candidates, with overlapping rereads and non-unit jumps.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6074–6187. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6074-L6187).

### Read sites

- Site 1: lines 6108–6108; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 6114–6114; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 6137–6137; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 6143–6143; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 6166–6166; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 6172–6172; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 6078–6103, 6119–6132, 6148–6161, 6177–6184. The original contextual region was lines 6074–6187.

Archive member `regex-2026.9.29/src/_regex.c`, lines 6074–6077. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6074-L6077).

```c
Py_LOCAL_INLINE(Py_ssize_t) fast_string_search_ign_rev(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, Py_ssize_t limit) {
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6104–6118. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6104-L6118).

```c

        while (text_ptr >= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[0];
            if (any_case(ch, case_count, cases)) {
                Py_ssize_t pos;

                pos = 1;
                while (pos < length && same_char_ign(encoding, locale_info,
                  text_ptr[pos], values[pos]))
                    ++pos;

                if (pos >= length)
                    return text_ptr - (Py_UCS1*)text + length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6133–6147. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6133-L6147).

```c

        while (text_ptr >= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[0];
            if (any_case(ch, case_count, cases)) {
                Py_ssize_t pos;

                pos = 1;
                while (pos < length && same_char_ign(encoding, locale_info,
                  text_ptr[pos], values[pos]))
                    ++pos;

                if (pos >= length)
                    return text_ptr - (Py_UCS2*)text + length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6162–6176. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6162-L6176).

```c

        while (text_ptr >= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[0];
            if (any_case(ch, case_count, cases)) {
                Py_ssize_t pos;

                pos = 1;
                while (pos < length && same_char_ign(encoding, locale_info,
                  text_ptr[pos], values[pos]))
                    ++pos;

                if (pos >= length)
                    return text_ptr - (Py_UCS4*)text + length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6185–6187. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6185-L6187).

```c

    return -1;
}
```


<a id="case-043"></a>

## 43. `fast_string_search_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Reverse Boyer-Moore subtracts pattern length from caller text_pos, reads text_ptr[0] then scans text_ptr[pos] forward within a candidate. Shift tables move to earlier candidates, with overlapping rereads and non-unit jumps.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6190–6295. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6190-L6295).

### Read sites

- Site 1: lines 6219–6219; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 2: lines 6224–6224; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 3: lines 6247–6247; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 4: lines 6252–6252; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 5: lines 6275–6275; typed codepoint pointer read; index expression `0`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.
- Site 6: lines 6280–6280; typed codepoint pointer read; index expression `pos`. text_ptr aliases state->text plus caller-selected text_pos; Py_UCS1/2/4 branches are codepoint-width alternatives.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 6194–6214, 6229–6242, 6257–6270, 6285–6292. The original contextual region was lines 6190–6295.

Archive member `regex-2026.9.29/src/_regex.c`, lines 6190–6193. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6190-L6193).

```c
Py_LOCAL_INLINE(Py_ssize_t) fast_string_search_rev(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit) {
    void* text;
    Py_ssize_t length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6215–6228. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6215-L6228).

```c

        while (text_ptr >= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[0];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = 1;
                while (pos < length && same_char(text_ptr[pos], values[pos]))
                    ++pos;

                if (pos >= length)
                    return text_ptr - (Py_UCS1*)text + length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6243–6256. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6243-L6256).

```c

        while (text_ptr >= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[0];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = 1;
                while (pos < length && same_char(text_ptr[pos], values[pos]))
                    ++pos;

                if (pos >= length)
                    return text_ptr - (Py_UCS2*)text + length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6271–6284. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6271-L6284).

```c

        while (text_ptr >= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[0];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = 1;
                while (pos < length && same_char(text_ptr[pos], values[pos]))
                    ++pos;

                if (pos >= length)
                    return text_ptr - (Py_UCS4*)text + length;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6293–6295. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6293-L6295).

```c

    return -1;
}
```


<a id="case-044"></a>

## 44. `string_search_fld`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Full-casefold search reads at text_pos, advances after consuming a folded character, but on mismatch increments start_pos and resets text_pos=start_pos, f_pos=0 and s_pos=0; input may be reread.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6637–6708. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6637-L6708).

### Read sites

- Site 1: lines 6682–6682; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 6641–6677, 6687–6705. The original contextual region was lines 6637–6708.

Archive member `regex-2026.9.29/src/_regex.c`, lines 6637–6640. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6637-L6640).

```c
Py_LOCAL_INLINE(Py_ssize_t) string_search_fld(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, Py_ssize_t* new_pos, bool* is_partial)
  {
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6678–6686. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6678-L6686).

```c

                return -1;
            }

            folded_len = full_case_fold(locale_info, char_at(text, text_pos),
              folded);
            f_pos = 0;
        }

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6706–6708. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6706-L6708).

```c

    return start_pos;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-045"></a>

## 45. `string_search_fld_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Reverse full-casefold search reads text_pos-1 and decrements it after consuming a fold; mismatch decrements start_pos and resets text_pos=start_pos, f_pos=0 and s_pos=0, revisiting input.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6711–6781. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6711-L6781).

### Read sites

- Site 1: lines 6755–6756; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 6715–6750, 6761–6778. The original contextual region was lines 6711–6781.

Archive member `regex-2026.9.29/src/_regex.c`, lines 6711–6714. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6711-L6714).

```c
Py_LOCAL_INLINE(Py_ssize_t) string_search_fld_rev(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, Py_ssize_t* new_pos, bool*
  is_partial) {
    RE_EncodingTable* encoding;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6751–6760. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6751-L6760).

```c

                return -1;
            }

            folded_len = full_case_fold(locale_info, char_at(text, text_pos -
              1), folded);
            f_pos = 0;
        }

        if (s_pos < length && same_char_ign_turkic(encoding, locale_info,
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 6779–6781. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6779-L6781).

```c

    return start_pos;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-046"></a>

## 46. `try_match_ANY`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6919–6931. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6919-L6931).

### Read sites

- Site 1: lines 6929–6930; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 6919–6931. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6919-L6931).

```c
Py_LOCAL_INLINE(int) try_match_ANY(RE_State* state, RE_Node* node, Py_ssize_t
  text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_ANY(state->encoding, node, state->char_at(state->text,
      text_pos)));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-047"></a>

## 47. `try_match_ANY_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6962–6974. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6962-L6974).

### Read sites

- Site 1: lines 6972–6973; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 6962–6974. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6962-L6974).

```c
Py_LOCAL_INLINE(int) try_match_ANY_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_ANY(state->encoding, node, state->char_at(state->text, text_pos -
      1)));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-048"></a>

## 48. `try_match_ANY_U`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6978–6990. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6978-L6990).

### Read sites

- Site 1: lines 6988–6989; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 6978–6990. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6978-L6990).

```c
Py_LOCAL_INLINE(int) try_match_ANY_U(RE_State* state, RE_Node* node, Py_ssize_t
  text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_ANY_U(state->encoding, node, state->char_at(state->text,
      text_pos)));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-049"></a>

## 49. `try_match_ANY_U_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 6995–7007. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6995-L7007).

### Read sites

- Site 1: lines 7005–7006; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 6995–7007. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6995-L7007).

```c
Py_LOCAL_INLINE(int) try_match_ANY_U_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_ANY_U(state->encoding, node, state->char_at(state->text, text_pos
      - 1)));
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-050"></a>

## 50. `try_match_CHARACTER`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7026–7038. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7026-L7038).

### Read sites

- Site 1: lines 7037–7037; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7026–7038. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7026-L7038).

```c
Py_LOCAL_INLINE(int) try_match_CHARACTER(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_CHARACTER(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-051"></a>

## 51. `try_match_CHARACTER_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7041–7053. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7041-L7053).

### Read sites

- Site 1: lines 7052–7052; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7041–7053. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7041-L7053).

```c
Py_LOCAL_INLINE(int) try_match_CHARACTER_IGN(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_CHARACTER_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-052"></a>

## 52. `try_match_CHARACTER_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7057–7069. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7057-L7069).

### Read sites

- Site 1: lines 7068–7068; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7057–7069. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7057-L7069).

```c
Py_LOCAL_INLINE(int) try_match_CHARACTER_IGN_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_CHARACTER_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-053"></a>

## 53. `try_match_CHARACTER_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7072–7084. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7072-L7084).

### Read sites

- Site 1: lines 7083–7083; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7072–7084. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7072-L7084).

```c
Py_LOCAL_INLINE(int) try_match_CHARACTER_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_CHARACTER(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-054"></a>

## 54. `try_match_END_OF_LINE`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Line-boundary probe reads text_pos (end-of-line) or text_pos-1 (start-of-line); caller may select any position.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7108–7112. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7108-L7112).

### Read sites

- Site 1: lines 7111–7111; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7108–7112. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7108-L7112).

```c
Py_LOCAL_INLINE(int) try_match_END_OF_LINE(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    return bool_as_status(text_pos >= state->slice_end ||
      state->char_at(state->text, text_pos) == '\n');
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-055"></a>

## 55. `try_match_PROPERTY`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7154–7166. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7154-L7166).

### Read sites

- Site 1: lines 7165–7165; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7154–7166. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7154-L7166).

```c
Py_LOCAL_INLINE(int) try_match_PROPERTY(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_PROPERTY(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-056"></a>

## 56. `try_match_PROPERTY_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7171–7183. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7171-L7183).

### Read sites

- Site 1: lines 7182–7182; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7171–7183. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7171-L7183).

```c
Py_LOCAL_INLINE(int) try_match_PROPERTY_IGN(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_PROPERTY_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-057"></a>

## 57. `try_match_PROPERTY_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7188–7200. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7188-L7200).

### Read sites

- Site 1: lines 7199–7199; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7188–7200. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7188-L7200).

```c
Py_LOCAL_INLINE(int) try_match_PROPERTY_IGN_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_PROPERTY_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-058"></a>

## 58. `try_match_PROPERTY_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7205–7217. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7205-L7217).

### Read sites

- Site 1: lines 7216–7216; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7205–7217. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7205-L7217).

```c
Py_LOCAL_INLINE(int) try_match_PROPERTY_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_PROPERTY(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-059"></a>

## 59. `try_match_RANGE`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7220–7232. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7220-L7232).

### Read sites

- Site 1: lines 7231–7231; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7220–7232. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7220-L7232).

```c
Py_LOCAL_INLINE(int) try_match_RANGE(RE_State* state, RE_Node* node, Py_ssize_t
  text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_RANGE(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-060"></a>

## 60. `try_match_RANGE_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7237–7249. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7237-L7249).

### Read sites

- Site 1: lines 7248–7248; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7237–7249. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7237-L7249).

```c
Py_LOCAL_INLINE(int) try_match_RANGE_IGN(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_RANGE_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-061"></a>

## 61. `try_match_RANGE_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7254–7266. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7254-L7266).

### Read sites

- Site 1: lines 7265–7265; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7254–7266. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7254-L7266).

```c
Py_LOCAL_INLINE(int) try_match_RANGE_IGN_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_RANGE_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-062"></a>

## 62. `try_match_RANGE_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7271–7283. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7271-L7283).

### Read sites

- Site 1: lines 7282–7282; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7271–7283. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7271-L7283).

```c
Py_LOCAL_INLINE(int) try_match_RANGE_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_RANGE(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-063"></a>

## 63. `try_match_SET`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7292–7304. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7292-L7304).

### Read sites

- Site 1: lines 7303–7303; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7292–7304. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7292-L7304).

```c
Py_LOCAL_INLINE(int) try_match_SET(RE_State* state, RE_Node* node, Py_ssize_t
  text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_SET(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-064"></a>

## 64. `try_match_SET_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos after a slice bound check. A one-index probe is not a complete forward iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7309–7321. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7309-L7321).

### Read sites

- Site 1: lines 7320–7320; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7309–7321. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7309-L7321).

```c
Py_LOCAL_INLINE(int) try_match_SET_IGN(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos >= state->text_end) {
        if (state->partial_side == RE_PARTIAL_RIGHT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos < state->slice_end &&
      matches_SET_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-065"></a>

## 65. `try_match_SET_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7326–7338. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7326-L7338).

### Read sites

- Site 1: lines 7337–7337; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7326–7338. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7326-L7338).

```c
Py_LOCAL_INLINE(int) try_match_SET_IGN_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_SET_IGN(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-066"></a>

## 66. `try_match_SET_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Tests exactly one codepoint at caller-provided text_pos-1 after a slice bound check; a reverse-position probe, not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7343–7355. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7343-L7355).

### Read sites

- Site 1: lines 7354–7354; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7343–7355. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7343-L7355).

```c
Py_LOCAL_INLINE(int) try_match_SET_REV(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    if (text_pos <= state->text_start) {
        if (state->partial_side == RE_PARTIAL_LEFT)
            return RE_ERROR_PARTIAL;

        return RE_ERROR_FAILURE;
    }

    return bool_as_status(text_pos > state->slice_start &&
      matches_SET(state->encoding, state->locale_info, node,
      state->char_at(state->text, text_pos - 1)) == node->match);
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-067"></a>

## 67. `try_match_START_OF_LINE`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Line-boundary probe reads text_pos (end-of-line) or text_pos-1 (start-of-line); caller may select any position.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7358–7362. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7358-L7362).

### Read sites

- Site 1: lines 7360–7361; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7358–7362. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7358-L7362).

```c
Py_LOCAL_INLINE(int) try_match_START_OF_LINE(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    return bool_as_status(text_pos <= state->text_start || state->char_at(state->text, text_pos
      - 1) == '\n');
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-068"></a>

## 68. `try_match_STRING`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Checks a pattern-length region beginning at caller text_pos using text_pos+s_pos, with s_pos=0..length-1; exits on mismatch or partial-slice boundary. This is a forward subrange traversal, not a full string pass.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7383–7412. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7383-L7412).

### Read sites

- Site 1: lines 7404–7404; codepoint read via helper; index expression `text_pos + s_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7383–7412. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7383-L7412).

```c
Py_LOCAL_INLINE(int) try_match_STRING(RE_State* state, RE_NextNode* next,
  RE_Node* node, Py_ssize_t text_pos, RE_Position* next_position) {
    Py_ssize_t length;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    RE_CODE* values;
    Py_ssize_t s_pos;

    length = (Py_ssize_t)node->value_count;
    char_at = state->char_at;
    values = node->values;

    for (s_pos = 0; s_pos < length; s_pos++) {
        if (text_pos + s_pos >= state->slice_end) {
            if (state->partial_side == RE_PARTIAL_RIGHT) {
                next_position->text_pos = text_pos;
                return RE_ERROR_PARTIAL;
            }

            return RE_ERROR_FAILURE;
        }

        if (!same_char(char_at(state->text, text_pos + s_pos), values[s_pos]))
            return RE_ERROR_FAILURE;
    }

    next_position->node = next->match_next;
    next_position->text_pos = text_pos + next->match_step;

    return RE_ERROR_SUCCESS;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-069"></a>

## 69. `try_match_STRING_FLD`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Consumes full-casefolded codepoints beginning at caller text_pos, only until the pattern-length region matches; advances text_pos after consuming each fold. Zero match_step may preserve the caller position for a later operation.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7415–7483. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7415-L7483).

### Read sites

- Site 1: lines 7457–7458; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 7419–7452, 7463–7480. The original contextual region was lines 7415–7483.

Archive member `regex-2026.9.29/src/_regex.c`, lines 7415–7418. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7415-L7418).

```c
Py_LOCAL_INLINE(int) try_match_STRING_FLD(RE_State* state, RE_NextNode* next,
  RE_Node* node, Py_ssize_t text_pos, RE_Position* next_position) {
    Py_ssize_t length;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 7453–7462. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7453-L7462).

```c

                return RE_ERROR_FAILURE;
            }

            folded_len = full_case_fold(locale_info, char_at(state->text,
              text_pos), folded);
            f_pos = 0;
        }

        if (!same_char_ign(encoding, locale_info, values[s_pos],
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 7481–7483. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7481-L7483).

```c

    return RE_ERROR_SUCCESS;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-070"></a>

## 70. `try_match_STRING_FLD_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Consumes folded codepoints at text_pos-1 and decrements text_pos after consuming each fold, bounded by pattern length and caller slice.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7488–7556. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7488-L7556).

### Read sites

- Site 1: lines 7530–7531; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 7492–7525, 7536–7553. The original contextual region was lines 7488–7556.

Archive member `regex-2026.9.29/src/_regex.c`, lines 7488–7491. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7488-L7491).

```c
Py_LOCAL_INLINE(int) try_match_STRING_FLD_REV(RE_State* state, RE_NextNode*
  next, RE_Node* node, Py_ssize_t text_pos, RE_Position* next_position) {
    Py_ssize_t length;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 7526–7535. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7526-L7535).

```c

                return RE_ERROR_FAILURE;
            }

            folded_len = full_case_fold(locale_info, char_at(state->text,
              text_pos - 1), folded);
            f_pos = 0;
        }

        if (!same_char_ign(encoding, locale_info, values[length - s_pos - 1],
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 7554–7556. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7554-L7556).

```c

    return RE_ERROR_SUCCESS;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-071"></a>

## 71. `try_match_STRING_IGN`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Checks a pattern-length region beginning at caller text_pos using text_pos+s_pos, with s_pos=0..length-1; exits on mismatch or partial-slice boundary. This is a forward subrange traversal, not a full string pass.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7559–7593. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7559-L7593).

### Read sites

- Site 1: lines 7584–7585; codepoint read via helper; index expression `text_pos + s_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7559–7593. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7559-L7593).

```c
Py_LOCAL_INLINE(int) try_match_STRING_IGN(RE_State* state, RE_NextNode* next,
  RE_Node* node, Py_ssize_t text_pos, RE_Position* next_position) {
    Py_ssize_t length;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;
    RE_CODE* values;
    Py_ssize_t s_pos;

    length = (Py_ssize_t)node->value_count;
    char_at = state->char_at;
    encoding = state->encoding;
    locale_info = state->locale_info;
    values = node->values;

    for (s_pos = 0; s_pos < length; s_pos++) {
        if (text_pos + s_pos >= state->slice_end) {
            if (state->partial_side == RE_PARTIAL_RIGHT) {
                next_position->text_pos = text_pos;
                return RE_ERROR_PARTIAL;
            }

            return RE_ERROR_FAILURE;
        }

        if (!same_char_ign(encoding, locale_info, char_at(state->text, text_pos
          + s_pos), values[s_pos]))
            return RE_ERROR_FAILURE;
    }

    next_position->node = next->match_next;
    next_position->text_pos = text_pos + next->match_step;

    return RE_ERROR_SUCCESS;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-072"></a>

## 72. `try_match_STRING_IGN_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Checks a pattern-length reverse region beginning immediately before caller text_pos using text_pos-s_pos-1; exits on mismatch or partial-slice boundary.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7598–7632. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7598-L7632).

### Read sites

- Site 1: lines 7623–7624; codepoint read via helper; index expression `text_pos - s_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7598–7632. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7598-L7632).

```c
Py_LOCAL_INLINE(int) try_match_STRING_IGN_REV(RE_State* state, RE_NextNode*
  next, RE_Node* node, Py_ssize_t text_pos, RE_Position* next_position) {
    Py_ssize_t length;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;
    RE_CODE* values;
    Py_ssize_t s_pos;

    length = (Py_ssize_t)node->value_count;
    char_at = state->char_at;
    encoding = state->encoding;
    locale_info = state->locale_info;
    values = node->values;

    for (s_pos = 0; s_pos < length; s_pos++) {
        if (text_pos - s_pos <= state->slice_start) {
            if (state->partial_side == RE_PARTIAL_LEFT) {
                next_position->text_pos = text_pos;
                return RE_ERROR_PARTIAL;
            }

            return RE_ERROR_FAILURE;
        }

        if (!same_char_ign(encoding, locale_info, char_at(state->text, text_pos
          - s_pos - 1), values[length - s_pos - 1]))
            return RE_ERROR_FAILURE;
    }

    next_position->node = next->match_next;
    next_position->text_pos = text_pos + next->match_step;

    return RE_ERROR_SUCCESS;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-073"></a>

## 73. `try_match_STRING_REV`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Checks a pattern-length reverse region beginning immediately before caller text_pos using text_pos-s_pos-1; exits on mismatch or partial-slice boundary.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 7635–7665. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7635-L7665).

### Read sites

- Site 1: lines 7656–7656; codepoint read via helper; index expression `text_pos - s_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 7635–7665. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L7635-L7665).

```c
Py_LOCAL_INLINE(int) try_match_STRING_REV(RE_State* state, RE_NextNode* next,
  RE_Node* node, Py_ssize_t text_pos, RE_Position* next_position) {
    Py_ssize_t length;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    RE_CODE* values;
    Py_ssize_t s_pos;

    length = (Py_ssize_t)node->value_count;
    char_at = state->char_at;
    values = node->values;

    for (s_pos = 0; s_pos < length; s_pos++) {
        if (text_pos - s_pos <= state->slice_start) {
            if (state->partial_side == RE_PARTIAL_LEFT) {
                next_position->text_pos = text_pos;
                return RE_ERROR_PARTIAL;
            }

            return RE_ERROR_FAILURE;
        }

        if (!same_char(char_at(state->text, text_pos - s_pos - 1),
          values[length - s_pos - 1]))
            return RE_ERROR_FAILURE;
    }

    next_position->node = next->match_next;
    next_position->text_pos = text_pos + next->match_step;

    return RE_ERROR_SUCCESS;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-074"></a>

## 74. `search_start_END_OF_LINE`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Searches from caller text_pos forward to the next newline boundary, with early return. START_OF_LINE reads text_pos-1; neither requires starting at zero or reading to full end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 8039–8053. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8039-L8053).

### Read sites

- Site 1: lines 8044–8045; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 8039–8053. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8039-L8053).

```c
Py_LOCAL_INLINE(Py_ssize_t) search_start_END_OF_LINE(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, bool* is_partial) {
    *is_partial = false;

    for (;;) {
        if (text_pos >= state->text_end || state->char_at(state->text,
          text_pos) == '\n')
            return text_pos;

        if (text_pos >= state->slice_end)
            return -1;

        ++text_pos;
    }
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-075"></a>

## 75. `search_start_END_OF_LINE_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Searches backward from caller text_pos to the previous newline boundary; END reads text_pos and START reads text_pos-1, decrementing until slice_start.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 8056–8070. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8056-L8070).

### Read sites

- Site 1: lines 8061–8062; codepoint read via helper; index expression `text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 8056–8070. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8056-L8070).

```c
Py_LOCAL_INLINE(Py_ssize_t) search_start_END_OF_LINE_rev(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, bool* is_partial) {
    *is_partial = false;

    for (;;) {
        if (text_pos >= state->text_end || state->char_at(state->text,
          text_pos) == '\n')
            return text_pos;

        if (text_pos <= state->slice_start)
            return -1;

        --text_pos;
    }
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-076"></a>

## 76. `search_start_START_OF_LINE`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Searches from caller text_pos forward to the next newline boundary, with early return. START_OF_LINE reads text_pos-1; neither requires starting at zero or reading to full end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 8215–8228. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8215-L8228).

### Read sites

- Site 1: lines 8220–8220; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 8215–8228. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8215-L8228).

```c
Py_LOCAL_INLINE(Py_ssize_t) search_start_START_OF_LINE(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, bool* is_partial) {
    *is_partial = false;

    for (;;) {
        if (text_pos <= state->text_start || state->char_at(state->text, text_pos - 1) == '\n')
            return text_pos;

        if (text_pos >= state->slice_end)
            return -1;

        ++text_pos;
    }
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-077"></a>

## 77. `search_start_START_OF_LINE_rev`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Searches backward from caller text_pos to the previous newline boundary; END reads text_pos and START reads text_pos-1, decrementing until slice_start.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 8231–8244. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8231-L8244).

### Read sites

- Site 1: lines 8236–8236; codepoint read via helper; index expression `text_pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 8231–8244. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L8231-L8244).

```c
Py_LOCAL_INLINE(Py_ssize_t) search_start_START_OF_LINE_rev(RE_State* state,
  RE_Node* node, Py_ssize_t text_pos, bool* is_partial) {
    *is_partial = false;

    for (;;) {
        if (text_pos <= state->text_start || state->char_at(state->text, text_pos - 1) == '\n')
            return text_pos;

        if (text_pos <= state->slice_start)
            return -1;

        --text_pos;
    }
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-078"></a>

## 78. `fuzzy_ext_match`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Dispatch selects a single test at caller pos or pos-1 for forward/reverse opcodes. This function supports both directions and arbitrary caller-selected positions.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 9938–10015. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L9938-L10015).

### Read sites

- Site 1: lines 9952–9952; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 9956–9956; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 3: lines 9961–9961; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 4: lines 9964–9964; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 5: lines 9968–9968; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 6: lines 9972–9972; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 7: lines 9977–9977; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 8: lines 9980–9980; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 9: lines 9984–9984; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 10: lines 9988–9988; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 11: lines 9992–9992; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 12: lines 9996–9996; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 13: lines 10003–10003; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 14: lines 10010–10010; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 9942–9947. The original contextual region was lines 9938–10015.

Archive member `regex-2026.9.29/src/_regex.c`, lines 9938–9941. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L9938-L9941).

```c
Py_LOCAL_INLINE(bool) fuzzy_ext_match(RE_State* state, RE_Node* fuzzy_node,
  Py_ssize_t pos) {
    RE_Node* test_node;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 9948–10015. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L9948-L10015).

```c

    switch (test_node->op) {
    case RE_OP_CHARACTER:
        return pos < state->slice_end && matches_CHARACTER(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_CHARACTER_IGN:
        return pos < state->slice_end && matches_CHARACTER_IGN(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_CHARACTER_IGN_REV:
        return pos > state->slice_start &&
          matches_CHARACTER_IGN(state->encoding, state->locale_info, test_node,
          state->char_at(state->text, pos - 1)) == test_node->match;
    case RE_OP_CHARACTER_REV:
        return pos > state->slice_start && matches_CHARACTER(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos - 1))
          == test_node->match;
    case RE_OP_PROPERTY:
        return pos < state->slice_end && matches_PROPERTY(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_PROPERTY_IGN:
        return pos < state->slice_end && matches_PROPERTY_IGN(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_PROPERTY_IGN_REV:
        return pos > state->slice_start &&
          matches_PROPERTY_IGN(state->encoding, state->locale_info, test_node,
          state->char_at(state->text, pos - 1)) == test_node->match;
    case RE_OP_PROPERTY_REV:
        return pos > state->slice_start && matches_PROPERTY(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos - 1))
          == test_node->match;
    case RE_OP_RANGE:
        return pos < state->slice_end && matches_RANGE(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_RANGE_IGN:
        return pos < state->slice_end && matches_RANGE_IGN(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_RANGE_IGN_REV:
        return pos > state->slice_start && matches_RANGE_IGN(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos - 1))
          == test_node->match;
    case RE_OP_RANGE_REV:
        return pos > state->slice_start && matches_RANGE(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos - 1))
          == test_node->match;
    case RE_OP_SET_DIFF:
    case RE_OP_SET_INTER:
    case RE_OP_SET_SYM_DIFF:
    case RE_OP_SET_UNION:
        return pos < state->slice_end && matches_SET(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    case RE_OP_SET_DIFF_IGN:
    case RE_OP_SET_INTER_IGN:
    case RE_OP_SET_SYM_DIFF_IGN:
    case RE_OP_SET_UNION_IGN:
        return pos < state->slice_end && matches_SET_IGN(state->encoding,
          state->locale_info, test_node, state->char_at(state->text, pos)) ==
          test_node->match;
    }

    return true;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-079"></a>

## 79. `folded_char_at`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive reader.

Reads the codepoint at caller pos, casefolds it into a stack array, and returns folded[folded_pos]. Both source-codepoint and fold-element indices are caller-selected.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Shared primitive reader counted once as a source function; callers count their own access algorithms, not every runtime invocation.
- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 10018–10030. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L10018-L10030).

### Read sites

- Site 1: lines 10026–10026; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 10018–10030. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L10018-L10030).

```c
Py_LOCAL_INLINE(Py_UCS4) folded_char_at(RE_State* state, Py_ssize_t pos, int
  folded_pos) {
    int (*full_case_fold)(RE_LocaleInfo* locale_info, Py_UCS4 ch, Py_UCS4*
      folded);
    Py_UCS4 folded[RE_MAX_FOLDED];

    full_case_fold = state->encoding->full_case_fold;

    full_case_fold(state->locale_info, state->char_at(state->text, pos),
      folded);

    return folded[folded_pos];
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-080"></a>

## 80. `fuzzy_ext_match_group_fld`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Dispatch invokes folded_char_at at state->text_pos or state->text_pos-1 and caller folded_pos or folded_pos-1. The callee reads the indexed original codepoint before selecting a fold element.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 10033–10113. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L10033-L10113).

### Read sites

- Site 1: lines 10045–10045; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 10050–10050; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 3: lines 10055–10055; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 4: lines 10060–10060; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 5: lines 10065–10065; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 6: lines 10070–10070; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 7: lines 10075–10075; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 8: lines 10080–10080; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 9: lines 10085–10085; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 10: lines 10090–10090; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 11: lines 10095–10095; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 12: lines 10100–10100; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 13: lines 10108–10108; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 10037–10040. The original contextual region was lines 10033–10113.

Archive member `regex-2026.9.29/src/_regex.c`, lines 10033–10036. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L10033-L10036).

```c
Py_LOCAL_INLINE(bool) fuzzy_ext_match_group_fld(RE_State* state, RE_Node*
  fuzzy_node, int folded_pos) {
    RE_Node* test_node;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 10041–10113. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L10041-L10113).

```c
    switch (test_node->op) {
    case RE_OP_CHARACTER:
        return state->text_pos < state->slice_end &&
          matches_CHARACTER(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    case RE_OP_CHARACTER_IGN:
        return state->text_pos < state->slice_end &&
          matches_CHARACTER_IGN(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    case RE_OP_CHARACTER_IGN_REV:
        return state->text_pos > state->slice_start &&
          matches_CHARACTER_IGN(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos - 1, folded_pos - 1)) ==
          test_node->match;
    case RE_OP_CHARACTER_REV:
        return state->text_pos > state->slice_start &&
          matches_CHARACTER(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos - 1, folded_pos - 1)) ==
          test_node->match;
    case RE_OP_PROPERTY:
        return state->text_pos < state->slice_end &&
          matches_PROPERTY(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    case RE_OP_PROPERTY_IGN:
        return state->text_pos < state->slice_end &&
          matches_PROPERTY_IGN(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    case RE_OP_PROPERTY_IGN_REV:
        return state->text_pos > state->slice_start &&
          matches_PROPERTY_IGN(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos - 1, folded_pos - 1)) ==
          test_node->match;
    case RE_OP_PROPERTY_REV:
        return state->text_pos > state->slice_start &&
          matches_PROPERTY(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos - 1, folded_pos - 1)) ==
          test_node->match;
    case RE_OP_RANGE:
        return state->text_pos < state->slice_end &&
          matches_RANGE(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    case RE_OP_RANGE_IGN:
        return state->text_pos < state->slice_end &&
          matches_RANGE_IGN(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    case RE_OP_RANGE_IGN_REV:
        return state->text_pos > state->slice_start &&
          matches_RANGE_IGN(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos - 1, folded_pos - 1)) ==
          test_node->match;
    case RE_OP_RANGE_REV:
        return state->text_pos > state->slice_start &&
          matches_RANGE(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos - 1, folded_pos - 1)) ==
          test_node->match;
    case RE_OP_SET_DIFF:
    case RE_OP_SET_INTER:
    case RE_OP_SET_SYM_DIFF:
    case RE_OP_SET_UNION:
        return state->text_pos < state->slice_end &&
          matches_SET(state->encoding, state->locale_info, test_node,
          folded_char_at(state, state->text_pos, folded_pos)) ==
          test_node->match;
    }

    return true;
}
```

### Callee analysis

- `folded_char_at` in `regex-2026.9.29/src/_regex.c`, lines 10018–10030: Reads char_at(state->text,pos), full_case_fold, then folded[folded_pos]. arbitrary-index source read confirmed

Available source context:

- [`folded_char_at`](#helper-002) (`regex-2026.9.29/src/_regex.c`, lines 10018–10030).

<a id="case-081"></a>

## 81. `partial_string_match`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Compares text_pos+ofs for ofs=0..pattern_length-1, beginning at caller text_pos and stopping at mismatch or slice_end. Forward contiguous subrange, not a whole-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 11655–11678. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11655-L11678).

### Read sites

- Site 1: lines 11671–11671; codepoint read via helper; index expression `text_pos + ofs`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 11655–11678. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11655-L11678).

```c
Py_LOCAL_INLINE(bool) partial_string_match(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    Py_ssize_t length;
    RE_CODE* values;
    Py_ssize_t ofs;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);

    length = (Py_ssize_t)node->value_count;
    values = node->values;
    ofs = 0;
    char_at = state->char_at;

    while (ofs < length) {
        if (text_pos + ofs >= state->slice_end)
            return true;

        if (char_at(state->text, text_pos + ofs) != values[ofs])
            return false;

        ++ofs;
    }

    return true;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-082"></a>

## 82. `partial_string_match_ign`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Compares text_pos+ofs for ofs=0..pattern_length-1, beginning at caller text_pos and stopping at mismatch or slice_end. Forward contiguous subrange, not a whole-string traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 11683–11711. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11683-L11711).

### Read sites

- Site 1: lines 11703–11704; codepoint read via helper; index expression `text_pos + ofs`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Archive member `regex-2026.9.29/src/_regex.c`, lines 11683–11711. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11683-L11711).

```c
Py_LOCAL_INLINE(bool) partial_string_match_ign(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos) {
    Py_ssize_t length;
    RE_CODE* values;
    Py_ssize_t ofs;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;

    length = (Py_ssize_t)node->value_count;
    values = node->values;
    ofs = 0;
    char_at = state->char_at;
    encoding = state->encoding;
    locale_info = state->locale_info;

    while (ofs < length) {
        if (text_pos + ofs >= state->slice_end)
            return true;

        if (!same_char_ign(encoding, locale_info, char_at(state->text, text_pos
          + ofs), values[ofs]))
            return false;

        ++ofs;
    }

    return true;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="case-083"></a>

## 83. `basic_match`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing, backward traversal, lookahead or lookbehind, reset or backtracking, multiple passes, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Main depth-first matcher mixes forward/reverse reads, stored-capture backreferences at string_pos, full-casefold matching, repeat scans and stack-controlled restoration of text_pos. It can reread regions and return to prior positions; state slice begins at caller start. The explicit char_at sites and dispatch into typed matcher/search helpers are all recorded.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 11714–17406. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11714-L17406).

### Read sites

- Site 1: lines 12133–12133; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 12156–12156; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 3: lines 12178–12178; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 4: lines 12200–12200; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 5: lines 13814–13814; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 6: lines 13837–13837; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 7: lines 13859–13859; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 8: lines 13881–13881; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 9: lines 13923–13923; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 10: lines 13947–13947; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 11: lines 13969–13969; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 12: lines 13990–13990; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 13: lines 14034–14034; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 14: lines 14035–14035; codepoint read via helper; index expression `string_pos`. Exact read expression; access pattern explained at function level.
- Site 15: lines 14095–14096; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 16: lines 14097–14098; codepoint read via helper; index expression `string_pos`. Exact read expression; access pattern explained at function level.
- Site 17: lines 14111–14111; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 18: lines 14121–14121; codepoint read via helper; index expression `string_pos`. Exact read expression; access pattern explained at function level.
- Site 19: lines 14196–14197; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 20: lines 14198–14199; codepoint read via helper; index expression `string_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 21: lines 14212–14212; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 22: lines 14222–14222; codepoint read via helper; index expression `string_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 23: lines 14292–14293; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 24: lines 14293–14293; codepoint read via helper; index expression `string_pos`. Exact read expression; access pattern explained at function level.
- Site 25: lines 14348–14349; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 26: lines 14349–14349; codepoint read via helper; index expression `string_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 27: lines 14405–14405; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 28: lines 14406–14406; codepoint read via helper; index expression `string_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 29: lines 14457–14457; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 30: lines 14482–14482; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 31: lines 14506–14507; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 32: lines 14530–14530; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 33: lines 14743–14743; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 34: lines 14800–14800; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 35: lines 14822–14822; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 36: lines 14906–14906; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 37: lines 14928–14928; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 38: lines 15013–15014; codepoint read via helper; index expression `state->text_pos`. Exact read expression; access pattern explained at function level.
- Site 39: lines 15070–15071; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 40: lines 15127–15127; codepoint read via helper; index expression `state->text_pos - 1`. Exact read expression; access pattern explained at function level.
- Site 41: lines 15922–15922; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 42: lines 15944–15944; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 43: lines 15966–15966; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 44: lines 15987–15987; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 45: lines 16567–16567; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 46: lines 16605–16605; codepoint read via helper; index expression `pos`. Exact read expression; access pattern explained at function level.
- Site 47: lines 16643–16643; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.
- Site 48: lines 16680–16680; codepoint read via helper; index expression `pos - 1`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 11725–11740, 11750, 11769–11776. The original contextual region was lines 11714–11779.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 12122–12128, 12138–12151, 12161–12173, 12183–12195, 12205–12212. The original contextual region was lines 12118–12215.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 13766–13809, 13819–13832, 13842–13854, 13864–13876, 13886–13893. The original contextual region was lines 13762–13896.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 13912–13918, 13928–13942, 13952–13964, 13974–13985, 13995–14002. The original contextual region was lines 13908–14005.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 14084–14090, 14103–14106, 14116, 14126–14133. The original contextual region was lines 14080–14136.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 14185–14191, 14204–14207, 14217, 14227–14234. The original contextual region was lines 14181–14237.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 14446–14452, 14462–14477, 14487–14501, 14512–14525, 14535–14542. The original contextual region was lines 14442–14545.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 14789–14795, 14805–14817, 14827–14834. The original contextual region was lines 14785–14837.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 14895–14901, 14911–14923, 14933–14940. The original contextual region was lines 14891–14943.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 15360–15363, 15373–15377, 15387–15402. The original contextual region was lines 15355–15412.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 15689–15710, 15725–15728. The original contextual region was lines 15682–15739.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 15911–15917, 15927–15939, 15949–15961, 15971–15982, 15992–15999. The original contextual region was lines 15907–16002.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 16487–16489. The original contextual region was lines 16469–16505.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 17216–17245, 17258–17267. The original contextual region was lines 17204–17277.

Archive member `regex-2026.9.29/src/_regex.c`, lines 11714–11724. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11714-L11724).

```c
Py_LOCAL_INLINE(int) basic_match(RE_State* state, bool search) {
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;
    PatternObject* pattern;
    RE_Node* start_node;
    RE_NextNode start_pair;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    Py_ssize_t pattern_step; /* The overall step of the pattern (forwards or backwards). */
    Py_ssize_t string_pos;
    bool do_search_start;
    Py_ssize_t found_pos;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 11741–11749. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11741-L11749).

```c
    switch (start_pair.test->op) {
    case RE_OP_END_OF_STRING:
        if (state->reverse) {
            /* Searching backwards. */
            if (state->text_pos != state->text_end)
                return RE_ERROR_FAILURE;

            /* Don't bother to search further because it's anchored. */
            search = false;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 11751–11768. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11751-L11768).

```c
        break;
    case RE_OP_START_OF_STRING:
        if (!state->reverse) {
            /* Searching forwards. */
            if (state->text_pos != state->text_start)
                return RE_ERROR_FAILURE;

            /* Don't bother to search further because it's anchored. */
            search = false;
        }
        break;
    }

    char_at = state->char_at;
    pattern_step = state->reverse ? -1 : 1;
    string_pos = -1;
    do_search_start = pattern->do_search_start;
    state->fewest_errors = state->max_errors;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 11777–11779. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L11777-L11779).

```c

    if (!push_uint8(state, &state->bstack, RE_OP_FAILURE))
        return RE_ERROR_MEMORY;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 12118–12121. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L12118-L12121).

```c
             */

            node = node->next_1.node;
            break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 12129–12137. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L12129-L12137).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end &&
              matches_CHARACTER(encoding, locale_info, node,
              char_at(state->text, state->text_pos)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, 1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 12152–12160. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L12152-L12160).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end &&
              matches_CHARACTER_IGN(encoding, locale_info, node,
              char_at(state->text, state->text_pos)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, 1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 12174–12182. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L12174-L12182).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start &&
              matches_CHARACTER_IGN(encoding, locale_info, node,
              char_at(state->text, state->text_pos - 1)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, -1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 12196–12204. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L12196-L12204).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start &&
              matches_CHARACTER(encoding, locale_info, node,
              char_at(state->text, state->text_pos - 1)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, -1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 12213–12215. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L12213-L12215).

```c
        case RE_OP_CONDITIONAL: /* Start of a conditional subpattern. */
        {
            RE_LookaroundStateData data_l;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13762–13765. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13762-L13765).

```c
            TRACE(("%s %d\n", re_op_text[node->op], node->match))

            data_l.node = node;
            data_l.slice_start = state->slice_start;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13810–13818. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13810-L13818).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end &&
              matches_PROPERTY(encoding, locale_info, node,
              char_at(state->text, state->text_pos)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, 1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13833–13841. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13833-L13841).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end &&
              matches_PROPERTY_IGN(encoding, locale_info, node,
              char_at(state->text, state->text_pos)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, 1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13855–13863. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13855-L13863).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start &&
              matches_PROPERTY_IGN(encoding, locale_info, node,
              char_at(state->text, state->text_pos - 1)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, -1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13877–13885. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13877-L13885).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start &&
              matches_PROPERTY(encoding, locale_info, node,
              char_at(state->text, state->text_pos - 1)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, -1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13894–13896. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13894-L13896).

```c
        case RE_OP_PRUNE: /* Prune the backtracking. */
            TRACE(("%s\n", re_op_text[node->op]))

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13908–13911. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13908-L13911).

```c
             *
             * pstack: bstack
             */

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13919–13927. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13919-L13927).

```c
              RE_PARTIAL_RIGHT)
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end && matches_RANGE(encoding,
              locale_info, node, char_at(state->text, state->text_pos)) ==
              node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13943–13951. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13943-L13951).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end &&
              matches_RANGE_IGN(encoding, locale_info, node,
              char_at(state->text, state->text_pos)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, 1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13965–13973. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13965-L13973).

```c
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start &&
              matches_RANGE_IGN(encoding, locale_info, node,
              char_at(state->text, state->text_pos - 1)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, -1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 13986–13994. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L13986-L13994).

```c
            if (state->text_pos <= state->text_start && state->partial_side == RE_PARTIAL_LEFT)
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start && matches_RANGE(encoding,
              locale_info, node, char_at(state->text, state->text_pos - 1)) ==
              node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14003–14005. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14003-L14005).

```c
            break;
        case RE_OP_REF_GROUP: /* Reference to a capture group. */
        {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14019–14050. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14019-L14050).

```c
            if (group->current < 0)
                goto backtrack;

            span = &group->captures[group->current];

            if (string_pos < 0)
                string_pos = span->start;

            /* Try comparing. */
            while (string_pos < span->end) {
                if (state->text_pos >= state->text_end &&
                  state->partial_side == RE_PARTIAL_RIGHT)
                    return RE_ERROR_PARTIAL;

                if (state->text_pos < state->slice_end &&
                  same_char(char_at(state->text, state->text_pos),
                  char_at(state->text, string_pos))) {
                    ++string_pos;
                    ++state->text_pos;
                } else if (node->status & RE_STATUS_FUZZY) {
                    status = fuzzy_match_string(state, search, node,
                      &string_pos, 1);
                    if (status < 0)
                        return status;

                    if (status == RE_ERROR_FAILURE) {
                        string_pos = -1;
                        goto backtrack;
                    }
                } else {
                    string_pos = -1;
                    goto backtrack;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14080–14083. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14080-L14083).

```c
            group = &state->groups[node->values[0] - 1];
            if (group->current < 0)
                goto backtrack;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14091–14102. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14091-L14102).

```c
                folded_len = 0;
                gfolded_pos = 0;
                gfolded_len = 0;
            } else {
                folded_len = full_case_fold(locale_info, char_at(state->text,
                  state->text_pos), folded);
                gfolded_len = full_case_fold(locale_info, char_at(state->text,
                  string_pos), gfolded);
            }

            /* Try comparing. */
            while (string_pos < span->end) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14107–14115. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14107-L14115).

```c
                        return RE_ERROR_PARTIAL;

                    if (state->text_pos < state->slice_end)
                        folded_len = full_case_fold(locale_info,
                          char_at(state->text, state->text_pos), folded);
                    else
                        folded_len = 0;

                    folded_pos = 0;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14117–14125. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14117-L14125).

```c

                /* Case-fold at current position in group. */
                if (gfolded_pos >= gfolded_len) {
                    gfolded_len = full_case_fold(locale_info,
                      char_at(state->text, string_pos), gfolded);
                    gfolded_pos = 0;
                }

                if (folded_pos < folded_len && same_char_ign(encoding,
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14134–14136. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14134-L14136).

```c
                        return status;

                    if (status == RE_ERROR_FAILURE) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14181–14184. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14181-L14184).

```c
            group = &state->groups[node->values[0] - 1];
            if (group->current < 0)
                goto backtrack;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14192–14203. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14192-L14203).

```c
                folded_len = 0;
                gfolded_pos = 0;
                gfolded_len = 0;
            } else {
                folded_len = full_case_fold(locale_info, char_at(state->text,
                  state->text_pos - 1), folded);
                gfolded_len = full_case_fold(locale_info, char_at(state->text,
                  string_pos - 1), gfolded);
            }

            /* Try comparing. */
            while (string_pos > span->start) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14208–14216. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14208-L14216).

```c
                        return RE_ERROR_PARTIAL;

                    if (state->text_pos > state->slice_start)
                        folded_len = full_case_fold(locale_info,
                          char_at(state->text, state->text_pos - 1), folded);
                    else
                        folded_len = 0;

                    folded_pos = folded_len;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14218–14226. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14218-L14226).

```c

                /* Case-fold at current position in group. */
                if (gfolded_pos <= 0) {
                    gfolded_len = full_case_fold(locale_info,
                      char_at(state->text, string_pos - 1), gfolded);
                    gfolded_pos = gfolded_len;
                }

                if (folded_pos > 0 && same_char_ign(encoding, locale_info,
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14235–14237. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14235-L14237).

```c
                        return status;

                    if (status == RE_ERROR_FAILURE) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14277–14308. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14277-L14308).

```c
            if (group->current < 0)
                goto backtrack;

            span = &group->captures[group->current];

            if (string_pos < 0)
                string_pos = span->start;

            /* Try comparing. */
            while (string_pos < span->end) {
                if (state->text_pos >= state->text_end &&
                  state->partial_side == RE_PARTIAL_RIGHT)
                    return RE_ERROR_PARTIAL;

                if (state->text_pos < state->slice_end &&
                  same_char_ign(encoding, locale_info, char_at(state->text,
                  state->text_pos), char_at(state->text, string_pos))) {
                    ++string_pos;
                    ++state->text_pos;
                } else if (node->status & RE_STATUS_FUZZY) {
                    status = fuzzy_match_string(state, search, node,
                      &string_pos, 1);
                    if (status < 0)
                        return status;

                    if (status == RE_ERROR_FAILURE) {
                        string_pos = -1;
                        goto backtrack;
                    }
                } else {
                    string_pos = -1;
                    goto backtrack;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14333–14364. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14333-L14364).

```c
            if (group->current < 0)
                goto backtrack;

            span = &group->captures[group->current];

            if (string_pos < 0)
                string_pos = span->end;

            /* Try comparing. */
            while (string_pos > span->start) {
                if (state->text_pos <= state->text_start && state->partial_side ==
                  RE_PARTIAL_LEFT)
                    return RE_ERROR_PARTIAL;

                if (state->text_pos > state->slice_start &&
                  same_char_ign(encoding, locale_info, char_at(state->text,
                  state->text_pos - 1), char_at(state->text, string_pos - 1)))
                  {
                    --string_pos;
                    --state->text_pos;
                } else if (node->status & RE_STATUS_FUZZY) {
                    status = fuzzy_match_string(state, search, node,
                      &string_pos, -1);
                    if (status < 0)
                        return status;

                    if (status == RE_ERROR_FAILURE) {
                        string_pos = -1;
                        goto backtrack;
                    }
                } else {
                    string_pos = -1;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14390–14421. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14390-L14421).

```c
            if (group->current < 0)
                goto backtrack;

            span = &group->captures[group->current];

            if (string_pos < 0)
                string_pos = span->end;

            /* Try comparing. */
            while (string_pos > span->start) {
                if (state->text_pos <= state->text_start && state->partial_side ==
                  RE_PARTIAL_LEFT)
                    return RE_ERROR_PARTIAL;

                if (state->text_pos > state->slice_start &&
                  same_char(char_at(state->text, state->text_pos - 1),
                  char_at(state->text, string_pos - 1))) {
                    --string_pos;
                    --state->text_pos;
                } else if (node->status & RE_STATUS_FUZZY) {
                    status = fuzzy_match_string(state, search, node,
                      &string_pos, -1);
                    if (status < 0)
                        return status;

                    if (status == RE_ERROR_FAILURE) {
                        string_pos = -1;
                        goto backtrack;
                    }
                } else {
                    string_pos = -1;
                    goto backtrack;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14442–14445. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14442-L14445).

```c
                    goto backtrack;
            } else
                goto backtrack;
            break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14453–14461. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14453-L14461).

```c
              RE_PARTIAL_RIGHT)
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end && matches_SET(encoding,
              locale_info, node, char_at(state->text, state->text_pos)) ==
              node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14478–14486. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14478-L14486).

```c
              RE_PARTIAL_RIGHT)
                return RE_ERROR_PARTIAL;

            if (state->text_pos < state->slice_end && matches_SET_IGN(encoding,
              locale_info, node, char_at(state->text, state->text_pos)) ==
              node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14502–14511. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14502-L14511).

```c
            if (state->text_pos <= state->text_start && state->partial_side == RE_PARTIAL_LEFT)
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start &&
              matches_SET_IGN(encoding, locale_info, node, char_at(state->text,
              state->text_pos - 1)) == node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
                status = fuzzy_match_item(state, search, &node, -1);
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14526–14534. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14526-L14534).

```c
            if (state->text_pos <= state->text_start && state->partial_side == RE_PARTIAL_LEFT)
                return RE_ERROR_PARTIAL;

            if (state->text_pos > state->slice_start && matches_SET(encoding,
              locale_info, node, char_at(state->text, state->text_pos - 1)) ==
              node->match) {
                state->text_pos += node->step;
                node = node->next_1.node;
            } else if (node->status & RE_STATUS_FUZZY) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14543–14545. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14543-L14545).

```c
            break;
        case RE_OP_SKIP: /* Skip the part of the text already matched. */
            TRACE(("%s\n", re_op_text[node->op]))
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14728–14758. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14728-L14758).

```c
            else {
                length = (Py_ssize_t)node->value_count;

                if (string_pos < 0)
                    string_pos = 0;

                values = node->values;

                /* Try comparing. */
                while (string_pos < length) {
                    if (state->text_pos >= state->text_end &&
                      state->partial_side == RE_PARTIAL_RIGHT)
                        return RE_ERROR_PARTIAL;

                    if (state->text_pos < state->slice_end &&
                      same_char(char_at(state->text, state->text_pos),
                      values[string_pos])) {
                        ++string_pos;
                        ++state->text_pos;
                    } else if (node->status & RE_STATUS_FUZZY) {
                        status = fuzzy_match_string(state, search, node,
                          &string_pos, 1);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE) {
                            string_pos = -1;
                            goto backtrack;
                        }
                    } else {
                        string_pos = -1;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14785–14788. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14785-L14788).

```c

            if ((node->status & RE_STATUS_REQUIRED) && state->text_pos ==
              state->req_pos && string_pos < 0)
                state->text_pos = state->req_end;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14796–14804. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14796-L14804).

```c
                    folded_pos = 0;
                    folded_len = 0;
                } else {
                    folded_len = full_case_fold(locale_info,
                      char_at(state->text, state->text_pos), folded);
                    if (folded_pos >= folded_len) {
                        if (state->text_pos >= state->slice_end)
                            goto backtrack;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14818–14826. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14818-L14826).

```c
                            return RE_ERROR_PARTIAL;

                        if (state->text_pos < state->slice_end)
                            folded_len = full_case_fold(locale_info,
                              char_at(state->text, state->text_pos), folded);
                        else
                            folded_len = 0;

                        folded_pos = 0;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14835–14837. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14835-L14837).

```c
                            ++state->text_pos;
                    } else if (node->status & RE_STATUS_FUZZY) {
                        status = fuzzy_match_string_fld(state, search, node,
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14891–14894. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14891-L14894).

```c

            if ((node->status & RE_STATUS_REQUIRED) && state->text_pos ==
              state->req_pos && string_pos < 0)
                state->text_pos = state->req_end;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14902–14910. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14902-L14910).

```c
                    folded_pos = 0;
                    folded_len = 0;
                } else {
                    folded_len = full_case_fold(locale_info,
                      char_at(state->text, state->text_pos - 1), folded);
                    if (folded_pos <= 0) {
                        if (state->text_pos <= state->slice_start)
                            goto backtrack;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14924–14932. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14924-L14932).

```c
                            return RE_ERROR_PARTIAL;

                        if (state->text_pos > state->slice_start)
                            folded_len = full_case_fold(locale_info,
                              char_at(state->text, state->text_pos - 1),
                              folded);
                        else
                            folded_len = 0;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14941–14943. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14941-L14943).

```c
                        if (folded_pos <= 0)
                            --state->text_pos;
                    } else if (node->status & RE_STATUS_FUZZY) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 14998–15029. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L14998-L15029).

```c
            else {
                length = (Py_ssize_t)node->value_count;

                if (string_pos < 0)
                    string_pos = 0;

                values = node->values;

                /* Try comparing. */
                while (string_pos < length) {
                    if (state->text_pos >= state->text_end &&
                      state->partial_side == RE_PARTIAL_RIGHT)
                        return RE_ERROR_PARTIAL;

                    if (state->text_pos < state->slice_end &&
                      same_char_ign(encoding, locale_info, char_at(state->text,
                      state->text_pos), values[string_pos])) {
                        ++string_pos;
                        ++state->text_pos;
                    } else if (node->status & RE_STATUS_FUZZY) {
                        status = fuzzy_match_string(state, search, node,
                          &string_pos, 1);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE) {
                            string_pos = -1;
                            goto backtrack;
                        }
                    } else {
                        string_pos = -1;
                        goto backtrack;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15055–15086. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15055-L15086).

```c
            else {
                length = (Py_ssize_t)node->value_count;

                if (string_pos < 0)
                    string_pos = length;

                values = node->values;

                /* Try comparing. */
                while (string_pos > 0) {
                    if (state->text_pos <= state->text_start && state->partial_side ==
                      RE_PARTIAL_LEFT)
                        return RE_ERROR_PARTIAL;

                    if (state->text_pos > state->slice_start &&
                      same_char_ign(encoding, locale_info, char_at(state->text,
                      state->text_pos - 1), values[string_pos - 1])) {
                        --string_pos;
                        --state->text_pos;
                    } else if (node->status & RE_STATUS_FUZZY) {
                        status = fuzzy_match_string(state, search, node,
                          &string_pos, -1);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE) {
                            string_pos = -1;
                            goto backtrack;
                        }
                    } else {
                        string_pos = -1;
                        goto backtrack;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15112–15142. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15112-L15142).

```c
            else {
                length = (Py_ssize_t)node->value_count;

                if (string_pos < 0)
                    string_pos = length;

                values = node->values;

                /* Try comparing. */
                while (string_pos > 0) {
                    if (state->text_pos <= state->text_start && state->partial_side ==
                      RE_PARTIAL_LEFT)
                        return RE_ERROR_PARTIAL;

                    if (state->text_pos > state->slice_start &&
                      same_char(char_at(state->text, state->text_pos - 1),
                      values[string_pos - 1])) {
                        --string_pos;
                        --state->text_pos;
                    } else if (node->status & RE_STATUS_FUZZY) {
                        status = fuzzy_match_string(state, search, node,
                          &string_pos, -1);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE) {
                            string_pos = -1;
                            goto backtrack;
                        }
                    } else {
                        string_pos = -1;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15355–15359. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15355-L15359).

```c
            TRACE(("%s\n", re_op_text[op]))

            /* sstack: -
             *
             * bstack: text_pos node
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15364–15372. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15364-L15372).

```c
            if (!pop_ssize(state, &state->bstack, &state->text_pos))
                return RE_ERROR_MEMORY;
            goto advance;
        case RE_OP_CALL_REF: /* A group call ref. */
            TRACE(("%s\n", re_op_text[op]))

            /* sstack: NULL
             *
             * bstack: -
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15378–15386. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15378-L15386).

```c
        case RE_OP_CONDITIONAL: /* Conditional subpattern. */
        {
            RE_Node* conditional;
            RE_LookaroundStateData data_l;
            TRACE(("%s\n", re_op_text[op]))

            /* sstack: node slice_start slice_end text_pos ...
             *
             * bstack: captures repeats fuzzy_counts capture_change sstack
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15403–15412. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15403-L15412).

```c
            if (!ByteStack_pop_block(state, &state->sstack, (void*)&data_l,
              sizeof(data_l)))
                return RE_ERROR_MEMORY;

            state->text_pos = data_l.text_pos;
            state->slice_end = data_l.slice_end;
            state->slice_start = data_l.slice_start;
            conditional = data_l.node;

            /* sstack: -
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15682–15688. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15682-L15688).

```c
            TRACE(("%s\n", re_op_text[op]))

            /* Have we been looking for a POSIX match? */
            if (state->found_match) {
                restore_best_match(state);
                return RE_OP_SUCCESS;
            }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15711–15724. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15711-L15724).

```c
                bool is_partial;

                /* How many characters did the repeat actually match? */
                count = count_one(state, start_node->nonstring.next_2.node,
                  state->text_pos, start_node->values[2], &is_partial);

                /* If it's fewer than the maximum then skip over those
                 * characters.
                 */
                if (count < start_node->values[2])
                    state->text_pos += (Py_ssize_t)count * pattern_step;
                break;
            }
            }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15729–15739. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15729-L15739).

```c
            if (state->reverse) {
                if (state->text_pos > state->slice_end)
                    state->text_pos = state->slice_end;
                else
                    --state->text_pos;
            } else {
                if (state->text_pos < state->slice_start)
                    state->text_pos = state->slice_start;
                else
                    ++state->text_pos;
            }
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15829–15860. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15829-L15860).

```c
            TRACE(("%s\n", re_op_text[op]))

            /* bstack: count start node index */

            if (!ByteStack_pop_block(state, &state->bstack,
              (void*)&data_ro,sizeof(data_ro)))
                return RE_ERROR_MEMORY;

            index = data_ro.index;
            node = data_ro.node;
            start = data_ro.start;
            saved_count = data_ro.count;

            rp_data = &state->repeats[index];

            /* Unmatch one character at a time until the tail could match or we
             * have reached the minimum.
             */
            state->text_pos = rp_data->start;

            count = rp_data->count;
            step = node->nonstring.next_2.test->step;
            pos = state->text_pos + (Py_ssize_t)count * step;
            limit = state->text_pos + (Py_ssize_t)node->values[1] * step;

            /* The tail failed to match at this position. */
            if (!guard_repeat(state, index, pos, RE_STATUS_TAIL, true))
                return RE_ERROR_MEMORY;

            /* A (*SKIP) might have changed the size of the slice. */
            if (step > 0) {
                if (limit < state->slice_start)
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15907–15910. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15907-L15910).

```c
            } else {
                /* A repeated single-character match is often followed by a
                 * literal, so checking specially for it can be a good
                 * optimisation when working with long strings.
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15918–15926. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15918-L15926).

```c

                    for (;;) {
                        --pos;

                        if (same_char(char_at(state->text, pos), ch) == m &&
                          !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15940–15948. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15940-L15948).

```c
                    for (;;) {
                        --pos;

                        if (same_char_ign(encoding, locale_info,
                          char_at(state->text, pos), ch) == m &&
                          !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15962–15970. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15962-L15970).

```c
                    for (;;) {
                        ++pos;

                        if (same_char_ign(encoding, locale_info,
                          char_at(state->text, pos - 1), ch) == m &&
                          !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 15983–15991. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L15983-L15991).

```c

                    for (;;) {
                        ++pos;

                        if (same_char(char_at(state->text, pos - 1), ch) == m
                          && !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16000–16002. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16000-L16002).

```c
                {
                    Py_ssize_t length;

```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16469–16486. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16469-L16486).

```c
            TRACE(("%s\n", re_op_text[op]))

            /* bstack: count start node index */

            if (!ByteStack_pop_block(state, &state->bstack, (void*)&data,
              sizeof(data)))
                return RE_ERROR_MEMORY;

            index = data.index;
            node = data.node;
            start = data.start;
            saved_count = data.count;

            rp_data = &state->repeats[index];

            /* Match one character at a time until the tail could match or we
             * have reached the maximum.
             */
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16490–16505. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16490-L16505).

```c
            step = node->nonstring.next_2.test->step;
            pos = state->text_pos + (Py_ssize_t)count * step;
            available = step > 0 ? state->slice_end - state->text_pos :
              state->text_pos - state->slice_start;
            max_count = min_size_t((size_t)available, node->values[2]);
            limit = state->text_pos + (Py_ssize_t)max_count * step;

            repeated = node->nonstring.next_2.node;

            test = node->next_1.test;

            m = test->match;
            index = node->values[0];

            match = false;
            skip_pos = -1;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16552–16582. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16552-L16582).

```c
                          state->partial_side == RE_PARTIAL_RIGHT)
                            return RE_ERROR_PARTIAL;

                        if (pos >= limit)
                            break;

                        status = match_one(state, repeated, pos);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE)
                            break;

                        ++pos;

                        if (same_char(char_at(state->text, pos), ch) == m &&
                          !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
                        }
                    }
                    break;
                }
                case RE_OP_CHARACTER_IGN:
                {
                    Py_UCS4 ch;

                    ch = test->values[0];

                    /* The tail is a character. We don't want to go off the end
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16590–16620. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16590-L16620).

```c
                            return RE_ERROR_PARTIAL;

                        if (pos >= limit)
                            break;

                        status = match_one(state, repeated, pos);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE)
                            break;

                        ++pos;

                        if (same_char_ign(encoding, locale_info,
                          char_at(state->text, pos), ch) == m &&
                          !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
                        }
                    }
                    break;
                }
                case RE_OP_CHARACTER_IGN_REV:
                {
                    Py_UCS4 ch;

                    ch = test->values[0];

                    /* The tail is a character. We don't want to go off the end
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16628–16658. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16628-L16658).

```c
                            return RE_ERROR_PARTIAL;

                        if (pos <= limit)
                            break;

                        status = match_one(state, repeated, pos);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE)
                            break;

                        --pos;

                        if (same_char_ign(encoding, locale_info,
                          char_at(state->text, pos - 1), ch) == m &&
                          !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
                        }
                    }
                    break;
                }
                case RE_OP_CHARACTER_REV:
                {
                    Py_UCS4 ch;

                    ch = test->values[0];

                    /* The tail is a character. We don't want to go off the end
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 16665–16695. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L16665-L16695).

```c
                          RE_PARTIAL_LEFT)
                            return RE_ERROR_PARTIAL;

                        if (pos <= limit)
                            break;

                        status = match_one(state, repeated, pos);
                        if (status < 0)
                            return status;

                        if (status == RE_ERROR_FAILURE)
                            break;

                        --pos;

                        if (same_char(char_at(state->text, pos - 1), ch) == m
                          && !is_repeat_guarded(state, index, pos,
                          RE_STATUS_TAIL)) {
                            match = true;
                            break;
                        }
                    }
                    break;
                }
                case RE_OP_STRING:
                {
                    Py_ssize_t length;

                    length = (Py_ssize_t)test->value_count;

                    /* The tail is a string. We don't want to go off the end of
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 17120–17153. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L17120-L17153).

```c
            TRACE(("%s\n", re_op_text[op]))

            /* sstack: node slice_start slice_end text_pos ...
             *
             * bstack: [captures TRUE | FALSE] fuzzy_counts capture_change
             * sstack
             *
             * pstack: bstack
             */

            if (!drop_bstack(state))
                return RE_ERROR_MEMORY;
            if (!pop_sstack(state))
                return RE_ERROR_MEMORY;

            /* sstack: node slice_start slice_end text_pos
             *
             * bstack: [captures TRUE | FALSE] fuzzy_counts capture_change
             *
             * pstack: -
             */

            if (!ByteStack_pop_block(state, &state->sstack, (void*)&data_l,
              sizeof(data_l)))
                return RE_ERROR_MEMORY;

            state->text_pos = data_l.text_pos;
            state->slice_end = data_l.slice_end;
            state->slice_start = data_l.slice_start;
            lookaround = data_l.node;

            /* sstack: -
             *
             * bstack: [captures TRUE | FALSE] fuzzy_counts capture_change
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 17204–17215. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L17204-L17215).

```c
            TRACE(("%s %u\n", re_op_text[op], (unsigned int)index))

            /* We want to match the body. */
            rp_data = &state->repeats[index];

            /* Restore the repeat info. */
            rp_data->count = count;
            rp_data->start = start;
            rp_data->capture_change = capture_change;

            /* Record backtracking info in case the body fails to match. */
            if (!push_code(state, &state->bstack, index))
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 17246–17257. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L17246-L17257).

```c
            capture_change = data_mbt.capture_change;
            start = data_mbt.start;
            count = data_mbt.count;
            position = data_mbt.position;
            TRACE(("%s %u\n", re_op_text[op], (unsigned int)index))

            /* We want to match the tail. */
            rp_data = &state->repeats[index];

            /* Restore the repeat info. */
            rp_data->count = count;
            rp_data->start = start;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 17268–17277. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L17268-L17277).

```c
            /* bstack: index text_pos TAIL_START */

            /* Advance into the tail. */
            node = position.node;
            state->text_pos = position.text_pos;
            goto advance;
        }
        case RE_OP_REF_GROUP: /* Reference to a capture group. */
        case RE_OP_REF_GROUP_IGN: /* Reference to a capture group, ignoring case. */
        case RE_OP_REF_GROUP_IGN_REV: /* Reference to a capture group, backwards, ignoring case. */
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte
- `match_many_CHARACTER` in `regex-2026.9.29/src/_regex.c`, lines 3803–3858: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Forward pointer traversal starts at caller-provided text_pos and stops at caller limit or first mismatch; text_ptr=(Py_UCS1/2/4*)state->text + text_pos, not guaranteed start0/end. Width branches duplicate the same codepoint algorithm.
- `match_many_CHARACTER_REV` in `regex-2026.9.29/src/_regex.c`, lines 3987–4042: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Backward pointer traversal starts at caller-provided text_pos and reads text_ptr[-1] while decrementing toward caller limit or stopping at mismatch. Width branches duplicate the same codepoint algorithm.
- `simple_string_search` in `regex-2026.9.29/src/_regex.c`, lines 5231–5377: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Search outer loop advances text_ptr from caller text_pos; each candidate checks text_ptr[0], then text_ptr[s_pos] with s_pos reset to 1. Failed candidates restart comparison at the next position; overlapping input is reread.
- `fast_string_search` in `regex-2026.9.29/src/_regex.c`, lines 5846–5953: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Boyer-Moore reads text_ptr[last_pos], then scans text_ptr[pos] backward through a candidate. good_suffix_offset[pos] or bad_character_offset[ch & 0xFF] controls a non-unit jump to the next candidate; arbitrary codepoint offset view is needed for existing behavior.
- `string_search_fld` in `regex-2026.9.29/src/_regex.c`, lines 6637–6708: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Full-casefold search reads at text_pos, advances after consuming a folded character, but on mismatch increments start_pos and resets text_pos=start_pos, f_pos=0 and s_pos=0; input may be reread.
- `unicode_at_default_boundary` in `regex-2026.9.29/src/_regex.c`, lines 1531–1749: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Unicode word-boundary test reads left_pos=text_pos-1 and right_pos=text_pos, probes left_pos-1/right_pos+1, walks left over Extend/Format/ZWJ, and revisits the left side to count regional indicators.
- `unicode_at_grapheme_boundary` in `regex-2026.9.29/src/_regex.c`, lines 1786–1933: Opcode dispatch via match_many/try_match/search_start and encoding boundary function tables resolves to these same-file readers. Grapheme-boundary test probes text_pos-1/text_pos, then independently walks backward through Indic conjuncts, emoji Extend sequences and regional indicators; the same prefix can be revisited.

Available source context:
Omitted from `regex-2026.9.29/src/_regex.c`: lines 3815–3816, 3826–3830, 3840–3844. The original contextual region was lines 3803–3858.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 3999–4000, 4011–4014, 4025–4028. The original contextual region was lines 3987–4042.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 5244–5245, 5255–5268, 5278–5309, 5319–5350, 5369–5374. The original contextual region was lines 5231–5377.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 5867–5885, 5895–5900, 5910–5913, 5923–5933. The original contextual region was lines 5846–5953.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 6657–6664, 6674–6677, 6701–6705. The original contextual region was lines 6637–6708.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 1537–1538, 1548–1593, 1604–1645, 1655–1734. The original contextual region was lines 1531–1749.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 1793–1795, 1805–1806, 1816–1888, 1898–1899, 1911–1917. The original contextual region was lines 1786–1933.

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).
- [`match_many_CHARACTER`](#helper-003) (`regex-2026.9.29/src/_regex.c`, lines 3803–3814).
- [`match_many_CHARACTER`](#helper-004) (`regex-2026.9.29/src/_regex.c`, lines 3817–3825).
- [`match_many_CHARACTER`](#helper-005) (`regex-2026.9.29/src/_regex.c`, lines 3831–3839).
- [`match_many_CHARACTER`](#helper-006) (`regex-2026.9.29/src/_regex.c`, lines 3845–3858).
- [`match_many_CHARACTER_REV`](#helper-007) (`regex-2026.9.29/src/_regex.c`, lines 3987–3998).
- [`match_many_CHARACTER_REV`](#helper-008) (`regex-2026.9.29/src/_regex.c`, lines 4001–4010).
- [`match_many_CHARACTER_REV`](#helper-009) (`regex-2026.9.29/src/_regex.c`, lines 4015–4024).
- [`match_many_CHARACTER_REV`](#helper-010) (`regex-2026.9.29/src/_regex.c`, lines 4029–4042).
- [`simple_string_search`](#helper-011) (`regex-2026.9.29/src/_regex.c`, lines 5231–5243).
- [`simple_string_search`](#helper-012) (`regex-2026.9.29/src/_regex.c`, lines 5246–5254).
- [`simple_string_search`](#helper-013) (`regex-2026.9.29/src/_regex.c`, lines 5269–5277).
- [`simple_string_search`](#helper-014) (`regex-2026.9.29/src/_regex.c`, lines 5310–5318).
- [`simple_string_search`](#helper-015) (`regex-2026.9.29/src/_regex.c`, lines 5351–5368).
- [`simple_string_search`](#helper-016) (`regex-2026.9.29/src/_regex.c`, lines 5375–5377).
- [`fast_string_search`](#helper-017) (`regex-2026.9.29/src/_regex.c`, lines 5846–5866).
- [`fast_string_search`](#helper-018) (`regex-2026.9.29/src/_regex.c`, lines 5886–5894).
- [`fast_string_search`](#helper-019) (`regex-2026.9.29/src/_regex.c`, lines 5901–5909).
- [`fast_string_search`](#helper-020) (`regex-2026.9.29/src/_regex.c`, lines 5914–5922).
- [`fast_string_search`](#helper-021) (`regex-2026.9.29/src/_regex.c`, lines 5934–5953).
- [`string_search_fld`](#helper-022) (`regex-2026.9.29/src/_regex.c`, lines 6637–6656).
- [`string_search_fld`](#helper-023) (`regex-2026.9.29/src/_regex.c`, lines 6665–6673).
- [`string_search_fld`](#helper-024) (`regex-2026.9.29/src/_regex.c`, lines 6678–6700).
- [`string_search_fld`](#helper-025) (`regex-2026.9.29/src/_regex.c`, lines 6706–6708).
- [`unicode_at_default_boundary`](#helper-026) (`regex-2026.9.29/src/_regex.c`, lines 1531–1536).
- [`unicode_at_default_boundary`](#helper-027) (`regex-2026.9.29/src/_regex.c`, lines 1539–1547).
- [`unicode_at_default_boundary`](#helper-028) (`regex-2026.9.29/src/_regex.c`, lines 1594–1603).
- [`unicode_at_default_boundary`](#helper-029) (`regex-2026.9.29/src/_regex.c`, lines 1646–1654).
- [`unicode_at_default_boundary`](#helper-030) (`regex-2026.9.29/src/_regex.c`, lines 1735–1749).
- [`unicode_at_grapheme_boundary`](#helper-031) (`regex-2026.9.29/src/_regex.c`, lines 1786–1792).
- [`unicode_at_grapheme_boundary`](#helper-032) (`regex-2026.9.29/src/_regex.c`, lines 1796–1804).
- [`unicode_at_grapheme_boundary`](#helper-033) (`regex-2026.9.29/src/_regex.c`, lines 1807–1815).
- [`unicode_at_grapheme_boundary`](#helper-034) (`regex-2026.9.29/src/_regex.c`, lines 1889–1897).
- [`unicode_at_grapheme_boundary`](#helper-035) (`regex-2026.9.29/src/_regex.c`, lines 1900–1910).
- [`unicode_at_grapheme_boundary`](#helper-036) (`regex-2026.9.29/src/_regex.c`, lines 1918–1933).

<a id="case-084"></a>

## 84. `get_string`

**Classification:** B. **Subtypes:** mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** pointer acquisition.

Acquires PyUnicode_DATA/KIND/length and hands the representation to known callers. state_init_2 stores it for the B matcher; check_replacement_string and fold_case perform A scans. Thus handoff resolves to mixed B rather than unresolved C. This acquisition-only record is explicitly separated from actual-reader count.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Not a dereferencing function. Included as a resolved handoff; publish acquisition-excluded subtotal to avoid mistaking it for an extra semantic input scan.
- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 18226–18265. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18226-L18265).

### Read sites

- Site 1: lines 18239–18239; pointer handoff; index expression `pointer, codepoint length and element width`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 18230–18234, 18244–18262. The original contextual region was lines 18226–18265.

Archive member `regex-2026.9.29/src/_regex.c`, lines 18226–18229. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18226-L18229).

```c
Py_LOCAL_INLINE(bool) get_string(PyObject* string, RE_StringInfo* str_info) {
    /* Given a Python object, return a data pointer, a length (in characters),
     * and a character size. Return false if the object is not a string (or not
     * compatible).
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 18235–18243. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18235-L18243).

```c
        /* Unicode strings don't always support the buffer interface. */
        if (PyUnicode_READY(string) == -1)
            return false;

        str_info->characters = (void*)PyUnicode_DATA(string);
        str_info->length = PyUnicode_GetLength(string);
        str_info->charsize = PyUnicode_KIND(string);
        str_info->is_unicode = true;
        str_info->should_release = false;
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 18263–18265. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18263-L18265).

```c

    return true;
}
```

### Callee analysis

- `state_init_2` in `regex-2026.9.29/src/_regex.c`, lines 18282–18577: Call chains receive str_info.characters from get_string; state_init wrapper forwards str_info to state_init_2. B tail probes; representation cached for engine
- `check_replacement_string` in `regex-2026.9.29/src/_regex.c`, lines 19884–19918: Call chains receive str_info.characters from get_string; state_init wrapper forwards str_info to state_init_2. A forward with early exit
- `fold_case` in `regex-2026.9.29/src/_regex.c`, lines 26209–26357: Call chains receive str_info.characters from get_string; state_init wrapper forwards str_info to state_init_2. A mutually exclusive full forward passes

Available source context:
Omitted from `regex-2026.9.29/src/_regex.c`: lines 18286–18290, 18300–18363, 18373–18406, 18416–18461, 18478–18558, 18569–18574. The original contextual region was lines 18282–18577.
Omitted from `regex-2026.9.29/src/_regex.c`: lines 26216–26230, 26246–26315, 26325–26329, 26342–26354. The original contextual region was lines 26209–26357.

- [`state_init_2`](#helper-037) (`regex-2026.9.29/src/_regex.c`, lines 18282–18285).
- [`state_init_2`](#helper-038) (`regex-2026.9.29/src/_regex.c`, lines 18291–18299).
- [`state_init_2`](#helper-039) (`regex-2026.9.29/src/_regex.c`, lines 18364–18372).
- [`state_init_2`](#helper-040) (`regex-2026.9.29/src/_regex.c`, lines 18407–18415).
- [`state_init_2`](#helper-041) (`regex-2026.9.29/src/_regex.c`, lines 18462–18477).
- [`state_init_2`](#helper-042) (`regex-2026.9.29/src/_regex.c`, lines 18559–18568).
- [`state_init_2`](#helper-043) (`regex-2026.9.29/src/_regex.c`, lines 18575–18577).
- [`check_replacement_string`](#helper-044) (`regex-2026.9.29/src/_regex.c`, lines 19884–19918).
- [`fold_case`](#helper-045) (`regex-2026.9.29/src/_regex.c`, lines 26209–26215).
- [`fold_case`](#helper-046) (`regex-2026.9.29/src/_regex.c`, lines 26231–26245).
- [`fold_case`](#helper-047) (`regex-2026.9.29/src/_regex.c`, lines 26316–26324).
- [`fold_case`](#helper-048) (`regex-2026.9.29/src/_regex.c`, lines 26330–26341).
- [`fold_case`](#helper-049) (`regex-2026.9.29/src/_regex.c`, lines 26355–26357).

<a id="case-085"></a>

## 85. `state_init_2`

**Classification:** B. **Subtypes:** caller-provided start or range, a subset starting after position zero, lookahead or lookbehind. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

Stores the DATA-derived representation in state->text, clamps caller start/end, chooses initial forward/reverse position, and immediately reads end-1 plus optional preceding CR (end-2) to locate final line separators. These are tail probes, not full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Unicode branch: one Py_UCS1/2/4 element is one Python codepoint; all positions/lengths are codepoints. Bytes branch uses one byte per position. Surrogates are not normalized and embedded NUL does not terminate these length-bounded reads.

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

- Pointer is borrowed from immutable Unicode, retained in RE_State with a strong string reference (18534-18535); matching may be multithreaded (18540-18552). Current PyUnicode_DATA lifetime is stable. No repeated FSR getter is present; a proposed evictable materialization must preserve this long-lived pointer contract.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/fc/f2/af1da9d3ceed77bfcdce40427d49ba0be94e4fe84245e3bfef68c10e75b6/regex-2026.9.29.tar.gz). Archive SHA-256: `8b5fcc4771732191b2b7d1dd68d8f0353f47f8d90b6150f6dce58bf1112442cb`.

**Function source:** `regex-2026.9.29/src/_regex.c`, lines 18282–18577. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`.

[Verified immutable function link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18282-L18577).

### Read sites

- Site 1: lines 18466–18466; codepoint read via helper; index expression `final_pos`. Exact read expression; access pattern explained at function level.
- Site 2: lines 18474–18474; codepoint read via helper; index expression `final_pos`. Exact read expression; access pattern explained at function level.

### Contextual source excerpts

Omitted from `regex-2026.9.29/src/_regex.c`: lines 18286–18461, 18479–18574. The original contextual region was lines 18282–18577.

Archive member `regex-2026.9.29/src/_regex.c`, lines 18282–18285. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18282-L18285).

```c
Py_LOCAL_INLINE(bool) state_init_2(RE_State* state, PatternObject* pattern,
  PyObject* string, RE_StringInfo* str_info, Py_ssize_t start, Py_ssize_t end,
  bool overlapped, int concurrent, bool partial, bool use_lock, bool
  visible_captures, bool match_all, Py_ssize_t timeout) {
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 18462–18478. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18462-L18478).

```c
    final_pos = state->text_end - 1;
    if (final_pos >= 0) {
        Py_UCS4 ch;

        ch = state->char_at(state->text, final_pos);
        if (ch == 0x0A) {
            /* The string ends with LF. */
            state->final_newline = final_pos;
            state->final_line_sep = final_pos;

            /* Does the string end with CR/LF? */
            --final_pos;
            if (final_pos >= 0 && state->char_at(state->text, final_pos) ==
              0x0D)
                state->final_line_sep = final_pos;
        } else {
            /* The string doesn't end with LF, but it could be another kind of
```

Archive member `regex-2026.9.29/src/_regex.c`, lines 18575–18577. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18575-L18577).

```c
    state->fuzzy_guards = NULL;
    return false;
}
```

### Callee analysis

- `bytes{1,2,4}_char_at` in `regex-2026.9.29/src/_regex.c`, lines 763–795: state_init_2 lines18409-18424 chooses these aliases by charsize; each dereferences ((Py_UCS1/2/4*)text)[pos]. caller index denotes codepoint, not UTF-8 byte

Available source context:

- [`bytes{1,2,4}_char_at`](#helper-001) (`regex-2026.9.29/src/_regex.c`, lines 763–795).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `bytes{1,2,4}_char_at`

Archive member `regex-2026.9.29/src/_regex.c`, lines 763–795. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L763-L795).

```c
static Py_UCS4 bytes1_char_at(void* text, Py_ssize_t pos) {
    return *((Py_UCS1*)text + pos);
}

/* Sets a character at a position assuming 1 byte per character. */
static void bytes1_set_char_at(void* text, Py_ssize_t pos, Py_UCS4 ch) {
    *((Py_UCS1*)text + pos) = (Py_UCS1)ch;
}

/* Gets a pointer to a position assuming 1 byte per character. */
static void* bytes1_point_to(void* text, Py_ssize_t pos) {
    return (Py_UCS1*)text + pos;
}

/* Gets a character at a position assuming 2 bytes per character. */
static Py_UCS4 bytes2_char_at(void* text, Py_ssize_t pos) {
    return *((Py_UCS2*)text + pos);
}

/* Sets a character at a position assuming 2 bytes per character. */
static void bytes2_set_char_at(void* text, Py_ssize_t pos, Py_UCS4 ch) {
    *((Py_UCS2*)text + pos) = (Py_UCS2)ch;
}

/* Gets a pointer to a position assuming 2 bytes per character. */
static void* bytes2_point_to(void* text, Py_ssize_t pos) {
    return (Py_UCS2*)text + pos;
}

/* Gets a character at a position assuming 4 bytes per character. */
static Py_UCS4 bytes4_char_at(void* text, Py_ssize_t pos) {
    return *((Py_UCS4*)text + pos);
}
```

<a id="helper-002"></a>

### 2. `folded_char_at`

Archive member `regex-2026.9.29/src/_regex.c`, lines 10018–10030. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L10018-L10030).

```c
Py_LOCAL_INLINE(Py_UCS4) folded_char_at(RE_State* state, Py_ssize_t pos, int
  folded_pos) {
    int (*full_case_fold)(RE_LocaleInfo* locale_info, Py_UCS4 ch, Py_UCS4*
      folded);
    Py_UCS4 folded[RE_MAX_FOLDED];

    full_case_fold = state->encoding->full_case_fold;

    full_case_fold(state->locale_info, state->char_at(state->text, pos),
      folded);

    return folded[folded_pos];
}
```

<a id="helper-003"></a>

### 3. `match_many_CHARACTER`

Archive member `regex-2026.9.29/src/_regex.c`, lines 3803–3814. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3803-L3814).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_CHARACTER(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    Py_UCS4 ch;

    text = state->text;
    match = node->match == match;
    ch = node->values[0];

    switch (state->charsize) {
    case 1:
    {
```

<a id="helper-004"></a>

### 4. `match_many_CHARACTER`

Archive member `regex-2026.9.29/src/_regex.c`, lines 3817–3825. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3817-L3825).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] == ch) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
```

<a id="helper-005"></a>

### 5. `match_many_CHARACTER`

Archive member `regex-2026.9.29/src/_regex.c`, lines 3831–3839. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3831-L3839).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] == ch) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
```

<a id="helper-006"></a>

### 6. `match_many_CHARACTER`

Archive member `regex-2026.9.29/src/_regex.c`, lines 3845–3858. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3845-L3858).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr < limit_ptr && (text_ptr[0] == ch) == match)
            ++text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
    }
    }

    return text_pos;
}
```

<a id="helper-007"></a>

### 7. `match_many_CHARACTER_REV`

Archive member `regex-2026.9.29/src/_regex.c`, lines 3987–3998. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L3987-L3998).

```c
Py_LOCAL_INLINE(Py_ssize_t) match_many_CHARACTER_REV(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool match) {
    void* text;
    Py_UCS4 ch;

    text = state->text;
    match = node->match == match;
    ch = node->values[0];

    switch (state->charsize) {
    case 1:
    {
```

<a id="helper-008"></a>

### 8. `match_many_CHARACTER_REV`

Archive member `regex-2026.9.29/src/_regex.c`, lines 4001–4010. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4001-L4010).

```c

        text_ptr = (Py_UCS1*)text + text_pos;
        limit_ptr = (Py_UCS1*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] == ch) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS1*)text;
        break;
    }
```

<a id="helper-009"></a>

### 9. `match_many_CHARACTER_REV`

Archive member `regex-2026.9.29/src/_regex.c`, lines 4015–4024. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4015-L4024).

```c

        text_ptr = (Py_UCS2*)text + text_pos;
        limit_ptr = (Py_UCS2*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] == ch) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS2*)text;
        break;
    }
```

<a id="helper-010"></a>

### 10. `match_many_CHARACTER_REV`

Archive member `regex-2026.9.29/src/_regex.c`, lines 4029–4042. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L4029-L4042).

```c

        text_ptr = (Py_UCS4*)text + text_pos;
        limit_ptr = (Py_UCS4*)text + limit;

        while (text_ptr > limit_ptr && (text_ptr[-1] == ch) == match)
            --text_ptr;

        text_pos = text_ptr - (Py_UCS4*)text;
        break;
    }
    }

    return text_pos;
}
```

<a id="helper-011"></a>

### 11. `simple_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5231–5243. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5231-L5243).

```c
Py_LOCAL_INLINE(Py_ssize_t) simple_string_search(RE_State* state, RE_Node*
  node, Py_ssize_t text_pos, Py_ssize_t limit, bool* is_partial) {
    Py_ssize_t length;
    RE_CODE* values;
    Py_UCS4 check_char;

    length = (Py_ssize_t)node->value_count;
    values = node->values;
    check_char = values[0];

    *is_partial = false;

    switch (state->charsize) {
```

<a id="helper-012"></a>

### 12. `simple_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5246–5254. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5246-L5254).

```c
        Py_UCS1* text = (Py_UCS1*)state->text;
        Py_UCS1* text_ptr = text + text_pos;
        Py_UCS1* limit_ptr = text + limit;

        while (text_ptr < limit_ptr) {
            if (text_ptr[0] == check_char) {
                Py_ssize_t s_pos;

                s_pos = 1;
```

<a id="helper-013"></a>

### 13. `simple_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5269–5277. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5269-L5277).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[s_pos], values[s_pos]))
                        break;

                    ++s_pos;
                }
```

<a id="helper-014"></a>

### 14. `simple_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5310–5318. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5310-L5318).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[s_pos], values[s_pos]))
                        break;

                    ++s_pos;
                }
```

<a id="helper-015"></a>

### 15. `simple_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5351–5368. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5351-L5368).

```c
                        return -1;

                    }

                    if (!same_char(text_ptr[s_pos], values[s_pos]))
                        break;

                    ++s_pos;
                }
            }

            ++text_ptr;
        }
        text_pos = text_ptr - text;
        break;
    }
    }

```

<a id="helper-016"></a>

### 16. `simple_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5375–5377. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5375-L5377).

```c

    return -1;
}
```

<a id="helper-017"></a>

### 17. `fast_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5846–5866. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5846-L5866).

```c
Py_LOCAL_INLINE(Py_ssize_t) fast_string_search(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit) {
    void* text;
    Py_ssize_t length;
    RE_CODE* values;
    Py_ssize_t* bad_character_offset;
    Py_ssize_t* good_suffix_offset;
    Py_ssize_t last_pos;
    Py_UCS4 check_char;

    text = state->text;
    length = (Py_ssize_t)node->value_count;
    values = node->values;
    good_suffix_offset = node->string.good_suffix_offset;
    bad_character_offset = node->string.bad_character_offset;
    last_pos = length - 1;
    check_char = values[last_pos];
    limit -= length;

    switch (state->charsize) {
    case 1:
```

<a id="helper-018"></a>

### 18. `fast_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5886–5894. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5886-L5894).

```c
                    return text_ptr - (Py_UCS1*)text;

                text_ptr += good_suffix_offset[pos];
            } else
                text_ptr += bad_character_offset[ch & 0xFF];
        }
        break;
    }
    case 2:
```

<a id="helper-019"></a>

### 19. `fast_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5901–5909. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5901-L5909).

```c

        while (text_ptr <= limit_ptr) {
            Py_UCS4 ch;

            ch = text_ptr[last_pos];
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = last_pos - 1;
```

<a id="helper-020"></a>

### 20. `fast_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5914–5922. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5914-L5922).

```c
                    return text_ptr - (Py_UCS2*)text;

                text_ptr += good_suffix_offset[pos];
            } else
                text_ptr += bad_character_offset[ch & 0xFF];
        }
        break;
    }
    case 4:
```

<a id="helper-021"></a>

### 21. `fast_string_search`

Archive member `regex-2026.9.29/src/_regex.c`, lines 5934–5953. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L5934-L5953).

```c
            if (ch == check_char) {
                Py_ssize_t pos;

                pos = last_pos - 1;
                while (pos >= 0 && same_char(text_ptr[pos], values[pos]))
                    --pos;

                if (pos < 0)
                    return text_ptr - (Py_UCS4*)text;

                text_ptr += good_suffix_offset[pos];
            } else
                text_ptr += bad_character_offset[ch & 0xFF];
        }
        break;
    }
    }

    return -1;
}
```

<a id="helper-022"></a>

### 22. `string_search_fld`

Archive member `regex-2026.9.29/src/_regex.c`, lines 6637–6656. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6637-L6656).

```c
Py_LOCAL_INLINE(Py_ssize_t) string_search_fld(RE_State* state, RE_Node* node,
  Py_ssize_t text_pos, Py_ssize_t limit, Py_ssize_t* new_pos, bool* is_partial)
  {
    RE_EncodingTable* encoding;
    RE_LocaleInfo* locale_info;
    int (*full_case_fold)(RE_LocaleInfo* locale_info, Py_UCS4 ch, Py_UCS4*
      folded);
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    void* text;
    RE_CODE* values;
    Py_ssize_t start_pos;
    int f_pos;
    int folded_len;
    Py_ssize_t length;
    Py_ssize_t s_pos;
    Py_UCS4 folded[RE_MAX_FOLDED];

    encoding = state->encoding;
    locale_info = state->locale_info;
    full_case_fold = encoding->full_case_fold;
```

<a id="helper-023"></a>

### 23. `string_search_fld`

Archive member `regex-2026.9.29/src/_regex.c`, lines 6665–6673. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6665-L6673).

```c
    s_pos = 0;

    *is_partial = false;

    while (s_pos < length || f_pos < folded_len) {
        if (f_pos >= folded_len) {
            /* Fetch and casefold another character. */
            if (text_pos >= limit) {
                if (text_pos >= state->text_end && state->partial_side ==
```

<a id="helper-024"></a>

### 24. `string_search_fld`

Archive member `regex-2026.9.29/src/_regex.c`, lines 6678–6700. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6678-L6700).

```c

                return -1;
            }

            folded_len = full_case_fold(locale_info, char_at(text, text_pos),
              folded);
            f_pos = 0;
        }

        if (s_pos < length && same_char_ign_turkic(encoding, locale_info,
          values[s_pos], folded[f_pos])) {
            ++s_pos;
            ++f_pos;

            if (f_pos >= folded_len)
                ++text_pos;
        } else {
            ++start_pos;
            text_pos = start_pos;
            f_pos = 0;
            folded_len = 0;
            s_pos = 0;
        }
```

<a id="helper-025"></a>

### 25. `string_search_fld`

Archive member `regex-2026.9.29/src/_regex.c`, lines 6706–6708. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L6706-L6708).

```c

    return start_pos;
}
```

<a id="helper-026"></a>

### 26. `unicode_at_default_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1531–1536. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1531-L1536).

```c
static bool unicode_at_default_boundary(RE_State* state, Py_ssize_t text_pos) {
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    Py_ssize_t left_pos;
    Py_ssize_t right_pos;
    Py_UCS4 left_char;
    Py_UCS4 right_char;
```

<a id="helper-027"></a>

### 27. `unicode_at_default_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1539–1547. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1539-L1547).

```c
    Py_ssize_t pos;

    /* Break at the start and end of text, unless the text is empty. */
    /* WB1 and WB2 */
    if (text_pos <= state->text_start || text_pos >= state->text_end)
        return state->text_end > state->text_start;

    /* In this function, left_pos is inclusive, i.e. it's the index of the
     * character.
```

<a id="helper-028"></a>

### 28. `unicode_at_default_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1594–1603. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1594-L1603).

```c
    while (left_prop == RE_WBREAK_EXTEND || left_prop == RE_WBREAK_FORMAT ||
      left_prop == RE_WBREAK_ZWJ) {
        if (left_pos <= state->text_start)
            return false;
        --left_pos;
        left_char = char_at(state->text, left_pos);
        left_prop = re_get_word_break(left_char);
    }

    /* Do not break between most letters. */
```

<a id="helper-029"></a>

### 29. `unicode_at_default_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1646–1654. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1646-L1654).

```c
    if (right_pos + 1 < state->text_end) {
        Py_UCS4 right_right_char;
        uint32_t right_right_prop;

        right_right_char = char_at(state->text, right_pos + 1);
        right_right_prop = re_get_word_break(right_right_char);

        if (left_prop == RE_WBREAK_HEBREWLETTER && right_prop ==
          RE_WBREAK_DOUBLEQUOTE && right_right_prop == RE_WBREAK_HEBREWLETTER)
```

<a id="helper-030"></a>

### 30. `unicode_at_default_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1735–1749. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1735-L1749).

```c
     */
    /* WB15 and WB16 */
    pos = left_pos;

    while (pos >= state->text_start && re_get_word_break(char_at(state->text, pos)) ==
      RE_WBREAK_REGIONALINDICATOR)
        --pos;

    if ((left_pos - pos) % 2 == 1)
        return false;

    /* Otherwise, break everywhere (including around ideographs). */
    /* WB999 */
    return true;
}
```

<a id="helper-031"></a>

### 31. `unicode_at_grapheme_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1786–1792. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1786-L1792).

```c
static bool unicode_at_grapheme_boundary(RE_State* state, Py_ssize_t text_pos)
  {
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    Py_ssize_t left_pos;
    Py_ssize_t right_pos;
    Py_UCS4 left_char;
    Py_UCS4 right_char;
```

<a id="helper-032"></a>

### 32. `unicode_at_grapheme_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1796–1804. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1796-L1804).

```c
    Py_ssize_t pos;

    /* Break at the start and end of text, unless the text is empty. */
    /* GB1 and GB2 */
    if (text_pos <= state->text_start || text_pos >= state->text_end)
        return state->text_end > state->text_start;

    /* In this function, left_pos is inclusive, i.e. it's the index of the
     * character.
```

<a id="helper-033"></a>

### 33. `unicode_at_grapheme_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1807–1815. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1807-L1815).

```c

    left_pos = text_pos - 1;
    right_pos = text_pos;
    left_char = char_at(state->text, left_pos);
    right_char = char_at(state->text, right_pos);

    /* Do not break between a CR and LF. Otherwise, break before and after
     * controls.
     */
```

<a id="helper-034"></a>

### 34. `unicode_at_grapheme_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1889–1897. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1889-L1897).

```c
            default:
                goto end_GB9c;
            }

            --pos;
        } while (pos >= state->text_start);
    }

end_GB9c:
```

<a id="helper-035"></a>

### 35. `unicode_at_grapheme_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1900–1910. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1900-L1910).

```c
    if (left_prop == RE_GBREAK_ZWJ && re_get_extended_pictographic(right_char))
      {
        pos = left_pos - 1;

        while (pos >= state->text_start && re_get_grapheme_cluster_break(char_at(state->text,
          pos)) == RE_GBREAK_EXTEND)
            --pos;

        if (pos >= state->text_start && re_get_extended_pictographic(char_at(state->text,
          pos)))
            return false;
```

<a id="helper-036"></a>

### 36. `unicode_at_grapheme_boundary`

Archive member `regex-2026.9.29/src/_regex.c`, lines 1918–1933. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L1918-L1933).

```c
    /* GB12 and GB13 */
    if (right_prop == RE_GBREAK_REGIONALINDICATOR) {
        pos = left_pos;

        while (pos >= state->text_start && re_get_grapheme_cluster_break(char_at(state->text,
          pos)) == RE_GBREAK_REGIONALINDICATOR)
            --pos;

        if ((left_pos - pos) % 2 == 1)
            return false;
    }

    /* Otherwise, break everywhere. */
    /* GB999 */
    return true;
}
```

<a id="helper-037"></a>

### 37. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18282–18285. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18282-L18285).

```c
Py_LOCAL_INLINE(bool) state_init_2(RE_State* state, PatternObject* pattern,
  PyObject* string, RE_StringInfo* str_info, Py_ssize_t start, Py_ssize_t end,
  bool overlapped, int concurrent, bool partial, bool use_lock, bool
  visible_captures, bool match_all, Py_ssize_t timeout) {
```

<a id="helper-038"></a>

### 38. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18291–18299. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18291-L18299).

```c
    ByteStack_init(state, &state->sstack);
    ByteStack_init(state, &state->bstack);
    ByteStack_init(state, &state->pstack);

    /* We might already have some cached storage we can use for bstack. */
    #if defined(Py_GIL_DISABLED)
    PyMutex_Lock(&pattern->mutex);
    #endif

```

<a id="helper-039"></a>

### 39. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18364–18372. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18364-L18372).

```c
                if (!captures) {
                    size_t i;

                    for (i = 0; i < g; i++)
                        re_dealloc(state->groups[i].captures);

                    goto error;
                }

```

<a id="helper-040"></a>

### 40. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18407–18415. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18407-L18415).

```c
        state->view = str_info->view;

    switch (state->charsize) {
    case 1:
        state->char_at = bytes1_char_at;
        state->set_char_at = bytes1_set_char_at;
        state->point_to = bytes1_point_to;
        break;
    case 2:
```

<a id="helper-041"></a>

### 41. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18462–18477. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18462-L18477).

```c
    final_pos = state->text_end - 1;
    if (final_pos >= 0) {
        Py_UCS4 ch;

        ch = state->char_at(state->text, final_pos);
        if (ch == 0x0A) {
            /* The string ends with LF. */
            state->final_newline = final_pos;
            state->final_line_sep = final_pos;

            /* Does the string end with CR/LF? */
            --final_pos;
            if (final_pos >= 0 && state->char_at(state->text, final_pos) ==
              0x0D)
                state->final_line_sep = final_pos;
        } else {
```

<a id="helper-042"></a>

### 42. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18559–18568. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18559-L18568).

```c
     */
    if (state->is_multithreaded && use_lock)
        state->lock = PyThread_allocate_lock();

    for (p = 0; p < MAX_SEARCH_POSITIONS; p++)
        state->search_positions[p].start_pos = -1;

    return true;

error:
```

<a id="helper-043"></a>

### 43. `state_init_2`

Archive member `regex-2026.9.29/src/_regex.c`, lines 18575–18577. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L18575-L18577).

```c
    state->fuzzy_guards = NULL;
    return false;
}
```

<a id="helper-044"></a>

### 44. `check_replacement_string`

Archive member `regex-2026.9.29/src/_regex.c`, lines 19884–19918. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L19884-L19918).

```c
Py_LOCAL_INLINE(Py_ssize_t) check_replacement_string(PyObject* str_replacement,
  unsigned char special_char) {
    RE_StringInfo str_info;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    Py_ssize_t pos;

    if (!get_string(str_replacement, &str_info))
        return -1;

    switch (str_info.charsize) {
    case 1:
        char_at = bytes1_char_at;
        break;
    case 2:
        char_at = bytes2_char_at;
        break;
    case 4:
        char_at = bytes4_char_at;
        break;
    default:
        release_buffer(&str_info);
        return -1;
    }

    for (pos = 0; pos < str_info.length; pos++) {
        if (char_at(str_info.characters, pos) == special_char) {
            release_buffer(&str_info);
            return -1;
        }
    }

    release_buffer(&str_info);

    return str_info.length;
}
```

<a id="helper-045"></a>

### 45. `fold_case`

Archive member `regex-2026.9.29/src/_regex.c`, lines 26209–26215. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26209-L26215).

```c
static PyObject* fold_case(PyObject* self_, PyObject* args) {
    RE_StringInfo str_info;
    Py_UCS4 (*char_at)(void* text, Py_ssize_t pos);
    RE_EncodingTable* encoding;
    RE_LocaleInfo locale_info;
    Py_ssize_t folded_charsize;
    void (*set_char_at)(void* text, Py_ssize_t pos, Py_UCS4 ch);
```

<a id="helper-046"></a>

### 46. `fold_case`

Archive member `regex-2026.9.29/src/_regex.c`, lines 26231–26245. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26231-L26245).

```c
    /* Get the string. */
    if (!get_string(string, &str_info))
        return NULL;

    /* Get the function for reading from the original string. */
    switch (str_info.charsize) {
    case 1:
        char_at = bytes1_char_at;
        break;
    case 2:
        char_at = bytes2_char_at;
        break;
    case 4:
        char_at = bytes4_char_at;
        break;
```

<a id="helper-047"></a>

### 47. `fold_case`

Archive member `regex-2026.9.29/src/_regex.c`, lines 26316–26324. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26316-L26324).

```c
        for (i = 0; i < str_info.length; i++) {
            int count;
            int j;

            count = full_case_fold(&locale_info, char_at(str_info.characters,
              i), codepoints);
            for (j = 0; j < count; j++)
                set_char_at(folded, folded_len + j, codepoints[j]);

```

<a id="helper-048"></a>

### 48. `fold_case`

Archive member `regex-2026.9.29/src/_regex.c`, lines 26330–26341. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26330-L26341).

```c
        Py_ssize_t i;

        simple_case_fold = encoding->simple_case_fold;

        for (i = 0; i < str_info.length; i++) {
            Py_UCS4 ch;

            ch = simple_case_fold(&locale_info, char_at(str_info.characters,
              i));
            set_char_at(folded, i, ch);
        }

```

<a id="helper-049"></a>

### 49. `fold_case`

Archive member `regex-2026.9.29/src/_regex.c`, lines 26355–26357. Member SHA-256: `5a09aba56ea3de42138cf0e7c00b65a5e85ee97f31bd6829c7aba376030a9a11`. [Verified immutable source link](https://github.com/mrabarnett/mrab-regex/blob/0e8cb0596ba6572c66e5d153a1d7c901b381e15e/src/_regex.c#L26355-L26357).

```c

    return result;
}
```
