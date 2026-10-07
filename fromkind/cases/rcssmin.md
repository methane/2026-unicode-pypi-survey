# rcssmin 1.2.2

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0154: legacy Unicode API compatibility macro

**Disposition:** non-use context; `macro_definition`; `handwritten`.

**Kind:** forwarded_ignored_kind; expression `forwarded/dynamic; see snippets`.

**Input:** `(Py_UNICODE *)(data)` — no observed operational consumer. Compatibility definition forwards data/length to PyUnicode_FromUnicode and ignores kind; only present under absent PyUnicode_GET_LENGTH. All retained files scanned for caller closure; none invokes it.

**Length:** `length`; legacy Py_UNICODE elements (2 or 4 bytes per Py_UNICODE_SIZE).

**Confirmed:** Exact retained source snippet included (rcssmin-1.2.2/cext.h:199–241) Actual input/output UTF8 constructor path, not target alias activation (rcssmin-1.2.2/rcssmin.c:1206–1210) Actual input/output UTF8 constructor path, not target alias activation (rcssmin-1.2.2/rcssmin.c:1259–1263) Actual input/output UTF8 constructor path, not target alias activation (rcssmin-1.2.2/rcssmin.c:1271–1275) Actual input/output UTF8 constructor path, not target alias activation (rcssmin-1.2.2/rcssmin.c:1327–1331)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** No FromKindAndData consumer established in saved source; active minifier paths encode input to UTF8 bytes and decode UTF8 output.

**Activation / tracing:** Provider definition only, not API use. Both packages share byte-identical cext.h.

**Source:** `rcssmin-1.2.2/cext.h:199–241`; SHA-256 `7410c4410cf9948f0f9deb73724b37bc9c56dedeff5700b7c2d2dbf03922dd7f`.

`rcssmin-1.2.2/cext.h` lines 199–214 (GitHub mapping not verified in saved evidence)

```
/*
 * Fake py 3.3 Unicode APIs
 */
#ifndef PyUnicode_GET_LENGTH

#ifdef EXT_PEP393
#undef EXT_PEP393
#endif

#define EXT_UNI_CP Py_UNICODE
enum PyUnicode_Kind {
/* String contains only wstr byte characters.  This is only possible
   when the string was created with a legacy API and _PyUnicode_Ready()
   has not been called yet.  */
    PyUnicode_WCHAR_KIND = 0,
/* Return values of the PyUnicode_KIND() macro: */
```

Closing lines 236–241 (GitHub mapping not verified in saved evidence)

```
    do { \
        ((Py_UNICODE *)(data))[(index)] = (Py_UNICODE)(value); \
    } while(0)

#define PyUnicode_FromKindAndData(kind, data, length) \
    (PyUnicode_FromUnicode((Py_UNICODE *)data, length))
```

Original reviewed range 199–241 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/81/af/c9654b4f9b054ec163ed7cb20d8db0e5ae05e2e9ce99a4c11d91a2180b3f/rcssmin-1.2.2.tar.gz); archive SHA-256 `806986eaf7414545edc28a1d29523e9560e49e151ff4a337d9d1f0271d6e1cc4`.
