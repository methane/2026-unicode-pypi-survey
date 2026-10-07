# pyqt6 6.11.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0180: PyCustomWidgets::importPlugins

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `native_dir.constData()` — borrowed_external_qstring. Borrowed QString.constData() QChar array. Qt code treats each QChar::unicode() as ushort, checks paired high/low surrogates, and adjusts Python length when converting through its separate general QString converter. Here no such decoding step occurs: the raw 16-bit values are passed directly to the kind-2 constructor.

**Length:** `native_dir.length()`; QString UTF-16 code units / QChar elements; interpreted by the API as 16-bit code point values, not bytes and not decoded scalar count.

**Confirmed:** The actual operands are fixed kind 2, constData(), and length(). General qpycore_PyObject_FromQString explicitly says FromKindAndData does not handle surrogate pairs in UCS2 strings, and its own algorithm combines pairs with QChar::surrogateToUcs4. These plugin calls do not invoke that converter.

**Inference / unresolved:** QChar native-endian 16-bit storage is the Qt ABI assumption made by this direct call; no Qt headers or package code were executed. Surrogate-pair-containing paths therefore enter this constructor as two surrogate code point values rather than one decoded supplementary scalar.

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: borrowed_external_qstring; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Borrowed QString storage is external Qt QChar/UTF-16 storage, not a borrowed Python Unicode FSR view. Local path conversion/constructor operands require no Python DATA/KIND read.; support_span_refs: package: pyqt6; path: pyqt6-6.11.0/designer/pluginloader.cpp; source_sha256: 6974e7d1bf20ab1f6cd7b7d0b4c6a790f8761e13f1c5d81ef9e81b89a31fb502; evidence_path: read-access-analysis/sources/pyqt6/6974e7d1bf20ab1f6cd7b7d0b4c6a790f8761e13f1c5d81ef9e81b89a31fb502.cpp; start: 208; end: 208; snippet_sha256: 660307bc607aa3e7fc01896c9b2dc8666ec5123b7646fc0b2afa519b2ac5ef31; verified_permalink: 

**Migration implication:** External 16-bit input remains an independent public-constructor compatibility requirement even if Python storage becomes UTF-8. Preserve kind-2 element semantics: substituting a UTF-16 decoder would combine surrogate pairs and change these calls' existing result.

**Activation / tracing:** Unconditional constructor in this source Plugin directory is converted for insertion into Python sys.path. Borrow lasts only through the copying constructor; QString remains alive. PyQt5/PyQt6 share this implementation lineage, with separate package records.

**Source:** `pyqt6-6.11.0/designer/pluginloader.cpp:208–208`; SHA-256 `6974e7d1bf20ab1f6cd7b7d0b4c6a790f8761e13f1c5d81ef9e81b89a31fb502`.

`pyqt6-6.11.0/designer/pluginloader.cpp` lines 208–208 (GitHub mapping not verified in saved evidence)

```
    PyObject *dobj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, native_dir.constData(), native_dir.length());
```

`pyqt6-6.11.0/designer/pluginloader.cpp` lines 205–208 (GitHub mapping not verified in saved evidence)

```
    // Convert the directory to a Python object with native separators.
    QString native_dir = QDir::toNativeSeparators(dir);

    PyObject *dobj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, native_dir.constData(), native_dir.length());
```

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 36–51 (GitHub mapping not verified in saved evidence)

```
    int qt_len = qstr.length();
    int kind;
    void *data;

    // We have to work out exactly which kind to use.  We assume ASCII while we
    // are checking so that we only go through the string once in the most
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.

    if ((obj = sipUnicodeNew(qt_len, 0x007f, &kind, &data)) == NULL)
        return NULL;

    const QChar *qch = qstr.constData();

    for (int qt_i = 0; qt_i < qt_len; ++qt_i)
    {
```

Closing lines 52–52 (GitHub mapping not verified in saved evidence)

```
        ushort uch = qch->unicode();
```

Original reviewed range 36–52 is recorded in `data/sites.json`; public excerpts are bounded.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 74–82 (GitHub mapping not verified in saved evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz); archive SHA-256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.

## K0181: PyQt6QmlPlugin::addToSysPath

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_2; expression `PyUnicode_2BYTE_KIND`.

**Input:** `py_plugin_dir.constData()` — borrowed_external_qstring. Borrowed QString.constData() QChar array. Qt code treats each QChar::unicode() as ushort, checks paired high/low surrogates, and adjusts Python length when converting through its separate general QString converter. Here no such decoding step occurs: the raw 16-bit values are passed directly to the kind-2 constructor.

**Length:** `py_plugin_dir.length()`; QString UTF-16 code units / QChar elements; interpreted by the API as 16-bit code point values, not bytes and not decoded scalar count.

**Confirmed:** The actual operands are fixed kind 2, constData(), and length(). General qpycore_PyObject_FromQString explicitly says FromKindAndData does not handle surrogate pairs in UCS2 strings, and its own algorithm combines pairs with QChar::surrogateToUcs4. These plugin calls do not invoke that converter.

**Inference / unresolved:** QChar native-endian 16-bit storage is the Qt ABI assumption made by this direct call; no Qt headers or package code were executed. Surrogate-pair-containing paths therefore enter this constructor as two surrogate code point values rather than one decoded supplementary scalar.

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: borrowed_external_qstring; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: none_locally_required; borrowed_fsr_dependency: none; api_symbols: ; public_owned_export_dependency: False; explanation: Borrowed QString storage is external Qt QChar/UTF-16 storage, not a borrowed Python Unicode FSR view. Local path conversion/constructor operands require no Python DATA/KIND read.; support_span_refs: package: pyqt6; path: pyqt6-6.11.0/qmlscene/pluginloader.cpp; source_sha256: b822b044db844afb6f93b11ef5234dc434649676b5901f80e6a19ec3bb02979b; evidence_path: read-access-analysis/sources/pyqt6/b822b044db844afb6f93b11ef5234dc434649676b5901f80e6a19ec3bb02979b.cpp; start: 336; end: 337; snippet_sha256: e5397993c22ee1acbbd5e1900f8c0f8efed48e784067f083ae9a7b77276311e6; verified_permalink: 

**Migration implication:** External 16-bit input remains an independent public-constructor compatibility requirement even if Python storage becomes UTF-8. Preserve kind-2 element semantics: substituting a UTF-16 decoder would combine surrogate pairs and change these calls' existing result.

**Activation / tracing:** Unconditional constructor in this source Plugin directory is converted for insertion into Python sys.path. Borrow lasts only through the copying constructor; QString remains alive. PyQt5/PyQt6 share this implementation lineage, with separate package records.

**Source:** `pyqt6-6.11.0/qmlscene/pluginloader.cpp:336–337`; SHA-256 `b822b044db844afb6f93b11ef5234dc434649676b5901f80e6a19ec3bb02979b`.

`pyqt6-6.11.0/qmlscene/pluginloader.cpp` lines 336–337 (GitHub mapping not verified in saved evidence)

```
    PyObject *plugin_dir_obj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND,
            py_plugin_dir.constData(), py_plugin_dir.length());
```

`pyqt6-6.11.0/qmlscene/pluginloader.cpp` lines 328–337 (GitHub mapping not verified in saved evidence)

```
// Add a directory to sys.path.
bool PyQt6QmlPlugin::addToSysPath(const QString &py_plugin_dir)
{
    PyObject *sys_path = getModuleAttr("sys", "path");

    if (!sys_path)
        return false;

    PyObject *plugin_dir_obj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND,
            py_plugin_dir.constData(), py_plugin_dir.length());
```

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 36–51 (GitHub mapping not verified in saved evidence)

```
    int qt_len = qstr.length();
    int kind;
    void *data;

    // We have to work out exactly which kind to use.  We assume ASCII while we
    // are checking so that we only go through the string once in the most
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.

    if ((obj = sipUnicodeNew(qt_len, 0x007f, &kind, &data)) == NULL)
        return NULL;

    const QChar *qch = qstr.constData();

    for (int qt_i = 0; qt_i < qt_len; ++qt_i)
    {
```

Closing lines 52–52 (GitHub mapping not verified in saved evidence)

```
        ushort uch = qch->unicode();
```

Original reviewed range 36–52 is recorded in `data/sites.json`; public excerpts are bounded.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 74–82 (GitHub mapping not verified in saved evidence)

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

[Frozen source distribution](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz); archive SHA-256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.

## K0184: qpycore_PyObject_FromQString

**Disposition:** non-use context; `comment_explanation`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** API name occurs in a comment explaining why this wrapper avoids it. Wrapper performs sipUnicodeNew/sipUnicodeWrite construction and explicitly joins surrogate pairs.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** This function is an alternative constructor, not an alias/wrapper around FromKindAndData.

**Source:** `pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp:42–43`; SHA-256 `3b8abccbdaaa1aa82845e2c0d099d4ed7b8d675ba76431e08c0dcc02b166441a`.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 42–43 (GitHub mapping not verified in saved evidence)

```
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.
```

[Frozen source distribution](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz); archive SHA-256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.

## K0185: qpycore_PyObject_FromQString

**Disposition:** non-use context; `alternative_constructor`; `handwritten`.

**Kind:** dynamic_output_kind_not_FromKind_input; expression `sipUnicodeNew(..., maxchar, &kind, &data)`.

**Input:** `qstr.constData()` — borrowed_external_qstring. Reads QChar units individually; joins valid high/low pairs, retains unpaired unit values, and writes code points into a newly allocated Python Unicode result. No FromKindAndData invocation.

**Length:** `qt_len=qstr.length(); py_len=qt_len minus matched surrogate-pair count`; Input: UTF-16/QChar units. Output: joined code point values (possibly unpaired surrogates)..

**Confirmed:** Active implementation uses sipUnicodeNew and sipUnicodeWrite rather than the named constructor.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** Separate output allocation/write dependency, outside the FromKindAndData active-call count. Its explicit surrogate handling explains why the plugin-path constructor semantics must not be described as UTF-16 decoding.

**Activation / tracing:** Active general QString conversion.

**Source:** `pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp:33–127`; SHA-256 `3b8abccbdaaa1aa82845e2c0d099d4ed7b8d675ba76431e08c0dcc02b166441a`.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 33–48 (GitHub mapping not verified in saved evidence)

```
PyObject *qpycore_PyObject_FromQString(const QString &qstr)
{
    PyObject *obj;
    int qt_len = qstr.length();
    int kind;
    void *data;

    // We have to work out exactly which kind to use.  We assume ASCII while we
    // are checking so that we only go through the string once in the most
    // common case.  Note that we can't use PyUnicode_FromKindAndData() because
    // it doesn't handle surrogates in UCS2 strings.

    if ((obj = sipUnicodeNew(qt_len, 0x007f, &kind, &data)) == NULL)
        return NULL;

    const QChar *qch = qstr.constData();
```

Closing lines 57–62 (GitHub mapping not verified in saved evidence)

```
            Py_DECREF(obj);

            // Work out what kind we really need and what the Python length
            // should be.
            uint maxchar = 0x00ff;

```

Original reviewed range 33–62 is recorded in `data/sites.json`; public excerpts are bounded.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 63–78 (GitHub mapping not verified in saved evidence)

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
                        maxchar = 0x10ffff;
```

Closing lines 87–92 (GitHub mapping not verified in saved evidence)

```
            }

            // Create the correctly sized object.
            if ((obj = sipUnicodeNew(py_len, maxchar, &kind, &data)) == NULL)
                return NULL;

```

Original reviewed range 63–92 is recorded in `data/sites.json`; public excerpts are bounded.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 93–108 (GitHub mapping not verified in saved evidence)

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
                {
```

Closing lines 117–122 (GitHub mapping not verified in saved evidence)

```

            break;
        }

        ++qch;

```

Original reviewed range 93–122 is recorded in `data/sites.json`; public excerpts are bounded.

`pyqt6-6.11.0/qpy/QtCore/qpycore_qstring.cpp` lines 123–127 (GitHub mapping not verified in saved evidence)

```
        sipUnicodeWrite(kind, data, qt_i, uch);
    }

    return obj;
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz); archive SHA-256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.

## K0186: %ConvertFromTypeCode for QChar

**Disposition:** non-use context; `commented_out_call`; `handwritten`.

**Kind:** fixed_2_in_inactive_proposal; expression `PyUnicode_2BYTE_KIND`.

**Input:** `sipCpp` — inactive_proposal. None

**Length:** `1`; one QChar / UTF-16 unit in inactive proposal.

**Confirmed:** The return FromKindAndData statement is prefixed // and accompanied by TODO. The active C++ return in the executable SIP directive calls qpycore_PyObject_FromQString(QString(*sipCpp)).

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** SIP directive code is executable generated-binding input despite lexical non_code labeling. The API statement itself is nevertheless a C++ comment.

**Source:** `pyqt6-6.11.0/sip/QtCore/qchar.sip:48–52`; SHA-256 `1e8b967f45479654e7a1b267404dda21af6ab70835f0317f6967c5ffd921e3a3`.

`pyqt6-6.11.0/sip/QtCore/qchar.sip` lines 48–52 (GitHub mapping not verified in saved evidence)

```
%ConvertFromTypeCode
// TODO: replace with...
// return PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, sipCpp, 1);
return qpycore_PyObject_FromQString(QString(*sipCpp));
%End
```

[Frozen source distribution](https://files.pythonhosted.org/packages/8b/47/b25c13eca5bebc6505394d0223e46d7ebf0c57dcac2ed908d7d19b18ab6b/pyqt6-6.11.0.tar.gz); archive SHA-256 `45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889`.
