# numpy — non-simple Unicode reads

[All packages](README.md)

Version: 2.5.3. **4 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`parse_control_character`](#case-001)
- [`copy_to_field_buffer<UCS>`](#case-002)
- [`tokenizer_core<UCS>`](#case-003)
- [`npy_tokenize`](#case-004)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `parse_control_character`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads only index0 after length==1 validation.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz). Archive SHA-256: `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

**Function source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/readtext.c`, lines 86–100. Member SHA-256: `d9270da4cef5e51a72b3ddc9acbe60df07fcaa8cfcbae0219cc232c5dfe26729`.

[Verified immutable function link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/readtext.c#L86-L100).

### Read sites

- Site 1: lines 92–99; scalar; index expression `0`. Delimiter/quote/comment configuration.

### Contextual source excerpts

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/readtext.c`, lines 86–100. Member SHA-256: `d9270da4cef5e51a72b3ddc9acbe60df07fcaa8cfcbae0219cc232c5dfe26729`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/readtext.c#L86-L100).

```c
parse_control_character(PyObject *obj, Py_UCS4 *character)
{
    if (obj == Py_None) {
        *character = (Py_UCS4)-1;  /* character beyond unicode range */
        return 1;
    }
    if (!PyUnicode_Check(obj) || PyUnicode_GetLength(obj) != 1) {
        PyErr_Format(PyExc_TypeError,
                "Text reading control character must be a single unicode "
                "character or None; but got: %.100R", obj);
        return 0;
    }
    *character = PyUnicode_READ_CHAR(obj, 0);
    return 1;
}
```


<a id="case-002"></a>

## 2. `copy_to_field_buffer<UCS>`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Rereads a caller-selected [chunk_start,chunk_end) region forward to widen into UCS4 output; usually follows tokenizer scan of that region.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** pointer indices are Unicode codepoints

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz). Archive SHA-256: `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

**Function source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 44–74. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`.

[Verified immutable function link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L44-L74).

### Read sites

- Site 1: lines 47–72; pointer range; index expression `chunk_start..chunk_end`. Nonzero segment start allowed; source Unicode FSR data from tokenizer_core.

### Contextual source excerpts

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 42–74. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L42-L74).

```cpp
template <typename UCS>
static inline int
copy_to_field_buffer(tokenizer_state *ts,
        const UCS *chunk_start, const UCS *chunk_end)
{
    npy_intp chunk_length = chunk_end - chunk_start;
    /* Space for length +1 termination, +2 additional padding for add_field */
    npy_intp size = chunk_length + ts->field_buffer_pos + 3;

    if (NPY_UNLIKELY(ts->field_buffer_length < size)) {
        npy_intp alloc_size = grow_size_and_multiply(&size, 32, sizeof(Py_UCS4));
        if (alloc_size < 0) {
            PyErr_Format(PyExc_ValueError,
                    "line too long to handle while reading file.");
            return -1;
        }
        Py_UCS4 *grown = (Py_UCS4 *)PyMem_Realloc(ts->field_buffer, alloc_size);
        if (grown == nullptr) {
            PyErr_NoMemory();
            return -1;
        }
        ts->field_buffer_length = size;
        ts->field_buffer = grown;
    }

    Py_UCS4 *write_pos = ts->field_buffer + ts->field_buffer_pos;
    for (; chunk_start < chunk_end; chunk_start++, write_pos++) {
        *write_pos = (Py_UCS4)*chunk_start;
    }
    *write_pos = '\0';  /* always ensure we end with NUL */
    ts->field_buffer_pos += chunk_length;
    return 0;
}
```

### Callee analysis

- `tokenizer_core` in `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 148–211: Scans to field end then passes chunk_start,pos here. Input region read again

Available source context:
Omitted from `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`: lines 154–206. The original contextual region was lines 148–211.

- [`tokenizer_core`](#helper-001) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 148–153).
- [`tokenizer_core`](#helper-002) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 207–211).

<a id="case-003"></a>

## 3. `tokenizer_core<UCS>`

**Classification:** B. **Subtypes:** caller-provided start or range, multiple passes, lookahead or lookbehind, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts from persistent ts->pos (often partway in string/chunk), scans field boundaries, then copy helper rereads same region. Quote checks/lookahead may leave pos unchanged for another state.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** UCS pointer step is one codepoint (1/2/4 bytes)

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Input owner keeps Unicode reference across row calls; future cached FSR eviction cannot invalidate ts->pos between calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz). Archive SHA-256: `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

**Function source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 115–264. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`.

[Verified immutable function link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L115-L264).

### Read sites

- Site 1: lines 117–143; saved pointer; index expression `ts->pos..ts->end`. Whitespace and first-character quote tests.
- Site 2: lines 146–229; field scan and copy; index expression `pos increments; chunk_start..pos reread`. Input fields scanned then copied; state transitions may reexamine same codepoint.
- Site 3: lines 231–255; line tail; index expression `pos..stop`. Comment tail/CRLF handling.

### Contextual source excerpts

Omitted from `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`: lines 122–131, 143–144, 154–165. The original contextual region was lines 113–170.
Omitted from `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`: lines 154–217. The original contextual region was lines 143–232.
Omitted from `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`: lines 207–217, 227–228, 238–248. The original contextual region was lines 200–255.

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 113–121. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L113-L121).

```cpp
template <typename UCS>
static inline int
tokenizer_core(tokenizer_state *ts, parser_config *const config)
{
    UCS *pos = (UCS *)ts->pos;
    UCS *stop = (UCS *)ts->end;
    UCS *chunk_start;

    if (ts->state == TOKENIZE_CHECK_QUOTED) {
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 132–142. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L132-L142).

```cpp
        }

        /* Setting chunk effectively starts the field */
        if (*pos == config->quote) {
            ts->fields[ts->num_fields - 1].quoted = true;
            ts->state = TOKENIZE_QUOTED;
            pos++;  /* TOKENIZE_QUOTED is OK with pos == stop */
        }
        else {
            /* Set to TOKENIZE_QUOTED or TOKENIZE_QUOTED_WHITESPACE */
            ts->state = ts->unquoted_state;
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 145–153. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L145-L153).

```cpp

    switch (ts->state) {
        case TOKENIZE_UNQUOTED:
            chunk_start = pos;
            for (; pos < stop; pos++) {
                if (*pos == '\r') {
                    ts->state = TOKENIZE_EAT_CRLF;
                    break;
                }
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 166–170. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L166-L170).

```cpp
            }
            if (copy_to_field_buffer(ts, chunk_start, pos) < 0) {
                return -1;
            }
            pos++;
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 143–153. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L143-L153).

```cpp
        }
    }

    switch (ts->state) {
        case TOKENIZE_UNQUOTED:
            chunk_start = pos;
            for (; pos < stop; pos++) {
                if (*pos == '\r') {
                    ts->state = TOKENIZE_EAT_CRLF;
                    break;
                }
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 218–232. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L218-L232).

```cpp
                        &config->quote, &config->quote+1) < 0) {
                    return -1;
                }
                ts->state = TOKENIZE_QUOTED;
                pos++;
            }
            else {
                /* continue parsing as if unquoted */
                /* Set to TOKENIZE_UNQUOTED or TOKENIZE_UNQUOTED_WHITESPACE */
                ts->state = ts->unquoted_state;
            }
            break;

        case TOKENIZE_GOTO_LINE_END:
            if (ts->buf_state != BUFFER_MAY_CONTAIN_NEWLINE) {
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 200–206. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L200-L206).

```cpp
        case TOKENIZE_QUOTED:
            chunk_start = pos;
            for (; pos < stop; pos++) {
                if (*pos == config->quote) {
                    ts->state = TOKENIZE_QUOTED_CHECK_DOUBLE_QUOTE;
                    break;
                }
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 218–226. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L218-L226).

```cpp
                        &config->quote, &config->quote+1) < 0) {
                    return -1;
                }
                ts->state = TOKENIZE_QUOTED;
                pos++;
            }
            else {
                /* continue parsing as if unquoted */
                /* Set to TOKENIZE_UNQUOTED or TOKENIZE_UNQUOTED_WHITESPACE */
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 229–237. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L229-L237).

```cpp
            break;

        case TOKENIZE_GOTO_LINE_END:
            if (ts->buf_state != BUFFER_MAY_CONTAIN_NEWLINE) {
                pos = stop;  /* advance to next buffer */
                ts->state = TOKENIZE_LINE_END;
                break;
            }
            for (; pos < stop; pos++) {
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 249–255. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L249-L255).

```cpp

        case TOKENIZE_EAT_CRLF:
            /* "Universal newline" support: remove \n in \r\n. */
            if (*pos == '\n') {
                pos++;
            }
            ts->state = TOKENIZE_LINE_END;
```

### Callee analysis

- `copy_to_field_buffer` in `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 42–74: Second forward read of chunk_start..pos after delimiter scan. B selected range reread

Available source context:

- [`copy_to_field_buffer`](#helper-003) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 42–74).

<a id="case-004"></a>

## 4. `npy_tokenize`

**Classification:** B. **Subtypes:** caller-provided start or range, multiple passes, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Row tokenizer invokes kind-specialized core on persistent source cursor; stops at row end and resumes partway on next row call. Core rereads fields via copy helper.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** byte pointers cast to kind-width codepoints

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/13/01/11703282db468b85f6f7b8c7f22d058de5970d5c7e60a3a8aaa313c3de36/numpy-2.5.3.tar.gz). Archive SHA-256: `df2d5874ff183595a4ba404edd04f6bd9b5505c1d7708573f6a6c17489a67563`.

**Function source:** `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 290–404. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`.

[Verified immutable function link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L290-L404).

### Read sites

- Site 1: lines 314–360; helper pipeline; index expression `ts->pos/end, unicode_kind`. Acquires next Unicode buffer only when exhausted; repeatedly calls core.

### Contextual source excerpts

Omitted from `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`: lines 301–309, 327–332, 342, 356–357. The original contextual region was lines 297–360.

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 297–300. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L297-L300).

```cpp
    /* Reset to start of buffer */
    ts->field_buffer_pos = 0;
    ts->num_fields = 0;

```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 310–326. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L310-L326).

```cpp
            }
            ts->state = TOKENIZE_CHECK_QUOTED;
        }

        if (NPY_UNLIKELY(ts->pos >= ts->end)) {
            if (ts->buf_state == BUFFER_IS_LINEND &&
                    ts->state != TOKENIZE_QUOTED) {
                /*
                 * Finished line, do not read anymore (also do not eat \n).
                 * If we are in a quoted field and the "line" does not end with
                 * a newline, the quoted field will not have it either.
                 * I.e. `np.loadtxt(['"a', 'b"'], dtype="S2", quotechar='"')`
                 * reads "ab". This matches `next(csv.reader(['"a', 'b"']))`.
                 */
                break;
            }
            /* fetch new data */
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 333–341. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L333-L341).

```cpp
                finished_reading_file = 1;
                ts->pos = ts->end;  /* stream should ensure this. */
                break;
            }
            else if (ts->pos == ts->end) {
                /* This must be an empty line (and it must be indicated!). */
                assert(ts->buf_state == BUFFER_IS_LINEND);
                break;
            }
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 343–355. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L343-L355).

```cpp
        int status;
        if (ts->unicode_kind == PyUnicode_1BYTE_KIND) {
            status = tokenizer_core<Py_UCS1>(ts, config);
        }
        else if (ts->unicode_kind == PyUnicode_2BYTE_KIND) {
            status = tokenizer_core<Py_UCS2>(ts, config);
        }
        else {
            assert(ts->unicode_kind == PyUnicode_4BYTE_KIND);
            status = tokenizer_core<Py_UCS4>(ts, config);
        }
        if (status < 0) {
            return -1;
```

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 358–360. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L358-L360).

```cpp
        if (ts->state == TOKENIZE_LINE_END) {
            break;
        }
```

### Callee analysis

- `stream_nextbuf → buffer_info_from_unicode` in `numpy-2.5.3/numpy/_core/src/multiarray/textreading/stream_pyobject.c`, lines 67–85: Typed Unicode DATA yields ts->pos/end. Source verified
- `tokenizer_core<UCS>` in `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 113–264: Paused scan and field-region copy reread. B derived read pipeline

Available source context:
Omitted from `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`: lines 122–131, 141–257. The original contextual region was lines 113–264.

- [`stream_nextbuf → buffer_info_from_unicode`](#helper-004) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/stream_pyobject.c`, lines 67–85).
- [`tokenizer_core<UCS>`](#helper-005) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 113–121).
- [`tokenizer_core<UCS>`](#helper-006) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 132–140).
- [`tokenizer_core<UCS>`](#helper-007) (`numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 258–264).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `tokenizer_core`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 148–153. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L148-L153).

```cpp
            chunk_start = pos;
            for (; pos < stop; pos++) {
                if (*pos == '\r') {
                    ts->state = TOKENIZE_EAT_CRLF;
                    break;
                }
```

<a id="helper-002"></a>

### 2. `tokenizer_core`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 207–211. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L207-L211).

```cpp
            }
            if (copy_to_field_buffer(ts, chunk_start, pos) < 0) {
                return -1;
            }
            pos++;
```

<a id="helper-003"></a>

### 3. `copy_to_field_buffer`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 42–74. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L42-L74).

```cpp
template <typename UCS>
static inline int
copy_to_field_buffer(tokenizer_state *ts,
        const UCS *chunk_start, const UCS *chunk_end)
{
    npy_intp chunk_length = chunk_end - chunk_start;
    /* Space for length +1 termination, +2 additional padding for add_field */
    npy_intp size = chunk_length + ts->field_buffer_pos + 3;

    if (NPY_UNLIKELY(ts->field_buffer_length < size)) {
        npy_intp alloc_size = grow_size_and_multiply(&size, 32, sizeof(Py_UCS4));
        if (alloc_size < 0) {
            PyErr_Format(PyExc_ValueError,
                    "line too long to handle while reading file.");
            return -1;
        }
        Py_UCS4 *grown = (Py_UCS4 *)PyMem_Realloc(ts->field_buffer, alloc_size);
        if (grown == nullptr) {
            PyErr_NoMemory();
            return -1;
        }
        ts->field_buffer_length = size;
        ts->field_buffer = grown;
    }

    Py_UCS4 *write_pos = ts->field_buffer + ts->field_buffer_pos;
    for (; chunk_start < chunk_end; chunk_start++, write_pos++) {
        *write_pos = (Py_UCS4)*chunk_start;
    }
    *write_pos = '\0';  /* always ensure we end with NUL */
    ts->field_buffer_pos += chunk_length;
    return 0;
}
```

<a id="helper-004"></a>

### 4. `stream_nextbuf → buffer_info_from_unicode`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/stream_pyobject.c`, lines 67–85. Member SHA-256: `14d865b71ddffe1975944670e27f34c28d4f8784e77f8b1ae069ba9e43c7195e`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/stream_pyobject.c#L67-L85).

```c
static inline void
buffer_info_from_unicode(PyObject *str, char **start, char **end, int *kind)
{
    Py_ssize_t length = PyUnicode_GET_LENGTH(str);
    *kind = PyUnicode_KIND(str);

    if (*kind == PyUnicode_1BYTE_KIND) {
        *start = (char *)PyUnicode_1BYTE_DATA(str);
    }
    else if (*kind == PyUnicode_2BYTE_KIND) {
        *start = (char *)PyUnicode_2BYTE_DATA(str);
        length *= sizeof(Py_UCS2);
    }
    else if (*kind == PyUnicode_4BYTE_KIND) {
        *start = (char *)PyUnicode_4BYTE_DATA(str);
        length *= sizeof(Py_UCS4);
    }
    *end = *start + length;
}
```

<a id="helper-005"></a>

### 5. `tokenizer_core<UCS>`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 113–121. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L113-L121).

```cpp
template <typename UCS>
static inline int
tokenizer_core(tokenizer_state *ts, parser_config *const config)
{
    UCS *pos = (UCS *)ts->pos;
    UCS *stop = (UCS *)ts->end;
    UCS *chunk_start;

    if (ts->state == TOKENIZE_CHECK_QUOTED) {
```

<a id="helper-006"></a>

### 6. `tokenizer_core<UCS>`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 132–140. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L132-L140).

```cpp
        }

        /* Setting chunk effectively starts the field */
        if (*pos == config->quote) {
            ts->fields[ts->num_fields - 1].quoted = true;
            ts->state = TOKENIZE_QUOTED;
            pos++;  /* TOKENIZE_QUOTED is OK with pos == stop */
        }
        else {
```

<a id="helper-007"></a>

### 7. `tokenizer_core<UCS>`

Archive member `numpy-2.5.3/numpy/_core/src/multiarray/textreading/tokenize.cpp`, lines 258–264. Member SHA-256: `5363aa25c98badac176b1a6db88b8d7d4f982c0a8e60922b9fca3e5de7cc8083`. [Verified immutable source link](https://github.com/numpy/numpy/blob/dd88c0c19b54ad9ed3533224221285bf0873249a/numpy/_core/src/multiarray/textreading/tokenize.cpp#L258-L264).

```cpp
        default:
            assert(0);
    }

    ts->pos = (char *)pos;
    return 0;
}
```
