# pywinpty 3.0.5

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0190: Bundled CPython API declaration

**Disposition:** non-use context; `non_use`; `vendor_or_compatibility`.

**Kind:** not_applicable; expression ``.

**Input:** `` — No actual input buffer passed by an executable call in this region.. 

**Length:** ``; .

**Confirmed:** Bundled PythonARM CPython header declares the API and documents the buffer contract. There is no function implementation or call here, and activation by the pywinpty extension is not established.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No actual constructor consumer to migrate here. Declaration/binding/linker references track API availability; comments alone do not establish runtime use.

**Activation / tracing:** 

**Source:** `pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h:569–574`; SHA-256 `ef0ab5b3066e835d4bbf8a0bc70290e0d11f7765d8a38e1d4da2bcf94bf4b9ad`.

`pywinpty-3.0.5/pythonarm64/tools/include/cpython/unicodeobject.h` lines 569–574 (GitHub mapping not verified in saved evidence)

```
/* Create a new string from a buffer of Py_UCS1, Py_UCS2 or Py_UCS4 characters.
   Scan the string to find the maximum character. */
PyAPI_FUNC(PyObject*) PyUnicode_FromKindAndData(
    int kind,
    const void *buffer,
    Py_ssize_t size);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/a9/ef/2d27f30c59a67be7025b2d7858c8c2d282b74d66544b2384730b82de74fd/pywinpty-3.0.5.tar.gz); archive SHA-256 `61db0db063de9865adbea66db294628f8577f608d9764a4c7d3384eeacc4e81b`.
