# srsly 2.5.4

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0156: Object_newString

**Disposition:** static use; `direct_api_call`; `vendor_or_compatibility`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `(Py_UCS4 *)start` — constructed codepoint array. start/end delimit decoder escape scratch, typed 32-bit; compile-time sizeof assertion matches Py_UCS4. Surrogate-pair handling combines pairs and can retain lone surrogate values.

**Length:** `end - start`; uint32_t codepoint elements.

**Confirmed:** Exact retained source snippet included (srsly-2.5.4/srsly/ujson/JSONtoObj.c:68–73) Callback registration (srsly-2.5.4/srsly/ujson/JSONtoObj.c:127–151) Input encoding and decoder invocation (srsly-2.5.4/srsly/ujson/JSONtoObj.c:166–189) Independent scratch allocation and callback activation (srsly-2.5.4/srsly/ujson/lib/ultrajsondec.c:428–491) Surrogate handling and scalar appends (srsly-2.5.4/srsly/ujson/lib/ultrajsondec.c:547–581)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** String arguments are encoded with surrogatepass; bytes input also accepted. Decoder then constructs an independent uint32_t/JSUINT32 array from JSON escapes and encoded bytes.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** ujson calls static helper directly on closing quote; srsly sets newString callback to Object_newString before JSON_DecodeObject.

**Source:** `srsly-2.5.4/srsly/ujson/JSONtoObj.c:68–73`; SHA-256 `78e88fdde7891f570977b1d53ff5eeef0c30a6f0026f22762fba7b823457f763`.

`srsly-2.5.4/srsly/ujson/JSONtoObj.c` lines 68–73 (GitHub mapping not verified in saved evidence)

```
typedef char assert_py_ucs4_is_jsuint32[1 - 2*!(sizeof(Py_UCS4) == sizeof(JSUINT32))];

static JSOBJ Object_newString(void *prv, JSUINT32 *start, JSUINT32 *end)
{
  return PyUnicode_FromKindAndData (PyUnicode_4BYTE_KIND, (Py_UCS4 *) start, (end - start));
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/4b/9b/a55dbb041cf2e44811323ea3fccada06acdd8dbc8ac856f224e0e093d428/srsly-2.5.4.tar.gz); archive SHA-256 `7589a35dd6bf1d177803c4ed454098f2f690b3704b80cca337a50be95ba59b3a`.
