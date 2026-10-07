# biopython — non-simple Unicode reads

[All packages](README.md)

Version: 1.88. **5 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`AlignmentCounts_new`](#case-001)
- [`Aligner_set_wildcard`](#case-002)
- [`Aligner_set_wildcard`](#case-003)
- [`strand_converter`](#case-004)
- [`extract_single_character`](#case-005)

<a id="case-001"></a>

## 1. `AlignmentCounts_new`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Unicode wildcard argument read only at index0 after length==1.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz). Archive SHA-256: `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

**Function source:** `biopython-1.88/Bio/Align/_alignmentcounts.c`, lines 1144–1625. Member SHA-256: `399ceaca36e10767f8c0362a26d06c19797b1cf1080c0ee1da0af6912452b9fb`.

[Verified immutable function link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_alignmentcounts.c#L1144-L1625).

### Read sites

- Site 1: lines 1226–1234; scalar; index expression `0`. Single wildcard value used by downstream numeric alignment loops; these do not index the Unicode argument.

### Contextual source excerpts

Archive member `biopython-1.88/Bio/Align/_alignmentcounts.c`, lines 1226–1234. Member SHA-256: `399ceaca36e10767f8c0362a26d06c19797b1cf1080c0ee1da0af6912452b9fb`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_alignmentcounts.c#L1226-L1234).

```c
    else if (PyUnicode_Check(argument)) {
        if (PyUnicode_READY(argument) == -1) goto exit;
        if (PyUnicode_GET_LENGTH(argument) != 1) {
            PyErr_SetString(PyExc_ValueError,
                            "wildcard should be a single character, or None");
            goto exit;
        }
        wildcard = PyUnicode_READ_CHAR(argument, 0);
    }
```


<a id="case-002"></a>

## 2. `Aligner_set_wildcard`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Single-codepoint wildcard read at index0 after length==1; rejects >=256.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz). Archive SHA-256: `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

**Function source:** `biopython-1.88/Bio/Align/_codonaligner.c`, lines 458–480. Member SHA-256: `62af072949edb30cfb388db46f9b0c2a55b860f2387389ca2f14bd4ebcc544f7`.

[Verified immutable function link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_codonaligner.c#L458-L480).

### Read sites

- Site 1: lines 457–479; scalar; index expression `0`. One wildcard codepoint, not sequence traversal.

### Contextual source excerpts

Archive member `biopython-1.88/Bio/Align/_codonaligner.c`, lines 454–482. Member SHA-256: `62af072949edb30cfb388db46f9b0c2a55b860f2387389ca2f14bd4ebcc544f7`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_codonaligner.c#L454-L482).

```c
    return PyUnicode_FromFormat("%c", self->wildcard);
}

static int
Aligner_set_wildcard(Aligner* self, PyObject* value, void* closure)
{
    Py_UCS4 wildcard;
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "wildcard should be a single ASCII character");
        return -1;
    }
    if (PyUnicode_READY(value) == -1) return -1;
    if (PyUnicode_GET_LENGTH(value) != 1) {
        PyErr_SetString(PyExc_ValueError,
                        "wildcard should be a single ASCII character");
        return -1;
    }
    wildcard = PyUnicode_READ_CHAR(value, 0);
    if (wildcard >= 256) {
        PyErr_SetString(PyExc_ValueError,
                        "wildcard should be a single ASCII character");
        return -1;
    }
    self->wildcard = (char)wildcard;
    return 0;
}

static char Aligner_wildcard__doc__[] = "wildcard character";
```

Archive member `biopython-1.88/Bio/Align/_codonaligner.c`, lines 458–480. Member SHA-256: `62af072949edb30cfb388db46f9b0c2a55b860f2387389ca2f14bd4ebcc544f7`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_codonaligner.c#L458-L480).

```c
Aligner_set_wildcard(Aligner* self, PyObject* value, void* closure)
{
    Py_UCS4 wildcard;
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "wildcard should be a single ASCII character");
        return -1;
    }
    if (PyUnicode_READY(value) == -1) return -1;
    if (PyUnicode_GET_LENGTH(value) != 1) {
        PyErr_SetString(PyExc_ValueError,
                        "wildcard should be a single ASCII character");
        return -1;
    }
    wildcard = PyUnicode_READ_CHAR(value, 0);
    if (wildcard >= 256) {
        PyErr_SetString(PyExc_ValueError,
                        "wildcard should be a single ASCII character");
        return -1;
    }
    self->wildcard = (char)wildcard;
    return 0;
}
```


<a id="case-003"></a>

## 3. `Aligner_set_wildcard`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Single-codepoint wildcard read at index0 after length==1.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz). Archive SHA-256: `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

**Function source:** `biopython-1.88/Bio/Align/_pairwisealigner.c`, lines 3838–3857. Member SHA-256: `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`.

[Verified immutable function link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L3838-L3857).

### Read sites

- Site 1: lines 3837–3857; scalar; index expression `0`. None is separate branch.

### Contextual source excerpts

Archive member `biopython-1.88/Bio/Align/_pairwisealigner.c`, lines 3834–3860. Member SHA-256: `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L3834-L3860).

```c
    }
}

static int
Aligner_set_wildcard(Aligner* self, PyObject* value, void* closure)
{
    if (value == Py_None) {
        self->wildcard = -1;
        return 0;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "wildcard should be a single character, or None");
        return -1;
    }
    if (PyUnicode_READY(value) == -1) return -1;
    if (PyUnicode_GET_LENGTH(value) != 1) {
        PyErr_SetString(PyExc_ValueError,
                        "wildcard should be a single character, or None");
        return -1;
    }
    self->wildcard = PyUnicode_READ_CHAR(value, 0);
    return 0;
}

static char Aligner_algorithm__doc__[] = "alignment algorithm";

```

Archive member `biopython-1.88/Bio/Align/_pairwisealigner.c`, lines 3838–3857. Member SHA-256: `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L3838-L3857).

```c
Aligner_set_wildcard(Aligner* self, PyObject* value, void* closure)
{
    if (value == Py_None) {
        self->wildcard = -1;
        return 0;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "wildcard should be a single character, or None");
        return -1;
    }
    if (PyUnicode_READY(value) == -1) return -1;
    if (PyUnicode_GET_LENGTH(value) != 1) {
        PyErr_SetString(PyExc_ValueError,
                        "wildcard should be a single character, or None");
        return -1;
    }
    self->wildcard = PyUnicode_READ_CHAR(value, 0);
    return 0;
}
```


<a id="case-004"></a>

## 4. `strand_converter`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Single-codepoint strand read at index0 after length==1; accepts only +/-.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz). Archive SHA-256: `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

**Function source:** `biopython-1.88/Bio/Align/_pairwisealigner.c`, lines 7349–7366. Member SHA-256: `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`.

[Verified immutable function link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L7349-L7366).

### Read sites

- Site 1: lines 7348–7366; scalar; index expression `0`. ASCII strand selector.

### Contextual source excerpts

Archive member `biopython-1.88/Bio/Align/_pairwisealigner.c`, lines 7345–7369. Member SHA-256: `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L7345-L7369).

```c
    return Py_CLEANUP_SUPPORTED;
}
 
static int
strand_converter(PyObject* argument, void* pointer)
{
    if (!PyUnicode_Check(argument)) goto error;
    if (PyUnicode_READY(argument) == -1) return 0;
    if (PyUnicode_GET_LENGTH(argument) == 1) {
        const Py_UCS4 ch = PyUnicode_READ_CHAR(argument, 0);
        if (ch < 128) {
            const char c = ch;
            if (ch == '+' || ch == '-') {
                *((char*)pointer) = c;
                return 1;
            }
        }
    }
error:
    PyErr_SetString(PyExc_ValueError, "strand must be '+' or '-'");
    return 0;
}

static const char Aligner_score__doc__[] = "calculates the alignment score";

```

Archive member `biopython-1.88/Bio/Align/_pairwisealigner.c`, lines 7349–7366. Member SHA-256: `e64700d1dcfe608fa99ff65e2500d7c6548b4dc69039390d326c9fb84093514e`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Align/_pairwisealigner.c#L7349-L7366).

```c
strand_converter(PyObject* argument, void* pointer)
{
    if (!PyUnicode_Check(argument)) goto error;
    if (PyUnicode_READY(argument) == -1) return 0;
    if (PyUnicode_GET_LENGTH(argument) == 1) {
        const Py_UCS4 ch = PyUnicode_READ_CHAR(argument, 0);
        if (ch < 128) {
            const char c = ch;
            if (ch == '+' || ch == '-') {
                *((char*)pointer) = c;
                return 1;
            }
        }
    }
error:
    PyErr_SetString(PyExc_ValueError, "strand must be '+' or '-'");
    return 0;
}
```


<a id="case-005"></a>

## 5. `extract_single_character`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Single-codepoint configuration checked by length==1 then read at index0.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/f6/a0/cf657d076ec56a5f9e5c29a560c1f97b8eb6ae6608dc8bc95b4e2437f129/biopython-1.88.tar.gz). Archive SHA-256: `9aaa31c0bda4d059f7b2ee00bfdb5cbb73ade3057aa4b737a7cc0187091d071a`.

**Function source:** `biopython-1.88/Bio/Cluster/clustermodule.c`, lines 13–38. Member SHA-256: `d60d139738517a730f61a1e26b0cc645b4fc0766f1dae77fb9b61f2c4ee99ed3`.

[Verified immutable function link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Cluster/clustermodule.c#L13-L38).

### Read sites

- Site 1: lines 18–36; scalar; index expression `0`. Accepts only ASCII character among allowed choices.

### Contextual source excerpts

Archive member `biopython-1.88/Bio/Cluster/clustermodule.c`, lines 13–38. Member SHA-256: `d60d139738517a730f61a1e26b0cc645b4fc0766f1dae77fb9b61f2c4ee99ed3`. [Verified immutable source link](https://github.com/biopython/biopython/blob/d7e4b8b19399668b09442a5b35765d9186b5f665/Bio/Cluster/clustermodule.c#L13-L38).

```c
extract_single_character(PyObject* object, const char variable[],
                         const char allowed[])
{
    Py_UCS4 ch;
    Py_ssize_t n;
    if (!PyUnicode_Check(object)) {
        PyErr_Format(PyExc_ValueError, "%s should be a string", variable);
        return 0;
    }
    if (PyUnicode_READY(object) == -1) return 0;
    n = PyUnicode_GET_LENGTH(object);
    if (n != 1) {
        PyErr_Format(PyExc_ValueError,
                     "%s should be a single character", variable);
        return 0;
    }
    ch = PyUnicode_READ_CHAR(object, 0);
    if (ch < 128) {
        const char c = ch;
        if (strchr(allowed, c)) return c;
    }
    PyErr_Format(PyExc_ValueError,
                 "unknown %s function specified (should be one of '%s')",
                 variable, allowed);
    return 0;
}
```
