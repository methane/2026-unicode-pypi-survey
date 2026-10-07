# tokenizers 0.23.2

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0188: Commented alternative in NumPy string-array conversion

**Disposition:** non-use context; `non_use`; `handwritten`.

**Kind:** not_applicable; expression ``.

**Input:** `` — No actual input buffer passed by an executable call in this region.. 

**Length:** ``; .

**Confirmed:** Entire FromKindAndData construction and subsequent Python-string conversion are commented out. Active code above converts the raw bytes through Rust str::from_utf8 and to_owned; it does not call this API.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No actual constructor consumer to migrate here. Declaration/binding/linker references track API availability; comments alone do not establish runtime use.

**Activation / tracing:** 

**Source:** `tokenizers-0.23.2/bindings/python/src/tokenizer.rs:332–346`; SHA-256 `86b4e924985a822ae4e57bfa6ca43997d33fc974b74b8ccd4eee584dda30c097`.

`tokenizers-0.23.2/bindings/python/src/tokenizer.rs` lines 332–346 (GitHub mapping not verified in saved evidence)

```
            let seq = (0..n_elem)
                .map(|i| {
                    let bytes = &all_bytes[i * elsize..(i + 1) * elsize];
                    Ok(std::str::from_utf8(bytes)
                        .map_err(|e| exceptions::PyValueError::new_err(e.to_string()))?
                        .to_owned())
                    // let unicode = pyo3::ffi::PyUnicode_FromKindAndData(
                    //     pyo3::ffi::PyUnicode_4BYTE_KIND as _,
                    //     bytes.as_ptr() as *const _,
                    //     elsize as isize / alignment as isize,
                    // );
                    // let py = ob.py();
                    // let obj = Py<PyAny>::from_owned_ptr(py, unicode);
                    // let s = obj.downcast_bound::<PyString>(py)?;
                    // Ok(s.to_string_lossy().trim_matches(char::from(0)).to_owned())
```

[Frozen source distribution](https://files.pythonhosted.org/packages/18/1e/bc6587c5ab643b2e17776cace9070a2ae73549c86bffac9934a600bf3c31/tokenizers-0.23.2.tar.gz); archive SHA-256 `7f0f085686b9de0d0079e6f874ae053600db64c5d13049e0bbc0119926d25aac`.
