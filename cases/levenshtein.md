# levenshtein — non-simple Unicode reads

[All packages](README.md)

Version: 0.27.5. **7 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`lev_quick_median`](#case-001)
- [`lev_greedy_median`](#case-002)
- [`finish_distance_computations`](#case-003)
- [`lev_median_improve`](#case-004)
- [`lev_set_median`](#case-005)
- [`lev_edit_seq_distance`](#case-006)
- [`lev_set_distance`](#case-007)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `lev_quick_median`

**Classification:** B. **Subtypes:** a subset starting after position zero, multiple passes, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Constructs symbol map, then for each target position reads proportional interior span istart+1..iend-1 plus fractional endpoints s1[istart],s1[iend-1]; spans/endpoints can overlap and start partway.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 98–189. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L98-L189).

### Read sites

- Site 1: lines 119–121; derived read; index expression `SymMap(strings)`. Initial full source pass
- Site 2: lines 123–171; derived read; index expression `s1[k],s1[istart],s1[iend-1]`. Caller-computed proportional input ranges

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`: lines 102–114, 133–145, 155–157. The original contextual region was lines 98–171.
Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`: lines 102–114, 133–145, 155–157, 170–186. The original contextual region was lines 98–189.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 98–101. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L98-L101).

```cpp
std::vector<uint32_t> lev_quick_median(const std::vector<RF_String>& strings,
                                       const std::vector<double>& weights)
{
    std::vector<uint32_t> median; /* the resulting string */
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 115–132. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L115-L132).

```cpp
    if (median.empty()) return median;

    /* find the symbol set;
     * now an empty symbol set is really a failure */
    SymMap symmap(strings);

    for (size_t j = 0; j < median.size(); j++) {
        /* clear the symbol probabilities */
        symmap.clear();

        /* let all strings vote */
        for (size_t i = 0; i < strings.size(); i++) {
            visit(strings[i], [&](auto s1) {
                double weighti = weights[i];
                size_t lengthi = (size_t)s1.size();
                if (lengthi == 0) return;
                double start = (double)lengthi / ml * (double)j;
                double end = start + (double)lengthi / ml;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 146–154. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L146-L154).

```cpp
                    p->s += weighti;
                }
                /* the initial fraction */
                {
                    uint32_t c = static_cast<uint32_t>(s1[istart]);
                    int key = (c + (c >> 7)) & 0xff;
                    HQItem* p = symmap.get() + key;
                    while (p->c != c)
                        p = p->n;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 158–171. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L158-L171).

```cpp
                 * actually belong here.
                 * this strategy works also when istart+1 == iend (i.e., everything
                 * happens inside a one character) */
                {
                    uint32_t c = static_cast<uint32_t>(s1[iend - 1]);
                    int key = (c + (c >> 7)) & 0xff;
                    HQItem* p = symmap.get() + key;
                    while (p->c != c)
                        p = p->n;
                    p->s -= weighti * ((double)iend - end);
                }
            });
        }

```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 98–101. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L98-L101).

```cpp
std::vector<uint32_t> lev_quick_median(const std::vector<RF_String>& strings,
                                       const std::vector<double>& weights)
{
    std::vector<uint32_t> median; /* the resulting string */
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 115–132. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L115-L132).

```cpp
    if (median.empty()) return median;

    /* find the symbol set;
     * now an empty symbol set is really a failure */
    SymMap symmap(strings);

    for (size_t j = 0; j < median.size(); j++) {
        /* clear the symbol probabilities */
        symmap.clear();

        /* let all strings vote */
        for (size_t i = 0; i < strings.size(); i++) {
            visit(strings[i], [&](auto s1) {
                double weighti = weights[i];
                size_t lengthi = (size_t)s1.size();
                if (lengthi == 0) return;
                double start = (double)lengthi / ml * (double)j;
                double end = start + (double)lengthi / ml;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 146–154. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L146-L154).

```cpp
                    p->s += weighti;
                }
                /* the initial fraction */
                {
                    uint32_t c = static_cast<uint32_t>(s1[istart]);
                    int key = (c + (c >> 7)) & 0xff;
                    HQItem* p = symmap.get() + key;
                    while (p->c != c)
                        p = p->n;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 158–169. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L158-L169).

```cpp
                 * actually belong here.
                 * this strategy works also when istart+1 == iend (i.e., everything
                 * happens inside a one character) */
                {
                    uint32_t c = static_cast<uint32_t>(s1[iend - 1]);
                    int key = (c + (c >> 7)) & 0xff;
                    HQItem* p = symmap.get() + key;
                    while (p->c != c)
                        p = p->n;
                    p->s -= weighti * ((double)iend - end);
                }
            });
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.cpp`, lines 187–189. Member SHA-256: `e044fc6a212ba79686fd1c9b8cb64c6182d751f29e058c9930ef14a4eed44509`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.cpp#L187-L189).

```cpp

    return median;
}
```


<a id="case-002"></a>

## 2. `lev_greedy_median`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

make_symlist initial read; then repeatedly traverses every string for each candidate symbol and median position and recomputes rows using s1[k-1].

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 144–249. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L144-L249).

### Read sites

- Site 1: lines 147–148; derived read; index expression `make_symlist(strings)`. Initial full read
- Site 2: lines 182–239; derived read; index expression `ch:s1; s1[k-1]`. Repeated full passes inside candidate/position loops

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 153–177, 190–202, 212–223, 241–246. The original contextual region was lines 144–249.
Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 190–202, 212–223. The original contextual region was lines 180–240.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 144–149. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L144-L149).

```cpp
static inline std::vector<uint32_t> lev_greedy_median(const std::vector<RF_String>& strings,
                                                      const std::vector<double>& weights)
{
    /* find all symbols */
    std::vector<uint32_t> symlist = make_symlist(strings);
    if (symlist.empty()) return {};
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 144–152. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L144-L152).

```cpp
static inline std::vector<uint32_t> lev_greedy_median(const std::vector<RF_String>& strings,
                                                      const std::vector<double>& weights)
{
    /* find all symbols */
    std::vector<uint32_t> symlist = make_symlist(strings);
    if (symlist.empty()) return {};

    /* allocate and initialize per-string matrix rows and a common work buffer */
    std::vector<std::unique_ptr<size_t[]>> rows(strings.size());
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 178–189. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L178-L189).

```cpp
        mediandist[0] += strings[i].length + weights[i];

    /* build up the approximate median string symbol by symbol
     * XXX: we actually exit on break below, but on the same condition */
    for (size_t len = 1; len <= stoplen; len++) {
        uint32_t symbol = 0;
        double minminsum = std::numeric_limits<double>::max();
        row[0] = len;
        /* iterate over all symbols we may want to add */
        for (size_t j = 0; j < symlist.size(); j++) {
            double totaldist = 0.0;
            double minsum = 0.0;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 203–211. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L203-L211).

```cpp
                        if (x > *p + 1) x = *p + 1;
                        if (x < min) min = x;
                    }
                    minsum += (double)min * weights[i];
                    totaldist += (double)x * weights[i];
                });
            }
            /* is this symbol better than all the others? */
            if (minsum < minminsum) {
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 224–240. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L224-L240).

```cpp
        /* now the best symbol is known, so recompute all matrix rows for this
         * one */
        symbol = median[len - 1];
        for (size_t i = 0; i < strings.size(); i++)
            visit(strings[i], [&](auto s1) {
                size_t* oldrow = rows[i].get();
                /* compute a row of Levenshtein matrix */
                for (size_t k = 1; k <= (size_t)s1.size(); k++) {
                    size_t c1 = oldrow[k] + 1;
                    size_t c2 = row[k - 1] + 1;
                    size_t c3 = oldrow[k - 1] + (symbol != s1[k - 1]);
                    row[k] = c2 > c3 ? c3 : c2;
                    if (row[k] > c1) row[k] = c1;
                }
                memcpy(oldrow, row.get(), (s1.size() + 1) * sizeof(size_t));
            });
    }
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 247–249. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L247-L249).

```cpp
    median.resize(bestlen);
    return median;
}
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 180–189. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L180-L189).

```cpp
    /* build up the approximate median string symbol by symbol
     * XXX: we actually exit on break below, but on the same condition */
    for (size_t len = 1; len <= stoplen; len++) {
        uint32_t symbol = 0;
        double minminsum = std::numeric_limits<double>::max();
        row[0] = len;
        /* iterate over all symbols we may want to add */
        for (size_t j = 0; j < symlist.size(); j++) {
            double totaldist = 0.0;
            double minsum = 0.0;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 203–211. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L203-L211).

```cpp
                        if (x > *p + 1) x = *p + 1;
                        if (x < min) min = x;
                    }
                    minsum += (double)min * weights[i];
                    totaldist += (double)x * weights[i];
                });
            }
            /* is this symbol better than all the others? */
            if (minsum < minminsum) {
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 224–240. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L224-L240).

```cpp
        /* now the best symbol is known, so recompute all matrix rows for this
         * one */
        symbol = median[len - 1];
        for (size_t i = 0; i < strings.size(); i++)
            visit(strings[i], [&](auto s1) {
                size_t* oldrow = rows[i].get();
                /* compute a row of Levenshtein matrix */
                for (size_t k = 1; k <= (size_t)s1.size(); k++) {
                    size_t c1 = oldrow[k] + 1;
                    size_t c2 = row[k - 1] + 1;
                    size_t c3 = oldrow[k - 1] + (symbol != s1[k - 1]);
                    row[k] = c2 > c3 ? c3 : c2;
                    if (row[k] > c1) row[k] = c1;
                }
                memcpy(oldrow, row.get(), (s1.size() + 1) * sizeof(size_t));
            });
    }
```


<a id="case-003"></a>

## 3. `finish_distance_computations`

**Classification:** B. **Subtypes:** backward traversal, multiple passes, caller-provided start or range. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Removes common suffix from typed input range, then re-traverses s2 for each source candidate position; shortened s1 may start at offset supplied by caller.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Exact recovered common_impl.hpp confirms reverse suffix comparison before repeated residual range scans.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 257–316. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L257-L316).

### Read sites

- Site 1: lines 273–278; derived read; index expression `remove_common_suffix(s1_temp,s2)`. Backward suffix access
- Site 2: lines 295–309; derived read; index expression `s1_temp[i], for ch2:s2`. Repeated s2 passes

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 261–268, 283–290, 306–313. The original contextual region was lines 257–316.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 257–260. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L257-L260).

```cpp
static inline double finish_distance_computations(const Range<uint32_t*>& string1,
                                                  const std::vector<RF_String>& strings,
                                                  const std::vector<double>& weights,
                                                  std::vector<std::unique_ptr<size_t[]>>& rows,
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 269–282. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L269-L282).

```cpp
    }

    /* iterate through the strings and sum the distances */
    for (size_t j = 0; j < strings.size(); j++) {
        visit(strings[j], [&](auto s2) {
            size_t* rowi = rows[j].get(); /* current row */
            auto s1_temp = string1;       /* temporary string for suffix stripping */

            /* strip common suffix (prefix CAN'T be stripped) */
            rapidfuzz::detail::remove_common_suffix(s1_temp, s2);

            /* catch trivial cases */
            if (s1_temp.empty()) {
                distsum += (double)rowi[(size_t)s2.size()] * weights[j];
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 291–305. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L291-L305).

```cpp

            /* complete the matrix */
            std::copy_n(rowi, s2.size() + 1, row.get());

            for (size_t i = 0; i < (size_t)s1_temp.size(); i++) {
                auto ch1 = s1_temp[i];
                size_t* p = row.get() + 1;
                size_t D = i + 1 + offset;
                size_t x = D;
                for (auto ch2 : s2) {
                    size_t c3 = --D + (ch1 != ch2);
                    x++;
                    if (x > c3) x = c3;
                    D = *p;
                    D++;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 314–316. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L314-L316).

```cpp

    return distsum;
}
```

### Callee analysis

- `remove_common_suffix` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/details/common_impl.hpp`, lines 64–73: Exact frozen sdist source recovered and manually inspected B reverse iterators rbegin/rend

Available source context:

- [`remove_common_suffix`](#helper-001) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/details/common_impl.hpp`, lines 64–73).

<a id="case-004"></a>

## 4. `lev_median_improve`

**Classification:** B. **Subtypes:** multiple passes, caller-provided start or range, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Initial bulk copy of string, make_symlist pass, then repeatedly calls finish_distance_computations over varying median offsets and reads each FSR input s1[k-1] for each pos.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 336–461. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L336-L461).

### Read sites

- Site 1: lines 340–364; derived read; index expression `make_symlist; std::copy(begin,end)`. Initial reads
- Site 2: lines 370–454; derived read; index expression `s1[k-1]; finish_distance_computations`. Repeated FSR reads via perturbation loops

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 340–342, 380–394, 404–426, 436–438, 456–458. The original contextual region was lines 336–461.
Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 397–399. The original contextual region was lines 377–414.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 336–368. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L336-L368).

```cpp
static inline std::vector<uint32_t> lev_median_improve(const RF_String& string,
                                                       const std::vector<RF_String>& strings,
                                                       const std::vector<double>& weights)
{
    /* find all symbols */
    std::vector<uint32_t> symlist = make_symlist(strings);
    if (symlist.empty()) return {};

    /* allocate and initialize per-string matrix rows and a common work buffer */
    std::vector<std::unique_ptr<size_t[]>> rows(strings.size());
    size_t maxlen = (size_t)string.length;
    for (size_t i = 0; i < strings.size(); i++) {
        size_t leni = (size_t)strings[i].length;
        if (leni > maxlen) maxlen = leni;
        rows[i] = std::make_unique<size_t[]>(leni + 1);
        std::iota(rows[i].get(), rows[i].get() + leni + 1, 0);
    }

    size_t stoplen = 2 * maxlen + 1;
    auto row = std::make_unique<size_t[]>(stoplen + 2);

    /* initialize median to given string */
    auto _median = std::make_unique<uint32_t[]>(stoplen + 1);
    uint32_t* median = _median.get() + 1; /* we need -1st element for insertions at pos 0 */
    size_t medlen = (size_t)string.length;

    visit(string, [&](auto s1) {
        std::copy(std::begin(s1), std::end(s1), median);
    });

    double minminsum =
        finish_distance_computations(Range(median, median + medlen), strings, weights, rows, row);

```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 336–339. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L336-L339).

```cpp
static inline std::vector<uint32_t> lev_median_improve(const RF_String& string,
                                                       const std::vector<RF_String>& strings,
                                                       const std::vector<double>& weights)
{
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 343–379. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L343-L379).

```cpp

    /* allocate and initialize per-string matrix rows and a common work buffer */
    std::vector<std::unique_ptr<size_t[]>> rows(strings.size());
    size_t maxlen = (size_t)string.length;
    for (size_t i = 0; i < strings.size(); i++) {
        size_t leni = (size_t)strings[i].length;
        if (leni > maxlen) maxlen = leni;
        rows[i] = std::make_unique<size_t[]>(leni + 1);
        std::iota(rows[i].get(), rows[i].get() + leni + 1, 0);
    }

    size_t stoplen = 2 * maxlen + 1;
    auto row = std::make_unique<size_t[]>(stoplen + 2);

    /* initialize median to given string */
    auto _median = std::make_unique<uint32_t[]>(stoplen + 1);
    uint32_t* median = _median.get() + 1; /* we need -1st element for insertions at pos 0 */
    size_t medlen = (size_t)string.length;

    visit(string, [&](auto s1) {
        std::copy(std::begin(s1), std::end(s1), median);
    });

    double minminsum =
        finish_distance_computations(Range(median, median + medlen), strings, weights, rows, row);

    /* sequentially try perturbations on all positions */
    for (size_t pos = 0; pos <= medlen;) {
        uint32_t orig_symbol, symbol;
        LevEditType operation;
        double sum;

        symbol = median[pos];
        operation = LEV_EDIT_KEEP;
        /* IF pos < medlength: FOREACH symbol: try to replace the symbol
         * at pos, if some lower the total distance, chooste the best */
        if (pos < medlen) {
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 395–403. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L395-L403).

```cpp
         * distance, chooste the best (increase medlen)
         * We simulate insertion by replacing the character at pos-1 */
        orig_symbol = *(median + pos - 1);
        for (size_t j = 0; j < symlist.size(); j++) {
            *(median + pos - 1) = symlist[j];
            sum = finish_distance_computations(Range(median + pos - 1, median + medlen), strings, weights,
                                               rows, row);
            if (sum < minminsum) {
                minminsum = sum;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 427–435. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L427-L435).

```cpp
            break;

        case LEV_EDIT_DELETE:
            memmove(median + pos, median + pos + 1, (medlen - pos - 1) * sizeof(uint32_t));
            medlen--;
            break;

        default: break;
        }
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 439–455. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L439-L455).

```cpp
            symbol = median[pos];
            row[0] = pos + 1;

            for (size_t i = 0; i < strings.size(); i++) {
                visit(strings[i], [&](auto s1) {
                    size_t* oldrow = rows[i].get();
                    /* compute a row of Levenshtein matrix */
                    for (size_t k = 1; k <= (size_t)s1.size(); k++) {
                        size_t c1 = oldrow[k] + 1;
                        size_t c2 = row[k - 1] + 1;
                        size_t c3 = oldrow[k - 1] + (symbol != s1[k - 1]);
                        row[k] = c2 > c3 ? c3 : c2;
                        if (row[k] > c1) row[k] = c1;
                    }
                    std::copy_n(row.get(), s1.size() + 1, oldrow);
                });
            }
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 459–461. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L459-L461).

```cpp

    return std::vector<uint32_t>(median, median + medlen);
}
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 377–396. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L377-L396).

```cpp
        /* IF pos < medlength: FOREACH symbol: try to replace the symbol
         * at pos, if some lower the total distance, chooste the best */
        if (pos < medlen) {
            orig_symbol = median[pos];
            for (size_t j = 0; j < symlist.size(); j++) {
                if (symlist[j] == orig_symbol) continue;
                median[pos] = symlist[j];
                sum = finish_distance_computations(Range(median + pos, median + medlen), strings, weights,
                                                   rows, row);
                if (sum < minminsum) {
                    minminsum = sum;
                    symbol = symlist[j];
                    operation = LEV_EDIT_REPLACE;
                }
            }
            median[pos] = orig_symbol;
        }
        /* FOREACH symbol: try to add it at pos, if some lower the total
         * distance, chooste the best (increase medlen)
         * We simulate insertion by replacing the character at pos-1 */
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 400–414. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L400-L414).

```cpp
            sum = finish_distance_computations(Range(median + pos - 1, median + medlen), strings, weights,
                                               rows, row);
            if (sum < minminsum) {
                minminsum = sum;
                symbol = symlist[j];
                operation = LEV_EDIT_INSERT;
            }
        }
        *(median + pos - 1) = orig_symbol;
        /* IF pos < medlen: try to delete the symbol at pos, if it lowers
         * the total distance remember it (decrease medlen) */
        if (pos < medlen) {
            sum = finish_distance_computations(Range(median + pos + 1, median + medlen), strings, weights,
                                               rows, row);
            if (sum < minminsum) {
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 437–457. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L437-L457).

```cpp
        /* now the result is known, so recompute all matrix rows and move on */
        if (operation != LEV_EDIT_DELETE) {
            symbol = median[pos];
            row[0] = pos + 1;

            for (size_t i = 0; i < strings.size(); i++) {
                visit(strings[i], [&](auto s1) {
                    size_t* oldrow = rows[i].get();
                    /* compute a row of Levenshtein matrix */
                    for (size_t k = 1; k <= (size_t)s1.size(); k++) {
                        size_t c1 = oldrow[k] + 1;
                        size_t c2 = row[k - 1] + 1;
                        size_t c3 = oldrow[k - 1] + (symbol != s1[k - 1]);
                        row[k] = c2 > c3 ? c3 : c2;
                        if (row[k] > c1) row[k] = c1;
                    }
                    std::copy_n(row.get(), s1.size() + 1, oldrow);
                });
            }
            pos++;
        }
```


<a id="case-005"></a>

## 5. `lev_set_median`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Repeated cached metric readers: CachedLevenshtein/CachedIndel copy original candidate and build its pattern from the same buffer; each query uses affix/mBLeven/bitvector comparisons, including reset or reverse suffix paths.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Multiple calls per string are visible; exact codepoint access behavior depends on scorer implementation.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 478–526. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L478-L526).

### Read sites

- Site 1: lines 487–524; pointer handoff; index expression `s1/s2 ranges`. Scorer and bulk vector copy

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 482, 493–494, 515–518. The original contextual region was lines 478–526.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 478–481. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L478-L481).

```cpp
static inline std::vector<uint32_t> lev_set_median(const std::vector<RF_String>& strings,
                                                   const std::vector<double>& weights)
{
    if (strings.empty()) return {};
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 483–492. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L483-L492).

```cpp
    size_t minidx = 0;
    double mindist = std::numeric_limits<double>::max();
    std::vector<long int> distances(strings.size() * (strings.size() - 1) / 2, 0xff);

    for (size_t i = 0; i < strings.size(); i++) {
        visit(strings[i], [&](auto s1) {
            /* deduction guides are broken here on msvc */
            rapidfuzz::CachedLevenshtein<typename decltype(s1)::value_type> scorer(s1);
            double dist = 0.0;

```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 495–514. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L495-L514).

```cpp
            for (; j < i && dist < mindist; j++) {
                size_t dindex = (i - 1) * (i - 2) / 2 + j;
                long int d;
                if (distances[dindex] >= 0)
                    d = distances[dindex];
                else
                    d = (size_t)visit(strings[j], [&](auto s2) {
                        return scorer.distance(s2);
                    });
                dist += weights[j] * (double)d;
            }
            j++; /* no need to compare item with itself */
            /* above diagonal */
            for (; j < strings.size() && dist < mindist; j++) {
                size_t dindex = (j - 1) * (j - 2) / 2 + i;
                distances[dindex] = visit(strings[j], [&](auto s2) {
                    return scorer.distance(s2);
                });
                dist += weights[j] * (double)distances[dindex];
            }
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 519–526. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L519-L526).

```cpp
            }
        });
    }

    return visit(strings[minidx], [&](auto s1) {
        return std::vector<uint32_t>(std::begin(s1), std::end(s1));
    });
}
```

### Callee analysis

- `CachedLevenshtein::CachedLevenshtein` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434: Exact frozen sdist source recovered and manually inspected B copies s1 plus original PM
- `CachedIndel::_distance` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179: Exact frozen sdist source recovered and manually inspected Delegates LCSseq similarity over borrowed query
- `lcs_seq_similarity` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403: Exact frozen sdist source recovered and manually inspected B reverse affix and retry/reset variants

Available source context:

- [`CachedLevenshtein::CachedLevenshtein`](#helper-002) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434).
- [`CachedIndel::_distance`](#helper-003) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179).
- [`lcs_seq_similarity`](#helper-004) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403).

<a id="case-006"></a>

## 6. `lev_edit_seq_distance`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Repeated cached metric readers: CachedLevenshtein/CachedIndel copy original candidate and build its pattern from the same buffer; each query uses affix/mBLeven/bitvector comparisons, including reset or reverse suffix paths.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

Do not mislabel backward vector-of-strings traversal as Unicode backward traversal.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 553–626. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L553-L626).

### Read sites

- Site 1: lines 600–622; pointer handoff; index expression `typed ranges s1,s2`. Scorer handoff

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 557–595, 615–623. The original contextual region was lines 553–626.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 553–556. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L553-L556).

```cpp
static inline double lev_edit_seq_distance(const std::vector<RF_String>& strings1,
                                           const std::vector<RF_String>& strings2)
{
    if (strings1.size() > strings2.size()) return lev_edit_seq_distance(strings2, strings1);
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 596–614. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L596-L614).

```cpp
        auto strings2_it = strings2_start;
        double D = (double)i;
        double x = (double)i + 1.0;

        visit(strings1[i], [&](auto s1) {
            /* deduction guides are broken here on msvc */
            rapidfuzz::CachedIndel<typename decltype(s1)::value_type> scorer(s1);

            while (p != end) {
                size_t l = strings1[i].length + strings2_it->length;
                double q;
                if (l == 0)
                    q = D;
                else {
                    size_t d = visit(*strings2_it, [&](auto s2) {
                        return scorer.distance(s2);
                    });
                    strings2_it++;
                    q = D + 2.0 / (double)l * (double)d;
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 624–626. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L624-L626).

```cpp

    return *last;
}
```

### Callee analysis

- `CachedLevenshtein::CachedLevenshtein` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434: Exact frozen sdist source recovered and manually inspected B copies s1 plus original PM
- `CachedIndel::_distance` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179: Exact frozen sdist source recovered and manually inspected Delegates LCSseq similarity over borrowed query
- `lcs_seq_similarity` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403: Exact frozen sdist source recovered and manually inspected B reverse affix and retry/reset variants

Available source context:

- [`CachedLevenshtein::CachedLevenshtein`](#helper-002) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434).
- [`CachedIndel::_distance`](#helper-003) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179).
- [`lcs_seq_similarity`](#helper-004) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403).

<a id="case-007"></a>

## 7. `lev_set_distance`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Repeated cached metric readers: CachedLevenshtein/CachedIndel copy original candidate and build its pattern from the same buffer; each query uses affix/mBLeven/bitvector comparisons, including reset or reverse suffix paths.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/81/ab/d55fdebfdee7605df174913708d44f75dfec0ec5e4e5fd8e978bb88897eb/levenshtein-0.27.5.tar.gz). Archive SHA-256: `22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08`.

**Function source:** `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 649–688. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`.

[Verified immutable function link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L649-L688).

### Read sites

- Site 1: lines 665–684; pointer handoff; index expression `typed s1,s2 ranges`. Scorer handoffs

### Contextual source excerpts

Omitted from `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`: lines 653–660, 675–676. The original contextual region was lines 649–688.

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 649–652. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L649-L652).

```cpp
static inline double lev_set_distance(const std::vector<RF_String>& strings1,
                                      const std::vector<RF_String>& strings2)
{
    /* catch trivial cases */
```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 661–674. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L661-L674).

```cpp

    auto dists = std::make_unique<double[]>(strings1.size() * strings2.size());
    double* r = dists.get();

    for (const auto& str2 : strings2)
        visit(str2, [&](auto s1) {
            /* deduction guides are broken here on msvc */
            rapidfuzz::CachedIndel<typename decltype(s1)::value_type> scorer(s1);
            for (const auto& str1 : strings1)
                *(r++) = visit(str1, [&](auto s2) {
                    return scorer.normalized_distance(s2);
                });
        });

```

Archive member `levenshtein-0.27.5/src/Levenshtein/Levenshtein-c/_levenshtein.hpp`, lines 677–688. Member SHA-256: `7bf4b761b8b857dc488ab14e799049a30b914d035e21d3ba1ebe31f917beb478`. [Verified immutable source link](https://github.com/rapidfuzz/Levenshtein/blob/1efe2de821cbf33dbf5a100fc1532b35f9f4df4a/src/Levenshtein/Levenshtein-c/_levenshtein.hpp#L677-L688).

```cpp

    /* sum the set distance */
    double sum = (double)(strings2.size() - strings1.size());
    for (size_t j = 0; j < strings1.size(); j++) {
        size_t i = map[j];
        sum += 2.0 * visitor(strings1[j], strings2[i], [](auto s1, auto s2) {
                   return rapidfuzz::indel_normalized_distance(s1, s2);
               });
    }

    return sum;
}
```

### Callee analysis

- `CachedLevenshtein::CachedLevenshtein` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434: Exact frozen sdist source recovered and manually inspected B copies s1 plus original PM
- `CachedIndel::_distance` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179: Exact frozen sdist source recovered and manually inspected Delegates LCSseq similarity over borrowed query
- `lcs_seq_similarity` in `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403: Exact frozen sdist source recovered and manually inspected B reverse affix and retry/reset variants

Available source context:

- [`CachedLevenshtein::CachedLevenshtein`](#helper-002) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434).
- [`CachedIndel::_distance`](#helper-003) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179).
- [`lcs_seq_similarity`](#helper-004) (`levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `remove_common_suffix`

Archive member `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/details/common_impl.hpp`, lines 64–73. Member SHA-256: `2d59c0f890ded1668a399e1b0d671727054540e9ed5ea3a9ba365483e1721293`. [Verified immutable source link](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/6c10b68930df73bfe5679720e4008518ba4265b1/rapidfuzz/details/common_impl.hpp#L64-L73).

```cpp
size_t remove_common_suffix(Range<InputIt1>& s1, Range<InputIt2>& s2)
{
    auto rfirst1 = s1.rbegin();
    size_t suffix = static_cast<size_t>(
        std::distance(rfirst1, rf_mismatch(rfirst1, s1.rend(), s2.rbegin(), s2.rend()).first));
    s1.remove_suffix(suffix);
    s2.remove_suffix(suffix);
    return suffix;
}

```

<a id="helper-002"></a>

### 2. `CachedLevenshtein::CachedLevenshtein`

Archive member `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Levenshtein.hpp`, lines 430–434. Member SHA-256: `5eb5747a24666b5e12337627a04b9c62ae131324de538a67ba72ebc2f388be0d`. [Verified immutable source link](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/6c10b68930df73bfe5679720e4008518ba4265b1/rapidfuzz/distance/Levenshtein.hpp#L430-L434).

```cpp
    CachedLevenshtein(InputIt1 first1, InputIt1 last1, LevenshteinWeightTable aWeights = {1, 1, 1})
        : s1(first1, last1), PM(detail::make_range(first1, last1)), weights(aWeights)
    {}

private:
```

<a id="helper-003"></a>

### 3. `CachedIndel::_distance`

Archive member `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/Indel.hpp`, lines 170–179. Member SHA-256: `d59e6724f686255ff0cd19cf7d402afd5eb95e009064b6b1e10df22726f11625`. [Verified immutable source link](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/6c10b68930df73bfe5679720e4008518ba4265b1/rapidfuzz/distance/Indel.hpp#L170-L179).

```cpp
    template <typename InputIt2>
    size_t _distance(const detail::Range<InputIt2>& s2, size_t score_cutoff, size_t score_hint) const
    {
        size_t maximum_ = maximum(s2);
        size_t lcs_cutoff = (maximum_ / 2 >= score_cutoff) ? maximum_ / 2 - score_cutoff : 0;
        size_t lcs_cutoff_hint = (maximum_ / 2 >= score_hint) ? maximum_ / 2 - score_hint : 0;
        size_t lcs_sim = scorer.similarity(s2, lcs_cutoff, lcs_cutoff_hint);
        size_t dist = maximum_ - 2 * lcs_sim;
        return (dist <= score_cutoff) ? dist : score_cutoff + 1;
    }
```

<a id="helper-004"></a>

### 4. `lcs_seq_similarity`

Archive member `levenshtein-0.27.5/extern/rapidfuzz-cpp/rapidfuzz/distance/LCSseq_impl.hpp`, lines 376–403. Member SHA-256: `97f905a510c5eee8eac2e8e35eabc004b5501e4790a4b93206f4002170efa9ef`. [Verified immutable source link](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/6c10b68930df73bfe5679720e4008518ba4265b1/rapidfuzz/distance/LCSseq_impl.hpp#L376-L403).

```cpp
size_t lcs_seq_similarity(const BlockPatternMatchVector& block, Range<InputIt1> s1, Range<InputIt2> s2,
                          size_t score_cutoff)
{
    auto len1 = s1.size();
    auto len2 = s2.size();

    if (score_cutoff > len1 || score_cutoff > len2) return 0;

    size_t max_misses = len1 + len2 - 2 * score_cutoff;

    /* no edits are allowed */
    if (max_misses == 0 || (max_misses == 1 && len1 == len2)) return s1 == s2 ? len1 : 0;

    if (max_misses < abs_diff(len1, len2)) return 0;

    // do this first, since we can not remove any affix in encoded form
    if (max_misses >= 5) return longest_common_subsequence(block, s1, s2, score_cutoff);

    /* common affix does not effect Levenshtein distance */
    StringAffix affix = remove_common_affix(s1, s2);
    size_t lcs_sim = affix.prefix_len + affix.suffix_len;
    if (!s1.empty() && !s2.empty()) {
        size_t adjusted_cutoff = score_cutoff >= lcs_sim ? score_cutoff - lcs_sim : 0;
        lcs_sim += lcs_seq_mbleven2018(s1, s2, adjusted_cutoff);
    }

    return (lcs_sim >= score_cutoff) ? lcs_sim : 0;
}
```
