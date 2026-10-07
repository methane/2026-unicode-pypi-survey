# yarl — non-simple Unicode reads

[All packages](README.md)

Version: 1.25.1. **7 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`_skip_surrogates`](#case-001)
- [`_Quoter._do_quote_or_skip`](#case-002)
- [`_Quoter._do_quote`](#case-003)
- [`_widen_to_ucs4`](#case-004)
- [`_ucs4_write_slice`](#case-005)
- [`_Unquoter._unquote_from`](#case-006)
- [`_Unquoter._write_invalid`](#case-007)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `_skip_surrogates`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Starts at caller idx and skips surrogate run until non-surrogate/end; can begin anywhere.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 108–115. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L108-L115).

### Read sites

- Site 1: lines 108–115; scalar range; index expression `idx caller; idx<length; idx++`. Reads caller-selected subrange and stops on first non-surrogate.

### Contextual source excerpts

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 108–115. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L108-L115).

```cython
cdef inline Py_ssize_t _skip_surrogates(
    int kind, const void *data, Py_ssize_t idx, Py_ssize_t length
) noexcept:
    # Advance past lone surrogates; they cannot be UTF-8 encoded and are
    # dropped, so they must not break up a percent escape during requoting.
    while idx < length and _is_surrogate(PyUnicode_READ(kind, data, idx)):
        idx += 1
    return idx
```


<a id="case-002"></a>

## 2. `_Quoter._do_quote_or_skip`

**Classification:** B. **Subtypes:** backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Precheck starts idx=length, decrements before reads; if unsafe character found, reruns forward quote pass from zero.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 328–354. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L328-L354).

### Read sites

- Site 1: lines 328–348; backward loop; index expression `idx=length; while idx: --idx; READ(idx)`. Backward ASCII-safe search.
- Site 2: lines 350–354; restart handoff; index expression `_do_quote(...kind,data...) from idx0`. Forward re-traversal after partial backward pass.

### Contextual source excerpts

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 328–354. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L328-L354).

```cython
    cdef str _do_quote_or_skip(self, str val):
        cdef char[BUF_SIZE] buffer
        cdef Py_UCS4 ch
        cdef Py_ssize_t length = PyUnicode_GET_LENGTH(val)
        cdef Py_ssize_t idx = length
        cdef bint must_quote = 0
        cdef Writer writer
        cdef int kind = PyUnicode_KIND(val)
        cdef const void *data = PyUnicode_DATA(val)

        # If everything in the string is in the safe
        # table and all ASCII, we can skip quoting
        while idx:
            idx -= 1
            ch = PyUnicode_READ(kind, data, idx)
            if ch >= ASCII_LIMIT or not bit_at(self._safe_table, ch):
                must_quote = 1
                break

        if not must_quote:
            return val

        _init_writer(&writer, &buffer[0])
        try:
            return self._do_quote(<str>val, length, kind, data, &writer)
        finally:
            _release_writer(&writer)
```

### Callee analysis

- `_do_quote` in `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 356–418: Starts idx=0, looks ahead over surrogate runs and percent hex digits. B lookahead/reread.

Available source context:
Omitted from `yarl-1.25.1/yarl/_quoting_c.pyx`: lines 360–369, 391–413. The original contextual region was lines 356–418.

- [`_do_quote`](#helper-001) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 356–359).
- [`_do_quote`](#helper-002) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 370–390).
- [`_do_quote`](#helper-003) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 414–418).

<a id="case-003"></a>

## 3. `_Quoter._do_quote`

**Classification:** B. **Subtypes:** lookahead or lookbehind, reset or backtracking. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Main idx advances forward but _skip_surrogates checks ahead; reads pos1,pos2 again for percent escapes; failed escape leaves advanced lookahead to be traversed again.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Surrogates dropped deliberately before percent escape recognition; no surrogatepass normalization to a single scalar pair.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 356–418. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L356-L418).

### Read sites

- Site 1: lines 374–409; scalar with lookahead; index expression `idx; pos1=skip(idx); pos2=skip(pos1+1); READ(pos1),READ(pos2)`. Lookahead and repeated reads in requote branch.

### Contextual source excerpts

Omitted from `yarl-1.25.1/yarl/_quoting_c.pyx`: lines 360–369, 391–415. The original contextual region was lines 356–418.

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 356–359. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L356-L359).

```cython
    cdef str _do_quote(
        self,
        str val,
        Py_ssize_t length,
```

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 370–390. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L370-L390).

```cython
        cdef Py_ssize_t idx = 0
        cdef Py_ssize_t pos1
        cdef Py_ssize_t pos2

        while idx < length:
            ch = PyUnicode_READ(kind, data, idx)
            idx += 1
            if ch == '%' and self._requote and idx < length:
                # Lone surrogates are dropped (see _skip_surrogates), so look
                # through them for the two hex digits of the "%XX" escape; this
                # keeps the C quoter consistent with the pure-Python backend,
                # which strips surrogates before scanning.
                pos1 = _skip_surrogates(kind, data, idx, length)
                pos2 = _skip_surrogates(kind, data, pos1 + 1, length)
                if pos2 < length:
                    d1 = PyUnicode_READ(kind, data, pos1)
                    d2 = PyUnicode_READ(kind, data, pos2)
                    chl = _restore_ch(d1, d2)
                else:
                    chl = -1
                if chl != -1:
```

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 416–418. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L416-L418).

```cython
        if not writer.changed:
            return val
        return PyUnicode_DecodeASCII(writer.buf, writer.pos, "strict")
```

### Callee analysis

- `_skip_surrogates` in `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 108–115: Scans from arbitrary idx through surrogate run. B subset/prefix scanning.

Available source context:

- [`_skip_surrogates`](#helper-004) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 108–115).

<a id="case-004"></a>

## 4. `_widen_to_ucs4`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Generic fused typed helper reads src[i] for a supplied slice; root pointer may have caller nonzero start. Local loop forward from zero relative to that slice, not full original Unicode.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Typed input element offsets (1/2-byte codepoints); output UCS4.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 521–528. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L521-L528).

### Read sites

- Site 1: lines 521–528; typed loop; index expression `i=0..length; src[i], where src=DATA+start`. Copies range selected by caller.

### Contextual source excerpts

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 521–528. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L521-L528).

```cython
cdef inline void _widen_to_ucs4(
    Py_UCS4 *out, const _narrow_ucs *src, Py_ssize_t length
) noexcept:
    # No public API copies part of a str into a UCS4 buffer; CPython widens
    # with the same plain loop internally.
    cdef Py_ssize_t i
    for i in range(length):
        out[i] = src[i]
```


<a id="case-005"></a>

## 5. `_ucs4_write_slice`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Selected FSR range [start,end) is widened or memcpy copied into output. start is caller-provided and often nonzero.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L531-L549).

### Read sites

- Site 1: lines 531–549; typed range bulk; index expression `(Py_UCS1/2/4*)data + start; end-start`. Bulk subset read; scalar helper widens 1/2-byte.

### Contextual source excerpts

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L531-L549).

```cython
cdef inline void _ucs4_write_slice(
    UCS4Writer* writer,
    int kind,
    const void *data,
    Py_ssize_t start,
    Py_ssize_t end,
) noexcept:
    cdef Py_ssize_t length = end - start
    cdef Py_UCS4 *out
    if length <= 0:
        return
    out = writer.buf + writer.pos
    if kind == PyUnicode_1BYTE_KIND:
        _widen_to_ucs4(out, <const Py_UCS1*>data + start, length)
    elif kind == PyUnicode_2BYTE_KIND:
        _widen_to_ucs4(out, <const Py_UCS2*>data + start, length)
    else:
        memcpy(out, <const Py_UCS4*>data + start, length * sizeof(Py_UCS4))
    writer.pos += length
```

### Callee analysis

- `_widen_to_ucs4` in `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 521–528: out[i]=src[i], bounded length. Forward range copy with arbitrary origin start.

Available source context:

- [`_widen_to_ucs4`](#helper-005) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 521–528).

<a id="case-006"></a>

## 6. `_Unquoter._unquote_from`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking, multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Begins caller idx from first percent; prefix/runs copied separately. Looks ahead at idx,idx+1 for hex digits and revisits earlier invalid escapes via _write_invalid/_ucs4_write_slice.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- _find_percent uses public PyUnicode_FindChar on caller ranges; listed as trace context, not separate FSR read site.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 635–715. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L635-L715).

### Read sites

- Site 1: lines 635–655; range and lookahead; index expression `initial idx; READ(idx),READ(idx+1)`. Begin at caller offset and inspect two future hex digits.
- Site 2: lines 668–711; revisit range; index expression `idx - PCT_ESCAPE_LEN - buflen*PCT_ESCAPE_LEN; idx-1; length-buflen*PCT_ESCAPE_LEN`. Copy prior escapes/runs after validating them.

### Contextual source excerpts

Omitted from `yarl-1.25.1/yarl/_quoting_c.pyx`: lines 659–681, 691–712. The original contextual region was lines 635–715.

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 635–658. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L635-L658).

```cython
    cdef str _unquote_from(
        self, UCS4Writer* writer, str val, Py_ssize_t length, Py_ssize_t idx
    ):
        cdef uint8_t buffer[UTF8_MAX_BYTES]
        cdef Py_ssize_t buflen = 0
        cdef Py_ssize_t need = 0
        cdef Py_UCS4 ch
        cdef long chl
        cdef Py_ssize_t run_end
        cdef bint changed = 0
        cdef int kind = PyUnicode_KIND(val)
        cdef const void *data = PyUnicode_DATA(val)
        _ucs4_write_slice(writer, kind, data, 0, idx)
        while idx < length:
            ch = PyUnicode_READ(kind, data, idx)
            idx += 1
            if ch == '%' and idx <= length - PCT_HEX_LEN:
                chl = _restore_ch(
                    PyUnicode_READ(kind, data, idx),
                    PyUnicode_READ(kind, data, idx + 1)
                )
                if chl != -1:
                    changed = 1
                    ch = <Py_UCS4>chl
```

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 682–690. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L682-L690).

```cython
                            _ucs4_write_char(writer, ch)
                        continue
                    need = _utf8_sequence_length(<uint8_t>ch)
                    if need:
                        buffer[0] = <uint8_t>ch
                        buflen = 1
                    else:
                        self._write_invalid(
                            writer, kind, data, idx - PCT_ESCAPE_LEN, idx
```

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 713–715. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L713-L715).

```cython
        return PyUnicode_FromKindAndData(
            PyUnicode_4BYTE_KIND, writer.buf, writer.pos
        )
```

### Callee analysis

- `_ucs4_write_slice` in `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549: Typed DATA+start range copy. B caller_start_range.
- `_write_invalid` in `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 717–729: Either replace or copy earlier escape range. B caller range revisit.

Available source context:

- [`_ucs4_write_slice`](#helper-006) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549).
- [`_write_invalid`](#helper-007) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 717–729).

<a id="case-007"></a>

## 7. `_Unquoter._write_invalid`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Helper forwards caller-selected earlier range [start,end) to typed slice copier; often rereads prior percent escapes.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offsets; FSR element width selected by kind.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz). Archive SHA-256: `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

**Function source:** `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 717–729. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

[Verified immutable function link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L717-L729).

### Read sites

- Site 1: lines 717–729; range handoff; index expression `start,end supplied by caller`. Retained invalid escape copy.

### Contextual source excerpts

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 717–729. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L717-L729).

```cython
    cdef inline void _write_invalid(
        self,
        UCS4Writer* writer,
        int kind,
        const void *data,
        Py_ssize_t start,
        Py_ssize_t end,
    ) noexcept:
        """Write the escapes in val[start:end] that are not valid UTF-8."""
        if self._replace_invalid:
            _ucs4_write_char(writer, REPLACEMENT_CHARACTER)
        else:
            _ucs4_write_slice(writer, kind, data, start, end)
```

### Callee analysis

- `_ucs4_write_slice` in `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549: Typed DATA+start read/copy. B selected-range read.

Available source context:

- [`_ucs4_write_slice`](#helper-006) (`yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `_do_quote`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 356–359. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L356-L359).

```cython
    cdef str _do_quote(
        self,
        str val,
        Py_ssize_t length,
```

<a id="helper-002"></a>

### 2. `_do_quote`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 370–390. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L370-L390).

```cython
        cdef Py_ssize_t idx = 0
        cdef Py_ssize_t pos1
        cdef Py_ssize_t pos2

        while idx < length:
            ch = PyUnicode_READ(kind, data, idx)
            idx += 1
            if ch == '%' and self._requote and idx < length:
                # Lone surrogates are dropped (see _skip_surrogates), so look
                # through them for the two hex digits of the "%XX" escape; this
                # keeps the C quoter consistent with the pure-Python backend,
                # which strips surrogates before scanning.
                pos1 = _skip_surrogates(kind, data, idx, length)
                pos2 = _skip_surrogates(kind, data, pos1 + 1, length)
                if pos2 < length:
                    d1 = PyUnicode_READ(kind, data, pos1)
                    d2 = PyUnicode_READ(kind, data, pos2)
                    chl = _restore_ch(d1, d2)
                else:
                    chl = -1
                if chl != -1:
```

<a id="helper-003"></a>

### 3. `_do_quote`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 414–418. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L414-L418).

```cython
                raise

        if not writer.changed:
            return val
        return PyUnicode_DecodeASCII(writer.buf, writer.pos, "strict")
```

<a id="helper-004"></a>

### 4. `_skip_surrogates`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 108–115. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L108-L115).

```cython
cdef inline Py_ssize_t _skip_surrogates(
    int kind, const void *data, Py_ssize_t idx, Py_ssize_t length
) noexcept:
    # Advance past lone surrogates; they cannot be UTF-8 encoded and are
    # dropped, so they must not break up a percent escape during requoting.
    while idx < length and _is_surrogate(PyUnicode_READ(kind, data, idx)):
        idx += 1
    return idx
```

<a id="helper-005"></a>

### 5. `_widen_to_ucs4`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 521–528. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L521-L528).

```cython
cdef inline void _widen_to_ucs4(
    Py_UCS4 *out, const _narrow_ucs *src, Py_ssize_t length
) noexcept:
    # No public API copies part of a str into a UCS4 buffer; CPython widens
    # with the same plain loop internally.
    cdef Py_ssize_t i
    for i in range(length):
        out[i] = src[i]
```

<a id="helper-006"></a>

### 6. `_ucs4_write_slice`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 531–549. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L531-L549).

```cython
cdef inline void _ucs4_write_slice(
    UCS4Writer* writer,
    int kind,
    const void *data,
    Py_ssize_t start,
    Py_ssize_t end,
) noexcept:
    cdef Py_ssize_t length = end - start
    cdef Py_UCS4 *out
    if length <= 0:
        return
    out = writer.buf + writer.pos
    if kind == PyUnicode_1BYTE_KIND:
        _widen_to_ucs4(out, <const Py_UCS1*>data + start, length)
    elif kind == PyUnicode_2BYTE_KIND:
        _widen_to_ucs4(out, <const Py_UCS2*>data + start, length)
    else:
        memcpy(out, <const Py_UCS4*>data + start, length * sizeof(Py_UCS4))
    writer.pos += length
```

<a id="helper-007"></a>

### 7. `_write_invalid`

Archive member `yarl-1.25.1/yarl/_quoting_c.pyx`, lines 717–729. Member SHA-256: `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`. [Verified immutable source link](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L717-L729).

```cython
    cdef inline void _write_invalid(
        self,
        UCS4Writer* writer,
        int kind,
        const void *data,
        Py_ssize_t start,
        Py_ssize_t end,
    ) noexcept:
        """Write the escapes in val[start:end] that are not valid UTF-8."""
        if self._replace_invalid:
            _ucs4_write_char(writer, REPLACEMENT_CHARACTER)
        else:
            _ucs4_write_slice(writer, kind, data, start, end)
```
