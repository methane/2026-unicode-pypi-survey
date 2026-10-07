# pybase64 — non-simple Unicode reads

[All packages](README.md)

Version: 1.5.0. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`translate`](#case-001)
- [`translate_deprecated`](#case-002)

<a id="case-001"></a>

## 1. `translate`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Input pointer is caller-selected original source chunk (pybase64_decode_impl uses src+=src_slice). Reads increasing byte offsets with SIMD blocks and scalar tail; subrange may begin inside Unicode.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

ASCII standard-alphabet cases may use UTF-8 bytes; custom binary altchars require preservation of Latin1 codepoint bytes (FSR or iterator-to-Latin1 staging).

**Offsets and character semantics:** KIND1 input uses Latin1 codepoint bytes0..255. Standard Base64 alphabet is ASCII, but arbitrary-byte altchars buffers can include bytes>=128 and translate can accept matching Latin1 input characters. Direct UTF-8 substitution changes those successful custom-alphabet cases.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Sequential chunk operation; B range-continuation does not imply a random-access Unicode semantic need.
- parse_alphabet lines84-131 converts Unicode altchars to ASCII but accepts arbitrary length2 binary altchars. To preserve byte mapping, retain Latin1 FSR or iterate codepoints into Latin1 byte buffer before SIMD decode; surrogatepass UTF-8 cannot replace byte-oriented data universally.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz). Archive SHA-256: `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.

**Function source:** `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 190–275. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.

[Verified immutable function link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L190-L275).

### Read sites

- Site 1: lines 190–275; simd and scalar chunk; index expression `pSrc+i; i+=16 blocks then i++ tail`. Forward chunk traversal; no source reset or backward seek.

### Contextual source excerpts

Omitted from `pybase64-1.5.0/src/pybase64/_pybase64.c`: lines 199–250, 260–268. The original contextual region was lines 190–275.

Archive member `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 190–198. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`. [Verified immutable source link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L190-L198).

```c
static void translate(const char* pSrc, char* pDst, size_t len, const char* alphabet, int* has_bad_char)
{
    size_t i = 0U;
    const char c0 = alphabet[0];
    const char c1 = alphabet[1];
    const char replace_plus = ((c0 != '/') && (c0 != '+')) ? c0 : c1;
    const char replace_slash = ((c1 != '/') && (c1 != '+')) ? c1 : c0;

    (void)has_bad_char;
```

Archive member `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 251–259. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`. [Verified immutable source link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L251-L259).

```c
    }
#endif

    for (; i < len; ++i) {
        const char cs = pSrc[i];
        char cd;

        if (cs == c0) {
            cd = '+';
```

Archive member `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 269–275. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`. [Verified immutable source link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L269-L275).

```c
        }
        else {
            cd = cs;
        }
        pDst[i] = cd;
    }
}
```


<a id="case-002"></a>

## 2. `translate_deprecated`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Input pointer is caller-selected original source chunk (pybase64_decode_impl uses src+=src_slice). Reads increasing byte offsets with SIMD blocks and scalar tail; subrange may begin inside Unicode.

This is a monotonic continuation of a codepoint stream. Its nonzero entry position makes it B under the full-string definition; it does not, by itself, require random access. A codepoint iterator can preserve continuation state.

ASCII standard-alphabet cases may use UTF-8 bytes; custom binary altchars require preservation of Latin1 codepoint bytes (FSR or iterator-to-Latin1 staging).

**Offsets and character semantics:** KIND1 input uses Latin1 codepoint bytes0..255. Standard Base64 alphabet is ASCII, but arbitrary-byte altchars buffers can include bytes>=128 and translate can accept matching Latin1 input characters. Direct UTF-8 substitution changes those successful custom-alphabet cases.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

- Sequential chunk operation; B range-continuation does not imply a random-access Unicode semantic need.
- parse_alphabet lines84-131 converts Unicode altchars to ASCII but accepts arbitrary length2 binary altchars. To preserve byte mapping, retain Latin1 FSR or iterate codepoints into Latin1 byte buffer before SIMD decode; surrogatepass UTF-8 cannot replace byte-oriented data universally.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/d7/65/c513eab7211590250f729a06aacc0bc95eaf760b9235666e933d200105d0/pybase64-1.5.0.tar.gz). Archive SHA-256: `545ab2a433769e3b8e1ce2b4f7b07218bbde202f4954fbfe52948b2522120727`.

**Function source:** `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 277–371. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`.

[Verified immutable function link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L277-L371).

### Read sites

- Site 1: lines 277–371; simd and scalar chunk; index expression `pSrc+i; i+=16 blocks then i++ tail`. Forward chunk traversal; no source reset or backward seek.

### Contextual source excerpts

Omitted from `pybase64-1.5.0/src/pybase64/_pybase64.c`: lines 286–343, 353–363. The original contextual region was lines 277–371.

Archive member `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 277–285. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`. [Verified immutable source link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L277-L285).

```c
static void translate_deprecated(const char* pSrc, char* pDst, size_t len, const char* alphabet, int* has_bad_char)
{
    size_t i = 0U;
    const char c0 = alphabet[0];
    const char c1 = alphabet[1];
    int input_has_plus = 0;
    int input_has_slash = 0;

#ifdef __SSE2__
```

Archive member `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 344–352. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`. [Verified immutable source link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L344-L352).

```c
    }
#endif

    for (; i < len; ++i) {
        const char cs = pSrc[i];
        char cd;

        if (cs == c0) {
            cd = '+';
```

Archive member `pybase64-1.5.0/src/pybase64/_pybase64.c`, lines 364–371. Member SHA-256: `6ee473222de077c502fcb28f3df3e405c8ee5374c30291e6f99ecd3647ecc472`. [Verified immutable source link](https://github.com/mayeut/pybase64/blob/cbcf6af196611a41cb1db38dd287f6b692817d14/src/pybase64/_pybase64.c#L364-L371).

```c
        }
        else {
            cd = cs;
        }
        pDst[i] = cd;
    }
    *has_bad_char |= input_has_slash | input_has_plus;
}
```
