# Qt: actual FromKindAndData use and UTF16 semantics

QString stores UTF16 QChar elements. `PyUnicode_FromKindAndData(kind=2, ...)` consumes 16-bit integer code-point values; it is not a UTF16 decoder. The survey confirms four plugin-loader calls that directly pass a whole QString's storage. It does not establish correct non-BMP decoding at those calls. This narrows the earlier provisional description of an external Qt-buffer use.

| Package | Version | Function | Physical LF location |
| --- | --- | --- | --- |
| pyqt5 | 5.15.11 | PyCustomWidgets::importPlugins | `PyQt5-5.15.11/designer/pluginloader.cpp:182–182` |
| pyqt5 | 5.15.11 | PyQt5QmlPlugin::addToSysPath | `PyQt5-5.15.11/qmlscene/pluginloader.cpp:338–339` |
| pyqt6 | 6.11.0 | PyCustomWidgets::importPlugins | `pyqt6-6.11.0/designer/pluginloader.cpp:208–208` |
| pyqt6 | 6.11.0 | PyQt6QmlPlugin::addToSysPath | `pyqt6-6.11.0/qmlscene/pluginloader.cpp:336–337` |

PyQt5 `designer/pluginloader.cpp:178–182`:

```cpp
    // Convert the directory to a Python object with native separators.
    QString native_dir = QDir::toNativeSeparators(dir);

#if PY_VERSION_HEX >= 0x03030000
    PyObject *dobj = PyUnicode_FromKindAndData(PyUnicode_2BYTE_KIND, native_dir.constData(), native_dir.length());
```

`native_dir` is a QString; `constData()` is a `const QChar *`, and `length()` counts QChar/UTF16 code units. There is no `toUcs4()` or other pair-combining conversion between these statements. The other three sites use the same direct argument pattern. Their activation guard is `PY_VERSION_HEX >= 0x03030000`.

BMP non-surrogate values match the kind-2 input interpretation. A UTF16 pair `D83D DE00`, however, is taken as two values U+D83D and U+DE00 rather than combined as U+1F600. This is a consequence of the API contract, not a runtime test or proof of a observed plugin-path failure.

The separate `qpycore_PyObject_FromQString(const QString &qstr)` in PyQt5 `qpy/QtCore/qpycore_qstring.cpp:48–158` handles general QString conversion. In its `PYQT_PEP_393` branch it counts paired surrogates at lines92–98, reduces the Python length, and at lines117–131 explicitly uses `QChar::surrogateToUcs4(*qch, *(qch + 1))` followed by `sipUnicodeWrite`. It avoids the target constructor; its source comment gives the lack of surrogate-pair handling as the reason. Its historical `Py_UNICODE_WIDE` branch instead constructs `QVector<uint> ucs4 = qstr.toUcs4()` at line142. Neither is the four direct plugin-loader call paths.

The `qchar.sip` candidate is a commented TODO mentioning the target constructor, not an actual constructor call on a single QChar. SIP's active alternate converter invocations are supporting non-use evidence, separately recorded.

Authoritative semantic context checked on 2026-10-05: [Qt QString documentation](https://doc.qt.io/qt-6/qstring.html#details) and [Python constructor documentation](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromKindAndData). These live documentation links are context, not immutable source mappings. The package calls above are sourced from the frozen sdists. [PyQt5 evidence, member/archive hashes and exact snippets](cases/pyqt5.md); [PyQt6 evidence](cases/pyqt6.md). No Qt headers were separately downloaded or compiled.
