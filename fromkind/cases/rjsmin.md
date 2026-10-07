# rjsmin 1.2.5

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0153: legacy Unicode API compatibility macro

**Disposition:** non-use context; `macro_definition`; `handwritten`.

**Kind:** forwarded_ignored_kind; expression `forwarded/dynamic; see snippets`.

**Input:** `(Py_UNICODE *)(data)` — no observed operational consumer. Compatibility definition forwards data/length to PyUnicode_FromUnicode and ignores kind; only present under absent PyUnicode_GET_LENGTH. All retained files scanned for caller closure; none invokes it.

**Length:** `length`; legacy Py_UNICODE elements (2 or 4 bytes per Py_UNICODE_SIZE).

**Confirmed:** Exact retained source snippet included (rjsmin-1.2.5/cext.h:199–241) Actual input/output UTF8 constructor path, not target alias activation (rjsmin-1.2.5/rjsmin.c:567–571) Actual input/output UTF8 constructor path, not target alias activation (rjsmin-1.2.5/rjsmin.c:609–613) Actual input/output UTF8 constructor path, not target alias activation (rjsmin-1.2.5/rjsmin.c:621–625) Actual input/output UTF8 constructor path, not target alias activation (rjsmin-1.2.5/rjsmin.c:666–670)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** No FromKindAndData consumer established in saved source; active minifier paths encode input to UTF8 bytes and decode UTF8 output.

**Activation / tracing:** Provider definition only, not API use. Both packages share byte-identical cext.h.

**Source:** `rjsmin-1.2.5/cext.h:199–241`; SHA-256 `7410c4410cf9948f0f9deb73724b37bc9c56dedeff5700b7c2d2dbf03922dd7f`.

`rjsmin-1.2.5/cext.h` lines 199–214 (GitHub mapping not verified in saved evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/59/16/14288d309d0f42c6586440c47bf6ec1a880218f698f30293fa3782db4008/rjsmin-1.2.5.tar.gz); archive SHA-256 `a3f8040b0273dec773e0e807e86a4d0a9535516c0a0a35aa1bb6de6e15bb1f09`.
