# duckdb — non-simple Unicode reads

[All packages](README.md)

Version: 1.5.6. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`DecodePythonUnicode`](#case-001)
- [`NumpyScan::Scan`](#case-002)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `DecodePythonUnicode`

**Classification:** B. **Subtypes:** multiple passes. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

First pass measures UTF8 byte length, second pass encodes same codepoints from index0 again.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz). Archive SHA-256: `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.

**Function source:** `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 113–131. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`.

[Verified immutable function link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L113-L131).

### Read sites

- Site 1: lines 116–120; derived read; index expression `codepoints[i], i=0..count-1`. UTF8 length pass
- Site 2: lines 124–128; derived read; index expression `codepoints[i], i=0..count-1`. Encoding pass

### Contextual source excerpts

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 113–131. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L113-L131).

```cpp
static string_t DecodePythonUnicode(T *codepoints, idx_t codepoint_count, Vector &out) {
	// first figure out how many bytes to allocate
	idx_t utf8_length = 0;
	for (idx_t i = 0; i < codepoint_count; i++) {
		int len = Utf8Proc::CodepointLength(int(codepoints[i]));
		D_ASSERT(len >= 1);
		utf8_length += len;
	}
	int sz;
	auto result = StringVector::EmptyString(out, utf8_length);
	auto target = result.GetDataWriteable();
	for (idx_t i = 0; i < codepoint_count; i++) {
		Utf8Proc::CodepointToUtf8(int(codepoints[i]), sz, target);
		D_ASSERT(sz >= 1);
		target += sz;
	}
	result.Finalize();
	return result;
}
```


<a id="case-002"></a>

## 2. `NumpyScan::Scan`

**Classification:** B. **Subtypes:** multiple passes, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Mixed branches: compact ASCII/cached UTF8 handed to DuckDB string_t without encoding; absent UTF8 cache uses two-pass DecodePythonUnicode over full FSR codepoints.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** FSR decoder offsets are codepoints; string_t length is bytes (ASCII length coincides)

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

ASCII and cached UTF8 paths seek zero copy. Borrowed view needs existing backing storage lifetime. Row offset is NumPy array index, not Unicode codepoint offset.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz). Archive SHA-256: `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.

**Function source:** `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 202–472. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`.

[Verified immutable function link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L202-L472).

### Read sites

- Site 1: lines 414–440; derived read; index expression `DATA, cached utf8 pointer, typed DATA`. Branch-specific views/encoding

### Contextual source excerpts

Omitted from `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`: lines 206–411, 421–424, 443–469. The original contextual region was lines 202–472.
Omitted from `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`: lines 421–424, 443–448. The original contextual region was lines 409–451.

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 202–205. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L202-L205).

```cpp
void NumpyScan::Scan(PandasColumnBindData &bind_data, idx_t count, idx_t offset, Vector &out) {
	D_ASSERT(bind_data.pandas_col->Backend() == PandasColumnBackend::NUMPY);
	auto &numpy_col = reinterpret_cast<PandasNumpyColumn &>(*bind_data.pandas_col);
	auto &array = numpy_col.array;
```

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 412–420. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L412-L420).

```cpp
				continue;
			}
			if (PyUtil::PyUnicodeIsCompactASCII(val_handle)) {
				// ascii string: we can zero copy
				tgt_ptr[row] = string_t(PyUtil::PyUnicodeData(val_handle), PyUtil::PyUnicodeGetLength(val_handle));
			} else {
				// unicode gunk
				auto ascii_obj = reinterpret_cast<PyASCIIObject *>(val);
				auto unicode_obj = reinterpret_cast<PyCompactUnicodeObject *>(val);
```

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 425–442. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L425-L442).

```cpp
				} else if (PyUtil::PyUnicodeIsCompact(unicode_obj) &&
				           !PyUtil::PyUnicodeIsASCII(unicode_obj)) { // NOLINT
					auto kind = PyUtil::PyUnicodeKind(val_handle);
					switch (kind) {
					case PyUnicode_1BYTE_KIND:
						tgt_ptr[row] = DecodePythonUnicode<Py_UCS1>(PyUtil::PyUnicode1ByteData(val_handle),
						                                            PyUtil::PyUnicodeGetLength(val_handle), out);
						break;
					case PyUnicode_2BYTE_KIND:
						tgt_ptr[row] = DecodePythonUnicode<Py_UCS2>(PyUtil::PyUnicode2ByteData(val_handle),
						                                            PyUtil::PyUnicodeGetLength(val_handle), out);
						break;
					case PyUnicode_4BYTE_KIND:
						tgt_ptr[row] = DecodePythonUnicode<Py_UCS4>(PyUtil::PyUnicode4ByteData(val_handle),
						                                            PyUtil::PyUnicodeGetLength(val_handle), out);
						break;
					default:
						throw NotImplementedException(
```

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 470–472. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L470-L472).

```cpp
		throw NotImplementedException("Unsupported pandas type");
	}
}
```

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 409–420. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L409-L420).

```cpp
			py::handle val_handle(val);
			if (!py::isinstance<py::str>(val_handle)) {
				out_mask.SetInvalid(row);
				continue;
			}
			if (PyUtil::PyUnicodeIsCompactASCII(val_handle)) {
				// ascii string: we can zero copy
				tgt_ptr[row] = string_t(PyUtil::PyUnicodeData(val_handle), PyUtil::PyUnicodeGetLength(val_handle));
			} else {
				// unicode gunk
				auto ascii_obj = reinterpret_cast<PyASCIIObject *>(val);
				auto unicode_obj = reinterpret_cast<PyCompactUnicodeObject *>(val);
```

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 425–442. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L425-L442).

```cpp
				} else if (PyUtil::PyUnicodeIsCompact(unicode_obj) &&
				           !PyUtil::PyUnicodeIsASCII(unicode_obj)) { // NOLINT
					auto kind = PyUtil::PyUnicodeKind(val_handle);
					switch (kind) {
					case PyUnicode_1BYTE_KIND:
						tgt_ptr[row] = DecodePythonUnicode<Py_UCS1>(PyUtil::PyUnicode1ByteData(val_handle),
						                                            PyUtil::PyUnicodeGetLength(val_handle), out);
						break;
					case PyUnicode_2BYTE_KIND:
						tgt_ptr[row] = DecodePythonUnicode<Py_UCS2>(PyUtil::PyUnicode2ByteData(val_handle),
						                                            PyUtil::PyUnicodeGetLength(val_handle), out);
						break;
					case PyUnicode_4BYTE_KIND:
						tgt_ptr[row] = DecodePythonUnicode<Py_UCS4>(PyUtil::PyUnicode4ByteData(val_handle),
						                                            PyUtil::PyUnicodeGetLength(val_handle), out);
						break;
					default:
						throw NotImplementedException(
```

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 449–451. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L449-L451).

```cpp
		}
		break;
	}
```

### Callee analysis

- `DecodePythonUnicode` in `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 113–131: Exact frozen sdist source recovered and manually inspected B two-pass

Available source context:

- [`DecodePythonUnicode`](#helper-001) (`duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 113–131).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `DecodePythonUnicode`

Archive member `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp`, lines 113–131. Member SHA-256: `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`. [Verified immutable source link](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L113-L131).

```cpp
static string_t DecodePythonUnicode(T *codepoints, idx_t codepoint_count, Vector &out) {
	// first figure out how many bytes to allocate
	idx_t utf8_length = 0;
	for (idx_t i = 0; i < codepoint_count; i++) {
		int len = Utf8Proc::CodepointLength(int(codepoints[i]));
		D_ASSERT(len >= 1);
		utf8_length += len;
	}
	int sz;
	auto result = StringVector::EmptyString(out, utf8_length);
	auto target = result.GetDataWriteable();
	for (idx_t i = 0; i < codepoint_count; i++) {
		Utf8Proc::CodepointToUtf8(int(codepoints[i]), sz, target);
		D_ASSERT(sz >= 1);
		target += sz;
	}
	result.Finalize();
	return result;
}
```
