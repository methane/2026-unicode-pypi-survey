# bitarray — non-simple Unicode reads

[All packages](README.md)

Version: 3.11.0. **1 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`module_setup_table`](#case-001)

<a id="case-001"></a>

## 1. `module_setup_table`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Debug-only test function reads scalar index0 after asserting length1.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

Debug-only read consumer retained explicitly.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/04/f7/6765577df59e2345036e435f7e983e1c291d67b7d76a51918eff04ad1494/bitarray-3.11.0.tar.gz). Archive SHA-256: `bf19437ec00ec3d40aef82eaeedc14cf4000be9b635c4f5049796506e6630dd8`.

**Function source:** `bitarray-3.11.0/bitarray/_util.c`, lines 2624–2632. Member SHA-256: `84d3865232a5d8f140156e3fc541980d844afe6bfe2427112fe7cc67638957fc`.

[Verified immutable function link](https://github.com/ilanschnell/bitarray/blob/ec1ea4ac828cb9f1530a94f58cc497e48a593aa8/bitarray/_util.c#L2624-L2632).

### Read sites

- Site 1: lines 2622–2632; scalar; index expression `0`. Compiled only when NDEBUG is absent.

### Contextual source excerpts

Archive member `bitarray-3.11.0/bitarray/_util.c`, lines 2619–2635. Member SHA-256: `84d3865232a5d8f140156e3fc541980d844afe6bfe2427112fe7cc67638957fc`. [Verified immutable source link](https://github.com/ilanschnell/bitarray/blob/ec1ea4ac828cb9f1530a94f58cc497e48a593aa8/bitarray/_util.c#L2619-L2635).

```c

/* ---------- module functions exposed in debug mode for testing ------- */

#ifndef NDEBUG
static PyObject *
module_setup_table(PyObject *module, PyObject *obj)
{
    char table[256];

    assert(PyUnicode_Check(obj));
    assert(PyUnicode_GET_LENGTH(obj) == 1);
    setup_table(table, PyUnicode_READ_CHAR(obj, 0));
    return PyBytes_FromStringAndSize(table, 256);
}

/* Return zlw(a) as a new bitarray, rather than an int object.
   This makes testing easier, because the int result would depend
```

Archive member `bitarray-3.11.0/bitarray/_util.c`, lines 2624–2632. Member SHA-256: `84d3865232a5d8f140156e3fc541980d844afe6bfe2427112fe7cc67638957fc`. [Verified immutable source link](https://github.com/ilanschnell/bitarray/blob/ec1ea4ac828cb9f1530a94f58cc497e48a593aa8/bitarray/_util.c#L2624-L2632).

```c
module_setup_table(PyObject *module, PyObject *obj)
{
    char table[256];

    assert(PyUnicode_Check(obj));
    assert(PyUnicode_GET_LENGTH(obj) == 1);
    setup_table(table, PyUnicode_READ_CHAR(obj, 0));
    return PyBytes_FromStringAndSize(table, 256);
}
```
