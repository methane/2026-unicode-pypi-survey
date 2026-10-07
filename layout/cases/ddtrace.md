# ddtrace 4.15.4

4 confirmed layout regions; 9 reviewed regions including non-direct context.

## L1124: _PyASCIIObject_State_Hidden overlay declaration

**Classification:** non-direct context; project_source; `definition_layout`.

**Purpose:** Declare a local reinterpretation of Unicode state word used for hidden taint marker.

**Migration effect:** Relies on state word physical packing and availability of high24 bits; layout or metadata changes require redesign.

**Fields / layout:** 8-bit ignored low padding, 24-bit hidden high padding. Types: PyASCIIObject, _PyASCIIObject_State_Hidden.

**Source:** `ddtrace-4.15.4/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.h:13–19`. SHA-256 `14cfd3887352f0af66526c4934cb5d7aed8f6351c4c929a4115a3efc87e3eb00`.

**Activation / context:** This is an actual typedef provider for production casts, not a name-only UnicodeObject match.

Lines 13–19 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.h#L13-L19))

```
#define GET_HASH_KEY(hash) (hash & 0xFFFFFF)

typedef struct _PyASCIIObject_State_Hidden
{
    unsigned int : 8;
    unsigned int hidden : 24;
} PyASCIIObject_State_Hidden;
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1125: is_notinterned_notfasttainted_unicode

**Classification:** direct layout dependency; project_source; `state_padding_mutation_hash_read`.

**Purpose:** Read/write a hidden taint marker in Unicode state padding using low24 bits of cached/computed hash.

**Migration effect:** API-independent mutation of CPython metadata padding cannot be handled by an FSR view alone. Must preserve/customize marker storage or use external metadata.

**Fields / layout:** state, hidden:24, hash. Types: PyASCIIObject, _PyASCIIObject_State_Hidden.

**Source:** `ddtrace-4.15.4/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.cpp:19–40`. SHA-256 `b0e1c0d45519a325ac2baf3a06e0b184857324260f6f572d728b5955fd3cd820`.

**Activation / context:** Non-interned Unicode guarded by PyUnicode_Check/CHECK_INTERNED; setter calls PyObject_Hash if cache is -1 then sets e->hidden.

Lines 19–36 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.cpp#L19-L36))

```
is_notinterned_notfasttainted_unicode(const PyObject* objptr)
{
    if (!objptr) {
        return true; // cannot taint a nullptr
    }

    if (!PyUnicode_Check(objptr)) {
        return false; // not a unicode, continue evaluation
    }

    if (PyUnicode_CHECK_INTERNED(objptr)) {
        return true; // interned but it could still be tainted
    }

    const _PyASCIIObject_State_Hidden* e = (_PyASCIIObject_State_Hidden*)&(((PyASCIIObject*)objptr)->state);
    if (!e) {
        return true; // broken string object? better to skip it
    }
```

Excerpt shortened; the complete reviewed range 19–40 is in `data/cases.json`.

Closing lines 37–40 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.cpp#L37-L40))

```
    // it cannot be fast tainted if hash is set to -1 (not computed)
    Py_hash_t hash = ((PyASCIIObject*)objptr)->hash;
    return hash == -1 || e->hidden != GET_HASH_KEY(hash);
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1126: set_fast_tainted_if_notinterned_unicode

**Classification:** direct layout dependency; project_source; `state_padding_mutation_hash_read`.

**Purpose:** Read/write a hidden taint marker in Unicode state padding using low24 bits of cached/computed hash.

**Migration effect:** API-independent mutation of CPython metadata padding cannot be handled by an FSR view alone. Must preserve/customize marker storage or use external metadata.

**Fields / layout:** state, hidden:24, hash. Types: PyASCIIObject, _PyASCIIObject_State_Hidden.

**Source:** `ddtrace-4.15.4/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.cpp:46–58`. SHA-256 `b0e1c0d45519a325ac2baf3a06e0b184857324260f6f572d728b5955fd3cd820`.

**Activation / context:** Non-interned Unicode guarded by PyUnicode_Check/CHECK_INTERNED; setter calls PyObject_Hash if cache is -1 then sets e->hidden.

Lines 46–58 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/utils/string_utils.cpp#L46-L58))

```
set_fast_tainted_if_notinterned_unicode(PyObject* objptr)
{
    if (not objptr or !PyUnicode_Check(objptr) or PyUnicode_CHECK_INTERNED(objptr)) {
        return;
    }
    if (auto e = (_PyASCIIObject_State_Hidden*)&(((PyASCIIObject*)objptr)->state)) {
        Py_hash_t hash = ((PyASCIIObject*)objptr)->hash;
        if (hash == -1) {
            hash = PyObject_Hash(objptr);
        }
        e->hidden = GET_HASH_KEY(hash);
    }
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1127: Taint marker tests: hash/state mutations

**Classification:** direct layout dependency; test_or_fuzz; `test_fixture_metadata_mutation`.

**Purpose:** Force cached hashes and markers to verify production taint fast path.

**Migration effect:** Tests also require update when layout/marker policy changes; excluded from production-family count.

**Fields / layout:** hash, state.hidden. Types: PyASCIIObject, _PyASCIIObject_State_Hidden.

**Source:** `ddtrace-4.15.4/ddtrace/appsec/_iast/_taint_tracking/tests/test_stringutils.cpp:70–168`. SHA-256 `0899c87918601e061ed52f1a407bc04f1f371d6f50cdfce9bcebbb07bb52a726`.

**Activation / context:** Test-only setup mutates hash=-1/12345 and hidden state overlay.

Lines 70–87 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/tests/test_stringutils.cpp#L70-L87))

```
{
    EXPECT_TRUE(is_notinterned_notfasttainted_unicode(nullptr));
}

TEST_F(IsFastTaintedCheck, FastTaintedNonUnicodeReturnsFalse)
{
    PyObject* non_unicode = PyLong_FromLong(42);
    EXPECT_FALSE(is_notinterned_notfasttainted_unicode(non_unicode));
    Py_DECREF(non_unicode);
}

TEST_F(IsFastTaintedCheck, FastTaintedInternedUnicodeReturnsTrue)
{
    PyObject* interned_unicode = PyUnicode_InternFromString("interned");
    EXPECT_TRUE(is_notinterned_notfasttainted_unicode(interned_unicode));
    Py_DECREF(interned_unicode);
}

```

Excerpt shortened; the complete reviewed range 70–116 is in `data/cases.json`.

Closing lines 111–116 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/tests/test_stringutils.cpp#L111-L116))

```
      ->hidden = GET_HASH_KEY(12345);
    EXPECT_FALSE(is_notinterned_notfasttainted_unicode(non_interned_unicode));
    Py_DECREF(non_interned_unicode);
}

using SetFastTaintedCheck = PyEnvCheck;
```

Lines 130–147 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/tests/test_stringutils.cpp#L130-L147))

```
}

TEST_F(SetFastTaintedCheck, InternedUnicodeDoesNothing)
{
    PyObject* interned_unicode = PyUnicode_InternFromString("interned");
    set_fast_tainted_if_notinterned_unicode(interned_unicode);
    // No assertion needed, just ensure no crash
    Py_DECREF(interned_unicode);
}

TEST_F(SetFastTaintedCheck, NonInternedUnicodeSetsHidden)
{
    PyObject* non_interned_unicode = PyUnicode_FromString("non_interned");
    reinterpret_cast<PyASCIIObject*>(non_interned_unicode)->hash = 12345;
    set_fast_tainted_if_notinterned_unicode(non_interned_unicode);
    const _PyASCIIObject_State_Hidden* e =
      (_PyASCIIObject_State_Hidden*)&(((PyASCIIObject*)non_interned_unicode)->state);
    EXPECT_EQ(e->hidden, GET_HASH_KEY(12345));
```

Excerpt shortened; the complete reviewed range 130–168 is in `data/cases.json`.

Closing lines 163–168 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/tests/test_stringutils.cpp#L163-L168))

```
using IsTextCheck = PyEnvCheck;

TEST_F(IsTextCheck, NullptrReturnsFalse)
{
    EXPECT_FALSE(is_text(nullptr));
}
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1128: pyunicode_to_utf8

**Classification:** direct layout dependency; project_source; `remote_layout_snapshot_read`.

**Purpose:** Copy target process Unicode object header and decode selected character bytes from target memory.

**Migration effect:** Requires version-specific physical structs/offsets and payload rules. Remote memory reader cannot simply invoke target-object C APIs from the observing code. UTF8-native layout needs a revised remote decoder.

**Fields / layout:** full PyUnicodeObject snapshot, _base._base, state.kind, state.compact, length, _base.utf8, _base.utf8_length, sizeof(ascii). Types: PyASCIIObject, PyUnicodeObject.

**Source:** `ddtrace-4.15.4/ddtrace/internal/datadog/profiling/stack/src/echion/strings.cc:22–49`. SHA-256 `68b1432ab34e59cc26a031b630560d778edde91c73c4a20d7c4690fc791b82dc`.

**Activation / context:** Actual project-owned PyUnicodeObject variable, not typed API cast. copy_type snapshots the entire object; kind!=1 is rejected. compact branch adds sizeof(PyASCIIObject) regardless of ascii flag; record observed logic without assuming all kind1 objects are correctly decoded.

Lines 22–39 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/src/echion/strings.cc#L22-L39))

```
pyunicode_to_utf8(PyObject* str_addr)
{
    PyUnicodeObject str;
    if (copy_type(str_addr, str))
        return ErrorKind::PyUnicodeError;

    PyASCIIObject& ascii = str._base._base;

    if (ascii.state.kind != 1)
        return ErrorKind::PyUnicodeError;

    const char* data = ascii.state.compact
                         ? reinterpret_cast<const char*>(reinterpret_cast<const uint8_t*>(str_addr) + sizeof(ascii))
                         : static_cast<const char*>(str._base.utf8);
    if (data == NULL)
        return ErrorKind::PyUnicodeError;

    Py_ssize_t size = ascii.state.compact ? ascii.length : str._base.utf8_length;
```

Excerpt shortened; the complete reviewed range 22–49 is in `data/cases.json`.

Closing lines 44–49 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/src/echion/strings.cc#L44-L49))

```
    if (copy_generic(data, dest.data(), size))
        return ErrorKind::PyUnicodeError;

    return Result<std::string>(dest);
}

```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1129: StringTable::key remote-reader activation

**Classification:** non-direct context; project_source; `indirect_activation`.

**Purpose:** On first tagged object-address lookup call pyunicode_to_utf8 and retain resulting std::string in table.

**Migration effect:** Cache output is owned; physical decode dependency remains in reader.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `ddtrace-4.15.4/ddtrace/internal/datadog/profiling/stack/src/echion/strings.cc:51–70`. SHA-256 `68b1432ab34e59cc26a031b630560d778edde91c73c4a20d7c4690fc791b82dc`.

**Activation / context:** No additional named Unicode struct token in this caller; supporting activation only.

Lines 51–68 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/src/echion/strings.cc#L51-L68))

```
StringTable::key(PyObject* s, StringTag tag)
{
    const std::lock_guard<std::mutex> lock(table_lock);

    auto k = make_tagged_key(reinterpret_cast<uintptr_t>(s), tag);

    if (table_.find(k) == table_.end()) {
        auto maybe_unicode = pyunicode_to_utf8(s);
        if (!maybe_unicode) {
            return ErrorKind::PyUnicodeError;
        }

        table_.emplace(k, std::move(*maybe_unicode));
    }

    return Result<Key>(k);
}

```

Excerpt shortened; the complete reviewed range 51–70 is in `data/cases.json`.

Closing lines 69–70 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/src/echion/strings.cc#L69-L70))

```
[[nodiscard]] Result<std::reference_wrapper<const std::string>>
StringTable::lookup(StringTable::Key key) const
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1130: fuzz reader mentions/call activation

**Classification:** non-direct context; test_or_fuzz; `comment_and_fuzz_activation`.

**Purpose:** Comments identify reader and fuzz code invokes it.

**Migration effect:** Does not add an independent explicit struct access.

**Fields / layout:** none. Types: PyASCIIObject, PyUnicodeObject.

**Source:** `ddtrace-4.15.4/ddtrace/internal/datadog/profiling/stack/fuzz/fuzz_echion_pyunicode.cpp:1–35`. SHA-256 `397b0e27847f83d63e176ae61b06e4be99bed6d272c9fd8414c374d9590357b3`.

**Activation / context:** Comment-only named type occurrences; supporting test/fuzz evidence.

Lines 1–18 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/fuzz/fuzz_echion_pyunicode.cpp#L1-L18))

```
// Fuzz harness: pyunicode_to_utf8
//
// Exercises PyUnicodeObject parsing from remote memory.
// pyunicode_to_utf8 reads the PyASCIIObject header, validates
// string kind and compact state, resolves data pointer, copies
// the character buffer via copy_generic, and returns a std::string.

#include "fuzz_common.h"

#include <echion/strings.h>

// NOLINTBEGIN(performance-no-int-to-ptr)
extern "C" int
LLVMFuzzerTestOneInput(const uint8_t* data, size_t size)
{
    g_data = data;
    g_size = size;

```

Excerpt shortened; the complete reviewed range 1–35 is in `data/cases.json`.

Closing lines 30–35 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/fuzz/fuzz_echion_pyunicode.cpp#L30-L35))

```

    g_data = nullptr;
    g_size = 0;
    return 0;
}
// NOLINTEND(performance-no-int-to-ptr)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1131: fuzz StringTable reader mention

**Classification:** non-direct context; test_or_fuzz; `comment_and_fuzz_activation`.

**Purpose:** Comments describe Unicode remote path during StringTable fuzzing.

**Migration effect:** No direct named Unicode struct read in this file.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `ddtrace-4.15.4/ddtrace/internal/datadog/profiling/stack/fuzz/fuzz_echion_strings.cpp:20–35`. SHA-256 `a749fec5c296797c40db178e31ef8d5663ec0d1302c04aef7a250e673725d9a2`.

**Activation / context:** Supporting fuzz invocation only.

Lines 20–35 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/internal/datadog/profiling/stack/fuzz/fuzz_echion_strings.cpp#L20-L35))

```
    }

    uintptr_t p0 = addr_from_u64(load_u64_le(data, size, 0));
    uintptr_t p1 = addr_from_u64(load_u64_le(data, size, 8));

    EchionSampler echion_sampler;

    // StringTable::key — reads PyUnicodeObject from remote memory; exercises
    // string interning, UTF-8 conversion, and size validation.
    (void)echion_sampler.string_table().key(reinterpret_cast<PyObject*>(p0), StringTag::FuncName);

    // pybytes_to_bytes_and_size — reads PyBytesObject from remote memory;
    // exercises ob_size validation and copy_generic for variable-length data.
    {
        Py_ssize_t bytes_size = 0;
        (void)pybytes_to_bytes_and_size(reinterpret_cast<PyObject*>(p1), &bytes_size);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.

## L1132: str/bytes compatibility configuration comments

**Classification:** non-direct context; project_source; `comment`.

**Purpose:** Comment says pybind11 str can hold Unicode objects.

**Migration effect:** No layout dependence follows from this named mention.

**Fields / layout:** none. Types: PyUnicodeObject.

**Source:** `ddtrace-4.15.4/ddtrace/appsec/_iast/_taint_tracking/_vendor/pybind11/include/pybind11/detail/common.h:314–329`. SHA-256 `a455fde97288d2cacb50b2d21282064e4340349352fc0b3be2208e61e54ad62e`.

**Activation / context:** All three named tokens are comments.

Lines 314–329 ([verified immutable source](https://github.com/DataDog/dd-trace-py/blob/b97ac673e137d1b52ac4a921cc03dbf2a3f3feb8/ddtrace/appsec/_iast/_taint_tracking/_vendor/pybind11/include/pybind11/detail/common.h#L314-L329))

```
#    define PYBIND11_TYPE_GUARD_TYPE_HINT "typing_extensions.TypeGuard"
#endif

// #define PYBIND11_STR_LEGACY_PERMISSIVE
// If DEFINED, pybind11::str can hold PyUnicodeObject or PyBytesObject
//             (probably surprising and never documented, but this was the
//             legacy behavior until and including v2.6.x). As a side-effect,
//             pybind11::isinstance<str>() is true for both pybind11::str and
//             pybind11::bytes.
// If UNDEFINED, pybind11::str can only hold PyUnicodeObject, and
//               pybind11::isinstance<str>() is true only for pybind11::str.
//               However, for Python 2 only (!), the pybind11::str caster
//               implicitly decoded bytes to PyUnicodeObject. This was to ease
//               the transition from the legacy behavior to the non-permissive
//               behavior.

```

[Frozen source distribution](https://files.pythonhosted.org/packages/bb/39/9185fc5136dd2f7ad07cb0c12b76c3557a072fc90d70223fb1f504bd5d18/ddtrace-4.15.4.tar.gz); archive SHA-256 `bd8beffa63e77e803522fdeacbd5693d5816e51868bd99b7f602985efddc751b`.
