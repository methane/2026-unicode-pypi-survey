# tensorstore — non-simple Unicode reads

[All packages](README.md)

Version: 0.1.85. **1 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`GetContiguousLayoutOrderOrThrow`](#case-001)

<a id="case-001"></a>

## 1. `GetContiguousLayoutOrderOrThrow`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads exactly codepoint 0 after checking length is 1; selects C/F layout order.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Python codepoint 0; bytes branch byte 0; accepted values ASCII C/F.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/26/16/a6530387ed22d07e974af2ef55e34fb19a7251a6911c85a0be029a4dcf9c/tensorstore-0.1.85.tar.gz). Archive SHA-256: `26698bded0278e98e0988eb8f7d76ad248762afc5f55a38b9122ffd1474e505f`.

**Function source:** `tensorstore-0.1.85/python/tensorstore/array_type_caster.cc`, lines 311–335. Member SHA-256: `f96557908a14838ea7ce4031b3a2d2b7fbd4b1e501919ccda790d20f7ab4db54`.

[Verified immutable function link](https://github.com/google/tensorstore/blob/bc4fbc11f69ee5379b2f611a934663006e1f573f/python/tensorstore/array_type_caster.cc#L311-L335).

### Read sites

- Site 1: lines 311–334; scalar index; index expression `0`. Fixed one-character enum selector.

### Contextual source excerpts

Archive member `tensorstore-0.1.85/python/tensorstore/array_type_caster.cc`, lines 311–335. Member SHA-256: `f96557908a14838ea7ce4031b3a2d2b7fbd4b1e501919ccda790d20f7ab4db54`. [Verified immutable source link](https://github.com/google/tensorstore/blob/bc4fbc11f69ee5379b2f611a934663006e1f573f/python/tensorstore/array_type_caster.cc#L311-L335).

```cpp
ContiguousLayoutOrder GetContiguousLayoutOrderOrThrow(pybind11::handle obj) {
  Py_UCS4 c;
  if (PyUnicode_Check(obj.ptr())) {
    if (PyUnicode_READY(obj.ptr()) != 0) throw py::error_already_set();
    if (PyUnicode_GET_LENGTH(obj.ptr()) != 1) goto invalid;
    void* data = PyUnicode_DATA(obj.ptr());
    int kind = PyUnicode_KIND(obj.ptr());
    c = PyUnicode_READ(kind, data, 0);
  } else if (PyBytes_Check(obj.ptr())) {
    if (PyBytes_GET_SIZE(obj.ptr()) != 1) goto invalid;
    c = PyBytes_AS_STRING(obj.ptr())[0];
  } else {
    goto invalid;
  }
  switch (c) {
    case 'C':
      return ContiguousLayoutOrder::c;
    case 'F':
      return ContiguousLayoutOrder::fortran;
    default:
      break;
  }
invalid:
  throw py::type_error("`order` must be specified as 'C' or 'F'");
}
```
