# jiter 0.17.0

0 confirmed layout regions; 1 reviewed regions including non-direct context.

## L1133: pystring_ascii_new

**Classification:** non-direct context; project_source; `api_output_payload_mutation`.

**Purpose:** Create ASCII str through PyUnicode_New, then copy bytes into PyUnicode_DATA API result.

**Migration effect:** No explicit Unicode struct/layout cast; API/writable-view migration can address this path without hard-coded header offsets.

**Fields / layout:** none. Types: .

**Source:** `jiter-0.17.0/crates/jiter/src/py_string_cache.rs:319–355`. SHA-256 `26bf46c67e77a3a271eb732ca940794f7e4e00cf78ffda5766f2d152e2393103`.

**Activation / context:** cfg excludes PyPy/GraalPy/LIMITED_API; .cast() is on DATA return pointer, not to PyUnicodeObject/ASCII/Compact struct. No local Unicode layout aliases found.

Lines 319–336 ([verified immutable source](https://github.com/pydantic/jiter/blob/2b5ec63e505b44775e29b865c3161ea13bdad16b/crates/jiter/src/py_string_cache.rs#L319-L336))

```
        PyString::new(py, s)
    }
}

/// Faster creation of PyString from an ASCII string, inspired by
/// <https://github.com/ijl/orjson/blob/3.10.0/src/str/create.rs#L41>
///
/// # Safety
///
/// `s` must be ASCII only
pub unsafe fn pystring_ascii_new<'py>(py: Python<'py>, s: &str) -> Bound<'py, PyString> {
    unsafe {
        #[cfg(not(any(PyPy, GraalPy, Py_LIMITED_API)))]
        {
            if s.len() <= 1 {
                return PyString::new(py, s);
            }
            // SAFETY: `PyUnicode_New` returns a new owned reference or null. Converting it to a
```

Excerpt shortened; the complete reviewed range 319–355 is in `data/cases.json`.

Closing lines 350–355 ([verified immutable source](https://github.com/pydantic/jiter/blob/2b5ec63e505b44775e29b865c3161ea13bdad16b/crates/jiter/src/py_string_cache.rs#L350-L355))

```
        #[cfg(any(PyPy, GraalPy, Py_LIMITED_API))]
        {
            PyString::new(py, s)
        }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/9c/1f/8176d92e001f86505424b41664032ae26a882bc9ca41a32c803f373f9195/jiter-0.17.0.tar.gz); archive SHA-256 `03e432f226a453851079fb84cd17c6da9991eab723e28d716f14ae3d906e0c12`.
