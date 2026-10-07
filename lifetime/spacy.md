# spacy: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#spacy)

Cython entry directly invokes vendored polyleven on supplied original strings; same threshold-small accepted dense-mismatch pattern and scoped strbuf borrowing as polyleven.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## levenshtein.pyx: 10–27

Actual exposed typed Cython pair/fuzzy wrappers call vendored engine.

Archive member: `spacy-3.8.16/spacy/matcher/levenshtein.pyx`

Member SHA256: `371220e1bc5092dd2e338ececfa46880083439faac91c61548bbc7591069fc27`

[Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz); archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
cdef extern from "polyleven.c":
    int64_t polyleven(PyObject *o1, PyObject *o2, int64_t k)


cpdef int64_t levenshtein(a: str, b: str, k: Optional[int] = None):
    if k is None:
        k = -1
    return polyleven(<PyObject*>a, <PyObject*>b, k)


cpdef bint levenshtein_compare(input_text: str, pattern_text: str, fuzzy: int = -1):
    if fuzzy >= 0:
        max_edits = fuzzy
    else:
        # allow at least two edits (to allow at least one transposition) and up
        # to 30% of the pattern string length
        max_edits = max(2, round(0.3 * len(pattern_text)))
    return levenshtein(input_text, pattern_text, max_edits) <= max_edits
```

## polyleven.c: 49–56

Vendored strbuf DATA/kind/length capture.

Archive member: `spacy-3.8.16/spacy/matcher/polyleven.c`

Member SHA256: `8d6cc95a1e44c334c3a5c1ffe3011f7e8d7a0afea27345d769a7db7d16abce0a`

[Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz); archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.

[Verified permanent source](https://github.com/explosion/spaCy/blob/26b4d1dc04a812f426e4bef3e8a1b6f159d6f048/spacy/matcher/polyleven.c#L49-L56).

```
static void strbuf_init(struct strbuf *s, PyObject *o)
{
    s->ptr = PyUnicode_DATA(o);
    s->kind = PyUnicode_KIND(o);
    s->len = PyUnicode_GET_LENGTH(o);
}

#define strbuf_read(s, i) PyUnicode_READ((s)->kind, (s)->ptr, (i))
```

## polyleven.c: 117–140

Vendored threshold mBLeven reader (original +29 line shift).

Archive member: `spacy-3.8.16/spacy/matcher/polyleven.c`

Member SHA256: `8d6cc95a1e44c334c3a5c1ffe3011f7e8d7a0afea27345d769a7db7d16abce0a`

[Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz); archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.

[Verified permanent source](https://github.com/explosion/spaCy/blob/26b4d1dc04a812f426e4bef3e8a1b6f159d6f048/spacy/matcher/polyleven.c#L117-L140).

```
static int64_t mbleven(PyObject *o1, PyObject *o2, int64_t k)
{
    int pos;
    uint8_t m;
    int64_t i, j, c, r;
    struct strbuf s1, s2;

    strbuf_init(&s1, o1);
    strbuf_init(&s2, o2);

    if (s1.len < s2.len)
        return mbleven(o2, o1, k);

    if (k > 3)
        return -1;

    if (k < s1.len - s2.len)
        return k + 1;

    if (ISASCII(s1.kind) && ISASCII(s2.kind))
        return mbleven_ascii(s1.ptr, s1.len, s2.ptr, s2.len, k);

    pos = MBLEVEN_MATRIX_GET(k, s1.len - s2.len);
    r = k + 1;
```

## polyleven.c: 142–164

Vendored threshold mBLeven reader (original +29 line shift).

Archive member: `spacy-3.8.16/spacy/matcher/polyleven.c`

Member SHA256: `8d6cc95a1e44c334c3a5c1ffe3011f7e8d7a0afea27345d769a7db7d16abce0a`

[Frozen sdist](https://files.pythonhosted.org/packages/69/5d/b0b4cd2f6e8a0470e50f7f0cfc1cea6e2f25572e97fb5d404c7941d5e88a/spacy-3.8.16.tar.gz); archive SHA256 `a3d19da23637cc396b42d22fc33852680f675d8ddcb847d3e2a0d094712d1794`.

[Verified permanent source](https://github.com/explosion/spaCy/blob/26b4d1dc04a812f426e4bef3e8a1b6f159d6f048/spacy/matcher/polyleven.c#L142-L164).

```
    while (MBLEVEN_MATRIX[pos]) {
        m = MBLEVEN_MATRIX[pos++];
        i = j = c = 0;
        while (i < s1.len && j < s2.len) {
            if (strbuf_read(&s1, i) != strbuf_read(&s2, j)) {
                c++;
                if (!m) break;
                if (m & 1) i++;
                if (m & 2) j++;
                m >>= 2;
            } else {
                i++;
                j++;
            }
        }
        c += (s1.len - i) + (s2.len - j);
        r = MIN(r, c);
        if (r < 2) {
            return r;
        }
    }
    return r;
}
```
