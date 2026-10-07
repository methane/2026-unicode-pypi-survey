# pyqt5 5.15.11

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0178: PyCustomWidgets::importPlugins

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `native_dir.constData()` — borrowed_external_qstring. Borrowed QString.constData() QChar array. Qt code treats each QChar::unicode() as ushort, checks paired high/low surrogates, and adjusts Python length when converting through its separate general QString converter. Here no such decoding step occurs: the raw 16-bit values are passed directly to the kind-2 constructor.

**Length:** `native_dir.length()`; QString UTF-16 code units / QChar elements; interpreted by the API as 16-bit code point values, not bytes and not decoded scalar count.

**Confirmed:** The actual operands are fixed kind 2, constData(), and length(). General qpycore_PyObject_FromQString explicitly says FromKindAndData does not handle surrogate pairs in UCS2 strings, and its own algorithm combines pairs with QChar::surrogateToUcs4. These plugin calls do not invoke that converter.

**Inference / unresolved:** QChar native-endian 16-bit storage is the Qt ABI assumption made by this direct call; no Qt headers or package code were executed. Surrogate-pair-containing paths therefore enter this constructor as two surrogate code point values rather than one decoded supplementary scalar.

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: borrowed_external_qstring; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Borrowed QString storage is external Qt QChar/UTF-16 storage, not a borrowed Python Unicode FSR view. Local path conversion/constructor operands require no Python DATA/KIND read.; support_span_refs: package: pyqt5; path: PyQt5-5.15.11/designer/pluginloader.cpp; source_sha256: 984b906eec3cf070ce5a797bbf3fcee8411b2c493683fd3157544c6b3a8d5ae2; evidence_path: read-access-analysis/sources/pyqt5/984b906eec3cf070ce5a797bbf3fcee8411b2c493683fd3157544c6b3a8d5ae2.cpp; start: 182; end: 182; snippet_sha256: 660307bc607aa3e7fc01896c9b2dc8666ec5123b7646fc0b2afa519b2ac5ef31; verified_permalink: 

**Migration implication:** External 16-bit input remains an independent public-constructor compatibility requirement even if Python storage becomes UTF-8. Preserve kind-2 element semantics: substituting a UTF-16 decoder would combine surrogate pairs and change these calls' existing result.

**Activation / tracing:** PY_VERSION_HEX >= 0x03030000; older alternate constructors are outside this API scope Plugin directory is converted for insertion into Python sys.path. Borrow lasts only through the copying constructor; QString remains alive. PyQt5/PyQt6 share this implementation lineage, with separate package records.

**Source:** `PyQt5-5.15.11/designer/pluginloader.cpp:182–182`; SHA-256 `984b906eec3cf070ce5a797bbf3fcee8411b2c493683fd3157544c6b3a8d5ae2`.

`PyQt5-5.15.11/designer/pluginloader.cpp` lines 182–182 (GitHub mapping not verified in saved evidence)

```
    PyObject *dobj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, native_dir.constData(), native_dir.length());
```

`PyQt5-5.15.11/designer/pluginloader.cpp` lines 178–182 (GitHub mapping not verified in saved evidence)

```
    // Convert the directory to a Python object with native separators.
    QString native_dir = QDir::toNativeSeparators(dir);

#if PY_VERSION_HEX >= 0x03030000
    PyObject *dobj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, native_dir.constData(), native_dir.length());
```

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 53–68 (GitHub mapping not verified in saved evidence)

```
    // We have to work out exactly which kind to use.  We assume ASCII while we
    // are checking so that we only go through the string once in the most
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.
    int qt_len = qstr.length();
    int kind;
    void *data;

    if ((obj = sipUnicodeNew(qt_len, 0x007f, &kind, &data)) == NULL)
        return NULL;

    const QChar *qch = qstr.constData();

    for (int qt_i = 0; qt_i < qt_len; ++qt_i)
    {
        ushort uch = qch->unicode();
```

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 90–98 (GitHub mapping not verified in saved evidence)

```
                    // See if this is a surrogate pair.  Note that we cannot
                    // trust that the QString is terminated by a null QChar.
                    if (qch->isHighSurrogate() && qt_i + 1 < qt_len && (qch + 1)->isLowSurrogate())
                    {
                        maxchar = 0x10ffff;
                        --py_len;
                        ++qch;
                        ++qt_i;
                    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0e/07/c9ed0bd428df6f87183fca565a79fee19fa7c88c7f00a7f011ab4379e77a/PyQt5-5.15.11.tar.gz); archive SHA-256 `fda45743ebb4a27b4b1a51c6d8ef455c4c1b5d610c90d2934c7802b5c1557c52`.

## K0179: PyQt5QmlPlugin::addToSysPath

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `py_plugin_dir.constData()` — borrowed_external_qstring. Borrowed QString.constData() QChar array. Qt code treats each QChar::unicode() as ushort, checks paired high/low surrogates, and adjusts Python length when converting through its separate general QString converter. Here no such decoding step occurs: the raw 16-bit values are passed directly to the kind-2 constructor.

**Length:** `py_plugin_dir.length()`; QString UTF-16 code units / QChar elements; interpreted by the API as 16-bit code point values, not bytes and not decoded scalar count.

**Confirmed:** The actual operands are fixed kind 2, constData(), and length(). General qpycore_PyObject_FromQString explicitly says FromKindAndData does not handle surrogate pairs in UCS2 strings, and its own algorithm combines pairs with QChar::surrogateToUcs4. These plugin calls do not invoke that converter.

**Inference / unresolved:** QChar native-endian 16-bit storage is the Qt ABI assumption made by this direct call; no Qt headers or package code were executed. Surrogate-pair-containing paths therefore enter this constructor as two surrogate code point values rather than one decoded supplementary scalar.

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: borrowed_external_qstring; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Borrowed QString storage is external Qt QChar/UTF-16 storage, not a borrowed Python Unicode FSR view. Local path conversion/constructor operands require no Python DATA/KIND read.; support_span_refs: package: pyqt5; path: PyQt5-5.15.11/qmlscene/pluginloader.cpp; source_sha256: 32b6b4d6f57b2b82c75ba1c5cd4df323b7b21d939547502ef35f8a627a8dde64; evidence_path: read-access-analysis/sources/pyqt5/32b6b4d6f57b2b82c75ba1c5cd4df323b7b21d939547502ef35f8a627a8dde64.cpp; start: 338; end: 339; snippet_sha256: e5397993c22ee1acbbd5e1900f8c0f8efed48e784067f083ae9a7b77276311e6; verified_permalink: 

**Migration implication:** External 16-bit input remains an independent public-constructor compatibility requirement even if Python storage becomes UTF-8. Preserve kind-2 element semantics: substituting a UTF-16 decoder would combine surrogate pairs and change these calls' existing result.

**Activation / tracing:** PY_VERSION_HEX >= 0x03030000; older alternate constructors are outside this API scope Plugin directory is converted for insertion into Python sys.path. Borrow lasts only through the copying constructor; QString remains alive. PyQt5/PyQt6 share this implementation lineage, with separate package records.

**Source:** `PyQt5-5.15.11/qmlscene/pluginloader.cpp:338–339`; SHA-256 `32b6b4d6f57b2b82c75ba1c5cd4df323b7b21d939547502ef35f8a627a8dde64`.

`PyQt5-5.15.11/qmlscene/pluginloader.cpp` lines 338–339 (GitHub mapping not verified in saved evidence)

```
    PyObject *plugin_dir_obj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND,
            py_plugin_dir.constData(), py_plugin_dir.length());
```

`PyQt5-5.15.11/qmlscene/pluginloader.cpp` lines 329–339 (GitHub mapping not verified in saved evidence)

```
// Add a directory to sys.path.
bool PyQt5QmlPlugin::addToSysPath(const QString &py_plugin_dir)
{
    PyObject *sys_path = getModuleAttr("sys", "path");

    if (!sys_path)
        return false;

#if PY_VERSION_HEX >= 0x03030000
    PyObject *plugin_dir_obj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND,
            py_plugin_dir.constData(), py_plugin_dir.length());
```

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 53–68 (GitHub mapping not verified in saved evidence)

```
    // We have to work out exactly which kind to use.  We assume ASCII while we
    // are checking so that we only go through the string once in the most
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.
    int qt_len = qstr.length();
    int kind;
    void *data;

    if ((obj = sipUnicodeNew(qt_len, 0x007f, &kind, &data)) == NULL)
        return NULL;

    const QChar *qch = qstr.constData();

    for (int qt_i = 0; qt_i < qt_len; ++qt_i)
    {
        ushort uch = qch->unicode();
```

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 90–98 (GitHub mapping not verified in saved evidence)

```
                    // See if this is a surrogate pair.  Note that we cannot
                    // trust that the QString is terminated by a null QChar.
                    if (qch->isHighSurrogate() && qt_i + 1 < qt_len && (qch + 1)->isLowSurrogate())
                    {
                        maxchar = 0x10ffff;
                        --py_len;
                        ++qch;
                        ++qt_i;
                    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0e/07/c9ed0bd428df6f87183fca565a79fee19fa7c88c7f00a7f011ab4379e77a/PyQt5-5.15.11.tar.gz); archive SHA-256 `fda45743ebb4a27b4b1a51c6d8ef455c4c1b5d610c90d2934c7802b5c1557c52`.

## K0182: qpycore_PyObject_FromQString

**Disposition:** non-use context; `comment_explanation`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** API name occurs in a comment explaining why this wrapper avoids it. Wrapper performs sipUnicodeNew/sipUnicodeWrite construction and explicitly joins surrogate pairs.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** This function is an alternative constructor, not an alias/wrapper around FromKindAndData.

**Source:** `PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp:55–56`; SHA-256 `fbca7258407b4ac067e09875a73d0130aa1a40ab006414685406ec56d8837533`.

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 55–56 (GitHub mapping not verified in saved evidence)

```
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0e/07/c9ed0bd428df6f87183fca565a79fee19fa7c88c7f00a7f011ab4379e77a/PyQt5-5.15.11.tar.gz); archive SHA-256 `fda45743ebb4a27b4b1a51c6d8ef455c4c1b5d610c90d2934c7802b5c1557c52`.

## K0183: qpycore_PyObject_FromQString

**Disposition:** non-use context; `alternative_constructor`; `handwritten`.

**Kind:** dynamic_output_kind_not_FromKind_input; expression `sipUnicodeNew(..., maxchar, &kind, &data)`.

**Input:** `qstr.constData()` — borrowed_external_qstring. Reads QChar units individually; joins valid high/low pairs, retains unpaired unit values, and writes code points into a newly allocated Python Unicode result. No FromKindAndData invocation.

**Length:** `qt_len=qstr.length(); py_len=qt_len minus matched surrogate-pair count`; Input: UTF-16/QChar units. Output: joined code point values (possibly unpaired surrogates)..

**Confirmed:** Active implementation uses sipUnicodeNew and sipUnicodeWrite rather than the named constructor.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** Separate output allocation/write dependency, outside the FromKindAndData active-call count. Its explicit surrogate handling explains why the plugin-path constructor semantics must not be described as UTF-16 decoding.

**Activation / tracing:** PyQt5 PEP393 branch activated via PYQT_PEP_393 compiler/version guards. Legacy wide fallback uses qstr.toUcs4() + PyUnicode_FromUnicode/memcpy; narrow fallback uses qstr.utf16() + PyUnicode_FromUnicode/memcpy. Neither fallback calls FromKindAndData.

**Source:** `PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp:48–158`; SHA-256 `fbca7258407b4ac067e09875a73d0130aa1a40ab006414685406ec56d8837533`.

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 48–63 (GitHub mapping not verified in saved evidence)

```
PyObject *qpycore_PyObject_FromQString(const QString &qstr)
{
    PyObject *obj;

#if defined(PYQT_PEP_393)
    // We have to work out exactly which kind to use.  We assume ASCII while we
    // are checking so that we only go through the string once in the most
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.
    int qt_len = qstr.length();
    int kind;
    void *data;

    if ((obj = sipUnicodeNew(qt_len, 0x007f, &kind, &data)) == NULL)
        return NULL;

```

Closing lines 72–77 (GitHub mapping not verified in saved evidence)

```
            // This is useless.
            Py_DECREF(obj);

            // Work out what kind we really need and what the Python length
            // should be.
            uint maxchar = 0x00ff;
```

Original reviewed range 48–77 is recorded in `data/sites.json`; public excerpts are bounded.

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 78–93 (GitHub mapping not verified in saved evidence)

```

            int py_len = qt_len;

            while (qt_i < qt_len)
            {
                uch = qch->unicode();

                if (uch > 0x00ff)
                {
                    if (maxchar == 0x00ff)
                        maxchar = 0x00ffff;

                    // See if this is a surrogate pair.  Note that we cannot
                    // trust that the QString is terminated by a null QChar.
                    if (qch->isHighSurrogate() && qt_i + 1 < qt_len && (qch + 1)->isLowSurrogate())
                    {
```

Closing lines 102–107 (GitHub mapping not verified in saved evidence)

```
                ++qt_i;
            }

            // Create the correctly sized object.
            if ((obj = sipUnicodeNew(py_len, maxchar, &kind, &data)) == NULL)
                return NULL;
```

Original reviewed range 78–107 is recorded in `data/sites.json`; public excerpts are bounded.

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 108–123 (GitHub mapping not verified in saved evidence)

```

            qch = qstr.constData();

            int qt_i2 = 0;

            for (int py_i = 0; py_i < py_len; ++py_i)
            {
                uint py_ch;

                if (qch->isHighSurrogate() && qt_i2 + 1 < qt_len && (qch + 1)->isLowSurrogate())
                {
                    py_ch = QChar::surrogateToUcs4(*qch, *(qch + 1));
                    ++qt_i2;
                    ++qch;
                }
                else
```

Closing lines 132–137 (GitHub mapping not verified in saved evidence)

```
            }

            break;
        }

        ++qch;
```

Original reviewed range 108–137 is recorded in `data/sites.json`; public excerpts are bounded.

`PyQt5-5.15.11/qpy/QtCore/qpycore_qstring.cpp` lines 138–153 (GitHub mapping not verified in saved evidence)

```

        sipUnicodeWrite(kind, data, qt_i, uch);
    }
#elif defined(Py_UNICODE_WIDE)
    QVector<uint> ucs4 = qstr.toUcs4();

    if ((obj = PyUnicode_FromUnicode(NULL, ucs4.size())) == NULL)
        return NULL;

    memcpy(PyUnicode_AS_UNICODE(obj), ucs4.constData(),
            ucs4.size() * sizeof (Py_UNICODE));
#else
    if ((obj = PyUnicode_FromUnicode(NULL, qstr.length())) == NULL)
        return NULL;

    memcpy(PyUnicode_AS_UNICODE(obj), qstr.utf16(),
```

Closing lines 154–158 (GitHub mapping not verified in saved evidence)

```
            qstr.length() * sizeof (Py_UNICODE));
#endif

    return obj;
}
```

Original reviewed range 138–158 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/0e/07/c9ed0bd428df6f87183fca565a79fee19fa7c88c7f00a7f011ab4379e77a/PyQt5-5.15.11.tar.gz); archive SHA-256 `fda45743ebb4a27b4b1a51c6d8ef455c4c1b5d610c90d2934c7802b5c1557c52`.
