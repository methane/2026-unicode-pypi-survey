# orjson 3.12.0

11 confirmed layout regions; 15 reviewed regions including non-direct context.

## L1082: pyunicode_ascii

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from Rust UTF8 by allocating PyUnicode_New then writing after the selected ASCII/Compact header.

**Migration effect:** Header.add(1) and assumed payload width must change with layout; iterator/writer or UTF8 constructor can replace the raw destination.

**Fields / layout:** header size, 1/2/4-byte inline payload, trailing NUL. Types: PyASCIIObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/pyunicode_new.rs:15–24`. SHA-256 `6b1d500623b157f8b98767ebe5e64e8fd3b956346c2f442c6a1a400bcee7d7a0`.

**Activation / context:** Four width-specific helpers comprise one output-construction implementation; outputs were deliberately excluded from the earlier input-read survey.

Lines 15–24 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/pyunicode_new.rs#L15-L24))

```
pub(crate) fn pyunicode_ascii(buf: *const u8, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(usize_to_isize(num_chars), 127);
        let data_ptr = ptr.cast::<PyASCIIObject>().add(1).cast::<u8>();
        core::ptr::copy_nonoverlapping(buf, data_ptr, num_chars);
        core::ptr::write(data_ptr.add(num_chars), 0);
        validate_str!(ptr);
        ptr.cast::<PyObject>()
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1083: pyunicode_onebyte

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from Rust UTF8 by allocating PyUnicode_New then writing after the selected ASCII/Compact header.

**Migration effect:** Header.add(1) and assumed payload width must change with layout; iterator/writer or UTF8 constructor can replace the raw destination.

**Fields / layout:** header size, 1/2/4-byte inline payload, trailing NUL. Types: PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/pyunicode_new.rs:28–40`. SHA-256 `6b1d500623b157f8b98767ebe5e64e8fd3b956346c2f442c6a1a400bcee7d7a0`.

**Activation / context:** Four width-specific helpers comprise one output-construction implementation; outputs were deliberately excluded from the earlier input-read survey.

Lines 28–40 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/pyunicode_new.rs#L28-L40))

```
pub(crate) fn pyunicode_onebyte(buf: &str, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(usize_to_isize(num_chars), 255);
        let mut data_ptr = ptr.cast::<PyCompactUnicodeObject>().add(1).cast::<u8>();
        for each in buf.chars().fuse() {
            core::ptr::write(data_ptr, each as u8);
            data_ptr = data_ptr.add(1);
        }
        core::ptr::write(data_ptr, 0);
        validate_str!(ptr);
        ptr.cast::<PyObject>()
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1084: pyunicode_twobyte

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from Rust UTF8 by allocating PyUnicode_New then writing after the selected ASCII/Compact header.

**Migration effect:** Header.add(1) and assumed payload width must change with layout; iterator/writer or UTF8 constructor can replace the raw destination.

**Fields / layout:** header size, 1/2/4-byte inline payload, trailing NUL. Types: PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/pyunicode_new.rs:43–55`. SHA-256 `6b1d500623b157f8b98767ebe5e64e8fd3b956346c2f442c6a1a400bcee7d7a0`.

**Activation / context:** Four width-specific helpers comprise one output-construction implementation; outputs were deliberately excluded from the earlier input-read survey.

Lines 43–55 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/pyunicode_new.rs#L43-L55))

```
pub(crate) fn pyunicode_twobyte(buf: &str, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(usize_to_isize(num_chars), 65535);
        let mut data_ptr = ptr.cast::<PyCompactUnicodeObject>().add(1).cast::<u16>();
        for each in buf.chars().fuse() {
            core::ptr::write(data_ptr, each as u16);
            data_ptr = data_ptr.add(1);
        }
        core::ptr::write(data_ptr, 0);
        validate_str!(ptr);
        ptr.cast::<PyObject>()
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1085: pyunicode_fourbyte

**Classification:** direct layout dependency; project_source; `output_payload_header_arithmetic`.

**Purpose:** Create Unicode outputs from Rust UTF8 by allocating PyUnicode_New then writing after the selected ASCII/Compact header.

**Migration effect:** Header.add(1) and assumed payload width must change with layout; iterator/writer or UTF8 constructor can replace the raw destination.

**Fields / layout:** header size, 1/2/4-byte inline payload, trailing NUL. Types: PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/pyunicode_new.rs:58–70`. SHA-256 `6b1d500623b157f8b98767ebe5e64e8fd3b956346c2f442c6a1a400bcee7d7a0`.

**Activation / context:** Four width-specific helpers comprise one output-construction implementation; outputs were deliberately excluded from the earlier input-read survey.

Lines 58–70 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/pyunicode_new.rs#L58-L70))

```
pub(crate) fn pyunicode_fourbyte(buf: &str, num_chars: usize) -> *mut PyObject {
    unsafe {
        let ptr = PyUnicode_New(usize_to_isize(num_chars), 1114111);
        let mut data_ptr = ptr.cast::<PyCompactUnicodeObject>().add(1).cast::<u32>();
        for each in buf.chars().fuse() {
            core::ptr::write(data_ptr, each as u32);
            data_ptr = data_ptr.add(1);
        }
        core::ptr::write(data_ptr, 0);
        validate_str!(ptr);
        ptr.cast::<PyObject>()
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1086: PyStrRef::set_hash [inline_str]

**Classification:** direct layout dependency; project_source; `hash_state_metadata_read_write`.

**Purpose:** Hash the native Unicode byte representation then write cached .hash. Non-inline variant still writes .hash directly after using DATA/KIND API.

**Migration effect:** Hash field offset and Unicode hash byte semantics are independent migration obligations; changing cached representation requires equivalent hash semantics or public hash access.

**Fields / layout:** state, kind bitmask, compact/ascii bitmask, length, hash, header add(1). Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/object.rs:170–188`. SHA-256 `4ceba4b9f57151e7148638b8488041a57df42183d1acda3e5b4ad62c916261f1`.

**Activation / context:** inline_str feature gates manual bitmask/data-address branch; both feature variants write .hash. STATE_KIND_SHIFT varies with Py_3_14 and Py_GIL_DISABLED.

Lines 170–187 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L170-L187))

```
    fn set_hash(&mut self) {
        unsafe {
            let ptr = self.as_ptr().cast::<PyASCIIObject>();
            let data_ptr: *mut core::ffi::c_void =
                if (*ptr).state & STATE_COMPACT_ASCII == STATE_COMPACT_ASCII {
                    ptr.add(1).cast::<core::ffi::c_void>()
                } else {
                    ptr.cast::<PyCompactUnicodeObject>()
                        .add(1)
                        .cast::<core::ffi::c_void>()
                };
            #[allow(clippy::cast_possible_wrap)]
            let num_bytes =
                (*ptr).length * (((*ptr).state & STATE_KIND_MASK) >> STATE_KIND_SHIFT) as isize;
            let hash = Py_HashBuffer(data_ptr, num_bytes);
            (*ptr).hash = hash;
            debug_assert!((*ptr).hash != -1);
        }
```

Excerpt shortened; the complete reviewed range 170–188 is in `data/cases.json`.

Closing lines 188–188 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L188-L188))

```
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1087: PyStrRef::set_hash [not inline_str]

**Classification:** direct layout dependency; project_source; `hash_state_metadata_read_write`.

**Purpose:** Hash the native Unicode byte representation then write cached .hash. Non-inline variant still writes .hash directly after using DATA/KIND API.

**Migration effect:** Hash field offset and Unicode hash byte semantics are independent migration obligations; changing cached representation requires equivalent hash semantics or public hash access.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/object.rs:191–200`. SHA-256 `4ceba4b9f57151e7148638b8488041a57df42183d1acda3e5b4ad62c916261f1`.

**Activation / context:** not inline_str feature variant: payload through DATA/KIND APIs, cached hash write still direct.

Lines 191–200 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L191-L200))

```
    fn set_hash(&mut self) {
        unsafe {
            let data_ptr = PyUnicode_DATA(self.as_ptr());
            #[allow(clippy::cast_possible_wrap)]
            let num_bytes = PyUnicode_KIND(self.as_ptr()) as isize * Py_SIZE(self.as_ptr());
            let hash = Py_HashBuffer(data_ptr, num_bytes);
            (*self.as_ptr().cast::<PyASCIIObject>()).hash = hash;
            debug_assert!(self.hash() != -1);
        }
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1088: PyStrRef::as_str

**Classification:** direct layout dependency; project_source; `state_utf8_cache_read`.

**Purpose:** Fast Rust str view of compact ASCII inline payload or cached UTF8; fallback calls FFI conversion.

**Migration effect:** A UTF8-native representation is favorable, but direct state offsets, header size, and cache-field interpretation still must be rewritten.

**Fields / layout:** state, length, utf8, utf8_length, ASCII header add(1). Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/object.rs:203–229`. SHA-256 `4ceba4b9f57151e7148638b8488041a57df42183d1acda3e5b4ad62c916261f1`.

**Activation / context:** Only inline_str variant directly reads layout; non-inline as_str delegates to FFI. Returned Rust lifetime annotation is static, not proof that storage is immortal.

Lines 203–220 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L203-L220))

```
    #[cfg(feature = "inline_str")]
    pub fn as_str(&self) -> Option<&'static str> {
        unsafe {
            let op = self.as_ptr();
            if (*op.cast::<PyASCIIObject>()).state & STATE_COMPACT_ASCII == STATE_COMPACT_ASCII {
                let ptr = op.cast::<PyASCIIObject>().add(1).cast::<u8>();
                let len = crate::util::isize_to_usize((*op.cast::<PyASCIIObject>()).length);
                Some(str_from_slice!(ptr, len))
            } else if (*op.cast::<PyASCIIObject>()).state & STATE_COMPACT_ASCII == 0 {
                cold_path!();
                to_str_via_ffi(op)
            } else if (*op.cast::<PyCompactUnicodeObject>()).utf8_length != 0 {
                let ptr = ((*op.cast::<PyCompactUnicodeObject>()).utf8).cast::<u8>();
                let len =
                    crate::util::isize_to_usize((*op.cast::<PyCompactUnicodeObject>()).utf8_length);
                Some(str_from_slice!(ptr, len))
            } else {
                to_str_via_ffi(op)
```

Excerpt shortened; the complete reviewed range 203–229 is in `data/cases.json`.

Closing lines 224–229 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L224-L229))

```

    #[inline(always)]
    #[cfg(not(feature = "inline_str"))]
    pub fn as_str(&self) -> Option<&'static str> {
        to_str_via_ffi(self.as_ptr())
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1089: PyUnstable_Unicode_GET_CACHED_HASH local compatibility variants

**Classification:** direct layout dependency; project_source; `hash_metadata_read`.

**Purpose:** Read cached Unicode hash in GIL and free-threaded variants.

**Migration effect:** Local helper name resembles an API but its saved implementation directly dereferences .hash; change helper if field moves.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `orjson-3.12.0/src/ffi/compat.rs:238–264`. SHA-256 `0648a81ffde55fb9993f51ab7c23a1b1e4ba7bb1103f857e595a3d53f6e10ace`.

**Activation / context:** Both cfg variants are package-local implementation; free-threaded branch constructs AtomicIsize from the directly read hash and then loads it. This record describes source, not concurrency correctness.

Lines 238–255 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/compat.rs#L238-L255))

```
#[cfg(not(Py_GIL_DISABLED))]
#[inline(always)]
#[allow(non_snake_case)]
pub(crate) unsafe fn PyUnstable_Unicode_GET_CACHED_HASH(
    op: *mut pyo3_ffi::PyObject,
) -> pyo3_ffi::Py_hash_t {
    unsafe {
        let hash = (*op.cast::<pyo3_ffi::PyASCIIObject>()).hash;
        debug_assert!(hash != -1);
        hash
    }
}

#[cfg(Py_GIL_DISABLED)]
#[inline(always)]
#[allow(non_snake_case)]
pub(crate) unsafe fn PyUnstable_Unicode_GET_CACHED_HASH(
    op: *mut pyo3_ffi::PyObject,
```

Excerpt shortened; the complete reviewed range 238–264 is in `data/cases.json`.

Closing lines 259–264 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/compat.rs#L259-L264))

```
            core::sync::atomic::AtomicIsize::new((*op.cast::<pyo3_ffi::PyASCIIObject>()).hash)
                .load(core::sync::atomic::Ordering::Relaxed);
        debug_assert!(hash != -1);
        hash
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1090: pydict_contains pre-3.13 CPython macro variants

**Classification:** direct layout dependency; project_source; `hash_metadata_read`.

**Purpose:** Pass cached string hash to _PyDict_Contains_KnownHash.

**Migration effect:** Needs cached-hash API or updated field offset; not FSR payload indexing.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `orjson-3.12.0/src/util.rs:47–73`. SHA-256 `c0fedd865ea42798dbd360321e2460e64b3ac2308d9c22d3abd0779553217ac4`.

**Activation / context:** CPython Py_3_12&&!Py_3_13 and older CPython branches; Py_3_13 variant at40-45 uses API without this direct hash cast.

Lines 47–64 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/util.rs#L47-L64))

```
#[cfg(all(CPython, Py_3_12, not(Py_3_13)))]
macro_rules! pydict_contains {
    ($obj1:expr, $obj2:expr) => {
        unsafe {
            debug_assert!((*$obj2.cast::<crate::ffi::PyASCIIObject>()).hash != -1);
            crate::ffi::_PyDict_Contains_KnownHash(
                crate::ffi::PyType_GetDict($obj1),
                $obj2,
                (*$obj2.cast::<crate::ffi::PyASCIIObject>()).hash,
            ) == 1
        }
    };
}

#[cfg(all(CPython, not(Py_3_12)))]
macro_rules! pydict_contains {
    ($obj1:expr, $obj2:expr) => {
        unsafe {
```

Excerpt shortened; the complete reviewed range 47–73 is in `data/cases.json`.

Closing lines 68–73 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/util.rs#L68-L73))

```
                $obj2,
                (*$obj2.cast::<crate::ffi::PyASCIIObject>()).hash,
            ) == 1
        }
    };
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1091: pyo3_ffi type re-exports

**Classification:** non-direct context; project_source; `import_alias`.

**Purpose:** Re-export the named Unicode types from PyO3 ffi.

**Migration effect:** Imports are not runtime layout access.

**Fields / layout:** none. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/mod.rs:68–88`. SHA-256 `c4817d7cc1ea5ed9bd1b362d144005c730cd137bfd44b837981367922b6e3dfa`.

**Activation / context:** Provider source is bundled include/cargo/pyo3-ffi-0.28.3/src/cpython/unicodeobject.rs.

Lines 68–85 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/mod.rs#L68-L85))

```
};

#[allow(unused_imports)]
pub(crate) use pyo3_ffi::{
    METH_FASTCALL, METH_KEYWORDS, METH_O, Py_DECREF, Py_False, Py_INCREF, Py_None, Py_REFCNT,
    Py_TPFLAGS_DEFAULT, Py_TPFLAGS_DICT_SUBCLASS, Py_TPFLAGS_IMMUTABLETYPE,
    Py_TPFLAGS_LIST_SUBCLASS, Py_TPFLAGS_LONG_SUBCLASS, Py_TPFLAGS_TUPLE_SUBCLASS,
    Py_TPFLAGS_UNICODE_SUBCLASS, Py_TYPE, Py_True, Py_XDECREF, Py_buffer, Py_hash_t, Py_intptr_t,
    Py_mod_exec, Py_ssize_t, Py_tp_dealloc, Py_tp_new, PyASCIIObject, PyBool_Type,
    PyBuffer_IsContiguous, PyByteArray_AsString, PyByteArray_Size, PyByteArray_Type,
    PyBytes_FromStringAndSize, PyBytes_Type, PyCFunction_NewEx, PyCapsule_Import,
    PyCompactUnicodeObject, PyDateTime_CAPI, PyDateTime_DATE_GET_HOUR,
    PyDateTime_DATE_GET_MICROSECOND, PyDateTime_DATE_GET_MINUTE, PyDateTime_DATE_GET_SECOND,
    PyDateTime_DATE_GET_TZINFO, PyDateTime_DELTA_GET_DAYS, PyDateTime_DELTA_GET_SECONDS,
    PyDateTime_DateTime, PyDateTime_GET_DAY, PyDateTime_GET_MONTH, PyDateTime_GET_YEAR,
    PyDateTime_IMPORT, PyDateTime_TIME_GET_HOUR, PyDateTime_TIME_GET_MICROSECOND,
    PyDateTime_TIME_GET_MINUTE, PyDateTime_TIME_GET_SECOND, PyDateTime_Time, PyDict_Contains,
    PyDict_Next, PyDict_SetItem, PyDict_Type, PyDictObject, PyErr_Clear, PyErr_NewException,
```

Excerpt shortened; the complete reviewed range 68–88 is in `data/cases.json`.

Closing lines 86–88 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/mod.rs#L86-L88))

```
    PyErr_Occurred, PyErr_SetObject, PyExc_TypeError, PyException_SetCause, PyFloat_AS_DOUBLE,
    PyFloat_FromDouble, PyFloat_Type, PyImport_ImportModule, PyList_GET_ITEM, PyList_New,
    PyList_SET_ITEM, PyList_Type, PyListObject, PyLong_AsLongLong, PyLong_AsUnsignedLongLong,
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1092: type imports

**Classification:** non-direct context; project_source; `import_alias`.

**Purpose:** Import ffi types used in actual direct cases.

**Migration effect:** No direct access on import line.

**Fields / layout:** none. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/object.rs:3–12`. SHA-256 `4ceba4b9f57151e7148638b8488041a57df42183d1acda3e5b4ad62c916261f1`.

**Activation / context:** See actual cases later in this file.

Lines 3–12 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/object.rs#L3-L12))

```

#[allow(unused)]
use crate::ffi::{
    Py_HashBuffer, Py_SIZE, Py_ssize_t, PyASCIIObject, PyCompactUnicodeObject, PyObject,
    PyUnicode_AsUTF8AndSize,
};
#[cfg(all(CPython, not(feature = "inline_str")))]
use crate::ffi::{PyUnicode_DATA, PyUnicode_KIND};
use crate::typeref::{EMPTY_UNICODE, STR_TYPE};
use core::ptr::NonNull;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1093: type imports

**Classification:** non-direct context; project_source; `import_alias`.

**Purpose:** Import ffi header types.

**Migration effect:** No direct access on import line.

**Fields / layout:** none. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `orjson-3.12.0/src/ffi/pystrref/pyunicode_new.rs:4–5`. SHA-256 `6b1d500623b157f8b98767ebe5e64e8fd3b956346c2f442c6a1a400bcee7d7a0`.

**Activation / context:** Actual output helper cases above.

Lines 4–5 ([verified immutable source](https://github.com/ijl/orjson/blob/6737895a1a4e3e26df0569a40147893a786f9a58/src/ffi/pystrref/pyunicode_new.rs#L4-L5))

```
use crate::ffi::{PyASCIIObject, PyCompactUnicodeObject, PyObject, PyUnicode_New};
use crate::util::usize_to_isize;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1094: repr(C) Unicode header/state/data declarations

**Classification:** non-direct context; vendored_ffi_implementation; `definition_layout`.

**Purpose:** Declare CPython-compatible Rust mirror structs, state-bitfield backing storage and data union.

**Migration effect:** Definitions must track ABI/layout; declarations alone do not prove a package-owned read or write.

**Fields / layout:** ob_base, length, hash, state, wstr, _base, utf8_length, utf8, wstr_length, data.any/latin1/ucs2/ucs4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `orjson-3.12.0/include/cargo/pyo3-ffi-0.28.3/src/cpython/unicodeobject.rs:159–460`. SHA-256 `0affb26b65e7f9d594224f7b1b9a8db3c9ce164eacbd2b97966acf6e49a37aef`.

**Activation / context:** Vendored PyO3 provider; cfg controls older wstr fields and state accessor availability. Provider note says PyO3 does not access internal state on3.14+.

Lines 159–174 (immutable GitHub mapping unavailable in saved verification evidence)

```
/// Wrapper around the `PyASCIIObject.state` bitfield with getters and setters that work
/// on most little- and big-endian architectures.
///
/// Memory layout of C bitfields is implementation defined, so these functions are still
/// unsafe. Users must verify that they work as expected on the architectures they target.
#[cfg(not(Py_3_14))]
#[repr(C)]
struct PyASCIIObjectState {
    bitfield_align: [u8; 0],
    bitfield: BitfieldUnit<[u8; 4usize]>,
}

// c_uint and u32 are not necessarily the same type on all targets / architectures
#[cfg(not(any(GraalPy, Py_3_14)))]
#[allow(clippy::useless_transmute)]
impl PyASCIIObjectState {
```

Lines 281–298 (immutable GitHub mapping unavailable in saved verification evidence)

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    #[cfg(any(Py_3_11, not(PyPy)))]
    pub hash: Py_hash_t,
    /// A bit field with various properties.
    ///
    /// Rust doesn't expose bitfields. So we have accessor functions for
    /// retrieving values.
    ///
    /// Before 3.12:
    /// unsigned int interned:2; // SSTATE_* constants.
    /// unsigned int kind:3;     // PyUnicode_*_KIND constants.
    /// unsigned int compact:1;
    /// unsigned int ascii:1;
    /// unsigned int ready:1;
    /// unsigned int :24;
    ///
```

Excerpt shortened; the complete reviewed range 281–314 is in `data/cases.json`.

Closing lines 309–314 (immutable GitHub mapping unavailable in saved verification evidence)

```
    pub wstr: *mut wchar_t,
}

/// Interacting with the bitfield is not actually well-defined, so we mark these APIs unsafe.
#[cfg(not(any(GraalPy, Py_3_14)))]
impl PyASCIIObject {
```

Lines 439–456 (immutable GitHub mapping unavailable in saved verification evidence)

```
pub struct PyCompactUnicodeObject {
    pub _base: PyASCIIObject,
    pub utf8_length: Py_ssize_t,
    pub utf8: *mut c_char,
    #[cfg(not(Py_3_12))]
    pub wstr_length: Py_ssize_t,
}

#[repr(C)]
pub union PyUnicodeObjectData {
    pub any: *mut c_void,
    pub latin1: *mut Py_UCS1,
    pub ucs2: *mut Py_UCS2,
    pub ucs4: *mut Py_UCS4,
}

#[repr(C)]
pub struct PyUnicodeObject {
```

Excerpt shortened; the complete reviewed range 439–459 is in `data/cases.json`.

Closing lines 457–459 (immutable GitHub mapping unavailable in saved verification evidence)

```
    pub _base: PyCompactUnicodeObject,
    pub data: PyUnicodeObjectData,
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1095: PyASCIIObject state methods and helper-state accessors

**Classification:** direct layout dependency; vendored_ffi_implementation; `compatibility_implementation`.

**Purpose:** Implement unsafe getter/setter bitfield access to live Unicode header state.

**Migration effect:** Both bitfield representation and field offset require provider update if ABI changes.

**Fields / layout:** state, interned, kind, compact, ascii, ready, statically_allocated. Types: PyASCIIObject.

**Source:** `orjson-3.12.0/include/cargo/pyo3-ffi-0.28.3/src/cpython/unicodeobject.rs:174–435`. SHA-256 `0affb26b65e7f9d594224f7b1b9a8db3c9ce164eacbd2b97966acf6e49a37aef`.

**Activation / context:** Vendored implementation, not an independent handwritten orjson algorithm; cfg excludes GraalPy/Py_3_14 state access. Definitions overlap range but named declaration tokens are separately audited.

Lines 174–191 (immutable GitHub mapping unavailable in saved verification evidence)

```
impl PyASCIIObjectState {
    #[inline]
    unsafe fn interned(&self) -> c_uint {
        std::mem::transmute(
            self.bitfield
                .get(STATE_INTERNED_INDEX, STATE_INTERNED_WIDTH) as u32,
        )
    }

    #[inline]
    unsafe fn set_interned(&mut self, val: c_uint) {
        let val: u32 = std::mem::transmute(val);
        self.bitfield
            .set(STATE_INTERNED_INDEX, STATE_INTERNED_WIDTH, val as u64)
    }

    #[inline]
    unsafe fn kind(&self) -> c_uint {
```

Excerpt shortened; the complete reviewed range 174–280 is in `data/cases.json`.

Closing lines 275–280 (immutable GitHub mapping unavailable in saved verification evidence)

```
    fn from(value: PyASCIIObjectState) -> Self {
        u32::from_ne_bytes(value.bitfield.storage)
    }
}

#[repr(C)]
```

Lines 314–331 (immutable GitHub mapping unavailable in saved verification evidence)

```
impl PyASCIIObject {
    #[cfg_attr(not(Py_3_12), allow(rustdoc::broken_intra_doc_links))] // SSTATE_INTERNED_IMMORTAL_STATIC requires 3.12
    /// Get the `interned` field of the [`PyASCIIObject`] state bitfield.
    ///
    /// Returns one of: [`SSTATE_NOT_INTERNED`], [`SSTATE_INTERNED_MORTAL`],
    /// [`SSTATE_INTERNED_IMMORTAL`], or [`SSTATE_INTERNED_IMMORTAL_STATIC`].
    #[inline]
    pub unsafe fn interned(&self) -> c_uint {
        PyASCIIObjectState::from(self.state).interned()
    }

    #[cfg_attr(not(Py_3_12), allow(rustdoc::broken_intra_doc_links))] // SSTATE_INTERNED_IMMORTAL_STATIC requires 3.12
    /// Set the `interned` field of the [`PyASCIIObject`] state bitfield.
    ///
    /// Calling this function with an argument that is not [`SSTATE_NOT_INTERNED`],
    /// [`SSTATE_INTERNED_MORTAL`], [`SSTATE_INTERNED_IMMORTAL`], or
    /// [`SSTATE_INTERNED_IMMORTAL_STATIC`] is invalid.
    #[inline]
```

Excerpt shortened; the complete reviewed range 314–435 is in `data/cases.json`.

Closing lines 430–435 (immutable GitHub mapping unavailable in saved verification evidence)

```
    #[cfg(Py_3_12)]
    pub unsafe fn set_statically_allocated(&mut self, val: c_uint) {
        let mut state = PyASCIIObjectState::from(self.state);
        state.set_statically_allocated(val);
        self.state = u32::from(state);
    }
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.

## L1096: PyUnicode_IS_* / KIND / COMPACT_DATA / NONCOMPACT_DATA / GET_LENGTH / IS_READY API implementations

**Classification:** direct layout dependency; vendored_ffi_implementation; `compatibility_implementation`.

**Purpose:** Implement public/macro-like APIs by direct Rust layout dereference. NONCOMPACT_DATA explicitly reads full PyUnicodeObject.data.any.

**Migration effect:** These are real direct accesses in a compatibility provider, distinct from application code calling those APIs. Must update provider layouts and version cfg.

**Fields / layout:** state via methods, length, data.any, ASCII/Compact header offset(1). Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `orjson-3.12.0/include/cargo/pyo3-ffi-0.28.3/src/cpython/unicodeobject.rs:477–603`. SHA-256 `0affb26b65e7f9d594224f7b1b9a8db3c9ce164eacbd2b97966acf6e49a37aef`.

**Activation / context:** DATA switches compact vs noncompact; pre3.14 inline implementation,3.14 DATA external declaration. NONCOMPACT_DATA helper cfg excludes GraalPy/PyPy but does not by itself imply application activation.

Lines 477–494 (immutable GitHub mapping unavailable in saved verification evidence)

```
#[cfg(not(any(GraalPy, Py_3_14)))]
#[inline]
pub unsafe fn PyUnicode_IS_ASCII(op: *mut PyObject) -> c_uint {
    debug_assert!(crate::PyUnicode_Check(op) != 0);
    #[cfg(not(Py_3_12))]
    debug_assert!(PyUnicode_IS_READY(op) != 0);

    (*(op as *mut PyASCIIObject)).ascii()
}

#[cfg(not(any(GraalPy, Py_3_14)))]
#[inline]
pub unsafe fn PyUnicode_IS_COMPACT(op: *mut PyObject) -> c_uint {
    (*(op as *mut PyASCIIObject)).compact()
}

#[cfg(not(any(GraalPy, Py_3_14)))]
#[inline]
```

Excerpt shortened; the complete reviewed range 477–497 is in `data/cases.json`.

Closing lines 495–497 (immutable GitHub mapping unavailable in saved verification evidence)

```
pub unsafe fn PyUnicode_IS_COMPACT_ASCII(op: *mut PyObject) -> c_uint {
    ((*(op as *mut PyASCIIObject)).ascii() != 0 && PyUnicode_IS_COMPACT(op) != 0).into()
}
```

Lines 531–548 (immutable GitHub mapping unavailable in saved verification evidence)

```
#[cfg(all(not(GraalPy), not(Py_3_14)))]
#[inline]
pub unsafe fn PyUnicode_KIND(op: *mut PyObject) -> c_uint {
    debug_assert!(crate::PyUnicode_Check(op) != 0);
    #[cfg(not(Py_3_12))]
    debug_assert!(PyUnicode_IS_READY(op) != 0);

    (*(op as *mut PyASCIIObject)).kind()
}

#[cfg(not(any(GraalPy, Py_3_14)))]
#[inline]
pub unsafe fn _PyUnicode_COMPACT_DATA(op: *mut PyObject) -> *mut c_void {
    if PyUnicode_IS_ASCII(op) != 0 {
        (op as *mut PyASCIIObject).offset(1) as *mut c_void
    } else {
        (op as *mut PyCompactUnicodeObject).offset(1) as *mut c_void
    }
```

Excerpt shortened; the complete reviewed range 531–589 is in `data/cases.json`.

Closing lines 584–589 (immutable GitHub mapping unavailable in saved verification evidence)

```
pub unsafe fn PyUnicode_GET_LENGTH(op: *mut PyObject) -> Py_ssize_t {
    debug_assert!(crate::PyUnicode_Check(op) != 0);
    #[cfg(not(Py_3_12))]
    debug_assert!(PyUnicode_IS_READY(op) != 0);

    (*(op as *mut PyASCIIObject)).length
```

Lines 599–603 (immutable GitHub mapping unavailable in saved verification evidence)

```
#[cfg(not(any(GraalPy, Py_3_12)))]
#[inline]
pub unsafe fn PyUnicode_IS_READY(op: *mut PyObject) -> c_uint {
    (*(op as *mut PyASCIIObject)).ready()
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/0f/f3/742fb1f62b825f2c010697eaf4e828004bc2a81e7e806666989c132c7c42/orjson-3.12.0.tar.gz); archive SHA-256 `d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5`.
