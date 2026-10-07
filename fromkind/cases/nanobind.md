# nanobind 3.1.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0189: PyPy linker symbol reference

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** not_applicable; expression ``.

**Input:** `` — No actual input buffer passed by an executable call in this region.. 

**Length:** ``; .

**Confirmed:** darwin-ld-pypy.sym lists linker symbol arguments. The -U _PyPyUnicode_FromKindAndData line is a symbol reference, not source code, function pointer invocation, or callsite.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No actual constructor consumer to migrate here. Declaration/binding/linker references track API availability; comments alone do not establish runtime use.

**Activation / tracing:** 

**Source:** `nanobind-3.1.0/cmake/darwin-ld-pypy.sym:804–813`; SHA-256 `7420ba460bb22f5133164485d02a60416f7f01a128dbc5cf0b27c15cbfe9eb70`.

`nanobind-3.1.0/cmake/darwin-ld-pypy.sym` lines 804–813 (GitHub mapping not verified in saved evidence)

```
-U _PyPyUnicode_FromEncodedObject
-U _PyPyUnicode_FromFormat
-U _PyPyUnicode_FromFormatV
-U _PyPyUnicode_FromKindAndData
-U _PyPyUnicode_FromObject
-U _PyPyUnicode_FromOrdinal
-U _PyPyUnicode_FromString
-U _PyPyUnicode_FromStringAndSize
-U _PyPyUnicode_FromUnicode
-U _PyPyUnicode_FromWideChar
```

[Frozen source distribution](https://files.pythonhosted.org/packages/c7/1f/e28fae715401e8f57400e72aeaff4fde12046d31828164f34f61f0816da8/nanobind-3.1.0.tar.gz); archive SHA-256 `6661e3dc1434d78781ccf7913442d90361dab395c3424efadb63bbb6ddea7ea3`.
