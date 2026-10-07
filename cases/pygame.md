# pygame — non-simple Unicode reads

[All packages](README.md)

Version: 2.6.1. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`_view_kind`](#case-001)
- [`_view_kind`](#case-002)

<a id="case-001"></a>

## 1. `_view_kind`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

One scalar access at fixed index zero following exact length-one check. Per schema a direct index-zero read is not counted as an iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offset 0; bytes branch uses byte zero. Only ASCII selector letters are accepted.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/49/cc/08bba60f00541f62aaa252ce0cfbd60aebd04616c0b9574f755b583e45ae/pygame-2.6.1.tar.gz). Archive SHA-256: `56fb02ead529cee00d415c3e007f75e0780c655909aaa8e8bf616ee09c9feb1f`.

**Function source:** `pygame-2.6.1/src_c/pixelcopy.c`, lines 122–182. Member SHA-256: `bae071baaf3de69c46a4c9932b594f69af2481c94e21446ac171034a359bd63d`.

[Verified immutable function link](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/pixelcopy.c#L122-L182).

### Read sites

- Site 1: lines 128–135; scalar index; index expression `0`. Select view kind from a single character.

### Contextual source excerpts

Archive member `pygame-2.6.1/src_c/pixelcopy.c`, lines 122–146. Member SHA-256: `bae071baaf3de69c46a4c9932b594f69af2481c94e21446ac171034a359bd63d`. [Verified immutable source link](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/pixelcopy.c#L122-L146).

```c
static int
_view_kind(PyObject *obj, void *view_kind_vptr)
{
    unsigned long ch;
    _pc_view_kind_t *view_kind_ptr = (_pc_view_kind_t *)view_kind_vptr;

    if (PyUnicode_Check(obj)) {
        if (PyUnicode_GET_LENGTH(obj) != 1) {
            PyErr_SetString(PyExc_TypeError,
                            "expected a length 1 string for argument 3");
            return 0;
        }
        ch = PyUnicode_READ_CHAR(obj, 0);
    }
    else if (PyBytes_Check(obj)) {
        if (PyBytes_GET_SIZE(obj) != 1) {
            PyErr_SetString(PyExc_TypeError,
                            "expected a length 1 string for argument 3");
            return 0;
        }
        ch = *PyBytes_AS_STRING(obj);
    }
    else {
        PyErr_Format(PyExc_TypeError,
                     "expected a length one string for argument 3: got '%s'",
```


<a id="case-002"></a>

## 2. `_view_kind`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

One scalar access at fixed index zero following exact length-one check. Per schema a direct index-zero read is not counted as an iteration.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint offset 0; bytes branch uses byte zero. Only ASCII selector letters are accepted.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/49/cc/08bba60f00541f62aaa252ce0cfbd60aebd04616c0b9574f755b583e45ae/pygame-2.6.1.tar.gz). Archive SHA-256: `56fb02ead529cee00d415c3e007f75e0780c655909aaa8e8bf616ee09c9feb1f`.

**Function source:** `pygame-2.6.1/src_c/surface.c`, lines 3458–3522. Member SHA-256: `ad5433d3bfd6d4ab0f2efab910d47d3d852555fc1495063d2eb9fccf51dc5721`.

[Verified immutable function link](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/surface.c#L3458-L3522).

### Read sites

- Site 1: lines 3464–3471; scalar index; index expression `0`. Select view kind from a single character.

### Contextual source excerpts

Archive member `pygame-2.6.1/src_c/surface.c`, lines 3458–3482. Member SHA-256: `ad5433d3bfd6d4ab0f2efab910d47d3d852555fc1495063d2eb9fccf51dc5721`. [Verified immutable source link](https://github.com/pygame/pygame/blob/b92c0da9d1b5eba6c813138790fc1ab6cea0252c/src_c/surface.c#L3458-L3482).

```c
static int
_view_kind(PyObject *obj, void *view_kind_vptr)
{
    unsigned long ch;
    SurfViewKind *view_kind_ptr = (SurfViewKind *)view_kind_vptr;

    if (PyUnicode_Check(obj)) {
        if (PyUnicode_GET_LENGTH(obj) != 1) {
            PyErr_SetString(PyExc_TypeError,
                            "expected a length 1 string for argument 1");
            return 0;
        }
        ch = PyUnicode_READ_CHAR(obj, 0);
    }
    else if (PyBytes_Check(obj)) {
        if (PyBytes_GET_SIZE(obj) != 1) {
            PyErr_SetString(PyExc_TypeError,
                            "expected a length 1 string for argument 1");
            return 0;
        }
        ch = *PyBytes_AS_STRING(obj);
    }
    else {
        PyErr_Format(PyExc_TypeError,
                     "expected a length one string for argument 1: got '%s'",
```
