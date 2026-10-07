# polyleven: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#polyleven)

Each accepted call creates local strbuf views; same long non-ASCII equal-length strings differing throughout take only bounded reads per finite edit model before rejecting above cutoff, though whole DATA is acquired first.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## polyleven.c: 20–27

strbuf captures full DATA/kind/length in automatic local struct.

Archive member: `polyleven-0.11.0/polyleven.c`

Member SHA256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`

[Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz); archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

[Verified permanent source](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L20-L27).

```
static void strbuf_init(struct strbuf *s, PyObject *o)
{
    s->ptr = PyUnicode_DATA(o);
    s->kind = PyUnicode_KIND(o);
    s->len = PyUnicode_GET_LENGTH(o);
}

#define strbuf_read(s, i) PyUnicode_READ((s)->kind, (s)->ptr, (i))
```

## polyleven.c: 88–111

For k1..3 mBLeven reads borrowed data and stops edit models after bounded mismatches.

Archive member: `polyleven-0.11.0/polyleven.c`

Member SHA256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`

[Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz); archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

[Verified permanent source](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L88-L111).

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

## polyleven.c: 332–351

Dispatch rejects length gap before DATA; small positive threshold enters mBLeven.

Archive member: `polyleven-0.11.0/polyleven.c`

Member SHA256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`

[Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz); archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

[Verified permanent source](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L332-L351).

```
static int64_t levenshtein(PyObject *o1, PyObject *o2, int64_t k)
{
    int64_t len1, len2;

    len1 = PyUnicode_GET_LENGTH(o1);
    len2 = PyUnicode_GET_LENGTH(o2);

    if (len1 < len2)
        return levenshtein(o2, o1, k);

    if (k == 0)
        return PyUnicode_Compare(o1, o2) ? 1 : 0;

    if (0 < k && k < len1 - len2)
        return k + 1;

    if (len2 == 0)
        return len1;

    if (0 < k && k < 4)
```

## polyleven.c: 357–369

Exposed levenshtein argument entry and method registration.

Archive member: `polyleven-0.11.0/polyleven.c`

Member SHA256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`

[Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz); archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

[Verified permanent source](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L357-L369).

```
static PyObject* polyleven_levenshtein(PyObject *self, PyObject *args)
{
    PyObject *o1, *o2;
    int k = -1;
    int64_t ret;

    if (!PyArg_ParseTuple(args, "UU|i", &o1, &o2, &k))
        return NULL;

    ret = levenshtein(o1, o2, k);
    if (ret < 0)
        return NULL;
    if (0 < k && k < ret)
```

## polyleven.c: 113–135

For k1..3 mBLeven reads borrowed data and stops edit models after bounded mismatches.

Archive member: `polyleven-0.11.0/polyleven.c`

Member SHA256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`

[Frozen sdist](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz); archive SHA256 `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

[Verified permanent source](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L113-L135).

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
