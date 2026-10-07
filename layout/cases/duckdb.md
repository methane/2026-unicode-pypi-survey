# duckdb 1.5.6

1 confirmed layout regions; 3 reviewed regions including non-direct context.

## L1107: NumpyScan::Scan object-string branch

**Classification:** direct layout dependency; project_source; `utf8_cache_read`.

**Purpose:** Zero-copy string_t from cached UTF8 fields in NumPy/Pandas object column scan.

**Migration effect:** Field positions/cache availability change; native UTF8 may preserve fastpath through API. Zero-copy stored pointers require source lifetime independently of representation.

**Fields / layout:** utf8, utf8_length. Types: PyCompactUnicodeObject.

**Source:** `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp:351–449`. SHA-256 `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`.

**Activation / context:** unicode_obj is dereferenced at422/424; ascii_obj at419 is unused and its token is audited as typed_cast_unused. Compact checks pass typed pointer into API wrappers rather than direct state fields.

Lines 407–424 ([verified immutable source](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L407-L424))

```
			// Python 3 string representation:
			// https://github.com/python/cpython/blob/3a8fdb28794b2f19f6c8464378fb8b46bce1f5f4/Include/cpython/unicodeobject.h#L79
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
				// compact unicode string: is there utf8 data available?
				if (unicode_obj->utf8) {
					// there is! zero copy
					tgt_ptr[row] = string_t(const_char_ptr_cast(unicode_obj->utf8), unicode_obj->utf8_length);
```

Excerpt shortened; the complete reviewed range 407–449 is in `data/cases.json`.

Closing lines 444–449 ([verified immutable source](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L444-L449))

```
					}
				} else {
					throw InvalidInputException("Unsupported string type: no clue what this string is");
				}
			}
		}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz); archive SHA-256 `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.

## L1108: PyUtil::PyUnicodeIsCompact / PyUnicodeIsASCII

**Classification:** non-direct context; project_source; `typed_cast_api`.

**Purpose:** Typed pointer parameters are forwarded to PyUnicode_IS_COMPACT/IS_ASCII APIs.

**Migration effect:** Type names here do not establish explicit direct struct-field dependence. API implementation/macro expansion is provider-owned.

**Fields / layout:** none. Types: PyCompactUnicodeObject.

**Source:** `duckdb-1.5.6/src/duckdb_py/include/duckdb_python/pyutil.hpp:33–39`. SHA-256 `c7c988012cfabbcf693cd012a23e1e33cd60f2b71e54e3412a460e18bf7e4f7d`.

**Activation / context:** No member dereference, sizeof, pointer arithmetic, or output mutation in these methods.

Lines 33–39 ([verified immutable source](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/include/duckdb_python/pyutil.hpp#L33-L39))

```
	static bool PyUnicodeIsCompact(PyCompactUnicodeObject *obj) {
		return PyUnicode_IS_COMPACT(obj);
	}

	static bool PyUnicodeIsASCII(PyCompactUnicodeObject *obj) {
		return PyUnicode_IS_ASCII(obj);
	}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz); archive SHA-256 `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.

## L1137: unused ascii_obj cast

**Classification:** non-direct context; project_source; `typed_cast_unused`.

**Purpose:** Unused cast in non-ASCII branch.

**Migration effect:** No field access/arithmetic from this variable.

**Fields / layout:** none. Types: PyASCIIObject.

**Source:** `duckdb-1.5.6/src/duckdb_py/numpy/numpy_scan.cpp:419–419`. SHA-256 `e6ed41a73b8d8f5ad30b8b9f0de8f7dd0eacd1cfc3a0f126016e15817af65c73`.

**Activation / context:** unicode_obj separately has actual direct cache fields.

Lines 419–419 ([verified immutable source](https://github.com/duckdb/duckdb-python/blob/802a345bb627435d2a05d63cb74454fa98b60b5e/src/duckdb_py/numpy/numpy_scan.cpp#L419-L419))

```
				auto ascii_obj = reinterpret_cast<PyASCIIObject *>(val);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz); archive SHA-256 `166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8`.
