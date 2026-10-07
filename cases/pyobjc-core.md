# pyobjc-core — non-simple Unicode reads

[All packages](README.md)

Version: 12.2.2. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`parse_printf_args`](#case-001)
- [`depythonify_c_value`](#case-002)

<a id="case-001"></a>

## 1. `parse_printf_args`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Printf Unicode %c argument reads codepoint0 after requiring length1; main format traversal uses separate strict UTF-8 getter, outside FSR scope.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint0 for argument; format bytes traversed as ASCII UTF-8. Existing format parser byte offsets may treat multibyte input oddly as its own comment admits.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz). Archive SHA-256: `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.

**Function source:** `pyobjc_core-12.2.2/Modules/objc/libffi_support.m`, lines 795–1229. Member SHA-256: `e1112d0c5c25422fb7fffced4a487b86bb448277438dafed6ae5cdb1828bfa44`.

[Verified immutable function link](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/libffi_support.m#L795-L1229).

### Read sites

- Site 1: lines 984–1008; scalar index; index expression `PyUnicode_ReadChar(v,0)`. One-character integer printf argument.

### Contextual source excerpts

Archive member `pyobjc_core-12.2.2/Modules/objc/libffi_support.m`, lines 984–1008. Member SHA-256: `e1112d0c5c25422fb7fffced4a487b86bb448277438dafed6ae5cdb1828bfa44`. [Verified immutable source link](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/libffi_support.m#L984-L1008).

```objective-c
            byref[curarg] = PyMem_Malloc(sizeof(int));
            if (unlikely(byref[curarg] == NULL)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_NoMemory();
                Py_DECREF(encoded);
                return -1;
                // LCOV_EXCL_STOP
            }
            arglist[curarg] = PyObjCFFI_Typestr2FFI(@encode(int));
            v               = args[argoffset];
            if (PyUnicode_Check(v)) {

                if (PyUnicode_GetLength(v) != 1) {
                    PyErr_SetString(PyExc_ValueError, "Expecting string of length 1");
                    Py_DECREF(encoded);
                    return -1;
                }
                *(int*)byref[curarg] = PyUnicode_ReadChar(v, 0);

            } else if (depythonify_c_value(@encode(int), v, byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }

            values[curarg] = byref[curarg];
```


<a id="case-002"></a>

## 2. `depythonify_c_value`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

UniChar branch reads codepoint 0 after length-one/BMP KIND guards and copies scalar to foreign result.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** Codepoint index 0; rejects 4-byte KIND even if length 1; result is 16-bit UniChar.

**FSR lifetime assessment:** No risk was identified in this case.

No second representation getter or escaped input pointer is evident inside this read-bearing function.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/a5/78/abc4ce5920305780aeb36b4067a86253378b36e29ba96673a3deb02eb03a/pyobjc_core-12.2.2.tar.gz). Archive SHA-256: `3906452339cd06a3bb07df103c2511d4cb0f7a22d8771c0b802eba15d9a642b6`.

**Function source:** `pyobjc_core-12.2.2/Modules/objc/objc_support.m`, lines 2663–3157. Member SHA-256: `ff28164b3f61cd31b70be24fb487849300712f86566d2f84ab1699b60358e2be`.

[Verified immutable function link](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/objc_support.m#L2663-L3157).

### Read sites

- Site 1: lines 2790–2812; scalar index; index expression `0`. Single BMP codepoint for Objective-C UniChar.

### Contextual source excerpts

Archive member `pyobjc_core-12.2.2/Modules/objc/objc_support.m`, lines 2790–2812. Member SHA-256: `ff28164b3f61cd31b70be24fb487849300712f86566d2f84ab1699b60358e2be`. [Verified immutable source link](https://github.com/ronaldoussoren/pyobjc/blob/38cdf73fc049ef2d176973eff4ac8d5c76b0a34b/pyobjc-core/Modules/objc/objc_support.m#L2790-L2812).

```objective-c
    case _C_UNICHAR:
        if (PyUnicode_Check(argument) && PyUnicode_GetLength(argument) == 1) {

            /* Need to guard against values outside of the BMP, which cannot be
             * converted to UniChar
             */
            switch (PyUnicode_KIND(argument)) {
            case PyUnicode_1BYTE_KIND:
            case PyUnicode_2BYTE_KIND:
                break;

            default:
                PyErr_Format(PyExc_ValueError, "Expecting string of length 1, got a '%s'",
                             Py_TYPE(argument)->tp_name);
                return -1;
            }
            UniChar v = (UniChar)PyUnicode_ReadChar(argument, 0);
            memcpy(datum, (void*)&v, sizeof(UniChar));
            return 0;
        }
        PyErr_Format(PyExc_ValueError, "Expecting unicode string of length 1, got a '%s'",
                     Py_TYPE(argument)->tp_name);
        return -1;
```
