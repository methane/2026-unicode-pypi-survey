# polyleven — non-simple Unicode reads

[All packages](README.md)

Version: 0.11.0. **4 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`mbleven_ascii`](#case-001)
- [`mbleven`](#case-002)
- [`myers1999_block`](#case-003)
- [`myers1999`](#case-004)

<a id="case-001"></a>

## 1. `mbleven_ascii`

**Classification:** B. **Subtypes:** reset or backtracking, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

For each alternative edit model i=j=0 resets, then input indices advance independently; early breaks/returns possible.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** One-byte PEP393 units; ISASCII macro tests 1BYTE_KIND, so Latin1 too, not UTF8 bytes

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz). Archive SHA-256: `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

**Function source:** `polyleven-0.11.0/polyleven.c`, lines 54–86. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.

[Verified immutable function link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L54-L86).

### Read sites

- Site 1: lines 64–83; derived read; index expression `s1[i],s2[j]`. Repeated model traversal

### Contextual source excerpts

Archive member `polyleven-0.11.0/polyleven.c`, lines 54–86. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L54-L86).

```c
static int64_t mbleven_ascii(char *s1, int64_t len1,
                             char *s2, int64_t len2, int k)
{
    int pos;
    uint8_t m;
    int64_t i, j, c, r;

    pos = MBLEVEN_MATRIX_GET(k, len1 - len2);
    r = k + 1;

    while (MBLEVEN_MATRIX[pos]) {
        m = MBLEVEN_MATRIX[pos++];
        i = j = c = 0;
        while (i < len1 && j < len2) {
            if (s1[i] != s2[j]) {
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
        c += (len1 - i) + (len2 - j);
        r = MIN(r, c);
        if (r < 2) {
            return r;
        }
    }
    return r;
}
```


<a id="case-002"></a>

## 2. `mbleven`

**Classification:** B. **Subtypes:** reset or backtracking, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

DATA captured in strbuf; model alternatives repeatedly reset i=j=0 and compare strbuf_read(s1,i), strbuf_read(s2,j), or use byte helper.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz). Archive SHA-256: `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

**Function source:** `polyleven-0.11.0/polyleven.c`, lines 88–135. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.

[Verified immutable function link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L88-L135).

### Read sites

- Site 1: lines 94–128; derived read; index expression `i,j reset per model`. Repeated codepoint traversals

### Contextual source excerpts

Omitted from `polyleven-0.11.0/polyleven.c`: lines 92–105, 119–120, 130–132. The original contextual region was lines 88–135.

Archive member `polyleven-0.11.0/polyleven.c`, lines 20–27. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L20-L27).

```c
static void strbuf_init(struct strbuf *s, PyObject *o)
{
    s->ptr = PyUnicode_DATA(o);
    s->kind = PyUnicode_KIND(o);
    s->len = PyUnicode_GET_LENGTH(o);
}

#define strbuf_read(s, i) PyUnicode_READ((s)->kind, (s)->ptr, (i))
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 88–91. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L88-L91).

```c
static int64_t mbleven(PyObject *o1, PyObject *o2, int64_t k)
{
    int pos;
    uint8_t m;
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 106–118. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L106-L118).

```c

    if (ISASCII(s1.kind) && ISASCII(s2.kind))
        return mbleven_ascii(s1.ptr, s1.len, s2.ptr, s2.len, k);

    pos = MBLEVEN_MATRIX_GET(k, s1.len - s2.len);
    r = k + 1;

    while (MBLEVEN_MATRIX[pos]) {
        m = MBLEVEN_MATRIX[pos++];
        i = j = c = 0;
        while (i < s1.len && j < s2.len) {
            if (strbuf_read(&s1, i) != strbuf_read(&s2, j)) {
                c++;
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 121–129. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L121-L129).

```c
                if (m & 2) j++;
                m >>= 2;
            } else {
                i++;
                j++;
            }
        }
        c += (s1.len - i) + (s2.len - j);
        r = MIN(r, c);
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 133–135. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L133-L135).

```c
    }
    return r;
}
```


<a id="case-003"></a>

## 3. `myers1999_block`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Outer block b loop repeats complete i=0..s1->len-1 input traversal for each s2 block.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz). Archive SHA-256: `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

**Function source:** `polyleven-0.11.0/polyleven.c`, lines 210–267. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.

[Verified immutable function link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L210-L267).

### Read sites

- Site 1: lines 232–261; derived read; index expression `strbuf_read(s1,i)`. Full s1 pass repeated per b

### Contextual source excerpts

Omitted from `polyleven-0.11.0/polyleven.c`: lines 214–227, 261–264. The original contextual region was lines 210–267.

Archive member `polyleven-0.11.0/polyleven.c`, lines 210–213. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L210-L213).

```c
static int64_t myers1999_block(struct strbuf *s1, struct strbuf *s2,
                               struct blockmap *map)
{
    uint64_t Eq, Xv, Xh, Ph, Mh, Pv, Mv, Last;
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 228–260. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L228-L260).

```c
    memset(Phc, -1, hsize * sizeof(uint64_t));
    memset(Mhc, 0, hsize * sizeof(uint64_t));
    Last = (uint64_t)1 << ((s2->len - 1) % 64);

    for (b = 0; b < vsize; b++) {
        Mv = 0;
        Pv = (uint64_t) -1;
        Score = s2->len;

        for (i = 0; i < s1->len; i++) {
            Eq = blockmap_get(map, b, strbuf_read(s1, i));

            Pb = BIT(Phc[i / 64], i % 64);
            Mb = BIT(Mhc[i / 64], i % 64);

            Xv = Eq | Mv;
            Xh = ((((Eq | Mb) & Pv) + Pv) ^ Pv) | Eq | Mb;

            Ph = Mv | ~ (Xh | Pv);
            Mh = Pv & Xh;

            if (Ph & Last) Score++;
            if (Mh & Last) Score--;

            if ((Ph >> 63) ^ Pb)
                Phc[i / 64] = FLIP(Phc[i / 64], i % 64);

            if ((Mh >> 63) ^ Mb)
                Mhc[i / 64] = FLIP(Mhc[i / 64], i % 64);

            Ph = (Ph << 1) | Pb;
            Mh = (Mh << 1) | Mb;

```

Archive member `polyleven-0.11.0/polyleven.c`, lines 265–267. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L265-L267).

```c
    free(Phc);
    return Score;
}
```


<a id="case-004"></a>

## 4. `myers1999`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Resolved general helper chain first builds map of s2 and then repeats s1 per block in myers1999_block; short one-byte path is A.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/91/c7/e0b3bbe72e0003e5d02726e0d406ea47d523a2aec9c41d831817a8e0bce1/polyleven-0.11.0.tar.gz). Archive SHA-256: `d74d348387cf340051711c0dd6af993b4c264daa78470098de16f4a2b725785c`.

**Function source:** `polyleven-0.11.0/polyleven.c`, lines 306–327. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`.

[Verified immutable function link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L306-L327).

### Read sites

- Site 1: lines 312–327; derived read; index expression `s1,s2 DATA through helpers`. Mixed algorithm branches

### Contextual source excerpts

Archive member `polyleven-0.11.0/polyleven.c`, lines 232–261. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L232-L261).

```c
    for (b = 0; b < vsize; b++) {
        Mv = 0;
        Pv = (uint64_t) -1;
        Score = s2->len;

        for (i = 0; i < s1->len; i++) {
            Eq = blockmap_get(map, b, strbuf_read(s1, i));

            Pb = BIT(Phc[i / 64], i % 64);
            Mb = BIT(Mhc[i / 64], i % 64);

            Xv = Eq | Mv;
            Xh = ((((Eq | Mb) & Pv) + Pv) ^ Pv) | Eq | Mb;

            Ph = Mv | ~ (Xh | Pv);
            Mh = Pv & Xh;

            if (Ph & Last) Score++;
            if (Mh & Last) Score--;

            if ((Ph >> 63) ^ Pb)
                Phc[i / 64] = FLIP(Phc[i / 64], i % 64);

            if ((Mh >> 63) ^ Mb)
                Mhc[i / 64] = FLIP(Mhc[i / 64], i % 64);

            Ph = (Ph << 1) | Pb;
            Mh = (Mh << 1) | Mb;

            Pv = Mh | ~ (Xv | Ph);
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 306–327. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L306-L327).

```c
static int64_t myers1999(PyObject *o1, PyObject *o2)
{
    struct strbuf s1, s2;
    struct blockmap map;
    int64_t ret;

    strbuf_init(&s1, o1);
    strbuf_init(&s2, o2);

    if (s1.len < s2.len)
        return myers1999(o2, o1);

    if (ISASCII(s1.kind) && ISASCII(s2.kind) && s2.len < 65)
        return myers1999_simple(s1.ptr, s1.len, s2.ptr, s2.len);

    if (blockmap_init(&map, &s2))
        return -1;

    ret = myers1999_block(&s1, &s2, &map);
    blockmap_clear(&map);
    return ret;
}
```

Archive member `polyleven-0.11.0/polyleven.c`, lines 306–330. Member SHA-256: `0bc41b54c3e58bc5c96eee377468a894bb74dbeb2f53994fffbbb5614d6a8407`. [Verified immutable source link](https://github.com/fujimotos/polyleven/blob/a9844a4a714951c2fae57020d52a9c513be49e5e/polyleven.c#L306-L330).

```c
static int64_t myers1999(PyObject *o1, PyObject *o2)
{
    struct strbuf s1, s2;
    struct blockmap map;
    int64_t ret;

    strbuf_init(&s1, o1);
    strbuf_init(&s2, o2);

    if (s1.len < s2.len)
        return myers1999(o2, o1);

    if (ISASCII(s1.kind) && ISASCII(s2.kind) && s2.len < 65)
        return myers1999_simple(s1.ptr, s1.len, s2.ptr, s2.len);

    if (blockmap_init(&map, &s2))
        return -1;

    ret = myers1999_block(&s1, &s2, &map);
    blockmap_clear(&map);
    return ret;
}

/*
 * Interface functions
```
