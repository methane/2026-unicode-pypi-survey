# orjson 3.12.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0187: PyO3 FFI declaration and PyPy link-name binding

**Disposition:** non-use context; `non_use`; `vendor_or_compatibility`.

**Kind:** not_applicable; expression ``.

**Input:** `` — No actual input buffer passed by an executable call in this region.. 

**Length:** ``; .

**Confirmed:** Extern FFI declaration specifies API signature; cfg_attr(PyPy, link_name=...) maps the same Rust binding to a PyPy exported C symbol. Neither occurrence is a call.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No actual constructor consumer to migrate here. Declaration/binding/linker references track API availability; comments alone do not establish runtime use.

**Activation / tracing:** 

**Source:** `orjson-3.12.0/include/cargo/pyo3-ffi-0.28.3/src/cpython/unicodeobject.rs:661–666`; SHA-256 `0affb26b65e7f9d594224f7b1b9a8db3c9ce164eacbd2b97966acf6e49a37aef`.

`orjson-3.12.0/include/cargo/pyo3-ffi-0.28.3/src/cpython/unicodeobject.rs` lines 661–666 (GitHub mapping not verified in saved evidence)

```
    #[cfg_attr(PyPy, link_name = "PyPyUnicode_FromKindAndData")]
    pub fn PyUnicode_FromKindAndData(
        kind: c_int,
        buffer: *const c_void,
        size: Py_ssize_t,
    ) -> *mut PyObject;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.
