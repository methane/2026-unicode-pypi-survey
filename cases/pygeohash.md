# pygeohash — non-simple Unicode reads

[All packages](README.md)

Version: 3.5.1. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`decode_to_doubles`](#case-001)
- [`decode_call`](#case-002)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `decode_to_doubles`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Derived pointer consumer calculates strlen, then visits bytes 0..len once in unrolled pairs; early invalid-character return. Pair batching itself is forward sequential, not arbitrary random access.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** For PyUnicode DATA-origin path exact compact ASCII codepoints equal bytes. Callee also accepts other UTF-8 paths, where byte semantics intentionally validate Base32 alphabet.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

This helper is also called by a strict UTF-8 path; this case describes its use of a pointer derived from PyUnicode_DATA.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/d1/fe/c7ade848a10c697d48f19859ec7a71a992b5597fd6ce8d5f16ba867853d5/pygeohash-3.5.1.tar.gz). Archive SHA-256: `d9a6ed89cfb023e0eba041a06ed676444413450be52e6a3b2c89b4a7908673ec`.

**Function source:** `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 122–186. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`.

[Verified immutable function link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L122-L186).

### Read sites

- Site 1: lines 122–145; length then forward loop; index expression `strlen; i=0;i+1<len;i+=2; data[i],data[i+1]`. Length scan then second forward decode scan.
- Site 2: lines 164–179; tail index; index expression `geohash[i]`. Final odd byte; contiguous after previous pair.

### Contextual source excerpts

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 122–145. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L122-L145).

```c
static int decode_to_doubles(const char *geohash, double *out_lat, double *out_lon,
                             double *out_lat_err, double *out_lon_err) {
    double lat_lo = -90.0, lat_hi = 90.0;
    double lon_lo = -180.0, lon_hi = 180.0;
    double lat_err = 90.0;
    double lon_err = 180.0;
    size_t len = strlen(geohash);

    if (len < 1 || len > 12) {
        PyErr_SetString(PyExc_ValueError, "Geohash must be between 1 and 12 characters long");
        return -1;
    }

    size_t i = 0;
    for (; i + 1 < len; i += 2) {
        // The table guards every byte: non-alphabet bytes (including >= 128)
        // map to -1. Whether an invalid character is detected here or after
        // bisecting the first of the pair is unobservable: the caller discards
        // all interval state when -1 is returned.
        int cd0 = base32_decode_map[(unsigned char)geohash[i]];
        int cd1 = base32_decode_map[(unsigned char)geohash[i + 1]];
        if (cd0 < 0 || cd1 < 0) {
            PyErr_SetString(PyExc_ValueError, "Invalid character in geohash");
            return -1;
```

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 164–186. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L164-L186).

```c
    if (i < len) {
        // odd length: final character, even index -> starts on a longitude bit
        int cd = base32_decode_map[(unsigned char)geohash[i]];
        if (cd < 0) {
            PyErr_SetString(PyExc_ValueError, "Invalid character in geohash");
            return -1;
        }

        double mid;

        lon_err *= 0.5; mid = (lon_lo + lon_hi) * 0.5; if (cd & 16) { lon_lo = mid; } else { lon_hi = mid; }
        lat_err *= 0.5; mid = (lat_lo + lat_hi) * 0.5; if (cd &  8) { lat_lo = mid; } else { lat_hi = mid; }
        lon_err *= 0.5; mid = (lon_lo + lon_hi) * 0.5; if (cd &  4) { lon_lo = mid; } else { lon_hi = mid; }
        lat_err *= 0.5; mid = (lat_lo + lat_hi) * 0.5; if (cd &  2) { lat_lo = mid; } else { lat_hi = mid; }
        lon_err *= 0.5; mid = (lon_lo + lon_hi) * 0.5; if (cd &  1) { lon_lo = mid; } else { lon_hi = mid; }
    }

    *out_lat = (lat_lo + lat_hi) * 0.5;
    *out_lon = (lon_lo + lon_hi) * 0.5;
    *out_lat_err = lat_err;
    *out_lon_err = lon_err;
    return 0;
}
```


<a id="case-002"></a>

## 2. `decode_call`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

ASCII compact input is length-checked by strlen, then decode_to_doubles performs another strlen and codepoint-byte scan.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Compact ASCII only so bytes/codepoints align. Embedded NUL routes to historical parser rejection.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/d1/fe/c7ade848a10c697d48f19859ec7a71a992b5597fd6ce8d5f16ba867853d5/pygeohash-3.5.1.tar.gz). Archive SHA-256: `d9a6ed89cfb023e0eba041a06ed676444413450be52e6a3b2c89b4a7908673ec`.

**Function source:** `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 216–269. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`.

[Verified immutable function link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L216-L269).

### Read sites

- Site 1: lines 249–258; cstring length and handoff; index expression `strlen(geohash); then decode_from_utf8`. Length pass followed by length+decode traversal.

### Contextual source excerpts

Omitted from `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`: lines 230–244, 260–266. The original contextual region was lines 226–269.

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 226–229. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L226-L229).

```c
    if (nargs == 1 && PyUnicode_Check(args[0])) {
        PyObject *hash = args[0];
        PyObject *folded = NULL;
        if (Py_TYPE(hash) != &PyUnicode_Type
```

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 245–259. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L245-L259).

```c
            // A non-str lower() result falls through to decode_cold, where
            // PyArg_ParseTuple raises the same TypeError the old
            // wrapper-then-parser pipeline raised.
        }
        if (Py_TYPE(hash) == &PyUnicode_Type
            && PyUnicode_IS_COMPACT(hash) && PyUnicode_IS_ASCII(hash)) {
            // O(1) interned flags; compact ASCII data is already UTF-8 and the
            // decode table folds A-Z, so the bytes go straight to the walk
            // with no normalization pass and no UTF-8 re-encoding.
            const char *geohash = (const char *)PyUnicode_1BYTE_DATA(hash);
            if ((size_t)PyUnicode_GET_LENGTH(hash) == strlen(geohash)) {
                PyObject *result = decode_from_utf8(geohash, exact);
                Py_XDECREF(folded);
                return result;
            }
```

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 267–269. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L267-L269).

```c
    }
    return decode_cold(args, nargs, NULL, exact);
}
```

### Callee analysis

- `decode_from_utf8 -> decode_to_doubles` in `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 122–185: len=strlen, pair reads geohash[i],geohash[i+1], trailing final byte. B multiple passes, forward pair-unrolled decode after length scan.

Available source context:
Omitted from `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`: lines 126–130, 147–161, 171–182. The original contextual region was lines 122–185.

- [`decode_from_utf8 -> decode_to_doubles`](#helper-001) (`pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 122–125).
- [`decode_from_utf8 -> decode_to_doubles`](#helper-002) (`pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 131–146).
- [`decode_from_utf8 -> decode_to_doubles`](#helper-003) (`pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 162–170).
- [`decode_from_utf8 -> decode_to_doubles`](#helper-004) (`pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 183–185).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `decode_from_utf8 -> decode_to_doubles`

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 122–125. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L122-L125).

```c
static int decode_to_doubles(const char *geohash, double *out_lat, double *out_lon,
                             double *out_lat_err, double *out_lon_err) {
    double lat_lo = -90.0, lat_hi = 90.0;
    double lon_lo = -180.0, lon_hi = 180.0;
```

<a id="helper-002"></a>

### 2. `decode_from_utf8 -> decode_to_doubles`

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 131–146. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L131-L146).

```c
        PyErr_SetString(PyExc_ValueError, "Geohash must be between 1 and 12 characters long");
        return -1;
    }

    size_t i = 0;
    for (; i + 1 < len; i += 2) {
        // The table guards every byte: non-alphabet bytes (including >= 128)
        // map to -1. Whether an invalid character is detected here or after
        // bisecting the first of the pair is unobservable: the caller discards
        // all interval state when -1 is returned.
        int cd0 = base32_decode_map[(unsigned char)geohash[i]];
        int cd1 = base32_decode_map[(unsigned char)geohash[i + 1]];
        if (cd0 < 0 || cd1 < 0) {
            PyErr_SetString(PyExc_ValueError, "Invalid character in geohash");
            return -1;
        }
```

<a id="helper-003"></a>

### 3. `decode_from_utf8 -> decode_to_doubles`

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 162–170. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L162-L170).

```c
        lat_err *= 0.5; mid = (lat_lo + lat_hi) * 0.5; if (cd1 &  1) { lat_lo = mid; } else { lat_hi = mid; }
    }
    if (i < len) {
        // odd length: final character, even index -> starts on a longitude bit
        int cd = base32_decode_map[(unsigned char)geohash[i]];
        if (cd < 0) {
            PyErr_SetString(PyExc_ValueError, "Invalid character in geohash");
            return -1;
        }
```

<a id="helper-004"></a>

### 4. `decode_from_utf8 -> decode_to_doubles`

Archive member `pygeohash-3.5.1/pygeohash/cgeohash/geohash_module.c`, lines 183–185. Member SHA-256: `82e90109d174610afb9bb0072e47b4c2fc3adf5da76cd8945f67cdf13f2aee29`. [Verified immutable source link](https://github.com/wdm0006/pygeohash/blob/af9909bb42eee4755e292d661031f2f85a5b2f08/pygeohash/cgeohash/geohash_module.c#L183-L185).

```c
    *out_lat_err = lat_err;
    *out_lon_err = lon_err;
    return 0;
```
