# pyroscope-io 1.2.5

0 confirmed layout regions; 1 reviewed regions including non-direct context.

## L1134: unicode_to_sv_no_alloc

**Classification:** non-direct context; project_source; `api_only_unicode_view`.

**Purpose:** Borrow compact ASCII DATA and length via Unicode APIs inside allocator sampling.

**Migration effect:** No named explicit Unicode struct cast or local mirror in saved package corpus; macro provider layout is not application-owned direct source field access.

**Fields / layout:** none. Types: .

**Source:** `pyroscope_io-1.2.5/cpp/_memalloc_tb.cpp:8–25`. SHA-256 `c360b6a6190bef401e8c2d4bb8c9fa86a13cab14300533951406c275b81f85bc`.

**Activation / context:** Do not infer PyUnicodeObject dependence just because DATA/KIND APIs internally use CPython structs.

Lines 8–25 ([verified immutable source](https://github.com/grafana/pyroscope-python/blob/080e93b039ea0ceb2a4bae907ec144b423cc2958/cpp/_memalloc_tb.cpp#L8-L25))

```
 *
 * Uses only inline struct-field reads: PyUnicode_IS_COMPACT_ASCII,
 * PyUnicode_DATA, PyUnicode_GET_LENGTH. These are available on Python 3.3+.
 *
 * For non-ASCII strings (extremely rare for function names and filenames),
 * returns "<non-ascii>" rather than calling PyUnicode_AsUTF8AndSize which
 * can trigger allocation of a UTF-8 cache via PyObject_Malloc. */
static inline std::string_view
unicode_to_sv_no_alloc(PyObject* obj)
{
    if (obj == NULL || !PyUnicode_Check(obj)) {
        return "<unknown>";
    }
    if (PyUnicode_IS_COMPACT_ASCII(obj)) {
        return std::string_view((const char*)PyUnicode_DATA(obj), (size_t)PyUnicode_GET_LENGTH(obj));
    }
    return "<non-ascii>";
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/6a/50/0e7e817d1b09da1238a6d942f16a6f427d820c0a8bf715604449b207caac/pyroscope_io-1.2.5.tar.gz); archive SHA-256 `fa91783313c8b7abfb698cb82e08ab33392b765e8eb603cc409454c8c6aa9c37`.
