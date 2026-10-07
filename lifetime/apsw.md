# apsw: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#apsw)

Registered Python calls obtain local DATA/KIND and return without saving a view. An accepted long nonASCII str can be queried repeatedly for its first grapheme or a one-codepoint range. Existing work scales with selected boundary/range, while rebuilding a whole FSR after each return would scale with total string length.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## unicode.c: 185–208

Direct local provider, short boundary/range algorithm, public methods

Archive member: `apsw-3.53.4.0/src/unicode.c`

Member SHA256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`

[Frozen sdist](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

[Verified permanent source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L185-L208).

```
#define TEXT_INIT                                                                                                      \
  {                                                                                                                    \
    .pos = offset,                                                                                                     \
    .curchar = -1,                                                                                                     \
    .lookahead = (offset == text_end) ? EOT : cat_func(PyUnicode_READ(text_kind, text_data, offset)),                  \
  }

#define it_advance()                                                                                                   \
  do                                                                                                                   \
  {                                                                                                                    \
    assert(it.curchar != EOT);                                                                                         \
    it.curchar = it.lookahead;                                                                                         \
    if (it.curchar != EOT)                                                                                             \
    {                                                                                                                  \
      it.pos++;                                                                                                        \
      it.lookahead = (it.pos == text_end) ? EOT : cat_func(PyUnicode_READ(text_kind, text_data, it.pos));              \
    }                                                                                                                  \
  } while (0)

#define it_absorb(match, extend)                                                                                       \
  do                                                                                                                   \
  {                                                                                                                    \
    if (it.lookahead & (match))                                                                                        \
    {                                                                                                                  \
```

## unicode.c: 1334–1358

Direct local provider, short boundary/range algorithm, public methods

Archive member: `apsw-3.53.4.0/src/unicode.c`

Member SHA256: `83fc7526ec6d6e9b2b6af43326d7989aef9dad233a87c35b23320a40cd9711fd`

[Frozen sdist](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

[Verified permanent source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/unicode.c#L1334-L1358).

```
has_category(PyObject *Py_UNUSED(self), PyObject *const *fast_args, Py_ssize_t fast_nargs, PyObject *fast_kwnames)
{
  PyObject *text;
  Py_ssize_t start, end;
  unsigned long long mask;

#define has_category_KWARGS "text", "start", "end", "mask"
  ARG_PROLOG(4, has_category_KWARGS);
  ARG_MANDATORY ARG_PyUnicode(text);
  ARG_MANDATORY ARG_PyUnicode_offset(start, text);
  ARG_MANDATORY ARG_PyUnicode_offset(end, text);
  ARG_MANDATORY ARG_unsigned_long_long(mask);
  ARG_EPILOG(NULL, "has_category(text: str, start:int, end: int, mask: int)", );

  int kind = PyUnicode_KIND(text);
  void *data = PyUnicode_DATA(text);

  while (start < end)
  {
    if (category_category(PyUnicode_READ(kind, data, start)) & mask)
      Py_RETURN_TRUE;
    start++;
  }
  Py_RETURN_FALSE;
}
```
