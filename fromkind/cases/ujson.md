# ujson 6.0.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0155: Object_newString

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `(Py_UCS4 *)start` — constructed codepoint array. start/end delimit decoder escape scratch, typed 32-bit; compile-time sizeof assertion matches Py_UCS4. Surrogate-pair handling combines pairs and can retain lone surrogate values.

**Length:** `end - start`; uint32_t codepoint elements.

**Confirmed:** Exact retained source snippet included (ujson-6.0.0/src/ujson/decode.c:813–818) Scratch allocation and constructor activation (ujson-6.0.0/src/ujson/decode.c:370–415) Escapes, surrogate merging, decoded scalar append (ujson-6.0.0/src/ujson/decode.c:477–530) Bytes/Unicode input and stack scratch initialization (ujson-6.0.0/src/ujson/decode.c:833–889)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** String arguments are encoded with surrogatepass; bytes input also accepted. Decoder then constructs an independent uint32_t/JSUINT32 array from JSON escapes and encoded bytes.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** ujson calls static helper directly on closing quote; srsly sets newString callback to Object_newString before JSON_DecodeObject.

**Source:** `ujson-6.0.0/src/ujson/decode.c:813–818`; SHA-256 `c23c6c5a15666a6df182b0b827c9fedd676321027a45599af4f671272b464212`.

`ujson-6.0.0/src/ujson/decode.c` lines 813–818 (GitHub mapping not verified in saved evidence)

```
typedef char assert_py_ucs4_is_jsuint32[1 - 2*!(sizeof(Py_UCS4) == sizeof(uint32_t))];

static PyObject *Object_newString(uint32_t *start, uint32_t *end)
{
  return PyUnicode_FromKindAndData (PyUnicode_4BYTE_KIND, (Py_UCS4 *) start, (end - start));
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/64/7c/e1fa3fb70b53192436d751b5cb671f0ee960baa188b8351a7fec735223d3/ujson-6.0.0.tar.gz); archive SHA-256 `80e23393feb707582e0ad495c397a4477b646d08094d2df64f7316f9fafd8aae`.
