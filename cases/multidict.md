# multidict — non-simple Unicode reads

[All packages](README.md)

Version: 7.0.0. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`_ascii_has_upper`](#case-001)
- [`_ci_str_to_identity`](#case-002)

<a id="case-001"></a>

## 1. `_ascii_has_upper`

**Classification:** B. **Subtypes:** lookahead or lookbehind, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Scans from zero in 8-byte blocks, then re-reads a last overlapping word at len-8 for a partial final block; scalar short inputs are forward with early return.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** ASCII only; bytes equal codepoints

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz). Archive SHA-256: `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.

**Function source:** `multidict-7.0.0/multidict/_multilib/identity.h`, lines 85–111. Member SHA-256: `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`.

[Verified immutable function link](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L85-L111).

### Read sites

- Site 1: lines 91–110; derived read; index expression `s[i]; s+i; s+len-8`. Overlap at tail means not a single pass

### Contextual source excerpts

Archive member `multidict-7.0.0/multidict/_multilib/identity.h`, lines 85–111. Member SHA-256: `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`. [Verified immutable source link](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L85-L111).

```c
_ascii_has_upper(const Py_UCS1* s, Py_ssize_t len)
{
    /* Too short for a word.  A compact ASCII str is allocated as its header
       plus len + 1 bytes, so reading a whole word here would run off the end
       of the block, which is what AddressSanitizer reports.  This is also
       what lets the last word below start at len - 8. */
    if (len < 8) {
        for (Py_ssize_t i = 0; i < len; i++) {
            if (s[i] >= 'A' && s[i] <= 'Z') {
                return true;
            }
        }
        return false;
    }
    Py_ssize_t i = 0;
    for (; i + 8 <= len; i += 8) {
        if (_word_has_upper(s + i)) {
            return true;
        }
    }
    /* A last word ending at the end of the key rather than a byte loop: it
       overlaps the previous one when len is not a multiple of 8, and
       re-reading a few bytes costs nothing for a yes/no answer.  Scanning
       the leftover byte by byte instead is what made the eight-byte word
       lose to a four-byte one on short keys. */
    return i < len ? _word_has_upper(s + len - 8) : false;
}
```


<a id="case-002"></a>

## 2. `_ci_str_to_identity`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Passes input DATA to _ascii_has_upper (including overlapping tail read) and conditionally passes it again to _ascii_lower; thus mixed/two passes.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** ASCII fast path only; bytes equal codepoints

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/c4/64/642465a4827331a98ba4ae29f97658be25d1bdcb868872a2f78f7482b507/multidict-7.0.0.tar.gz). Archive SHA-256: `a7fcd089a0af2e0ef053c0d39c22c9ebf2434dddcb91034fd2f59ec99623788e`.

**Function source:** `multidict-7.0.0/multidict/_multilib/identity.h`, lines 160–176. Member SHA-256: `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`.

[Verified immutable function link](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L160-L176).

### Read sites

- Site 1: lines 165–173; derived read; index expression `data[0:len]`. Helper chain, conditional second full pass

### Contextual source excerpts

Archive member `multidict-7.0.0/multidict/_multilib/identity.h`, lines 85–111. Member SHA-256: `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`. [Verified immutable source link](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L85-L111).

```c
_ascii_has_upper(const Py_UCS1* s, Py_ssize_t len)
{
    /* Too short for a word.  A compact ASCII str is allocated as its header
       plus len + 1 bytes, so reading a whole word here would run off the end
       of the block, which is what AddressSanitizer reports.  This is also
       what lets the last word below start at len - 8. */
    if (len < 8) {
        for (Py_ssize_t i = 0; i < len; i++) {
            if (s[i] >= 'A' && s[i] <= 'Z') {
                return true;
            }
        }
        return false;
    }
    Py_ssize_t i = 0;
    for (; i + 8 <= len; i += 8) {
        if (_word_has_upper(s + i)) {
            return true;
        }
    }
    /* A last word ending at the end of the key rather than a byte loop: it
       overlaps the previous one when len is not a multiple of 8, and
       re-reading a few bytes costs nothing for a yes/no answer.  Scanning
       the leftover byte by byte instead is what made the eight-byte word
       lose to a four-byte one on short keys. */
    return i < len ? _word_has_upper(s + len - 8) : false;
}
```

Archive member `multidict-7.0.0/multidict/_multilib/identity.h`, lines 160–176. Member SHA-256: `733b0f1f86281539b12190e5399668758e20bd0bf0f1fe1d6666f7ff5a2dafa0`. [Verified immutable source link](https://github.com/aio-libs/multidict/blob/72f7c3c49503c8c6c0cd4c933257611b6afbed73/multidict/_multilib/identity.h#L160-L176).

```c
_ci_str_to_identity(mod_state* state, PyObject* key)
{
    /* Exact str only: a str subclass may override lower(), and callers rely
       on the override running. */
    if (PyUnicode_CheckExact(key) && PyUnicode_IS_ASCII(key)) {
        Py_ssize_t len = PyUnicode_GET_LENGTH(key);
        const Py_UCS1* data = (const Py_UCS1*)PyUnicode_DATA(key);
        if (!_ascii_has_upper(data, len)) {
            /* The key already is its own identity, so reuse it: no copy, and
               unicode_hash() gets the key's cached hash instead of hashing
               a fresh string. */
            return Py_NewRef(key);
        }
        return _ascii_lower(data, len);
    }
    return _ci_str_call_lower(state, key);
}
```
