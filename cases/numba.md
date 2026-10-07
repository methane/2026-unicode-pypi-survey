# numba — non-simple Unicode reads

[All packages](README.md)

Version: 0.68.0. **31 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`_get_code_point`](#case-001)
- [`_cmp_region`](#case-002)
- [`unicode_lt.lt_impl`](#case-003)
- [`unicode_gt.gt_impl`](#case-004)
- [`_default_find`](#case-005)
- [`_default_rfind`](#case-006)
- [`unicode_startswith.startswith_unicode_impl`](#case-007)
- [`unicode_endswith.endswith_impl`](#case-008)
- [`unicode_expandtabs.expandtabs_impl`](#case-009)
- [`unicode_split.split_impl`](#case-010)
- [`unicode_split.split_whitespace_impl`](#case-011)
- [`generate_rsplit_whitespace_impl.rsplit_whitespace_impl`](#case-012)
- [`unicode_rsplit.rsplit_impl._rsplit_char`](#case-013)
- [`generate_splitlines_func.impl`](#case-014)
- [`join_list`](#case-015)
- [`unicode_strip_left_bound`](#case-016)
- [`unicode_strip_right_bound`](#case-017)
- [`_strncpy`](#case-018)
- [`unicode_getitem.getitem_char`](#case-019)
- [`unicode_getitem.getitem_slice`](#case-020)
- [`gen_isAlX.unicode_isAlX.impl`](#case-021)
- [`case_operation.impl`](#case-022)
- [`_handle_capital_sigma`](#case-023)
- [`_lower_ucs4`](#case-024)
- [`_gen_unicode_upper_or_lower._do_upper_or_lower`](#case-025)
- [`_unicode_capitalize`](#case-026)
- [`_unicode_title`](#case-027)
- [`_unicode_swapcase`](#case-028)
- [`ol_ord.impl`](#case-029)
- [`iternext_unicode`](#case-030)
- [`gettyperecord_impl.impl`](#case-031)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `_get_code_point`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** primitive helper.

Typed dereference of a._data at caller-provided i; native index semantics are codepoints.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 288–298. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L288-L298).

### Read sites

- Site 1: lines 290–290; derived read; index expression `deref_uint8(a._data, i)`. Direct or resolved helper-derived FSR read
- Site 2: lines 292–292; derived read; index expression `deref_uint16(a._data, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 294–294; derived read; index expression `deref_uint32(a._data, i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 288–298. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L288-L298).

```python
def _get_code_point(a, i):
    if a._kind == PY_UNICODE_1BYTE_KIND:
        return deref_uint8(a._data, i)
    elif a._kind == PY_UNICODE_2BYTE_KIND:
        return deref_uint16(a._data, i)
    elif a._kind == PY_UNICODE_4BYTE_KIND:
        return deref_uint32(a._data, i)
    else:
        # there's also a wchar kind, but that's one of the above,
        # so skipping for this example
        return 0
```


<a id="case-002"></a>

## 2. `_cmp_region`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Compares n codepoints starting at caller-provided a_offset and b_offset, early mismatch exits.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 425–441. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L425-L441).

### Read sites

- Site 1: lines 434–434; derived read; index expression `_get_code_point(a, a_offset + i)`. Direct or resolved helper-derived FSR read
- Site 2: lines 435–435; derived read; index expression `_get_code_point(b, b_offset + i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 425–441. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L425-L441).

```python
def _cmp_region(a, a_offset, b, b_offset, n):
    if n == 0:
        return 0
    elif a_offset + n > a._length:
        return -1
    elif b_offset + n > b._length:
        return 1

    for i in range(n):
        a_chr = _get_code_point(a, a_offset + i)
        b_chr = _get_code_point(b, b_offset + i)
        if a_chr < b_chr:
            return -1
        elif a_chr > b_chr:
            return 1

    return 0
```


<a id="case-003"></a>

## 3. `unicode_lt.lt_impl`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Compares only prefix min(len(a),len(b)); one input can end before the other.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 543–550. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L543-L550).

### Read sites

- Site 1: lines 545–545; derived read; index expression `_cmp_region(a, 0, b, 0, minlen)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 543–550. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L543-L550).

```python
        def lt_impl(a, b):
            minlen = min(len(a), len(b))
            eqcode = _cmp_region(a, 0, b, 0, minlen)
            if eqcode == -1:
                return True
            elif eqcode == 0:
                return len(a) < len(b)
            return False
```


<a id="case-004"></a>

## 4. `unicode_gt.gt_impl`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Compares only prefix min(len(a),len(b)); one input can end before the other.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 559–566. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L559-L566).

### Read sites

- Site 1: lines 561–561; derived read; index expression `_cmp_region(a, 0, b, 0, minlen)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 559–566. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L559-L566).

```python
        def gt_impl(a, b):
            minlen = min(len(a), len(b))
            eqcode = _cmp_region(a, 0, b, 0, minlen)
            if eqcode == 1:
                return True
            elif eqcode == 0:
                return len(a) > len(b)
            return False
```


<a id="case-005"></a>

## 5. `_default_find`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind, reset or backtracking, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Boyer-Moore-style range search: starts at supplied start; reads tail at mlast+i then earlier i+j, lookahead mlast+i+1, reuses needle repeatedly.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 641–684. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L641-L684).

### Read sites

- Site 1: lines 648–648; derived read; index expression `_get_code_point(substr, mlast)`. Direct or resolved helper-derived FSR read
- Site 2: lines 653–653; derived read; index expression `_get_code_point(substr, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 660–660; derived read; index expression `_get_code_point(data, mlast + i)`. Direct or resolved helper-derived FSR read
- Site 4: lines 664–664; derived read; index expression `_get_code_point(data, i + j)`. Direct or resolved helper-derived FSR read
- Site 5: lines 665–665; derived read; index expression `_get_code_point(substr, j)`. Direct or resolved helper-derived FSR read
- Site 6: lines 673–673; derived read; index expression `_get_code_point(data, mlast + i + 1)`. Direct or resolved helper-derived FSR read
- Site 7: lines 679–679; derived read; index expression `_get_code_point(data, mlast + i + 1)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 641–684. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L641-L684).

```python
def _default_find(data, substr, start, end):
    """Left finder."""
    m = len(substr)
    if m == 0:
        return start

    gap = mlast = m - 1
    last = _get_code_point(substr, mlast)

    zero = types.intp(0)
    mask = _bloom_add(zero, last)
    for i in range(mlast):
        ch = _get_code_point(substr, i)
        mask = _bloom_add(mask, ch)
        if ch == last:
            gap = mlast - i - 1

    i = start
    while i <= end - m:
        ch = _get_code_point(data, mlast + i)
        if ch == last:
            j = 0
            while j < mlast:
                haystack_ch = _get_code_point(data, i + j)
                needle_ch = _get_code_point(substr, j)
                if haystack_ch != needle_ch:
                    break
                j += 1
            if j == mlast:
                # got a match
                return i

            ch = _get_code_point(data, mlast + i + 1)
            if _bloom_check(mask, ch) == 0:
                i += m
            else:
                i += gap
        else:
            ch = _get_code_point(data, mlast + i + 1)
            if _bloom_check(mask, ch) == 0:
                i += m
        i += 1

    return -1
```


<a id="case-006"></a>

## 6. `_default_rfind`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, lookahead or lookbehind, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Reverse range search starts end-m, decrements i/j with skips and reads i-1.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 688–733. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L688-L733).

### Read sites

- Site 1: lines 695–695; derived read; index expression `_get_code_point(substr, 0)`. Direct or resolved helper-derived FSR read
- Site 2: lines 699–699; derived read; index expression `_get_code_point(substr, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 707–707; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 4: lines 711–711; derived read; index expression `_get_code_point(data, i + j)`. Direct or resolved helper-derived FSR read
- Site 5: lines 712–712; derived read; index expression `_get_code_point(substr, j)`. Direct or resolved helper-derived FSR read
- Site 6: lines 721–721; derived read; index expression `_get_code_point(data, i - 1)`. Direct or resolved helper-derived FSR read
- Site 7: lines 728–728; derived read; index expression `_get_code_point(data, i - 1)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 688–733. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L688-L733).

```python
def _default_rfind(data, substr, start, end):
    """Right finder."""
    m = len(substr)
    if m == 0:
        return end

    skip = mlast = m - 1
    mfirst = _get_code_point(substr, 0)
    mask = _bloom_add(0, mfirst)
    i = mlast
    while i > 0:
        ch = _get_code_point(substr, i)
        mask = _bloom_add(mask, ch)
        if ch == mfirst:
            skip = i - 1
        i -= 1

    i = end - m
    while i >= start:
        ch = _get_code_point(data, i)
        if ch == mfirst:
            j = mlast
            while j > 0:
                haystack_ch = _get_code_point(data, i + j)
                needle_ch = _get_code_point(substr, j)
                if haystack_ch != needle_ch:
                    break
                j -= 1

            if j == 0:
                # got a match
                return i

            ch = _get_code_point(data, i - 1)
            if i > start and _bloom_check(mask, ch) == 0:
                i -= m
            else:
                i -= skip

        else:
            ch = _get_code_point(data, i - 1)
            if i > start and _bloom_check(mask, ch) == 0:
                i -= m
        i -= 1

    return -1
```


<a id="case-007"></a>

## 7. `unicode_startswith.startswith_unicode_impl`

**Classification:** B. **Subtypes:** caller-provided start or range, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Slices caller-supplied start:end (slice scans its FSR range) then compares prefix_length subset via _cmp_region.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 980–996. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L980-L996).

### Read sites

- Site 1: lines 996–996; derived read; index expression `_cmp_region(s_slice, 0, prefix, 0, prefix_length)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 980–996. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L980-L996).

```python
        def startswith_unicode_impl(s, prefix, start=None, end=None):
            length, prefix_length = len(s), len(prefix)
            if start is None:
                start = 0
            if end is None:
                end = length

            start, end = _adjust_indices(length, start, end)
            if end - start < prefix_length:
                return False

            if prefix_length == 0:
                return True

            s_slice = s[start:end]

            return _cmp_region(s_slice, 0, prefix, 0, prefix_length) == 0
```


<a id="case-008"></a>

## 8. `unicode_endswith.endswith_impl`

**Classification:** B. **Subtypes:** caller-provided start or range, a subset starting after position zero. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Computes offset=len(s)-len(substr) adjusted by start/end and compares substring-length suffix.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1027–1045. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1027-L1045).

### Read sites

- Site 1: lines 1045–1045; derived read; index expression `_cmp_region(s, offset, substr, 0, sub_length)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1027–1045. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1027-L1045).

```python
        def endswith_impl(s, substr, start=None, end=None):
            length = len(s)
            sub_length = len(substr)
            if start is None:
                start = 0
            if end is None:
                end = length

            start, end = _adjust_indices(length, start, end)
            if end - start < sub_length:
                return False

            if sub_length == 0:
                return True

            s = s[start:end]
            offset = len(s) - sub_length

            return _cmp_region(s, offset, substr, 0, sub_length) == 0
```


<a id="case-009"></a>

## 9. `unicode_expandtabs.expandtabs_impl`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Two full input passes: length/tab scan and subsequent rendering.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1071–1115. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1071-L1115).

### Read sites

- Site 1: lines 1076–1076; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 2: lines 1100–1100; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Omitted from `numba-0.68.0/numba/cpython/unicode.py`: lines 1081–1095, 1105–1112. The original contextual region was lines 1071–1115.

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1071–1080. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1071-L1080).

```python
    def expandtabs_impl(data, tabsize=8):
        length = len(data)
        j = line_pos = 0
        found = False
        for i in range(length):
            code_point = _get_code_point(data, i)
            if code_point == _Py_TAB:
                found = True
                if tabsize > 0:
                    # cannot overflow
```

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1096–1104. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1096-L1104).

```python

        res = _empty_string(data._kind, j, data._is_ascii)
        j = line_pos = 0
        for i in range(length):
            code_point = _get_code_point(data, i)
            if code_point == _Py_TAB:
                if tabsize > 0:
                    incr = tabsize - (line_pos % tabsize)
                    line_pos += incr
```

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1113–1115. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1113-L1115).

```python
                    line_pos = 0

        return res
```


<a id="case-010"></a>

## 10. `unicode_split.split_impl`

**Classification:** B. **Subtypes:** caller-provided start or range, multiple passes, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Single separator fast path is forward; general separator repeatedly compares candidate input range via _cmp_region and slices already visited spans.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1133–1166. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1133-L1166).

### Read sites

- Site 1: lines 1145–1145; derived read; index expression `_get_code_point(sep, 0)`. Direct or resolved helper-derived FSR read
- Site 2: lines 1147–1147; derived read; index expression `_get_code_point(a, idx)`. Direct or resolved helper-derived FSR read
- Site 3: lines 1155–1155; derived read; index expression `_cmp_region(a, idx, sep, 0, sep_len)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1133–1166. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1133-L1166).

```python
        def split_impl(a, sep=None, maxsplit=-1):
            a_len = len(a)
            sep_len = len(sep)

            if sep_len == 0:
                raise ValueError('empty separator')

            parts = []
            last = 0
            idx = 0

            if sep_len == 1 and maxsplit == -1:
                sep_code_point = _get_code_point(sep, 0)
                for idx in range(a_len):
                    if _get_code_point(a, idx) == sep_code_point:
                        parts.append(a[last:idx])
                        last = idx + 1
            else:
                split_count = 0

                while idx < a_len and (maxsplit == -1 or
                                       split_count < maxsplit):
                    if _cmp_region(a, idx, sep, 0, sep_len) == 0:
                        parts.append(a[last:idx])
                        idx += sep_len
                        last = idx
                        split_count += 1
                    else:
                        idx += 1

            if last <= a_len:
                parts.append(a[last:])

            return parts
```


<a id="case-011"></a>

## 11. `unicode_split.split_whitespace_impl`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Whitespace scan itself forward with maxsplit early exit; returned slice construction calls getitem_slice, which scans already visited codepoints to find minimal kind.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1170–1201. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1170-L1201).

### Read sites

- Site 1: lines 1180–1180; derived read; index expression `_get_code_point(a, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1170–1201. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1170-L1201).

```python
        def split_whitespace_impl(a, sep=None, maxsplit=-1):
            a_len = len(a)

            parts = []
            last = 0
            idx = 0
            split_count = 0
            in_whitespace_block = True

            for idx in range(a_len):
                code_point = _get_code_point(a, idx)
                is_whitespace = _PyUnicode_IsSpace(code_point)
                if in_whitespace_block:
                    if is_whitespace:
                        pass  # keep consuming space
                    else:
                        last = idx  # this is the start of the next string
                        in_whitespace_block = False
                else:
                    if not is_whitespace:
                        pass  # keep searching for whitespace transition
                    else:
                        parts.append(a[last:idx])
                        in_whitespace_block = True
                        split_count += 1
                        if maxsplit != -1 and split_count == maxsplit:
                            break

            if last <= a_len and not in_whitespace_block:
                parts.append(a[last:])

            return parts
```


<a id="case-012"></a>

## 12. `generate_rsplit_whitespace_impl.rsplit_whitespace_impl`

**Classification:** B. **Subtypes:** backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Moves i from len-1 backwards through whitespace/tokens, rereads boundaries and constructs slices of visited ranges.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1208–1244. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1208-L1244).

### Read sites

- Site 1: lines 1217–1217; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 2: lines 1226–1226; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 1237–1237; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Omitted from `numba-0.68.0/numba/cpython/unicode.py`: lines 1212, 1231–1232. The original contextual region was lines 1208–1244.

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1208–1211. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1208-L1211).

```python
    def rsplit_whitespace_impl(data, sep=None, maxsplit=-1):
        # https://github.com/python/cpython/blob/1d4b6ba19466aba0eb91c4ba01ba509acf18c723/Objects/stringlib/split.h#L192-L240    # noqa: E501
        if maxsplit < 0:
            maxsplit = sys.maxsize
```

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1213–1230. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1213-L1230).

```python
        result = []
        i = len(data) - 1
        while maxsplit > 0:
            while i >= 0:
                code_point = _get_code_point(data, i)
                if not isspace_func(code_point):
                    break
                i -= 1
            if i < 0:
                break
            j = i
            i -= 1
            while i >= 0:
                code_point = _get_code_point(data, i)
                if isspace_func(code_point):
                    break
                i -= 1
            result.append(data[i + 1:j + 1])
```

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1233–1244. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1233-L1244).

```python
        if i >= 0:
            # Only occurs when maxsplit was reached
            # Skip any remaining whitespace and copy to beginning of string
            while i >= 0:
                code_point = _get_code_point(data, i)
                if not isspace_func(code_point):
                    break
                i -= 1
            if i >= 0:
                result.append(data[0:i + 1])

        return result[::-1]
```


<a id="case-013"></a>

## 13. `unicode_rsplit.rsplit_impl._rsplit_char`

**Classification:** B. **Subtypes:** backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Reverse scan i=len(data)-1..0 with fixed separator index0, then output slice scans previously visited ranges.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1294–1309. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1294-L1309).

### Read sites

- Site 1: lines 1297–1297; derived read; index expression `_get_code_point(ch, 0)`. Direct or resolved helper-derived FSR read
- Site 2: lines 1300–1300; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1294–1309. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1294-L1309).

```python
        def _rsplit_char(data, ch, maxsplit):
            # https://github.com/python/cpython/blob/1d4b6ba19466aba0eb91c4ba01ba509acf18c723/Objects/stringlib/split.h#L242-L284    # noqa: E501
            result = []
            ch_code_point = _get_code_point(ch, 0)
            i = j = len(data) - 1
            while i >= 0 and maxsplit > 0:
                data_code_point = _get_code_point(data, i)
                if data_code_point == ch_code_point:
                    result.append(data[i + 1 : j + 1])
                    j = i = i - 1
                    maxsplit -= 1
                i -= 1
            if j >= -1:
                result.append(data[0 : j + 1])

            return result[::-1]
```


<a id="case-014"></a>

## 14. `generate_splitlines_func.impl`

**Classification:** B. **Subtypes:** lookahead or lookbehind, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Line scan rereads delimiter at i and looks ahead i+1 for CRLF; output slices revisit spans for kind checking.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1423–1451. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1423-L1451).

### Read sites

- Site 1: lines 1431–1431; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 2: lines 1440–1440; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 1441–1441; derived read; index expression `_get_code_point(data, i + 1)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1423–1451. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1423-L1451).

```python
    def impl(data, keepends):
        # https://github.com/python/cpython/blob/1d4b6ba19466aba0eb91c4ba01ba509acf18c723/Objects/stringlib/split.h#L335-L389    # noqa: E501
        length = len(data)
        result = []
        i = j = 0
        while i < length:
            # find a line and append it
            while i < length:
                code_point = _get_code_point(data, i)
                if is_line_break_func(code_point):
                    break
                i += 1

            # skip the line break reading CRLF as one line break
            eol = i
            if i < length:
                if i + 1 < length:
                    cur_cp = _get_code_point(data, i)
                    next_cp = _get_code_point(data, i + 1)
                    if _Py_ISCARRIAGERETURN(cur_cp) and _Py_ISLINEFEED(next_cp):
                        i += 1
                i += 1
                if keepends:
                    eol = i

            result.append(data[j:eol])
            j = i

        return result
```


<a id="case-015"></a>

## 15. `join_list`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

_strncpy copies each part, but same separator buffer is reread for every join boundary.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1488–1516. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1488-L1516).

### Read sites

- Site 1: lines 1507–1507; derived read; index expression `_strncpy(result, 0, part, 0, len(part))`. Direct or resolved helper-derived FSR read
- Site 2: lines 1510–1510; derived read; index expression `_strncpy(result, dst_offset, sep, 0, sep_len)`. Direct or resolved helper-derived FSR read
- Site 3: lines 1513–1513; derived read; index expression `_strncpy(result, dst_offset, part, 0, len(part))`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1488–1516. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1488-L1516).

```python
def join_list(sep, parts):
    parts_len = len(parts)
    if parts_len == 0:
        return ''

    # Precompute size and char_width of result
    sep_len = len(sep)
    length = (parts_len - 1) * sep_len
    kind = sep._kind
    is_ascii = sep._is_ascii
    for p in parts:
        length += len(p)
        kind = _pick_kind(kind, p._kind)
        is_ascii = _pick_ascii(is_ascii, p._is_ascii)

    result = _empty_string(kind, length, is_ascii)

    # populate string
    part = parts[0]
    _strncpy(result, 0, part, 0, len(part))
    dst_offset = len(part)
    for idx in range(1, parts_len):
        _strncpy(result, dst_offset, sep, 0, sep_len)
        dst_offset += sep_len
        part = parts[idx]
        _strncpy(result, dst_offset, part, 0, len(part))
        dst_offset += len(part)

    return result
```


<a id="case-016"></a>

## 16. `unicode_strip_left_bound`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Reads string[i] from left until non-strip codepoint; chars membership may repeatedly search its string via find.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1576–1589. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1576-L1589).

### Read sites

- Site 1: lines 1581–1587; derived read; index expression `string[i]`. getitem_char and membership search

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1576–1589. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1576-L1589).

```python
def unicode_strip_left_bound(string, chars):
    str_len = len(string)

    i = 0
    if chars is not None:
        for i in range(str_len):
            if string[i] not in chars:
                return i
    else:
        for i in range(str_len):
            if not _PyUnicode_IsSpace(string[i]):
                return i

    return str_len
```


<a id="case-017"></a>

## 17. `unicode_strip_right_bound`

**Classification:** B. **Subtypes:** backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Reverse traversal from len-1 until non-strip codepoint; chars membership may repeatedly search.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1593–1607. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1593-L1607).

### Read sites

- Site 1: lines 1597–1603; derived read; index expression `string[i]`. Backward native getitem

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1593–1607. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1593-L1607).

```python
def unicode_strip_right_bound(string, chars):
    str_len = len(string)
    i = 0
    if chars is not None:
        for i in range(str_len - 1, -1, -1):
            if string[i] not in chars:
                i += 1
                break
    else:
        for i in range(str_len - 1, -1, -1):
            if not _PyUnicode_IsSpace(string[i]):
                i += 1
                break

    return i
```


<a id="case-018"></a>

## 18. `_strncpy`

**Classification:** B. **Subtypes:** caller-provided start or range, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Same-kind bulk memcpy starts src_offset*byte_width; cross-kind loop reads src_offset+i for requested n, not necessarily full string.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1765–1776. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1765-L1776).

### Read sites

- Site 1: lines 1776–1776; derived read; index expression `_get_code_point(src, src_offset + i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1765–1776. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1765-L1776).

```python
def _strncpy(dst, dst_offset, src, src_offset, n):
    if src._kind == dst._kind:
        byte_width = _kind_to_byte_width(src._kind)
        src_byte_offset = byte_width * src_offset
        dst_byte_offset = byte_width * dst_offset
        nbytes = n * byte_width
        memcpy_region(dst._data, dst_byte_offset, src._data,
                      src_byte_offset, nbytes, align=1)
    else:
        for i in range(n):
            _set_code_point(dst, dst_offset + i,
                            _get_code_point(src, src_offset + i))
```


<a id="case-019"></a>

## 19. `unicode_getitem.getitem_char`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Normalizes arbitrary positive/negative caller index then dereferences one codepoint.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1821–1831. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1821-L1831).

### Read sites

- Site 1: lines 1823–1823; derived read; index expression `_get_code_point(s, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1821–1831. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1821-L1831).

```python
            def getitem_char(s, idx):
                idx = normalize_str_idx(idx, len(s))
                cp = _get_code_point(s, idx)
                kind = _codepoint_to_kind(cp)
                if kind == s._kind:
                    return _get_str_slice_view(s, idx, 1)
                else:
                    is_ascii = _codepoint_is_ascii(cp)
                    ret = _empty_string(kind, 1, is_ascii)
                    _set_code_point(ret, 0, cp)
                    return ret
```


<a id="case-020"></a>

## 20. `unicode_getitem.getitem_slice`

**Classification:** B. **Subtypes:** caller-provided start or range, backward traversal, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Caller slicing supports start/stop/step including negative step; scans minimal kind then either returns view or traverses same slice again to copy.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 1834–1868. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1834-L1868).

### Read sites

- Site 1: lines 1838–1838; derived read; index expression `_get_code_point(s, slice_idx.start)`. Direct or resolved helper-derived FSR read
- Site 2: lines 1845–1845; derived read; index expression `_get_code_point(s, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 1866–1866; derived read; index expression `_get_code_point(s, cur)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 1834–1868. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L1834-L1868).

```python
            def getitem_slice(s, idx):
                slice_idx = _normalize_slice(idx, len(s))
                span = _slice_span(slice_idx)

                cp = _get_code_point(s, slice_idx.start)
                kind = _codepoint_to_kind(cp)
                is_ascii = _codepoint_is_ascii(cp)

                # Check slice to see if it's homogeneous in kind
                for i in range(slice_idx.start + slice_idx.step,
                               slice_idx.stop, slice_idx.step):
                    cp = _get_code_point(s, i)
                    is_ascii &= _codepoint_is_ascii(cp)
                    new_kind = _codepoint_to_kind(cp)
                    if kind != new_kind:
                        kind = _pick_kind(kind, new_kind)
                    # TODO: it might be possible to break here if the kind
                    # is PY_UNICODE_4BYTE_KIND but there are potentially
                    # strings coming from other internal functions that are
                    # this wide and also actually ASCII (i.e. kind is larger
                    # than actually required for storing the code point), so
                    # it's necessary to continue.

                if slice_idx.step == 1 and kind == s._kind:
                    # Can return a view, the slice has the same kind as the
                    # string itself and it's a stride slice 1.
                    return _get_str_slice_view(s, slice_idx.start, span)
                else:
                    # It's heterogeneous in kind OR stride != 1
                    ret = _empty_string(kind, span, is_ascii)
                    cur = slice_idx.start
                    for i in range(span):
                        _set_code_point(ret, i, _get_code_point(s, cur))
                        cur += slice_idx.step
                    return ret
```


<a id="case-021"></a>

## 21. `gen_isAlX.unicode_isAlX.impl`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

ASCII predicate loop is followed by another full Unicode predicate loop when all ASCII checks pass (no intervening return).

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2000–2023. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2000-L2023).

### Read sites

- Site 1: lines 2006–2006; derived read; index expression `_get_code_point(data, 0)`. Direct or resolved helper-derived FSR read
- Site 2: lines 2014–2014; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read
- Site 3: lines 2019–2019; derived read; index expression `_get_code_point(data, i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2000–2023. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2000-L2023).

```python
        def impl(data):
            length = len(data)
            if length == 0:
                return False

            if length == 1:
                code_point = _get_code_point(data, 0)
                if data._is_ascii:
                    return ascii_func(code_point)
                else:
                    return unicode_func(code_point)

            if data._is_ascii:
                for i in range(length):
                    code_point = _get_code_point(data, i)
                    if not ascii_func(code_point):
                        return False

            for i in range(length):
                code_point = _get_code_point(data, i)
                if not unicode_func(code_point):
                    return False

            return True
```


<a id="case-022"></a>

## 22. `case_operation.impl`

**Classification:** B. **Subtypes:** mixed access patterns, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Input algorithm is supplied callback: most are forward, but lowercase/title/capitalize/swapcase call final-sigma context reader; local tmp read is new output buffer.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2230–2251. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2230-L2251).

### Read sites

- Site 1: lines 2249–2249; derived read; index expression `_get_code_point(tmp, i)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2230–2251. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2230-L2251).

```python
    def impl(data):
        length = len(data)
        if length == 0:
            return _empty_string(data._kind, length, data._is_ascii)

        if data._is_ascii:
            res = _empty_string(data._kind, length, 1)
            ascii_func(data, res)
            return res

        # https://github.com/python/cpython/blob/1d4b6ba19466aba0eb91c4ba01ba509acf18c723/Objects/unicodeobject.c#L9863-L9908    # noqa: E501
        tmp = _empty_string(PY_UNICODE_4BYTE_KIND, 3 * length, data._is_ascii)
        # maxchar should be inside of a list to be pass as argument by reference
        maxchars = [0]
        newlength = unicode_func(data, length, tmp, maxchars)
        maxchar = maxchars[0]
        newkind = _codepoint_to_kind(maxchar)
        res = _empty_string(newkind, newlength, _codepoint_is_ascii(maxchar))
        for i in range(newlength):
            _set_code_point(res, i, _get_code_point(tmp, i))

        return res
```


<a id="case-023"></a>

## 23. `_handle_capital_sigma`

**Classification:** B. **Subtypes:** backward traversal, lookahead or lookbehind, caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Scans before idx backwards, then after idx forwards to resolve final sigma.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2258–2277. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2258-L2277).

### Read sites

- Site 1: lines 2263–2263; derived read; index expression `_get_code_point(data, j)`. Direct or resolved helper-derived FSR read
- Site 2: lines 2271–2271; derived read; index expression `_get_code_point(data, j)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2258–2277. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2258-L2277).

```python
def _handle_capital_sigma(data, length, idx):
    """This is a translation of the function that handles the capital sigma."""
    c = 0
    j = idx - 1
    while j >= 0:
        c = _get_code_point(data, j)
        if not _PyUnicode_IsCaseIgnorable(c):
            break
        j -= 1
    final_sigma = (j >= 0 and _PyUnicode_IsCased(c))
    if final_sigma:
        j = idx + 1
        while j < length:
            c = _get_code_point(data, j)
            if not _PyUnicode_IsCaseIgnorable(c):
                break
            j += 1
        final_sigma = (j == length or (not _PyUnicode_IsCased(c)))

    return 0x3c2 if final_sigma else 0x3c3
```


<a id="case-024"></a>

## 24. `_lower_ucs4`

**Classification:** B. **Subtypes:** lookahead or lookbehind, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

For capital sigma delegates to _handle_capital_sigma, scanning surrounding input codepoints.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2282–2287. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2282-L2287).

### Read sites

- Site 1: lines 2285–2285; derived read; index expression `_handle_capital_sigma(data, length, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2282–2287. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2282-L2287).

```python
def _lower_ucs4(code_point, data, length, idx, mapped):
    """This is a translation of the function that lowers a character."""
    if code_point == 0x3A3:
        mapped[0] = _handle_capital_sigma(data, length, idx)
        return 1
    return _PyUnicode_ToLowerFull(code_point, mapped)
```


<a id="case-025"></a>

## 25. `_gen_unicode_upper_or_lower._do_upper_or_lower`

**Classification:** B. **Subtypes:** mixed access patterns, lookahead or lookbehind, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Upper variant reads forward; lower variant delegates context-sensitive sigma lookbehind/lookahead.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2292–2306. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2292-L2306).

### Read sites

- Site 1: lines 2296–2296; derived read; index expression `_get_code_point(data, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2292–2306. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2292-L2306).

```python
    def _do_upper_or_lower(data, length, res, maxchars):
        k = 0
        for idx in range(length):
            mapped = np.zeros(3, dtype=_Py_UCS4)
            code_point = _get_code_point(data, idx)
            if lower:
                n_res = _lower_ucs4(code_point, data, length, idx, mapped)
            else:
                # might be needed if call _do_upper_or_lower in unicode_upper
                n_res = _PyUnicode_ToUpperFull(code_point, mapped)
            for m in mapped[:n_res]:
                maxchars[0] = max(maxchars[0], m)
                _set_code_point(res, k, m)
                k += 1
        return k
```


<a id="case-026"></a>

## 26. `_unicode_capitalize`

**Classification:** B. **Subtypes:** lookahead or lookbehind, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Reads first codepoint then forwards, but each lowercase sigma invokes context scans before/after current index.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2371–2392. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2371-L2392).

### Read sites

- Site 1: lines 2375–2375; derived read; index expression `_get_code_point(data, 0)`. Direct or resolved helper-derived FSR read
- Site 2: lines 2385–2385; derived read; index expression `_get_code_point(data, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2371–2392. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2371-L2392).

```python
def _unicode_capitalize(data, length, res, maxchars):
    k = 0
    maxchar = 0
    mapped = np.zeros(3, dtype=_Py_UCS4)
    code_point = _get_code_point(data, 0)

    n_res = _PyUnicode_ToTitleFull(code_point, mapped)

    for m in mapped[:n_res]:
        maxchar = max(maxchar, m)
        _set_code_point(res, k, m)
        k += 1
    for idx in range(1, length):
        mapped.fill(0)
        code_point = _get_code_point(data, idx)
        n_res = _lower_ucs4(code_point, data, length, idx, mapped)
        for m in mapped[:n_res]:
            maxchar = max(maxchar, m)
            _set_code_point(res, k, m)
            k += 1
    maxchars[0] = maxchar
    return k
```


<a id="case-027"></a>

## 27. `_unicode_title`

**Classification:** B. **Subtypes:** lookahead or lookbehind, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Forward main loop invokes _lower_ucs4 for cased run, including context-sensitive sigma scans.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2413–2431. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2413-L2431).

### Read sites

- Site 1: lines 2420–2420; derived read; index expression `_get_code_point(data, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2413–2431. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2413-L2431).

```python
def _unicode_title(data, length, res, maxchars):
    """This is a translation of the function that titles a unicode string."""
    k = 0
    previous_cased = False
    mapped = np.empty(3, dtype=_Py_UCS4)
    for idx in range(length):
        mapped.fill(0)
        code_point = _get_code_point(data, idx)
        if previous_cased:
            n_res = _lower_ucs4(code_point, data, length, idx, mapped)
        else:
            n_res = _PyUnicode_ToTitleFull(_Py_UCS4(code_point), mapped)
        for m in mapped[:n_res]:
            maxchar, = maxchars
            maxchars[0] = max(maxchar, m)
            _set_code_point(res, k, m)
            k += 1
        previous_cased = _PyUnicode_IsCased(_Py_UCS4(code_point))
    return k
```


<a id="case-028"></a>

## 28. `_unicode_swapcase`

**Classification:** B. **Subtypes:** lookahead or lookbehind, backward traversal. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Forward main loop lowercase branch delegates context-sensitive sigma scans.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2476–2495. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2476-L2495).

### Read sites

- Site 1: lines 2482–2482; derived read; index expression `_get_code_point(data, idx)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2476–2495. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2476-L2495).

```python
def _unicode_swapcase(data, length, res, maxchars):
    k = 0
    maxchar = 0
    mapped = np.empty(3, dtype=_Py_UCS4)
    for idx in range(length):
        mapped.fill(0)
        code_point = _get_code_point(data, idx)
        if _PyUnicode_IsUppercase(code_point):
            n_res = _lower_ucs4(code_point, data, length, idx, mapped)
        elif _PyUnicode_IsLowercase(code_point):
            n_res = _PyUnicode_ToUpperFull(code_point, mapped)
        else:
            n_res = 1
            mapped[0] = code_point
        for m in mapped[:n_res]:
            maxchar = max(maxchar, m)
            _set_code_point(res, k, m)
            k += 1
    maxchars[0] = maxchar
    return k
```


<a id="case-029"></a>

## 29. `ol_ord.impl`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Requires length1 then fixed index0 read; no traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Numba handwritten native algorithm/code generator; a._data is borrowed FSR on unbox_unicode_str, owner PyObject retained through NRT meminfo. Native-created strings can use same helpers too.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2507–2512. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2507-L2512).

### Read sites

- Site 1: lines 2512–2512; derived read; index expression `_get_code_point(c, 0)`. Direct or resolved helper-derived FSR read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2507–2512. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2507-L2512).

```python
        def impl(c):
            lc = len(c)
            if lc != 1:
                # CPython does TypeError
                raise TypeError("ord() expected a character")
            return _get_code_point(c, 0)
```


<a id="case-030"></a>

## 30. `iternext_unicode`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_native_algorithm`.

**Role:** owning reader.

Single iteration step dereferences caller-managed current iterator index through getitem_impl; normal iterator owner increments monotonically but this function is not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode.py`, lines 2635–2672. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2635-L2672).

### Read sites

- Site 1: lines 2641–2667; derived read; index expression `iterator index`. Resolved getitem_char

### Contextual source excerpts

Omitted from `numba-0.68.0/numba/cpython/unicode.py`: lines 2639–2654, 2664–2669. The original contextual region was lines 2635–2672.

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2635–2638. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2635-L2638).

```python
def iternext_unicode(context, builder, sig, args, result):
    [iterty] = sig.args
    [iter] = args

```

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2655–2663. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2655-L2663).

```python
    # find the length of the string
    strlen = len_impl(builder, (iterobj.data,))

    # find the current index
    index = builder.load(iterobj.index)

    # see if the index is in range
    is_valid = builder.icmp_unsigned('<', index, strlen)
    result.set_valid(is_valid)
```

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 2670–2672. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L2670-L2672).

```python
        # bump index for next cycle
        nindex = cgutils.increment_index(builder, index)
        builder.store(nindex, iterobj.index)
```


<a id="case-031"></a>

## 31. `gettyperecord_impl.impl`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Unicode property convenience overload reads only index0 (len>1 rejected), then passes scalar codepoint to CPython property table. Not a full traversal.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz). Archive SHA-256: `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

**Function source:** `numba-0.68.0/numba/cpython/unicode_support.py`, lines 142–148. Member SHA-256: `d92a40315ab6e427711d7d84f2d6e415b08442cf7ef51b30e13f7506ebd61f3f`.

[Verified immutable function link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode_support.py#L142-L148).

### Read sites

- Site 1: lines 146–146; derived read; index expression `_get_code_point(a,0)`. Fixed-index native read

### Contextual source excerpts

Archive member `numba-0.68.0/numba/cpython/unicode_support.py`, lines 133–151. Member SHA-256: `d92a40315ab6e427711d7d84f2d6e415b08442cf7ef51b30e13f7506ebd61f3f`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode_support.py#L133-L151).

```python
@overload(_PyUnicode_gettyperecord)
def gettyperecord_impl(a):
    """
    Provides a _PyUnicode_gettyperecord binding, for convenience it will accept
    single character strings and code points.
    """
    if isinstance(a, types.UnicodeType):
        from numba.cpython.unicode import _get_code_point

        def impl(a):
            if len(a) > 1:
                msg = "gettyperecord takes a single unicode character"
                raise ValueError(msg)
            code_point = _get_code_point(a, 0)
            data = _gettyperecord_impl(_Py_UCS4(code_point))
            return data
        return impl
    if isinstance(a, types.Integer):
        return lambda a: _gettyperecord_impl(_Py_UCS4(a))
```

Archive member `numba-0.68.0/numba/cpython/unicode_support.py`, lines 142–148. Member SHA-256: `d92a40315ab6e427711d7d84f2d6e415b08442cf7ef51b30e13f7506ebd61f3f`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode_support.py#L142-L148).

```python
        def impl(a):
            if len(a) > 1:
                msg = "gettyperecord takes a single unicode character"
                raise ValueError(msg)
            code_point = _get_code_point(a, 0)
            data = _gettyperecord_impl(_Py_UCS4(code_point))
            return data
```

### Callee analysis

- `_get_code_point` in `numba-0.68.0/numba/cpython/unicode.py`, lines 288–298: Exact frozen sdist source recovered and manually inspected B typed data[i] dereference

Available source context:

- [`_get_code_point`](#helper-001) (`numba-0.68.0/numba/cpython/unicode.py`, lines 288–298).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `_get_code_point`

Archive member `numba-0.68.0/numba/cpython/unicode.py`, lines 288–298. Member SHA-256: `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`. [Verified immutable source link](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L288-L298).

```python
def _get_code_point(a, i):
    if a._kind == PY_UNICODE_1BYTE_KIND:
        return deref_uint8(a._data, i)
    elif a._kind == PY_UNICODE_2BYTE_KIND:
        return deref_uint16(a._data, i)
    elif a._kind == PY_UNICODE_4BYTE_KIND:
        return deref_uint32(a._data, i)
    else:
        # there's also a wchar kind, but that's one of the above,
        # so skipping for this example
        return 0
```
