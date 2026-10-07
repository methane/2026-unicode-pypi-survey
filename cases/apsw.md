# apsw — non-simple Unicode reads

[All packages](README.md)

Version: 3.53.4.0. **18 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`formatsqlvalue`](#case-001)
- [`grapheme_next_break`](#case-002)
- [`word_next_break`](#case-003)
- [`sentence_next_break`](#case-004)
- [`line_next_hard_break`](#case-005)
- [`line_next_break`](#case-006)
- [`category_name`](#case-007)
- [`get_category_category`](#case-008)
- [`has_category`](#case-009)
- [`casefold_ascii`](#case-010)
- [`casefold`](#case-011)
- [`strip`](#case-012)
- [`text_width`](#case-013)
- [`grapheme_find`](#case-014)
- [`grapheme_length`](#case-015)
- [`grapheme_substr`](#case-016)
- [`version_added`](#case-017)
- [`codepoint_name`](#case-018)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `formatsqlvalue`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

First full pass computes quoted SQL size; non-simple path restarts at zero for second full pass. Simple path bulk-copies source after first pass.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Explicit embedded NUL handling emits SQL concatenation with X'00'; surrogate codepoints copied, not UTF8 strict encoding. Output DATA at1535/1588 not read.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/apsw.c`, lines 1472–1605. Member SHA-256: `a5587241784d74d8ed58565501ba8d32f1b1935e27fb45379cd034dd8cbeed71`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/apsw.c#L1472-L1605).

### Read sites

- Site 1: lines 1509–1529; forward pass; index expression `pos=0..input_length-1`. Sizing/escaping assessment.
- Site 2: lines 1540–1543; bulk copy; index expression `value source_start0 length input_length`. CopyCharacters fast path.
- Site 3: lines 1548–1564; second pass; index expression `pos=0..input_length-1`. Restarts at zero to emit escaped SQL.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/apsw.c`: lines 1499–1504, 1516–1535. The original contextual region was lines 1495–1565.

Archive member `apsw-3.53.4.0/src/apsw.c`, lines 1495–1498. Member SHA-256: `a5587241784d74d8ed58565501ba8d32f1b1935e27fb45379cd034dd8cbeed71`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/apsw.c#L1495-L1498).

```c
  /* Unicode */
  if (PyUnicode_Check(value))
  {
    Py_ssize_t needed_chars = 2; /* leading and trailing quote */
```

Archive member `apsw-3.53.4.0/src/apsw.c`, lines 1505–1515. Member SHA-256: `a5587241784d74d8ed58565501ba8d32f1b1935e27fb45379cd034dd8cbeed71`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/apsw.c#L1505-L1515).

```c

    PyObject *strres;
    void *output_data;

    for (pos = 0; pos < input_length; pos++)
    {
      switch (PyUnicode_READ(input_kind, input_data, pos))
      {
      case '\'':
        needed_chars += 2;
        simple = 0;
```

Archive member `apsw-3.53.4.0/src/apsw.c`, lines 1536–1565. Member SHA-256: `a5587241784d74d8ed58565501ba8d32f1b1935e27fb45379cd034dd8cbeed71`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/apsw.c#L1536-L1565).

```c

    PyUnicode_WRITE(output_kind, output_data, 0, '\'');
    PyUnicode_WRITE(output_kind, output_data, needed_chars - 1, '\'');

    if (simple)
    {
      PyUnicode_CopyCharacters(strres, 1, value, 0, input_length);
      return strres;
    }

    outpos = 1;

    for (pos = 0; pos < input_length; pos++)
    {
      switch (ch = PyUnicode_READ(input_kind, input_data, pos))
      {
      case 0: {
        int i;
        for (i = 0; i < 11; i++)
          PyUnicode_WRITE(output_kind, output_data, outpos++, "'||X'00'||'"[i]);
      }
      break;
      case '\'':
        PyUnicode_WRITE(output_kind, output_data, outpos++, ch);
        /* fall through */
      default:
        PyUnicode_WRITE(output_kind, output_data, outpos++, ch);
      }
    }
    return strres;
```


<a id="case-002"></a>

## 2. `grapheme_next_break`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller-provided codepoint offset; TEXT_INIT fetches lookahead and it_advance reads pos+1; stops at selected boundary. Speculative transactions restore saved pos/category state and may reread later.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 280–394. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L280-L394).

### Read sites

- Site 1: lines 280–394; macro iterator; index expression `offset; ++it.pos; saved.pos rollback`. Uses TEXT_INIT/it_advance helpers; categories of current and lookahead compared.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 292–308, 318–341, 351–355, 365–377, 387–391. The original contextual region was lines 280–394.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 280–291. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L280-L291).

```c
grapheme_next_break(PyObject *text, Py_ssize_t offset)
{
  assert(PyUnicode_Check(text));
  assert(offset >= 0);

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

#define cat_func grapheme_category
  TextIterator it = TEXT_INIT;
  int it_has_accepted = 0;
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 309–317. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L309-L317).

```c
    if (it.curchar & (GC_Control | GC_CR | GC_LF))
    {
      /* GB5: break before if any chars are accepted */
      if (it_has_accepted)
        it.pos--;
      break;
    }

    /* GB6 */
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 342–350. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L342-L350).

```c
      it_advance();
      while (it.lookahead & (GC_InCB_Extend | GC_InCB_Linker))
      {
        seen_linker = seen_linker || it.lookahead & GC_InCB_Linker;
        it_advance();
      }
      if (seen_linker && it.lookahead & GC_InCB_Consonant)
      {
        it_commit();
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 356–364. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L356-L364).

```c
    /* GB11 */
    if (it.curchar & GC_Extended_Pictographic && it.lookahead & (GC_Extend | GC_ZWJ))
    {
      it_begin();
      while (it.lookahead & GC_Extend)
        it_advance();
      if (it.lookahead & GC_ZWJ)
      {
        it_advance();
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 378–386. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L378-L386).

```c

    /* GB12 */
    if (it.curchar & GC_Regional_Indicator && it.lookahead & GC_Regional_Indicator)
    {
      it_advance();
      /* reapply GB9 */
      if (it.lookahead & (GC_Extend | GC_ZWJ | GC_InCB_Extend))
        continue;
      break;
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 392–394. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L392-L394).

```c

  return it.pos;
}
```

### Callee analysis

- `TEXT_INIT / it_advance / it_rollback` in `apsw-3.53.4.0/src/unicode.c`, lines 185–234: Unicode READ at offset/pos; rollback restores saved position. B nonzero-start/lookahead/backtracking

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 197–207. The original contextual region was lines 185–234.

- [`TEXT_INIT / it_advance / it_rollback`](#helper-001) (`apsw-3.53.4.0/src/unicode.c`, lines 185–196).
- [`TEXT_INIT / it_advance / it_rollback`](#helper-002) (`apsw-3.53.4.0/src/unicode.c`, lines 208–234).

<a id="case-003"></a>

## 3. `word_next_break`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller-provided codepoint offset; TEXT_INIT fetches lookahead and it_advance reads pos+1; stops at selected boundary. Speculative transactions restore saved pos/category state and may reread later.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 412–590. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L412-L590).

### Read sites

- Site 1: lines 412–590; macro iterator; index expression `offset; ++it.pos; saved.pos rollback`. Uses TEXT_INIT/it_advance helpers; categories of current and lookahead compared.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 433–437, 447–452, 462–494, 507–576, 586–587. The original contextual region was lines 412–590.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 412–432. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L412-L432).

```c
word_next_break(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  PyObject *text = NULL;
  Py_ssize_t offset;

  ARG_PROLOG(2, break_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(offset, text);
  ARG_EPILOG(NULL, "word_next_break(text: str, offset: int)", );

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

#undef cat_func
#define cat_func word_category
  TextIterator it = TEXT_INIT;
  int it_has_accepted = 0;

  /* From spec */
#define AHLetter (WC_ALetter | WC_Hebrew_Letter)
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 438–446. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L438-L446).

```c
  while (it.pos < text_end)
  {
  loop_top:
    it_has_accepted = it.pos > offset;
    it_advance();

    /* WB3 */
    if (it.curchar & WC_CR && it.lookahead & WC_LF)
    {
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 453–461. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L453-L461).

```c
    {
      /* break before if any chars are accepted */
      if (it_has_accepted)
      {
        it.pos--;
        break;
      }
      /* else break after */
      break;
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 495–506. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L495-L506).

```c
          if (it.lookahead & WC_Extended_Pictographic)
            goto loop_top;
        }
        else
          it_advance();
      }
      /* ignore the extending chars */
      it.curchar = saved_char;
    }

    /* WB5 */
    if (it.curchar & AHLetter && it.lookahead & AHLetter)
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 577–585. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L577-L585).

```c

    /* WB15/16 */
    if (it.curchar & WC_Regional_Indicator && it.lookahead & WC_Regional_Indicator)
    {
      it_advance();
      it_absorb(WC_Extend | WC_ZWJ | WC_Format, 0);
      break;
    }

```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 588–590. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L588-L590).

```c
  }
  return PyLong_FromSsize_t(it.pos);
}
```

### Callee analysis

- `TEXT_INIT / it_advance / it_rollback` in `apsw-3.53.4.0/src/unicode.c`, lines 185–234: Unicode READ at offset/pos; rollback restores saved position. B nonzero-start/lookahead/backtracking

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 197–207. The original contextual region was lines 185–234.

- [`TEXT_INIT / it_advance / it_rollback`](#helper-001) (`apsw-3.53.4.0/src/unicode.c`, lines 185–196).
- [`TEXT_INIT / it_advance / it_rollback`](#helper-002) (`apsw-3.53.4.0/src/unicode.c`, lines 208–234).

<a id="case-004"></a>

## 4. `sentence_next_break`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller-provided codepoint offset; TEXT_INIT fetches lookahead and it_advance reads pos+1; stops at selected boundary. Speculative transactions restore saved pos/category state and may reread later.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 593–708. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L593-L708).

### Read sites

- Site 1: lines 593–708; macro iterator; index expression `offset; ++it.pos; saved.pos rollback`. Uses TEXT_INIT/it_advance helpers; categories of current and lookahead compared.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 631–675, 685–705. The original contextual region was lines 593–708.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 593–630. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L593-L630).

```c
sentence_next_break(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs,
                    PyObject *fast_kwnames)
{
  PyObject *text = NULL;
  Py_ssize_t offset;

  ARG_PROLOG(2, break_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(offset, text);
  ARG_EPILOG(NULL, "sentence_next_break(text: str, offset: int)", );

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

#undef cat_func
#define cat_func sentence_category
  TextIterator it = TEXT_INIT;

  /*  From spec */
#define ParaSep (SC_Sep | SC_CR | SC_LF)
#define SATerm (SC_STerm | SC_ATerm)

  /* SB1 implicit */

  /* SB2 */
  while (it.pos < text_end)
  {
    it_advance();

    /* SB3 */
    if (it.curchar & SC_CR && it.lookahead & SC_LF)
    {
      it_advance();
      break;
    }

    /* SB4 */
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 676–684. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L676-L684).

```c
      it_absorb(SC_Close, SC_Format | SC_Extend);
      it_absorb(SC_Sp, SC_Format | SC_Extend);
      if (it.lookahead & (SC_SContinue | SATerm))
      {
        it_advance();
        it_absorb(SC_Format | SC_Extend, 0);
        it_commit();
        continue;
      }
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 706–708. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L706-L708).

```c

  return PyLong_FromSsize_t(it.pos);
}
```

### Callee analysis

- `TEXT_INIT / it_advance / it_rollback` in `apsw-3.53.4.0/src/unicode.c`, lines 185–234: Unicode READ at offset/pos; rollback restores saved position. B nonzero-start/lookahead/backtracking

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 197–207. The original contextual region was lines 185–234.

- [`TEXT_INIT / it_advance / it_rollback`](#helper-001) (`apsw-3.53.4.0/src/unicode.c`, lines 185–196).
- [`TEXT_INIT / it_advance / it_rollback`](#helper-002) (`apsw-3.53.4.0/src/unicode.c`, lines 208–234).

<a id="case-005"></a>

## 5. `line_next_hard_break`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller-provided codepoint offset; TEXT_INIT fetches lookahead and it_advance reads pos+1; stops at selected boundary.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 711–748. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L711-L748).

### Read sites

- Site 1: lines 711–748; macro iterator; index expression `offset; ++it.pos; saved.pos rollback`. Uses TEXT_INIT/it_advance helpers; categories of current and lookahead compared.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 744–745. The original contextual region was lines 711–748.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 711–743. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L711-L743).

```c
line_next_hard_break(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs,
                     PyObject *fast_kwnames)
{
  PyObject *text = NULL;
  Py_ssize_t offset;

  ARG_PROLOG(2, break_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(offset, text);
  ARG_EPILOG(NULL, "line_next_hard_break(text: str, offset: int)", );

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

#undef cat_func
#define cat_func line_category
  TextIterator it = TEXT_INIT;

  while (it.pos < text_end)
  {
    it_advance();

    if (it.curchar & LB_BK)
      break;

    if (it.curchar & LB_CR && it.lookahead & LB_LF)
    {
      it_advance();
      break;
    }

    if (it.curchar & (LB_CR | LB_LF | LB_NL))
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 746–748. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L746-L748).

```c

  return PyLong_FromSsize_t(it.pos);
}
```

### Callee analysis

- `TEXT_INIT / it_advance / it_rollback` in `apsw-3.53.4.0/src/unicode.c`, lines 185–234: Unicode READ at offset/pos; rollback restores saved position. B nonzero-start/lookahead

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 197–207. The original contextual region was lines 185–234.

- [`TEXT_INIT / it_advance / it_rollback`](#helper-001) (`apsw-3.53.4.0/src/unicode.c`, lines 185–196).
- [`TEXT_INIT / it_advance / it_rollback`](#helper-002) (`apsw-3.53.4.0/src/unicode.c`, lines 208–234).

<a id="case-006"></a>

## 6. `line_next_break`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller-provided codepoint offset; TEXT_INIT fetches lookahead and it_advance reads pos+1; stops at selected boundary. Speculative transactions restore saved pos/category state and may reread later.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 751–1230. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L751-L1230).

### Read sites

- Site 1: lines 751–1230; macro iterator; index expression `offset; ++it.pos; saved.pos rollback`. Uses TEXT_INIT/it_advance helpers; categories of current and lookahead compared.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 772–872, 882–988, 998–1204, 1223–1227. The original contextual region was lines 751–1230.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 751–771. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L751-L771).

```c
line_next_break(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  PyObject *text = NULL;
  Py_ssize_t offset;

  ARG_PROLOG(2, break_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(offset, text);
  ARG_EPILOG(NULL, "line_next_break(text: str, offset: int)", );

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

#undef cat_func
#define cat_func line_category
  TextIterator it = TEXT_INIT;
  int it_has_accepted = 0;

  /* LB1 is already applied in the line_category data */

```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 873–881. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L873-L881).

```c
      if (it.curchar & LB_IS)
      {
        it_advance();
        while (it.curchar & (LB_CM | LB_ZWJ))
          it_advance();
      }
      if (it.curchar & LB_NU)
      {
        while (it.lookahead & (LB_NU | LB_SY | LB_IS))
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 989–997. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L989-L997).

```c
         implement that here too. */
      if (it.lookahead & LB_SP)
      {
        it_begin();
        it_advance();
        if (it.lookahead & (LB_HY | LB_HH))
        {
          it_advance();
          if (it.lookahead & (LB_AL | LB_HL))
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1205–1222. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1205-L1222).

```c

    /* LB30a */
    if (it.curchar & LB_RI && it.lookahead & LB_RI)
    {
      it_advance();
      it_absorb(LB_CM, 0);
      if (!LB7_APPLIES)
        break;
    }

    /* LB30b */
    if (it.curchar & LB_EB && it.lookahead & LB_EM)
      continue;
    if ((it.curchar & (LB_Extended_Pictographic | LB_OtherNotAssigned)) == (LB_Extended_Pictographic | LB_OtherNotAssigned)
        && it.lookahead & LB_EM)
      continue;

    if (LB7_APPLIES)
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1228–1230. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1228-L1230).

```c

  return PyLong_FromSsize_t(it.pos);
}
```

### Callee analysis

- `TEXT_INIT / it_advance / it_rollback` in `apsw-3.53.4.0/src/unicode.c`, lines 185–234: Unicode READ at offset/pos; rollback restores saved position. B nonzero-start/lookahead/backtracking

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 197–207. The original contextual region was lines 185–234.

- [`TEXT_INIT / it_advance / it_rollback`](#helper-001) (`apsw-3.53.4.0/src/unicode.c`, lines 185–196).
- [`TEXT_INIT / it_advance / it_rollback`](#helper-002) (`apsw-3.53.4.0/src/unicode.c`, lines 208–234).

<a id="case-007"></a>

## 7. `category_name`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

ARG_codepoint accepts a length1 Unicode argument and expands READ_CHAR at index0 (or takes numeric argument without Unicode reads).

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1261–1318. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1261-L1318).

### Read sites

- Site 1: lines 1268–1268; macro scalar; index expression `0`. ARG_codepoint expansion in src/argparse.c269-271.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1261–1271. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1261-L1271).

```c
category_name(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  const char *which = NULL;
  Py_UCS4 codepoint;

  ARG_PROLOG(2, category_name_KWNAMES);
  ARG_MANDATORY ARG_str(which);
  ARG_MANDATORY ARG_codepoint(codepoint);
  ARG_EPILOG(NULL, "category_name(which: str, codepoint: int)", );

  PyObject *res = NULL;
```

### Callee analysis

- `ARG_codepoint` in `apsw-3.53.4.0/src/argparse.c`, lines 266–287: READ_CHAR(useargs[argp_optindex],0) after length1 guard. B scalar

Available source context:

- [`ARG_codepoint`](#helper-003) (`apsw-3.53.4.0/src/argparse.c`, lines 266–287).

<a id="case-008"></a>

## 8. `get_category_category`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

ARG_codepoint accepts a length1 Unicode argument and expands READ_CHAR at index0 (or takes numeric argument without Unicode reads).

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1321–1331. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1321-L1331).

### Read sites

- Site 1: lines 1327–1327; macro scalar; index expression `0`. ARG_codepoint expansion in src/argparse.c269-271.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1321–1330. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1321-L1330).

```c
get_category_category(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs,
                      PyObject *fast_kwnames)
{
  Py_UCS4 codepoint;

  ARG_PROLOG(1, "codepoint");
  ARG_MANDATORY ARG_codepoint(codepoint);
  ARG_EPILOG(NULL, "category_category(codepoint: int)", );

  return PyLong_FromUnsignedLongLong(category_category(codepoint));
```

### Callee analysis

- `ARG_codepoint` in `apsw-3.53.4.0/src/argparse.c`, lines 266–287: READ_CHAR(useargs[argp_optindex],0) after length1 guard. B scalar

Available source context:

- [`ARG_codepoint`](#helper-003) (`apsw-3.53.4.0/src/argparse.c`, lines 266–287).

<a id="case-009"></a>

## 9. `has_category`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Caller supplies start/end codepoint range; scans only selected region, returns at first category match.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1334–1358. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1334-L1358).

### Read sites

- Site 1: lines 1340–1357; range; index expression `start while start<end, start++`. Nonzero start permitted.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1334–1358. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1334-L1358).

```c
has_category(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  PyObject *text;
  Py_ssize_t start, end;
  unsigned long long mask;

#define has_category_KWARGS "text", "start", "end", "mask"
  ARG_PROLOG(4, has_category_KWARGS);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(start, text);
  ARG_MANDATORY ARG_PyUnicode_offset(end, text);
  ARG_MANDATORY ARG_unsigned_long_long(mask);
  ARG_EPILOG(NULL, "has_category(text: str, start:int, end: int, mask: int)", );

  int kind = PyUnicode_KIND(text);
  void *data = PyUnicode_DATA(text);

  while (start < end)
  {
    if (category_category(PyUnicode_READ(kind, data, start)) & mask)
      Py_RETURN_TRUE;
    start++;
  }
  Py_RETURN_FALSE;
}
```


<a id="case-010"></a>

## 10. `casefold_ascii`

**Classification:** B. **Subtypes:** multiple passes, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

First forward pass stops at first uppercase, then restarts at0 for full folding pass if needed.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1361–1395. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1361-L1395).

### Read sites

- Site 1: lines 1368–1377; first pass; index expression `source_pos=0..first uppercase`. Early break determines no-change fast return.
- Site 2: lines 1385–1392; second pass; index expression `source_pos=0..source_length-1`. Resets to zero.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1361–1395. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1361-L1395).

```c
casefold_ascii(PyObject *text)
{
  Py_ssize_t source_length = PyUnicode_GET_LENGTH(text);
  int source_kind = PyUnicode_KIND(text);
  void *source_data = PyUnicode_DATA(text);
  Py_ssize_t source_pos;

  for (source_pos = 0; source_pos < source_length; source_pos++)
  {
    Py_UCS4 source_char = PyUnicode_READ(source_kind, source_data, source_pos);
    /* ascii detect */
    if (source_char >= 'A' && source_char <= 'Z')
      break;
  }
  /* no changes */
  if (source_pos == source_length)
    return Py_NewRef(text);

  PyObject *dest = PyUnicode_New(source_length, 127);
  if (!dest)
    return NULL;
  assert(source_kind == PyUnicode_KIND(dest));
  void *dest_data = PyUnicode_DATA(dest);

  for (source_pos = 0; source_pos < source_length; source_pos++)
  {
    Py_UCS4 source_char = PyUnicode_READ(source_kind, source_data, source_pos);
    /* ascii detect */
    if (source_char >= 'A' && source_char <= 'Z')
      source_char += 32;
    PyUnicode_WRITE(source_kind, dest_data, source_pos, source_char);
  }

  return dest;
}
```


<a id="case-011"></a>

## 11. `casefold`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Two full forward source passes: expansion/maxchar detection then casefold emission.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1398–1508. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1398-L1508).

### Read sites

- Site 1: lines 1434–1459; first pass; index expression `source_pos=0..source_length-1`. Detects changes, expansion and maxchar.
- Site 2: lines 1481–1506; second pass; index expression `source_pos=0..source_length-1`. Resets source to zero to emit folded result.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1410–1422. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1410-L1422).

```c
  Py_ssize_t source_length = PyUnicode_GET_LENGTH(text);
  int source_kind = PyUnicode_KIND(text);
  void *source_data = PyUnicode_DATA(text);

  /* We do two phases - the first looking for how much the result string
     is expanded because some codepoints expand to more than one folded
     codepoint.  During this phase we also detect if any changes would be
     made.  If not the original string can be returned.  We also need to
     work out what the resulting maxchar value will be because debug
     Python builds assertion fail if too generous.

     The second phase then does the folding.
*/
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1434–1459. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1434-L1459).

```c
  Py_ssize_t source_pos;
  for (source_pos = 0; source_pos < source_length; source_pos++)
  {
    Py_UCS4 source_char = PyUnicode_READ(source_kind, source_data, source_pos);
    /* ascii shortcut */
    if (source_char >= 'A' && source_char <= 'Z')
    {
      changed = 1;
      continue;
    }
    if (source_char <= 127)
      continue;
    switch (source_char)
    {
      /* generated, present in _unicodedb.c */
      CASEFOLD_EXPANSION
    default:
      /* unchanged codepoint */
      if (source_char >= 128 && source_char <= 255)
        maxchar |= CASEFOLD_MAXCHAR_255;
      else if (source_char >= 256 && source_char <= 65535)
        maxchar |= CASEFOLD_MAXCHAR_65535;
      else
        maxchar |= CASEFOLD_MAXCHAR_1114111;
    }
  }
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1472–1506. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1472-L1506).

```c
  PyObject *dest = PyUnicode_New(source_length + expansion, max_char_value);
  if (!dest)
    return NULL;

  int dest_kind = PyUnicode_KIND(dest);
  void *dest_data = PyUnicode_DATA(dest);

  Py_ssize_t dest_pos;

  for (source_pos = dest_pos = 0; source_pos < source_length; source_pos++)
  {
    /* each source corresponds to one or more dest chars.  The CASEFOLD_WRITE
       macro provides just the replacement for one, and writes all except
       the last when it is more than one.  That is why this macro needs to
       be available. */

#define WRITE_DEST(c)                                                                                                  \
  do                                                                                                                   \
  {                                                                                                                    \
    PyUnicode_WRITE(dest_kind, dest_data, dest_pos, (c));                                                              \
    dest_pos++;                                                                                                        \
  } while (0)

    Py_UCS4 dest_char = PyUnicode_READ(source_kind, source_data, source_pos);
    /* ascii shortcut */
    if (dest_char >= 'A' && dest_char <= 'Z')
      dest_char += 32;
    else
      switch (dest_char)
      {
        /* generated, present in _unicodedb.c */
        CASEFOLD_WRITE
      }
    WRITE_DEST(dest_char);
  }
```


<a id="case-012"></a>

## 12. `strip`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Two full forward source passes: result sizing/maxchar then replacement emission.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1511–1631. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1511-L1631).

### Read sites

- Site 1: lines 1541–1567; first pass; index expression `source_pos=0..source_length-1`. Computes result length and flags.
- Site 2: lines 1598–1626; second pass; index expression `source_pos=0..source_length-1`. Restarts at zero to generate result.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 1593, 1606–1623. The original contextual region was lines 1589–1626.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1520–1547. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1520-L1547).

```c
  Py_ssize_t source_length = PyUnicode_GET_LENGTH(text);
  int source_kind = PyUnicode_KIND(text);
  void *source_data = PyUnicode_DATA(text);

  /* We pack replacement codepoints into 21 bit chunks in the 64 bit value */
#define BITS21_MASK ((1 << 21) - 1)
#define CP0(x) ((x) & BITS21_MASK)
#define CP1(x) (((x) >> 21) & BITS21_MASK)

  /* Pass 1:
      * Figure out if there is any change
      * Figure out if max char value changes
      * Figure out length of replacement
  */
  /* would the result be any different */
  int is_changed = 0;
  /* new MAX_CHAR_VALUE  */
  unsigned long long maxchar_flags = 0;
  /* number of codepoints in result */
  Py_ssize_t result_length = 0;

  Py_ssize_t source_pos;
  for (source_pos = 0; source_pos < source_length; source_pos++)
  {
    Py_UCS4 source_char = PyUnicode_READ(source_kind, source_data, source_pos);
    unsigned long long conv = strip_category(source_char);
    /* it doesn't matter if we have the other bits */
    maxchar_flags |= conv;
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1538–1570. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1538-L1570).

```c
  /* number of codepoints in result */
  Py_ssize_t result_length = 0;

  Py_ssize_t source_pos;
  for (source_pos = 0; source_pos < source_length; source_pos++)
  {
    Py_UCS4 source_char = PyUnicode_READ(source_kind, source_data, source_pos);
    unsigned long long conv = strip_category(source_char);
    /* it doesn't matter if we have the other bits */
    maxchar_flags |= conv;

    conv &= ~STRIP_MAXCHAR_MASK;
    if (conv == 1)
    {
      result_length += 1;
      continue;
    }
    is_changed = 1;
    if (conv == 0)
      continue;

    if (conv < 30)
    {
      result_length += conv;
      continue;
    }
    result_length += 1;
    if (CP1(conv))
      result_length += 1;
  }

  if (!is_changed)
  {
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1569–1578. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1569-L1578).

```c
  if (!is_changed)
  {
    /* Sanity check */
    assert(result_length == source_length);
    return Py_NewRef(text);
  }

  /* Pass 2:
    Create and populate result string
  */
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1589–1592. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1589-L1592).

```c
  PyObject *dest = PyUnicode_New(result_length, maxchar);
  if (!dest)
    return NULL;

```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1594–1605. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1594-L1605).

```c
  void *dest_data = PyUnicode_DATA(dest);

  Py_ssize_t dest_pos;

  for (source_pos = dest_pos = 0; source_pos < source_length; source_pos++)
  {
    /* WRITE_DEST comes from casefold above */
    Py_UCS4 source_char = PyUnicode_READ(source_kind, source_data, source_pos);
    unsigned long long conv = strip_category(source_char) & ~STRIP_MAXCHAR_MASK;
    if (conv == 0)
      continue;
    if (conv == 1)
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1624–1626. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1624-L1626).

```c
      Py_UNREACHABLE();
    }
  }
```


<a id="case-013"></a>

## 13. `text_width`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller-provided codepoint offset and scans to end, with early invalid-width break.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1634–1682. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1634-L1682).

### Read sites

- Site 1: lines 1637–1658; range; index expression `offset..text_end-1`. Caller may request suffix width.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 1658–1679. The original contextual region was lines 1634–1682.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1634–1657. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1634-L1657).

```c
text_width(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  PyObject *text = NULL;
  Py_ssize_t offset;
  ARG_PROLOG(2, break_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(offset, text);
  ARG_EPILOG(NULL, "text_width(text: str, offset: int)", );

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

  Py_ssize_t width = 0;

  int last_was_zwj = 0;

  for (; offset < text_end; offset++)
  {
    Py_UCS4 codepoint = PyUnicode_READ(text_kind, text_data, offset);
    unsigned long long cat = category_category(codepoint);
    if (cat & Category_WIDTH_INVALID)
    {
      width = -1;
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1680–1682. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1680-L1682).

```c

  return PyLong_FromSsize_t(width);
}
```


<a id="case-014"></a>

## 14. `grapheme_find`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking, multiple passes, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Caller start/end bounds; repeatedly tests input[offset+check] against substring[check], retries from next grapheme boundary and calls break scanner. Mixed range/lookahead/repeated substring reads.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

text and substring can alias: future evictable FSR getter cannot invalidate first pointer on second getter or nested grapheme_next_break on same object.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1685–1760. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1685-L1760).

### Read sites

- Site 1: lines 1708–1720; bounds; index expression `start/end (negative normalized)`. Caller-selected window.
- Site 2: lines 1722–1758; nested indexed comparison; index expression `text[offset], substring[0], text[offset+check], substring[check]`. Restarts substring matching at each candidate; grapheme scanner may backtrack.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 1697–1705, 1739–1750. The original contextual region was lines 1693–1758.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1693–1696. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1693-L1696).

```c
  ARG_PROLOG(4, grapheme_find_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode(substring);
  ARG_MANDATORY ARG_Py_ssize_t(start);
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1706–1738. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1706-L1738).

```c
  Py_ssize_t substring_end = PyUnicode_GET_LENGTH(substring);

  /* fixup offsets */
  if (start < 0)
    start = Py_MAX(0, text_end + start);
  if (end < 0)
    end = text_end + end;
  end = Py_MIN(end, text_end) - substring_end + 1;

  /* zero length is always found if start is 0 even if end is before start! */
  if (substring_end == 0 && start == 0)
    return PyLong_FromLong(0);
  /* early out */
  if (substring_end > text_end || start >= end)
    goto notfound;

  Py_ssize_t offset = start;

  while (offset < end)
  {
    /* we only allow the empty substring to be found at grapheme boundaries */
    if (substring_end == 0
        || PyUnicode_READ(text_kind, text_data, offset) == PyUnicode_READ(substring_kind, substring_data, 0))
    {
      int matched = 1;
      for (Py_ssize_t check = 1; check < substring_end; check++)
      {
        if (PyUnicode_READ(text_kind, text_data, offset + check)
            != PyUnicode_READ(substring_kind, substring_data, check))
        {
          matched = 0;
          break;
        }
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1751–1758. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1751-L1758).

```c
          return PyLong_FromSsize_t(offset);
        }
      }
    }
    offset = grapheme_next_break(text, offset);
  }

notfound:
```

### Callee analysis

- `grapheme_next_break` in `apsw-3.53.4.0/src/unicode.c`, lines 280–394: Called at candidate boundary and to advance offset. B offset-start/lookahead/backtracking

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 292–308, 318–341, 351–355, 365–377, 387–391. The original contextual region was lines 280–394.

- [`grapheme_next_break`](#helper-004) (`apsw-3.53.4.0/src/unicode.c`, lines 280–291).
- [`grapheme_next_break`](#helper-005) (`apsw-3.53.4.0/src/unicode.c`, lines 309–317).
- [`grapheme_next_break`](#helper-006) (`apsw-3.53.4.0/src/unicode.c`, lines 342–350).
- [`grapheme_next_break`](#helper-007) (`apsw-3.53.4.0/src/unicode.c`, lines 356–364).
- [`grapheme_next_break`](#helper-008) (`apsw-3.53.4.0/src/unicode.c`, lines 378–386).
- [`grapheme_next_break`](#helper-009) (`apsw-3.53.4.0/src/unicode.c`, lines 392–394).

<a id="case-015"></a>

## 15. `grapheme_length`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Loops over grapheme_next_break from caller-provided offset; helper does offset-start lookahead/backtracking and stops at boundary, so this is not a simple codepoint iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Read-bearing algorithm through helper; wrapper get_grapheme_next_break excluded separately as orchestration-only.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1763–1783. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1763-L1783).

### Read sites

- Site 1: lines 1768–1780; helper iteration; index expression `offset=grapheme_next_break(text,offset)`. Caller may start partway; helper includes lookahead/rollback.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1763–1783. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1763-L1783).

```c
grapheme_length(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  PyObject *text = NULL;
  Py_ssize_t offset;

  ARG_PROLOG(2, break_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(offset, text);
  ARG_EPILOG(NULL, "grapheme_length(text: str, offset: int)", );

  Py_ssize_t text_length = PyUnicode_GET_LENGTH(text);
  size_t count = 0;

  while (offset < text_length)
  {
    offset = grapheme_next_break(text, offset);
    count++;
  }

  return PyLong_FromSize_t(count);
}
```

### Callee analysis

- `grapheme_next_break` in `apsw-3.53.4.0/src/unicode.c`, lines 280–394: Repeated helper calls at prior returned boundary. B non-simple traversal

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 292–308, 318–341, 351–355, 365–377, 387–391. The original contextual region was lines 280–394.

- [`grapheme_next_break`](#helper-004) (`apsw-3.53.4.0/src/unicode.c`, lines 280–291).
- [`grapheme_next_break`](#helper-005) (`apsw-3.53.4.0/src/unicode.c`, lines 309–317).
- [`grapheme_next_break`](#helper-006) (`apsw-3.53.4.0/src/unicode.c`, lines 342–350).
- [`grapheme_next_break`](#helper-007) (`apsw-3.53.4.0/src/unicode.c`, lines 356–364).
- [`grapheme_next_break`](#helper-008) (`apsw-3.53.4.0/src/unicode.c`, lines 378–386).
- [`grapheme_next_break`](#helper-009) (`apsw-3.53.4.0/src/unicode.c`, lines 392–394).

<a id="case-016"></a>

## 16. `grapheme_substr`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Uses repeated grapheme boundary scanner from zero, early stop for positive stop or full offsets list for negative indices; helper lookahead/rollback retains non-simple read behavior.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1786–1871. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1786-L1871).

### Read sites

- Site 1: lines 1804–1845; helper iteration; index expression `text_offset=grapheme_next_break(text,text_offset)`. Caller chooses grapheme range; negative index paths require whole-string offsets.

### Contextual source excerpts

Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 1805–1815, 1825–1832, 1842–1845. The original contextual region was lines 1801–1848.

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1791–1807. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1791-L1807).

```c
#define grapheme_substr_KWNAMES "text", "start", "stop"
  ARG_PROLOG(3, grapheme_substr_KWNAMES);
  ARG_MANDATORY ARG_PyUnicode(text);
  Py_ssize_t len_text = PyUnicode_GET_LENGTH(text);
  ARG_MANDATORY ARG_ifnone(start = 0) ARG_Py_ssize_t(start);
  ARG_MANDATORY ARG_ifnone(stop = len_text) ARG_Py_ssize_t(stop);
  ARG_EPILOG(NULL, "grapheme_substr(text: str, start: int, stop: int)", );

  if (start > len_text || start == stop || stop == 0 || (start > 0 && stop >= 0 && start >= stop))
    return PyUnicode_New(0, 0);

  PyObject *offsets = NULL;

  if (start < 0 || stop < 0)
  {
    /* we are doing addressing relative to the end of the string so we
       have to track offsets of the whole string and then index */
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1801–1804. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1801-L1804).

```c

  PyObject *offsets = NULL;

  if (start < 0 || stop < 0)
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1816–1824. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1816-L1824).

```c

  Py_ssize_t count = 0;
  Py_ssize_t text_offset = 0;

  Py_ssize_t start_offset = (start == 0) ? 0 : len_text;
  Py_ssize_t stop_offset = len_text;

  while (text_offset < len_text)
  {
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1833–1841. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1833-L1841).

```c
      Py_DECREF(o);
      if (added != 0)
        goto error;
    }
    if (start == count)
      start_offset = text_offset;
    if (stop == count)
    {
      stop_offset = text_offset;
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1846–1848. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1846-L1848).

```c

  if (!offsets)
  {
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1817–1845. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1817-L1845).

```c
  Py_ssize_t count = 0;
  Py_ssize_t text_offset = 0;

  Py_ssize_t start_offset = (start == 0) ? 0 : len_text;
  Py_ssize_t stop_offset = len_text;

  while (text_offset < len_text)
  {
    text_offset = grapheme_next_break(text, text_offset);
    count++;
    if (offsets)
    {
      PyObject *o = PyLong_FromSsize_t(text_offset);
      if (!o)
        goto error;
      int added = PyList_Append(offsets, o);
      Py_DECREF(o);
      if (added != 0)
        goto error;
    }
    if (start == count)
      start_offset = text_offset;
    if (stop == count)
    {
      stop_offset = text_offset;
      if (!offsets)
        break;
    }
  }
```

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1855–1864. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1855-L1864).

```c
  Py_ssize_t offsets_len = PyList_GET_SIZE(offsets) - 1;

  Py_ssize_t nchars = PySlice_AdjustIndices(offsets_len, &start, &stop, 1);
  if (nchars)
  {
    start_offset = PyLong_AsSsize_t(PyList_GET_ITEM(offsets, start));
    stop_offset = PyLong_AsSsize_t(PyList_GET_ITEM(offsets, stop));
    Py_CLEAR(offsets);
    return PyUnicode_Substring(text, start_offset, stop_offset);
  }
```

### Callee analysis

- `grapheme_next_break` in `apsw-3.53.4.0/src/unicode.c`, lines 280–394: Repeated calls from previous boundary. B non-simple read helper

Available source context:
Omitted from `apsw-3.53.4.0/src/unicode.c`: lines 292–308, 318–341, 351–355, 365–377, 387–391. The original contextual region was lines 280–394.

- [`grapheme_next_break`](#helper-004) (`apsw-3.53.4.0/src/unicode.c`, lines 280–291).
- [`grapheme_next_break`](#helper-005) (`apsw-3.53.4.0/src/unicode.c`, lines 309–317).
- [`grapheme_next_break`](#helper-006) (`apsw-3.53.4.0/src/unicode.c`, lines 342–350).
- [`grapheme_next_break`](#helper-007) (`apsw-3.53.4.0/src/unicode.c`, lines 356–364).
- [`grapheme_next_break`](#helper-008) (`apsw-3.53.4.0/src/unicode.c`, lines 378–386).
- [`grapheme_next_break`](#helper-009) (`apsw-3.53.4.0/src/unicode.c`, lines 392–394).

<a id="case-017"></a>

## 17. `version_added`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

ARG_codepoint accepts a length1 Unicode argument and expands READ_CHAR at index0 (or takes numeric argument without Unicode reads).

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1874–1886. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1874-L1886).

### Read sites

- Site 1: lines 1879–1879; macro scalar; index expression `0`. ARG_codepoint expansion in src/argparse.c269-271.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1874–1882. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1874-L1882).

```c
version_added(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  Py_UCS4 codepoint;

  ARG_PROLOG(1, "codepoint");
  ARG_MANDATORY ARG_codepoint(codepoint);
  ARG_EPILOG(NULL, "version_added(codepoint: int)", );

  const char *age = age_category(codepoint);
```

### Callee analysis

- `ARG_codepoint` in `apsw-3.53.4.0/src/argparse.c`, lines 266–287: READ_CHAR(useargs[argp_optindex],0) after length1 guard. B scalar

Available source context:

- [`ARG_codepoint`](#helper-003) (`apsw-3.53.4.0/src/argparse.c`, lines 266–287).

<a id="case-018"></a>

## 18. `codepoint_name`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

ARG_codepoint accepts a length1 Unicode argument and expands READ_CHAR at index0 (or takes numeric argument without Unicode reads).

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz). Archive SHA-256: `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

**Function source:** `apsw-3.53.4.0/src/unicode.c`, lines 1996–2013. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`.

[Verified immutable function link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1996-L2013).

### Read sites

- Site 1: lines 2001–2001; macro scalar; index expression `0`. ARG_codepoint expansion in src/argparse.c269-271.

### Contextual source excerpts

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 1996–2004. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1996-L2004).

```c
codepoint_name(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  Py_UCS4 codepoint;

  ARG_PROLOG(1, "codepoint");
  ARG_MANDATORY ARG_codepoint(codepoint);
  ARG_EPILOG(NULL, "codepoint_name(codepoint: int)", );

  NAME_RANGES(codepoint);
```

### Callee analysis

- `ARG_codepoint` in `apsw-3.53.4.0/src/argparse.c`, lines 266–287: READ_CHAR(useargs[argp_optindex],0) after length1 guard. B scalar

Available source context:

- [`ARG_codepoint`](#helper-003) (`apsw-3.53.4.0/src/argparse.c`, lines 266–287).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `TEXT_INIT / it_advance / it_rollback`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 185–196. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L185-L196).

```c
#define TEXT_INIT                                                                                                      \
  {                                                                                                                    \
    .pos = offset,                                                                                                     \
    .curchar = -1,                                                                                                     \
    .lookahead = (offset == text_end) ? EOT : cat_func(PyUnicode_READ(text_kind, text_data, offset)),                  \
  }

#define it_advance()                                                                                                   \
  do                                                                                                                   \
  {                                                                                                                    \
    assert(it.curchar != EOT);                                                                                         \
    it.curchar = it.lookahead;                                                                                         \
```

<a id="helper-002"></a>

### 2. `TEXT_INIT / it_advance / it_rollback`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 208–234. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L208-L234).

```c
    {                                                                                                                  \
      unsigned long long savechar = it.curchar;                                                                        \
      while (it.lookahead & (match))                                                                                   \
      {                                                                                                                \
        it_advance();                                                                                                  \
        while (it.lookahead & (extend))                                                                                \
          it_advance();                                                                                                \
      }                                                                                                                \
      it.curchar = savechar;                                                                                           \
    }                                                                                                                  \
  } while (0)

#define it_begin_base()                                                                                                \
  do                                                                                                                   \
  {                                                                                                                    \
    it.saved.pos = it.pos;                                                                                             \
    it.saved.curchar = it.curchar;                                                                                     \
    it.saved.lookahead = it.lookahead;                                                                                 \
  } while (0)

#define it_rollback_base()                                                                                             \
  do                                                                                                                   \
  {                                                                                                                    \
    it.pos = it.saved.pos;                                                                                             \
    it.curchar = it.saved.curchar;                                                                                     \
    it.lookahead = it.saved.lookahead;                                                                                 \
  } while (0)
```

<a id="helper-003"></a>

### 3. `ARG_codepoint`

Archive member `apsw-3.53.4.0/src/argparse.c`, lines 266–287. Member SHA-256: `594c3e6259d54fb03e694396539335c955a07ad4d093ac50d757bad04c7c4a2b`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/argparse.c#L266-L287).

```c
#define ARG_codepoint(varname)                                                                                         \
  do                                                                                                                   \
  {                                                                                                                    \
    if (PyUnicode_Check(useargs[argp_optindex]) && 1 == PyUnicode_GET_LENGTH(useargs[argp_optindex]))                  \
    {                                                                                                                  \
      varname = PyUnicode_READ_CHAR(useargs[argp_optindex], 0);                                                        \
    }                                                                                                                  \
    else if (PyLong_Check(useargs[argp_optindex]))                                                                     \
    {                                                                                                                  \
      long _tmpcp = PyLong_AsLong(useargs[argp_optindex]);                                                             \
      if (_tmpcp == (long)-1 && PyErr_Occurred())                                                                      \
        goto param_error;                                                                                              \
      if (_tmpcp < 0 || _tmpcp > 0x10ffff)                                                                             \
      {                                                                                                                \
        PyErr_Format(PyExc_ValueError, "Codepoint value %ld outside of range 0 to 0x10ffff", _tmpcp);                  \
        goto param_error;                                                                                              \
      }                                                                                                                \
      varname = (Py_UCS4)_tmpcp;                                                                                       \
    }                                                                                                                  \
    else                                                                                                               \
    {                                                                                                                  \
      PyErr_Format(PyExc_TypeError, "codepoint should be an int or one character str not %s",                          \
```

<a id="helper-004"></a>

### 4. `grapheme_next_break`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 280–291. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L280-L291).

```c
grapheme_next_break(PyObject *text, Py_ssize_t offset)
{
  assert(PyUnicode_Check(text));
  assert(offset >= 0);

  void *text_data = PyUnicode_DATA(text);
  int text_kind = PyUnicode_KIND(text);
  Py_ssize_t text_end = PyUnicode_GET_LENGTH(text);

#define cat_func grapheme_category
  TextIterator it = TEXT_INIT;
  int it_has_accepted = 0;
```

<a id="helper-005"></a>

### 5. `grapheme_next_break`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 309–317. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L309-L317).

```c
    if (it.curchar & (GC_Control | GC_CR | GC_LF))
    {
      /* GB5: break before if any chars are accepted */
      if (it_has_accepted)
        it.pos--;
      break;
    }

    /* GB6 */
```

<a id="helper-006"></a>

### 6. `grapheme_next_break`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 342–350. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L342-L350).

```c
      it_advance();
      while (it.lookahead & (GC_InCB_Extend | GC_InCB_Linker))
      {
        seen_linker = seen_linker || it.lookahead & GC_InCB_Linker;
        it_advance();
      }
      if (seen_linker && it.lookahead & GC_InCB_Consonant)
      {
        it_commit();
```

<a id="helper-007"></a>

### 7. `grapheme_next_break`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 356–364. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L356-L364).

```c
    /* GB11 */
    if (it.curchar & GC_Extended_Pictographic && it.lookahead & (GC_Extend | GC_ZWJ))
    {
      it_begin();
      while (it.lookahead & GC_Extend)
        it_advance();
      if (it.lookahead & GC_ZWJ)
      {
        it_advance();
```

<a id="helper-008"></a>

### 8. `grapheme_next_break`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 378–386. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L378-L386).

```c

    /* GB12 */
    if (it.curchar & GC_Regional_Indicator && it.lookahead & GC_Regional_Indicator)
    {
      it_advance();
      /* reapply GB9 */
      if (it.lookahead & (GC_Extend | GC_ZWJ | GC_InCB_Extend))
        continue;
      break;
```

<a id="helper-009"></a>

### 9. `grapheme_next_break`

Archive member `apsw-3.53.4.0/src/unicode.c`, lines 392–394. Member SHA-256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`. [Verified immutable source link](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L392-L394).

```c

  return it.pos;
}
```
