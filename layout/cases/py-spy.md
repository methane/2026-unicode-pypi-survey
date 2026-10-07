# py-spy 0.4.2

4 confirmed layout regions; 22 reviewed regions including non-direct context.

## L0001: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_10_0.rs:612–756`. SHA-256 `88c679479ffb335ecfb3b4c36996f4f656855c1f01235412cbb497d7f3cf90ea`.

**Activation / context:** Selected by target Python version module v3_10_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 612–629 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_10_0.rs#L612-L629))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 612–756 is in `data/cases.json`.

Closing lines 751–756 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_10_0.rs#L751-L756))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0002: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_11_0.rs:609–878`. SHA-256 `e40f44c84b92e58c56d5d1a3b399764a62584a4e24bce4c7b533ee7793978457`.

**Activation / context:** Selected by target Python version module v3_11_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 609–626 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_11_0.rs#L609-L626))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_align_1: [u8; 0],
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize]>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
```

Excerpt shortened; the complete reviewed range 609–878 is in `data/cases.json`.

Closing lines 873–878 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_11_0.rs#L873-L878))

```
        unsafe {
            ::std::ptr::write_bytes(s.as_mut_ptr(), 0, 1);
            s.assume_init()
        }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0003: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_12_0.rs:833–1062`. SHA-256 `d5db2ebd5e08caa1ccba12c0e873f20a5c72ae823328d7b3a31211bbc25e12a7`.

**Activation / context:** Selected by target Python version module v3_12_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 833–850 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_12_0.rs#L833-L850))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_align_1: [u8; 0],
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize]>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 833–1062 is in `data/cases.json`.

Closing lines 1057–1062 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_12_0.rs#L1057-L1062))

```
        unsafe {
            ::std::ptr::write_bytes(s.as_mut_ptr(), 0, 1);
            s.assume_init()
        }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0004: Generated global-string objects embedding Unicode headers

**Classification:** non-direct context; project_source; `embedded_replica_declarations`.

**Purpose:** Bindgen describes CPython static/interned Unicode global objects. These are nested ABI declarations, not separate executed Unicode readers.

**Migration effect:** Changed Unicode header sizes/representation can alter these replica/global ABI declarations; update bindings. No actual _global_strings Unicode field consumer was found outside generated bindings.

**Fields / layout:** _ascii, _latin1, inline _data arrays. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_12_0.rs:2800–14286`. SHA-256 `d5db2ebd5e08caa1ccba12c0e873f20a5c72ae823328d7b3a31211bbc25e12a7`.

**Activation / context:** Target version v3_12_0; embedded declaration count 719.

Lines 2800–2803 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_12_0.rs#L2800-L2803))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_1 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 11usize],
}
```

Lines 2815–2818 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_12_0.rs#L2815-L2818))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_2 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 10usize],
}
```

Lines 2830–2833 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_12_0.rs#L2830-L2833))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_3 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 9usize],
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0005: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_13_0.rs:752–894`. SHA-256 `b1f053099accdd3d95c985cba7c4ac36bb863cb3c529c33a4d31569688f701a0`.

**Activation / context:** Selected by target Python version module v3_13_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 752–769 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_13_0.rs#L752-L769))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
    #[inline]
```

Excerpt shortened; the complete reviewed range 752–894 is in `data/cases.json`.

Closing lines 889–894 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_13_0.rs#L889-L894))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0006: Generated global-string objects embedding Unicode headers

**Classification:** non-direct context; project_source; `embedded_replica_declarations`.

**Purpose:** Bindgen describes CPython static/interned Unicode global objects. These are nested ABI declarations, not separate executed Unicode readers.

**Migration effect:** Changed Unicode header sizes/representation can alter these replica/global ABI declarations; update bindings. No actual _global_strings Unicode field consumer was found outside generated bindings.

**Fields / layout:** _ascii, _latin1, inline _data arrays. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_13_0.rs:2631–11506`. SHA-256 `b1f053099accdd3d95c985cba7c4ac36bb863cb3c529c33a4d31569688f701a0`.

**Activation / context:** Target version v3_13_0; embedded declaration count 741.

Lines 2631–2634 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_13_0.rs#L2631-L2634))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_1 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 11usize],
}
```

Lines 2642–2645 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_13_0.rs#L2642-L2645))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_2 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 10usize],
}
```

Lines 2653–2656 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_13_0.rs#L2653-L2656))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_3 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 9usize],
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0007: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_14_0.rs:939–1206`. SHA-256 `b7de3373ce1cc922cdf7449fa26af574a55b5f0bc6e5a6f0f5cf0a19b49b0230`.

**Activation / context:** Selected by target Python version module v3_14_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 939–956 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_14_0.rs#L939-L956))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_align_1: [u8; 0],
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize]>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 939–1206 is in `data/cases.json`.

Closing lines 1201–1206 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_14_0.rs#L1201-L1206))

```
        unsafe {
            ::std::ptr::write_bytes(s.as_mut_ptr(), 0, 1);
            s.assume_init()
        }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0008: Generated global-string objects embedding Unicode headers

**Classification:** non-direct context; project_source; `embedded_replica_declarations`.

**Purpose:** Bindgen describes CPython static/interned Unicode global objects. These are nested ABI declarations, not separate executed Unicode readers.

**Migration effect:** Changed Unicode header sizes/representation can alter these replica/global ABI declarations; update bindings. No actual _global_strings Unicode field consumer was found outside generated bindings.

**Fields / layout:** _ascii, _latin1, inline _data arrays. Types: PyASCIIObject, PyCompactUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_14_0.rs:5674–18139`. SHA-256 `b7de3373ce1cc922cdf7449fa26af574a55b5f0bc6e5a6f0f5cf0a19b49b0230`.

**Activation / context:** Target version v3_14_0; embedded declaration count 780.

Lines 5674–5677 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_14_0.rs#L5674-L5677))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_1 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 11usize],
}
```

Lines 5689–5692 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_14_0.rs#L5689-L5692))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_2 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 10usize],
}
```

Lines 5704–5707 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_14_0.rs#L5704-L5707))

```
pub struct _Py_global_strings__bindgen_ty_1__bindgen_ty_3 {
    pub _ascii: PyASCIIObject,
    pub _data: [u8; 9usize],
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0009: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_3_7.rs:501–646`. SHA-256 `f4d3bd5669f2f9dce9b6dedebcc782fda068769196c4607fa1a561594e6db40d`.

**Activation / context:** Selected by target Python version module v3_3_7; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 501–518 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_3_7.rs#L501-L518))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 1usize], u8>,
    pub __bindgen_padding_0: [u8; 3usize],
    pub __bindgen_align: [u32; 0usize],
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
```

Excerpt shortened; the complete reviewed range 501–646 is in `data/cases.json`.

Closing lines 641–646 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_3_7.rs#L641-L646))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0010: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_4_8.rs:502–646`. SHA-256 `98bcd6d8ad6972cb27d92016fc698b1cfd4553e9479e04bbd9717d12e5843593`.

**Activation / context:** Selected by target Python version module v3_4_8; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 502–519 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_4_8.rs#L502-L519))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
    pub __bindgen_align: [u32; 0usize],
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 502–646 is in `data/cases.json`.

Closing lines 641–646 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_4_8.rs#L641-L646))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0011: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_5_5.rs:516–660`. SHA-256 `034b9751f4123808d262492dbbd5a3d0426202b2bbfcc658a4dc6169bd48af01`.

**Activation / context:** Selected by target Python version module v3_5_5; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 516–533 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_5_5.rs#L516-L533))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
    pub __bindgen_align: [u32; 0usize],
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 516–660 is in `data/cases.json`.

Closing lines 655–660 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_5_5.rs#L655-L660))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0012: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_6_6.rs:516–660`. SHA-256 `aff39a5add45af124e218c8d1be85b3aed3ea8f692494a034c07466176da6e14`.

**Activation / context:** Selected by target Python version module v3_6_6; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 516–533 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_6_6.rs#L516-L533))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
    pub __bindgen_align: [u32; 0usize],
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 516–660 is in `data/cases.json`.

Closing lines 655–660 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_6_6.rs#L655-L660))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0013: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_7_0.rs:554–698`. SHA-256 `adb81601c3a2989ecea913223f425d93958d3ee24878ed48de8c6990dfcf0585`.

**Activation / context:** Selected by target Python version module v3_7_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 554–571 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_7_0.rs#L554-L571))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
    pub __bindgen_align: [u32; 0usize],
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 554–698 is in `data/cases.json`.

Closing lines 693–698 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_7_0.rs#L693-L698))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0014: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_8_0.rs:614–883`. SHA-256 `40b495cc2c226f20f798a1c1baca1301cd8962fa4ddab03cb34fae2c00ebf1dc`.

**Activation / context:** Selected by target Python version module v3_8_0; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 614–631 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_8_0.rs#L614-L631))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_align_1: [u8; 0],
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize]>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
```

Excerpt shortened; the complete reviewed range 614–883 is in `data/cases.json`.

Closing lines 878–883 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_8_0.rs#L878-L883))

```
        unsafe {
            ::std::ptr::write_bytes(s.as_mut_ptr(), 0, 1);
            s.assume_init()
        }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0015: Versioned bindgen Unicode structs, bitfield accessors and Default implementations

**Classification:** non-direct context; project_source; `local_replica_definition_and_accessors`.

**Purpose:** Defines target-CPython ABI headers/unions and state bit positions; supplies types to Python3Impl StringObject. Generated defaults/setters are support definitions, not independent target-Unicode reads.

**Migration effect:** Regenerate/update versioned remote layout when target structs/bitfields change; definitions alone are not an actual consumer count.

**Fields / layout:** ob_base: PyObject, length: Py_ssize_t, hash: Py_hash_t, state: PyASCIIObject__bindgen_ty_1, wstr: *mut wchar_t, _base: PyASCIIObject, utf8: *mut ::std::os::raw::c_char, wstr_length: Py_ssize_t, _base: PyCompactUnicodeObject, data: PyUnicodeObject__bindgen_ty_1, any: *mut ::std::os::raw::c_void, latin1: *mut Py_UCS1, ucs2: *mut Py_UCS2, ucs4: *mut Py_UCS4. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_bindings/v3_9_5.rs:600–744`. SHA-256 `aa70bde292f58d34337334ba963966432edc36b1843b71715889fad974575ac2`.

**Activation / context:** Selected by target Python version module v3_9_5; 3.12+ snapshots omit old wstr/wstr_length/ready. Other fields such as utf8/hash are declared but not all used by StringObject.

Lines 600–617 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_9_5.rs#L600-L617))

```
pub struct PyASCIIObject {
    pub ob_base: PyObject,
    pub length: Py_ssize_t,
    pub hash: Py_hash_t,
    pub state: PyASCIIObject__bindgen_ty_1,
    pub wstr: *mut wchar_t,
}
#[repr(C)]
#[repr(align(4))]
#[derive(Debug, Default, Copy, Clone)]
pub struct PyASCIIObject__bindgen_ty_1 {
    pub _bitfield_1: __BindgenBitfieldUnit<[u8; 4usize], u8>,
}
impl PyASCIIObject__bindgen_ty_1 {
    #[inline]
    pub fn interned(&self) -> ::std::os::raw::c_uint {
        unsafe { ::std::mem::transmute(self._bitfield_1.get(0usize, 2u8) as u32) }
    }
```

Excerpt shortened; the complete reviewed range 600–744 is in `data/cases.json`.

Closing lines 739–744 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_bindings/v3_9_5.rs#L739-L744))

```
}
impl Default for PyUnicodeObject {
    fn default() -> Self {
        unsafe { ::std::mem::zeroed() }
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0016: Python3Impl StringObject::{ascii,size,kind,address}

**Classification:** direct layout dependency; project_source; `remote_header_fields_and_payload_offset`.

**Purpose:** Reads copied target header fields, chooses noncompact data.any or remote base+compact-header-size payload address.

**Migration effect:** Target UTF8-only representation requires changing remote offset/state interpretation and decoder; stable C API wrappers cannot help this out-of-process reader. Header+payload size contracts directly matter.

**Fields / layout:** _base._base.state.ascii, _base._base.state.compact, _base._base.state.kind, _base._base.length, data.any, sizeof(PyASCIIObject), sizeof(PyCompactUnicodeObject). Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_interpreters.rs:373–399`. SHA-256 `12477dae28fbebaffcc29e99f05447184a5b39b6497777c2c4f7f8af0c31fcac`.

**Activation / context:** Python3Impl instantiated for versioned target modules3.3 through3.14; fields belong to locally copied replicas, but values describe live target objects.

Lines 373–390 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_interpreters.rs#L373-L390))

```
        impl StringObject for $py::PyUnicodeObject {
            fn ascii(&self) -> bool {
                self._base._base.state.ascii() != 0
            }
            fn size(&self) -> usize {
                self._base._base.length as usize
            }
            fn kind(&self) -> u32 {
                self._base._base.state.kind()
            }

            fn address(&self, base: usize) -> usize {
                if self._base._base.state.compact() == 0 {
                    return unsafe { self.data.any as usize };
                }

                if self._base._base.state.ascii() == 1 {
                    base + std::mem::size_of::<$py::PyASCIIObject>()
```

Excerpt shortened; the complete reviewed range 373–399 is in `data/cases.json`.

Closing lines 394–399 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_interpreters.rs#L394-L399))

```
            }
        }

        impl ListObject for $py::PyListObject {
            type Object = $py::PyObject;
            fn size(&self) -> usize {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0017: Versioned StringObject associated types and macro-instantiation wiring

**Classification:** non-direct context; project_source; `consumer_type_wiring`.

**Purpose:** Associates interpreter/code-object versions with Unicode replica types; actual header read logic is recorded once in Python3Impl.

**Migration effect:** Type/version selection must use matching replicas; these lines are not independent direct-layout reads.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_interpreters.rs:425–856`. SHA-256 `12477dae28fbebaffcc29e99f05447184a5b39b6497777c2c4f7f8af0c31fcac`.

**Activation / context:** Version-dependent code/interpreter trait declarations and macro invocations; package-separated actual read family is the Python3Impl/copy_string chain.

Lines 425–425 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_interpreters.rs#L425-L425))

```
    type StringObject = v3_14_0::PyUnicodeObject;
```

Lines 501–501 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_interpreters.rs#L501-L501))

```
CompactCodeObjectImpl!(v3_14_0, PyBytesObject, PyUnicodeObject);
```

Lines 509–509 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_interpreters.rs#L509-L509))

```
    type StringObject = v3_13_0::PyUnicodeObject;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0018: copy_string<T:StringObject,P:ProcessMemory>

**Classification:** direct layout dependency; project_source; `remote_payload_copy_and_decode`.

**Purpose:** Copies target header, bounds strings to fewer than4096 codepoints, copies length*kind bytes, then decodes UCS4/UCS2/ASCII/Latin1.

**Migration effect:** Both byte extent and decoder assume target flexible Unicode codepoint storage. A UTF8-only payload requires byte length and UTF8 decode, with surrogate policy consideration.

**Fields / layout:** StringObject.size, StringObject.kind, StringObject.address, StringObject.ascii, payload indexed by kind. Types: PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_data_access.rs:13–51`. SHA-256 `6e5a6fabdce3d4a7441f7913d8d3981dff69d3204b72aa8eea08610b270c6ea6`.

**Activation / context:** Runtime remote-process reader; generic trait links to versioned PyUnicodeObject implementation, even though no named Unicode token appears inside this function.

Lines 13–30 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_data_access.rs#L13-L30))

```
pub fn copy_string<T: StringObject, P: ProcessMemory>(
    ptr: *const T,
    process: &P,
) -> Result<String, Error> {
    let obj = process.copy_pointer(ptr)?;
    if obj.size() == 0 {
        return Ok(String::new());
    }
    if obj.size() >= 4096 {
        return Err(format_err!(
            "Refusing to copy {} chars of a string",
            obj.size()
        ));
    }

    let kind = obj.kind();

    let bytes = process.copy(obj.address(ptr as usize), obj.size() * kind as usize)?;
```

Excerpt shortened; the complete reviewed range 13–51 is in `data/cases.json`.

Closing lines 46–51 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_data_access.rs#L46-L51))

```
        }
        (1, true) => Ok(String::from_utf8(bytes)?),
        (1, false) => Ok(bytes.iter().map(|&b| b as char).collect()),
        _ => Err(format_err!("Unknown string kind {}", kind)),
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0019: tests::AllocatedPyASCIIObject / to_asciiobject / test_copy_string

**Classification:** direct layout dependency; test_or_fuzz; `local_replica_test_construction`.

**Purpose:** Constructs fake compact ASCII layout in local memory, then exercises remote-layout reader using LocalProcess.

**Migration effect:** Test fixture must change with replica/header layout. This is explicit layout construction but not an additional production CPython consumer.

**Fields / layout:** length, state.compact, state.kind, state.ascii, sizeof(PyASCIIObject), header-adjacent storage, transmute to PyUnicodeObject. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/src/python_data_access.rs:528–605`. SHA-256 `6e5a6fabdce3d4a7441f7913d8d3981dff69d3204b72aa8eea08610b270c6ea6`.

**Activation / context:** Test module uses v3_13_0 replica and #[repr(C)]; only test build.

Lines 528–545 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_data_access.rs#L528-L545))

```
    use super::*;
    use crate::python_bindings::v3_7_0::{
        PyASCIIObject, PyBytesObject, PyUnicodeObject, PyVarObject,
    };
    use remoteprocess::LocalProcess;
    use std::ptr::copy_nonoverlapping;

    // python stores data after pybytesobject/pyasciiobject. hack by initializing a 4k buffer for testing.
    // TODO: get better at Rust and figure out a better solution
    #[allow(dead_code)]
    #[repr(C)]
    pub struct AllocatedPyByteObject {
        pub base: PyBytesObject,
        pub storage: [u8; 4096],
    }

    #[allow(dead_code)]
    #[repr(C)] // Rust can optimize the layout of this struct and break our pointer arithmetic
```

Excerpt shortened; the complete reviewed range 528–549 is in `data/cases.json`.

Closing lines 546–549 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_data_access.rs#L546-L549))

```
    pub struct AllocatedPyASCIIObject {
        pub base: PyASCIIObject,
        pub storage: [u8; 4096],
    }
```

Lines 574–591 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_data_access.rs#L574-L591))

```
    pub fn to_asciiobject(input: &str) -> AllocatedPyASCIIObject {
        let bytes: Vec<u8> = input.bytes().collect();
        let mut base = PyASCIIObject {
            length: bytes.len() as isize,
            ..Default::default()
        };
        base.state.set_compact(1);
        base.state.set_kind(1);
        base.state.set_ascii(1);
        let mut ret = AllocatedPyASCIIObject {
            base,
            storage: [0 as u8; 4096],
        };
        unsafe {
            let ptr = &mut ret as *mut AllocatedPyASCIIObject as *mut u8;
            let dst = ptr.offset(std::mem::size_of::<PyASCIIObject>() as isize);
            copy_nonoverlapping(bytes.as_ptr(), dst, bytes.len());
        }
```

Excerpt shortened; the complete reviewed range 574–605 is in `data/cases.json`.

Closing lines 600–605 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/src/python_data_access.rs#L600-L605))

```
        let unicode: &PyUnicodeObject = unsafe { std::mem::transmute(&obj.base) };
        let copied = copy_string(unicode, &LocalProcess).unwrap();
        assert_eq!(copied, original);
    }

    #[test]
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0020: generate_bindings bindgen allowlist command

**Classification:** non-direct context; project_source; `binding_generator_configuration`.

**Purpose:** Executable Python f-string shell command allowlists target Unicode structs for Rust ABI binding generation. Literal names are configuration, not comments or direct field reads.

**Migration effect:** Generator must regenerate ABI bindings for changed target versions; command itself does not consume Unicode layout.

**Fields / layout:** none. Types: PyASCIIObject, PyCompactUnicodeObject, PyUnicodeObject.

**Source:** `py_spy-0.4.2/generate_bindings.py:106–143`. SHA-256 `eb6b5ed8772a6f083879e33a332d4c5c9a23fb8768691ef454e2f0392c9d7596`.

**Activation / context:** Offline build/development generator only. Audited text statically; never executed.

Lines 106–123 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/generate_bindings.py#L106-L123))

```
    ret = os.system(
        f"""
        cd {cpython_path}
        git checkout {version}

        # need to run configure on the current branch to generate pyconfig.h sometimes
        {("./configure prefix=" + os.path.abspath(os.path.join(cpython_path, version))) if configure else ""}


        echo "// autogenerated by generate_bindings.py " > bindgen_input.h
        echo '#define Py_BUILD_CORE 1\n' >> bindgen_input.h
        cat Include/Python.h >> bindgen_input.h
        echo '#undef HAVE_STD_ATOMIC' >> bindgen_input.h
        cat Include/frameobject.h >> bindgen_input.h
        cat Include/internal/pycore_interp.h >> bindgen_input.h
        cat Include/internal/pycore_dict.h >> bindgen_input.h
        cat Include/internal/pycore_frame.h >> bindgen_input.h
        cat Include/internal/pycore_pystate.h >> bindgen_input.h
```

Excerpt shortened; the complete reviewed range 106–143 is in `data/cases.json`.

Closing lines 138–143 ([verified immutable source](https://github.com/benfred/py-spy/blob/d230d8208d652ba168256ffb66170d1c6cd8b650/generate_bindings.py#L138-L143))

```
            --allowlist-type PyListObject \
            --allowlist-type PyLongObject \
            --allowlist-type PyFloatObject \
            --allowlist-type PyDictObject \
            --allowlist-type PyDictKeysObject \
            --allowlist-type PyDictKeyEntry \
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0138: __Pyx_PyDict_GetItemStr[WithError] macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Pass already cached Unicode name hash to known-hash dictionary lookup; macro implementation, not a codepoint/data read.

**Migration effect:** Depends on private hash field offset/presence. A UTF8 representation does not require new FSR for this operation; use a cached-hash API or updated runtime to remove layout coupling.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `py_spy-0.4.2/ci/testdata/cython_test.c:392–392`. SHA-256 `db87922ba4519d858baa1537f1d0da66f5cde89c2a08436aa308ec38e58b6634`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS (or PEP393 gate in older runtime); ordinary modern CPython internal branch; PyPy/limited fallback uses API.

Lines 384–400 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.

## L0881: PyStringObject alias

**Classification:** non-direct context; generated_distribution_code; `type_alias_only`.

**Purpose:** Maps legacy PyStringObject type name to PyUnicodeObject on Python3; this named line does not access fields, sizes or character buffer.

**Migration effect:** Type-name alias alone is not evidence of direct layout use. Each actual named field use is classified separately.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `py_spy-0.4.2/ci/testdata/cython_test.c:452–452`. SHA-256 `db87922ba4519d858baa1537f1d0da66f5cde89c2a08436aa308ec38e58b6634`.

**Activation / context:** PY_MAJOR_VERSION>=3

Lines 444–460 (immutable GitHub mapping unavailable in saved verification evidence)

```
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
  #define PyObject_Unicode             PyObject_Str
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/93/d8/5b71371f50cf153b1307e5a11ac8a4ce4d85651dae946bd7e9a064146545/py_spy-0.4.2.tar.gz); archive SHA-256 `90e600b27bb6bb40479637baca5a5b4bc2ba3395c93d889e672315d93042c4ae`.
