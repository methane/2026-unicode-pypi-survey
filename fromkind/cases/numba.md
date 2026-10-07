# numba 0.68.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0108: PythonAPI.string_from_kind_and_data

**Disposition:** static use; `llvm_api_call_emitter`; `codegen`.

**Kind:** dynamic_1_2_4; expression `kind`.

**Input:** `string` — existing_unicode_or_constructed_native_fsr. LLVM C function signature (int32, char*, Py_ssize_t) resolved by API-name string; box caller supplies native struct kind,data,length. Can alias unboxed Python Unicode or own NRT allocation.

**Length:** `size`; code-point elements (not bytes).

**Confirmed:** Named runtime function emitted through builder.call. (numba-0.68.0/numba/core/pythonapi.py:1150–1154) Unbox borrows data with owning Python object; box emits constructor using native fields. (numba-0.68.0/numba/cpython/unicode.py:177–213) NRT allocation creates independent native strings. (numba-0.68.0/numba/cpython/unicode.py:248–283)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Mixed: native struct may retain borrowed PyUnicode FSR or independently allocated code-point array. Boxing buffer itself is not converted before constructor.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage. Native input can alias existing PyUnicode fixed-width data through unboxing, so a UTF8 transition also needs a supported native representation/lease or unboxing conversion; native-created buffers are independent.

**Activation / tracing:** 

**Source:** `numba-0.68.0/numba/core/pythonapi.py:1150–1154`; SHA-256 `62e3d815e9ce1168118ad9fd595ca468fb78e70023a83f2f5172680d05284c2e`.

`numba-0.68.0/numba/core/pythonapi.py` lines 1152–1154 (GitHub mapping not verified in saved evidence)

```
        fname = "PyUnicode_FromKindAndData"
        fn = self._get_function(fnty, name=fname)
        return self.builder.call(fn, [kind, string, size])
```

[Frozen source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA-256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.

## K0120: box_unicode_str

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (numba-0.68.0/numba/cpython/unicode.py:206–207)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `numba-0.68.0/numba/cpython/unicode.py:201–213`; SHA-256 `2c4c639a104dc05c46fc47d8b82a18f84e3ee1cbaa5f9615e5812fddc07171fe`.

`numba-0.68.0/numba/cpython/unicode.py` lines 206–207 ([verified immutable source](https://github.com/numba/numba/blob/d2227923e59d63b2ed67f891227219bcf6e6d323/numba/cpython/unicode.py#L206-L207))

```
    res = c.pyapi.string_from_kind_and_data(
        uni_str.kind, uni_str.data, uni_str.length)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/4e/cd/e8280f9ffa30fea9fabc5341223701231fcc5d53a31f51419d42d4bec3a6/numba-0.68.0.tar.gz); archive SHA-256 `8a781de54b980b98f43bff7f1093701b5f07c80d031c7cfa8a87493d8bf73f2d`.
