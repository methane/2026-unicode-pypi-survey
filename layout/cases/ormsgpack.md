# ormsgpack 1.12.2

9 confirmed layout regions; 12 reviewed regions including non-direct context.

## L1097: pyunicode_ascii

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from decoded Rust UTF8 by direct post-header writes.

**Migration effect:** Physical inline FSR header/payload assumptions must change; writing through a Unicode builder/UTF8 constructor avoids fixed offsets.

**Fields / layout:** header offset(1), inline1/2/4-byte payload, trailing NUL. Types: PyASCIIObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:30–38`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** One output-construction family across four widths; PyUnicode_New allocates fresh output before writes.

Lines 30–38 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L30-L38))

```
fn pyunicode_ascii(buf: &str) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(buf.len() as isize, 127);
        let data_ptr = ptr.cast::<PyASCIIObject>().offset(1).cast::<u8>();
        std::ptr::copy_nonoverlapping(buf.as_ptr(), data_ptr, buf.len());
        std::ptr::write(data_ptr.add(buf.len()), 0);
        ptr
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1098: pyunicode_onebyte

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from decoded Rust UTF8 by direct post-header writes.

**Migration effect:** Physical inline FSR header/payload assumptions must change; writing through a Unicode builder/UTF8 constructor avoids fixed offsets.

**Fields / layout:** header offset(1), inline1/2/4-byte payload, trailing NUL. Types: PyCompactUnicodeObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:42–53`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** One output-construction family across four widths; PyUnicode_New allocates fresh output before writes.

Lines 42–53 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L42-L53))

```
fn pyunicode_onebyte(buf: &str, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(num_chars as isize, 255);
        let mut data_ptr = ptr.cast::<PyCompactUnicodeObject>().offset(1).cast::<u8>();
        for each in buf.chars() {
            std::ptr::write(data_ptr, each as u8);
            data_ptr = data_ptr.offset(1);
        }
        std::ptr::write(data_ptr, 0);
        ptr
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1099: pyunicode_twobyte

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from decoded Rust UTF8 by direct post-header writes.

**Migration effect:** Physical inline FSR header/payload assumptions must change; writing through a Unicode builder/UTF8 constructor avoids fixed offsets.

**Fields / layout:** header offset(1), inline1/2/4-byte payload, trailing NUL. Types: PyCompactUnicodeObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:55–66`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** One output-construction family across four widths; PyUnicode_New allocates fresh output before writes.

Lines 55–66 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L55-L66))

```
fn pyunicode_twobyte(buf: &str, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(num_chars as isize, 65535);
        let mut data_ptr = ptr.cast::<PyCompactUnicodeObject>().offset(1).cast::<u16>();
        for each in buf.chars() {
            std::ptr::write(data_ptr, each as u16);
            data_ptr = data_ptr.offset(1);
        }
        std::ptr::write(data_ptr, 0);
        ptr
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1100: pyunicode_fourbyte

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from decoded Rust UTF8 by direct post-header writes.

**Migration effect:** Physical inline FSR header/payload assumptions must change; writing through a Unicode builder/UTF8 constructor avoids fixed offsets.

**Fields / layout:** header offset(1), inline1/2/4-byte payload, trailing NUL. Types: PyCompactUnicodeObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:68–79`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** One output-construction family across four widths; PyUnicode_New allocates fresh output before writes.

Lines 68–79 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L68-L79))

```
fn pyunicode_fourbyte(buf: &str, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(num_chars as isize, 1114111);
        let mut data_ptr = ptr.cast::<PyCompactUnicodeObject>().offset(1).cast::<u32>();
        for each in buf.chars() {
            std::ptr::write(data_ptr, each as u32);
            data_ptr = data_ptr.offset(1);
        }
        std::ptr::write(data_ptr, 0);
        ptr
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1101: hash_str [unicode_state]

**Classification:** direct layout dependency; project_source; `hash_metadata_read_write`.

**Purpose:** Hash compact Unicode data bytes and store cached hash.

**Migration effect:** Length/width/hash semantics and hash field offsets need preserving or public hash API.

**Fields / layout:** length, hash, payload width. Types: PyASCIIObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:83–91`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** unicode_state variant uses manual helpers; fallback uses DATA/KIND API but still accesses .length/.hash directly.

Lines 83–91 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L83-L91))

```
pub fn hash_str(op: *mut PyObject) -> Py_hash_t {
    unsafe {
        let ptr = pyunicode_compact_data(op);
        let len = (*op.cast::<PyASCIIObject>()).length * pyunicode_kind(op) as Py_ssize_t;
        let hash = compat::Py_HashBuffer(ptr, len);
        (*op.cast::<PyASCIIObject>()).hash = hash;
        hash
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1102: hash_str [not unicode_state]

**Classification:** direct layout dependency; project_source; `hash_metadata_read_write`.

**Purpose:** Hash compact Unicode data bytes and store cached hash.

**Migration effect:** Length/width/hash semantics and hash field offsets need preserving or public hash API.

**Fields / layout:** length, hash, payload width. Types: PyASCIIObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:95–103`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** unicode_state variant uses manual helpers; fallback uses DATA/KIND API but still accesses .length/.hash directly.

Lines 95–103 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L95-L103))

```
pub fn hash_str(op: *mut PyObject) -> Py_hash_t {
    unsafe {
        let ptr = PyUnicode_DATA(op);
        let len = (*op.cast::<PyASCIIObject>()).length * PyUnicode_KIND(op) as Py_ssize_t;
        let hash = compat::Py_HashBuffer(ptr, len);
        (*op.cast::<PyASCIIObject>()).hash = hash;
        hash
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1103: deserialize_map_with_str_keys

**Classification:** direct layout dependency; project_source; `hash_metadata_read`.

**Purpose:** Read string-key cached hash before known-hash dictionary insertion.

**Migration effect:** Metadata dependency rather than FSR indexed payload dependence.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `ormsgpack-1.12.2/src/deserialize/deserializer.rs:363–396`. SHA-256 `f9d321885c84a690997b34cd8b59521809539ad5fd6278391c73d504637ebaf1`.

**Activation / context:** Cached key already created/hashed by map key decoder; same family as hash_str producer.

Lines 363–380 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/deserialize/deserializer.rs#L363-L380))

```
    fn deserialize_map_with_str_keys(
        &mut self,
        len: u32,
    ) -> Result<NonNull<pyo3::ffi::PyObject>, Error> {
        let dict_ptr = unsafe { pydict_new_presized(len as pyo3::ffi::Py_ssize_t) };
        for _ in 0..len {
            let marker = self.read_marker()?;
            let key = match marker {
                Marker::FixStr(len) => self.deserialize_map_str_key(len.into()),
                Marker::Str8 => {
                    let len = self.read_u8()?;
                    self.deserialize_map_str_key(len.into())
                }
                Marker::Str16 => {
                    let len = self.read_u16()?;
                    self.deserialize_map_str_key(len.into())
                }
                Marker::Str32 => {
```

Excerpt shortened; the complete reviewed range 363–396 is in `data/cases.json`.

Closing lines 391–396 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/deserialize/deserializer.rs#L391-L396))

```
                pyo3::ffi::Py_DECREF(key.as_ptr());
                pyo3::ffi::Py_DECREF(value.as_ptr());
            }
        }
        unsafe { Ok(NonNull::new_unchecked(dict_ptr)) }
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1104: unicode_to_str unicode_state variant

**Classification:** direct layout dependency; project_source; `utf8_cache_header_read`.

**Purpose:** Expose ASCII inline data or existing UTF8 cache as Rust str; fallback invokes FFI.

**Migration effect:** UTF8 migration can simplify representation, but direct cache/header fields must change.

**Fields / layout:** length, utf8, utf8_length, ASCII header offset(1). Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode.rs:105–125`. SHA-256 `a011171ab81ec751b6e879b7ad4255212c59385df49b821631a91dd86d69cce4`.

**Activation / context:** unicode_state build cfg enabled for little-endian targets except Windows free-threaded Python; see retained build.rs.

Lines 105–122 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L105-L122))

```
#[cfg(unicode_state)]
#[inline]
pub fn unicode_to_str(op: *mut PyObject) -> Result<&'static str, UnicodeError> {
    unsafe {
        if unlikely!(!pyunicode_is_compact(op)) {
            unicode_to_str_via_ffi(op)
        } else if pyunicode_is_ascii(op) {
            let ptr = op.cast::<PyASCIIObject>().offset(1).cast::<u8>();
            let len = (*op.cast::<PyASCIIObject>()).length as usize;
            let slice = std::slice::from_raw_parts(ptr, len);
            Ok(std::str::from_utf8_unchecked(slice))
        } else if (*op.cast::<PyCompactUnicodeObject>()).utf8_length != 0 {
            let ptr = (*op.cast::<PyCompactUnicodeObject>()).utf8.cast::<u8>();
            let len = (*op.cast::<PyCompactUnicodeObject>()).utf8_length as usize;
            let slice = std::slice::from_raw_parts(ptr, len);
            Ok(std::str::from_utf8_unchecked(slice))
        } else {
            unicode_to_str_via_ffi(op)
```

Excerpt shortened; the complete reviewed range 105–125 is in `data/cases.json`.

Closing lines 123–125 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode.rs#L123-L125))

```
        }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1105: state flags and compact_data helpers

**Classification:** direct layout dependency; project_source; `state_bitfield_header_arithmetic`.

**Purpose:** Decode fixed state bits and return raw compact payload address.

**Migration effect:** State bit positions/header sizes are physical ABI assumptions, with explicit shift8 free-threaded3.14 vs shift2 other builds.

**Fields / layout:** state.kind, state.compact, state.ascii, header offset(1). Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/unicode_state.rs:29–68`. SHA-256 `be9fe46169fa6681ffc99317df8119dcccf9a8a38a6efa036f5a1a7c2e77302e`.

**Activation / context:** This supports UTF8 getter and hash_str; no struct declaration here. Types imported via pyo3::ffi::*.

Lines 29–46 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode_state.rs#L29-L46))

```

#[cfg(all(Py_3_14, Py_GIL_DISABLED))]
const STATE_KIND_INDEX: usize = 8;

#[cfg(not(all(Py_3_14, Py_GIL_DISABLED)))]
const STATE_KIND_INDEX: usize = 2;

const STATE_COMPACT_INDEX: usize = STATE_KIND_INDEX + 3;

const STATE_ASCII_INDEX: usize = STATE_COMPACT_INDEX + 1;

#[inline(always)]
pub unsafe fn pyunicode_kind(op: *mut PyObject) -> u32 {
    let state = (*op.cast::<PyASCIIObject>()).state;
    (state >> STATE_KIND_INDEX) & 7
}

#[inline(always)]
```

Excerpt shortened; the complete reviewed range 29–68 is in `data/cases.json`.

Closing lines 63–68 ([verified immutable source](https://github.com/ormsgpack/ormsgpack/blob/9645772ab1e19420fa509197a95fb40fcc92fe9f/src/ffi/cpython/unicode_state.rs#L63-L68))

```
    } else {
        op.cast::<PyCompactUnicodeObject>()
            .offset(1)
            .cast::<c_void>()
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1106: unicode_state activation

**Classification:** non-direct context; project_source; `activation_configuration`.

**Purpose:** Enable manual layout state access on supported target configurations.

**Migration effect:** Recorded guard, not a new layout access itself.

**Fields / layout:** none. Types: .

**Source:** `ormsgpack-1.12.2/build.rs:1–14`. SHA-256 `a0abb38494dd857849d38d735c4f26def6d5e03af292ac569e9a8f8bba7c963d`.

**Activation / context:** Reads build configuration only; saved script was never run.

Lines 1–14 (immutable GitHub mapping unavailable in saved verification evidence)

```
fn main() {
    pyo3_build_config::use_pyo3_cfgs();
    pyo3_build_config::add_extension_module_link_args();
    let python_config = pyo3_build_config::get();

    println!("cargo::rustc-check-cfg=cfg(unicode_state)");
    if std::env::var("CARGO_CFG_TARGET_ENDIAN").unwrap() == "little"
        && !(std::env::var("CARGO_CFG_TARGET_OS").unwrap() == "windows"
            && python_config.is_free_threaded())
    {
        println!("cargo:rustc-cfg=unicode_state");
    }
}

```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1135: CPython vs PyPy/GraalPy implementation module selection

**Classification:** non-direct context; project_source; `activation_configuration`.

**Purpose:** Select cpython implementation for non-PyPy/non-GraalPy targets.

**Migration effect:** Records actual activation guard; module selection itself accesses no Unicode layout.

**Fields / layout:** none. Types: .

**Source:** `ormsgpack-1.12.2/src/ffi/mod.rs:3–13`. SHA-256 `57bdfc6afadb038faf8af46a081d9374b5d14dbdd78f8e1d815364197bba017f`.

**Activation / context:** cfg_attr selects cpython/mod.rs, which exports the reviewed unicode functions; PyPy/GraalPy select base/mod.rs.

Lines 3–13 (immutable GitHub mapping unavailable in saved verification evidence)

```
mod critical_section;
#[cfg_attr(any(PyPy, GraalPy), path = "base/mod.rs")]
#[cfg_attr(not(any(PyPy, GraalPy)), path = "cpython/mod.rs")]
mod impl_;
mod int;
mod unicode;

pub use critical_section::*;
pub use impl_::*;
pub use int::*;
pub use unicode::*;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.

## L1136: PyO3 ffi import and Unicode helper exports

**Classification:** non-direct context; project_source; `import_alias`.

**Purpose:** Import pyo3::ffi types and export local unicode functions.

**Migration effect:** External PyO3 provider defines the named structs; this frozen package does not bundle that provider definition. No local AsciiObject/UnicodeObject aliases are inferred.

**Fields / layout:** none. Types: .

**Source:** `ormsgpack-1.12.2/src/ffi/cpython/mod.rs:3–11`. SHA-256 `b59bba992da5b5f8341b018a49d87857c7fb8e54fe5319d28ae89e63fcf6cba2`.

**Activation / context:** unicode_state module additionally gated by retained build.rs configuration; exact provider version/layout not inferred from another distribution bundled PyO3 source.

Lines 3–11 (immutable GitHub mapping unavailable in saved verification evidence)

```
use pyo3::ffi::*;
use std::os::raw::c_int;

mod int;
mod unicode;
#[cfg(unicode_state)]
mod unicode_state;

pub use unicode::*;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz); archive SHA-256 `944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33`.
