# wcwidth — non-simple Unicode reads

[All packages](README.md)

Version: 0.9.1. **1 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`wcwidth_impl`](#case-001)

<a id="case-001"></a>

## 1. `wcwidth_impl`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** algorithm.

After enforcing exactly one codepoint (except falsy input), reads PyUnicode_ReadChar(wc_obj,0). Single index-zero probe, not a traversal; this is the new core read API consumer.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** One UCS4 element is one Python codepoint. All cp/ptr offsets are codepoints. Python wchar copy supports embedded NUL via explicit lengths, but escape/parse paths use controls and may normalize surrogate scalars; source scalar ReadChar preserves lone surrogates.

**FSR lifetime assessment:** No risk was identified in this case.

- Stable-ABI PyUnicode_ReadChar returns a scalar; caller holds no representation pointer.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/dc/ac/3a943d2792c9bb368aaa8b50121c0f778460ba2d7fbdc0a0366201d9e761/wcwidth-0.9.1.tar.gz). Archive SHA-256: `5823209b0d43af322ce698c689380d7c15ca31fa8e6e3be8459f27031bef0af5`.

**Function source:** `wcwidth-0.9.1/wcwidth/_wcwidth_c.c`, lines 403–500. Member SHA-256: `fc6deed5f987ab2d64a4f8951c128dac6cbef6646eaa3c1ceb097d4b3673f199`.

[Verified immutable function link](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L403-L500).

### Read sites

- Site 1: lines 478–478; core read; index expression `wc_obj, 0`. Exact source expression; caller offsets/control flow described in function reason.

### Contextual source excerpts

Omitted from `wcwidth-0.9.1/wcwidth/_wcwidth_c.c`: lines 407–473, 483–497. The original contextual region was lines 403–500.

Archive member `wcwidth-0.9.1/wcwidth/_wcwidth_c.c`, lines 403–406. Member SHA-256: `fc6deed5f987ab2d64a4f8951c128dac6cbef6646eaa3c1ceb097d4b3673f199`. [Verified immutable source link](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L403-L406).

```c
static PyObject *
wcwidth_impl(PyObject *self, PyObject *const *args, Py_ssize_t nargs, PyObject *kwnames)
{
    PyObject *wc_obj = NULL;
```

Archive member `wcwidth-0.9.1/wcwidth/_wcwidth_c.c`, lines 474–482. Member SHA-256: `fc6deed5f987ab2d64a4f8951c128dac6cbef6646eaa3c1ceb097d4b3673f199`. [Verified immutable source link](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L474-L482).

```c
                         "ord() expected a character, but string of length %zd found",
                         char_count);
            return NULL;
        }
        ucs = PyUnicode_ReadChar(wc_obj, 0);
    }

    int result = wcwidth_u32(ucs, ambiguous_width);
    return PyLong_FromLong(result);
```

Archive member `wcwidth-0.9.1/wcwidth/_wcwidth_c.c`, lines 498–500. Member SHA-256: `fc6deed5f987ab2d64a4f8951c128dac6cbef6646eaa3c1ceb097d4b3673f199`. [Verified immutable source link](https://github.com/jquast/wcwidth/blob/074bc286335d33de6bb475cf3bab82eacd946c75/wcwidth/_wcwidth_c.c#L498-L500).

```c
        return NULL;
    }
}
```
