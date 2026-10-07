# rapidfuzz: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#rapidfuzz)

Same original non-ASCII inputs are captured in local RF_String wrappers on each independent pair call. Long strings differing at first (Prefix/cutoff0) or last (Postfix) codepoint need only a mismatch read; immediate eviction adds whole-string materialization per call.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## cpp_common.hpp: 294–310

Unicode conversion captures full borrowed DATA/kind/length.

Archive member: `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.hpp`

Member SHA256: `7365fa1397d9b9cfd85de296aab17f5b553f7ee7e5b85d7bc96d7c22901b1fcb`

[Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

[Verified permanent source](https://github.com/rapidfuzz/RapidFuzz/blob/d1b4a183f9ee445134989f4ebbf1e4acfacd4ed7/src/rapidfuzz/cpp_common.hpp#L294-L310).

```
static inline RF_String convert_string(PyObject* py_str)
{
    if (PyBytes_Check(py_str))
        return {nullptr, RF_UINT8, PyBytes_AS_STRING(py_str), static_cast<int64_t>(PyBytes_GET_SIZE(py_str)),
                nullptr};
    else {
        RF_StringType kind;
        switch (PyUnicode_KIND(py_str)) {
        case PyUnicode_1BYTE_KIND: kind = RF_UINT8; break;
        case PyUnicode_2BYTE_KIND: kind = RF_UINT16; break;
        default: kind = RF_UINT32; break;
        }

        return {nullptr, kind, PyUnicode_DATA(py_str), static_cast<int64_t>(PyUnicode_GET_LENGTH(py_str)),
                nullptr};
    }
}
```

## cpp_common.pxd: 398–418

With processor=None, each pair call converts both inputs into local wrappers.

Archive member: `rapidfuzz-3.14.6/src/rapidfuzz/cpp_common.pxd`

Member SHA256: `540af9abf7f62facb74c46261f37bf4a132a27c51d6741d620cb85bdb495daeb`

[Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
cdef inline bool preprocess_strings(s1, s2, processor, RF_StringWrapper* s1_proc, RF_StringWrapper* s2_proc) except False:
    cdef RF_Preprocessor* preprocess_context = NULL

    if not processor:
        s1_proc[0] = RF_StringWrapper(conv_sequence(s1))
        s2_proc[0] = RF_StringWrapper(conv_sequence(s2))
    else:
        processor_capsule = getattr(processor, '_RF_Preprocess', processor)
        if PyCapsule_IsValid(processor_capsule, NULL):
            preprocess_context = <RF_Preprocessor*>PyCapsule_GetPointer(processor_capsule, NULL)

        if preprocess_context != NULL and preprocess_context.version == 1:
            preprocess_context.preprocess(s1, &(s1_proc[0].string))
            preprocess_context.preprocess(s2, &(s2_proc[0].string))
        else:
            s1 = processor(s1)
            s1_proc[0] = RF_StringWrapper(conv_sequence(s1), s1)
            s2 = processor(s2)
            s2_proc[0] = RF_StringWrapper(conv_sequence(s2), s2)

    return True
```

## metrics_cpp.pyx: 1045–1063

Exposed native postfix metric entries call preprocess_strings then core scorer.

Archive member: `rapidfuzz-3.14.6/src/rapidfuzz/distance/metrics_cpp.pyx`

Member SHA256: `4dafe9d5b67bfffbbb730e6fd782a80b49c9632ec4d6e59d2337dc58e5e06368`

[Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
def postfix_distance(s1, s2, *, processor=None, score_cutoff=None):
    cdef size_t c_score_cutoff = get_score_cutoff_size_t(score_cutoff, SIZE_MAX, 0)
    cdef RF_StringWrapper s1_proc, s2_proc

    preprocess_strings(s1, s2, processor, &s1_proc, &s2_proc)
    return postfix_distance_func(s1_proc.string, s2_proc.string, c_score_cutoff)

def postfix_similarity(s1, s2, *, processor=None, score_cutoff=None):
    cdef size_t c_score_cutoff = get_score_cutoff_size_t(score_cutoff, 0, SIZE_MAX)
    cdef RF_StringWrapper s1_proc, s2_proc

    preprocess_strings(s1, s2, processor, &s1_proc, &s2_proc)
    return postfix_similarity_func(s1_proc.string, s2_proc.string, c_score_cutoff)

def postfix_normalized_distance(s1, s2, *, processor=None, score_cutoff=None):
    cdef RF_StringWrapper s1_proc, s2_proc
    setupPandas()
    if is_none(s1) or is_none(s2):
        return 1.0
```

## Prefix_impl.hpp: 23–27

Prefix stops at first mismatch.

Archive member: `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance/Prefix_impl.hpp`

Member SHA256: `ff483568dee2fc4a14a21d49004c83fc0e94ff3ded85323562369598eb9bad0a`

[Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

[Verified permanent source](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/distance/Prefix_impl.hpp#L23-L27).

```
    static size_t _similarity(Range<InputIt1> s1, Range<InputIt2> s2, size_t score_cutoff, size_t)
    {
        size_t dist = remove_common_prefix(s1, s2);
        return (dist >= score_cutoff) ? dist : 0;
    }
```

## Postfix_impl.hpp: 23–27

Postfix reverse suffix stops at first mismatch.

Archive member: `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/distance/Postfix_impl.hpp`

Member SHA256: `f24da62c37f46518d030db78bdfd0d0c571dfea9a72d3af06da0d2b3b199b20b`

[Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

[Verified permanent source](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/distance/Postfix_impl.hpp#L23-L27).

```
    static size_t _similarity(Range<InputIt1> s1, Range<InputIt2> s2, size_t score_cutoff, size_t)
    {
        size_t dist = remove_common_suffix(s1, s2);
        return (dist >= score_cutoff) ? dist : 0;
    }
```

## Range.hpp: 203–215

Range equality std::equal early mismatch, != delegates to equality.

Archive member: `rapidfuzz-3.14.6/extern/rapidfuzz-cpp/rapidfuzz/details/Range.hpp`

Member SHA256: `86f3809dea9db6d935f64131b6294a6537f6c3bd1ddfd52977362f2d0df0b1ac`

[Frozen sdist](https://files.pythonhosted.org/packages/18/97/226c43b7b5d957bc3840ed52ea99eed261f99834c4619be7a4742cbaeafa/rapidfuzz-3.14.6.tar.gz); archive SHA256 `e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60`.

[Verified permanent source](https://github.com/rapidfuzz/rapidfuzz-cpp/blob/82662f3623b3ca3645e543f677fc32fb8bd1fb95/rapidfuzz/details/Range.hpp#L203-L215).

```
inline bool operator==(const Range<InputIt1>& a, const Range<InputIt2>& b)
{
    if (a.size() != b.size()) return false;

    return std::equal(a.begin(), a.end(), b.begin());
}

template <typename InputIt1, typename InputIt2>
inline bool operator!=(const Range<InputIt1>& a, const Range<InputIt2>& b)
{
    return !(a == b);
}

```
