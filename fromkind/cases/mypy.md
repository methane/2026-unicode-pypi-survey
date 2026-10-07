# mypy 2.4.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0097: CPyStr_ChangeCase

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `tmp` — constructed_case_mapping_ucs4_array. tmp is allocated UCS4 output; unicode_func writes mapped 1..3 code points per source character into it.

**Length:** `out_len`; code-point elements (not bytes).

**Confirmed:** NonASCII before3.13 case transform reads source FSR, creates temporary4-byte output, constructs and frees. (mypy-2.4.0/mypyc/lib-rt/str_ops.c:715–741)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Immediate constructor buffer is independently owned; upstream write/case algorithm uses existing Unicode FSR. Retaining constructor does not fix upstream DATA/KIND API migration.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** Only !CPY_3_13_FEATURES and nonASCII nonempty input. On3.13+ nonASCII calls builtin str method without this constructor.

**Source:** `mypy-2.4.0/mypyc/lib-rt/str_ops.c:689–742`; SHA-256 `bef63a64f41f8c6eb8f4c1cc12be2385f5a7e6d0bad0a47d85e5e2385a5658d4`.

`mypy-2.4.0/mypyc/lib-rt/str_ops.c` lines 738–738 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L738-L738))

```
    PyObject *res = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, tmp, out_len);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0098: StringWriter_getvalue_internal

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** dynamic_1_2_4; expression `obj->kind`.

**Input:** `obj->buf` — constructed_private_stringwriter_buffer. Private embedded or allocated buffer, kind initialized1 and promoted2/4. append adds numeric code points; write copies/converts source Unicode into own buffer; len is element count.

**Length:** `obj->len`; code-point elements (not bytes).

**Confirmed:** Private heap buffer allocated in byte capacity*kind, copied/promoted. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:405–455) Starts with embedded buffer, kind1 length0. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:478–483) write copies source FSR to owned writer buffer. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:650–690) append stores1/2/4-byte scalar and increments element length. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:783–838)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Immediate constructor buffer is independently owned; upstream write/case algorithm uses existing Unicode FSR. Retaining constructor does not fix upstream DATA/KIND API migration.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** getvalue exposed Python method; internal getvalue exported capsule API and used by repr.

**Source:** `mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:539–543`; SHA-256 `3288ec85ef0e7d6d406fb8d32041c449f1fce94d120389fc6484997d8f52f804`.

`mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c` lines 542–542 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/strings/librt_strings.c#L542-L542))

```
    return PyUnicode_FromKindAndData(obj->kind, obj->buf, obj->len);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0099: StringWriter_getvalue

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** dynamic_1_2_4; expression `self->kind`.

**Input:** `self->buf` — constructed_private_stringwriter_buffer. Private embedded or allocated buffer, kind initialized1 and promoted2/4. append adds numeric code points; write copies/converts source Unicode into own buffer; len is element count.

**Length:** `self->len`; code-point elements (not bytes).

**Confirmed:** Private heap buffer allocated in byte capacity*kind, copied/promoted. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:405–455) Starts with embedded buffer, kind1 length0. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:478–483) write copies source FSR to owned writer buffer. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:650–690) append stores1/2/4-byte scalar and increments element length. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:783–838)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Immediate constructor buffer is independently owned; upstream write/case algorithm uses existing Unicode FSR. Retaining constructor does not fix upstream DATA/KIND API migration.

**Migration implication:** Preserve fixed-width input constructor semantics (convert input code points to UTF8 result); buffer is not an encoded UTF8 byte string. This call does not require the result to retain input kind or input storage.

**Activation / tracing:** getvalue exposed Python method; internal getvalue exported capsule API and used by repr.

**Source:** `mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:563–566`; SHA-256 `3288ec85ef0e7d6d406fb8d32041c449f1fce94d120389fc6484997d8f52f804`.

`mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c` lines 565–565 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/strings/librt_strings.c#L565-L565))

```
    return PyUnicode_FromKindAndData(self->kind, self->buf, self->len);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0121: CPyStr_Lower new-runtime

**Disposition:** non-use context; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (mypy-2.4.0/mypyc/lib-rt/str_ops.c:746–746)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** CPY_3_13_FEATURES; nonASCII calls built-in method, no FromKindAndData reached.

**Source:** `mypy-2.4.0/mypyc/lib-rt/str_ops.c:744–750`; SHA-256 `bef63a64f41f8c6eb8f4c1cc12be2385f5a7e6d0bad0a47d85e5e2385a5658d4`.

`mypy-2.4.0/mypyc/lib-rt/str_ops.c` lines 746–746 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L746-L746))

```
    return CPyStr_ChangeCase(self, CPy_ASCII_Lower, mypyc_interned_str.lower);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0122: CPyStr_Lower old-runtime

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (mypy-2.4.0/mypyc/lib-rt/str_ops.c:748–748)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** !CPY_3_13_FEATURES, nonempty nonASCII reaches constructor.

**Source:** `mypy-2.4.0/mypyc/lib-rt/str_ops.c:744–750`; SHA-256 `bef63a64f41f8c6eb8f4c1cc12be2385f5a7e6d0bad0a47d85e5e2385a5658d4`.

`mypy-2.4.0/mypyc/lib-rt/str_ops.c` lines 748–748 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L748-L748))

```
    return CPyStr_ChangeCase(self, CPy_ASCII_Lower, _PyUnicode_ToLowerFull);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0123: CPyStr_Upper new-runtime

**Disposition:** non-use context; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (mypy-2.4.0/mypyc/lib-rt/str_ops.c:754–754)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** CPY_3_13_FEATURES; nonASCII calls built-in method, no FromKindAndData reached.

**Source:** `mypy-2.4.0/mypyc/lib-rt/str_ops.c:752–758`; SHA-256 `bef63a64f41f8c6eb8f4c1cc12be2385f5a7e6d0bad0a47d85e5e2385a5658d4`.

`mypy-2.4.0/mypyc/lib-rt/str_ops.c` lines 754–754 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L754-L754))

```
    return CPyStr_ChangeCase(self, CPy_ASCII_Upper, mypyc_interned_str.upper);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0124: CPyStr_Upper old-runtime

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (mypy-2.4.0/mypyc/lib-rt/str_ops.c:756–756)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** !CPY_3_13_FEATURES, nonempty nonASCII reaches constructor.

**Source:** `mypy-2.4.0/mypyc/lib-rt/str_ops.c:752–758`; SHA-256 `bef63a64f41f8c6eb8f4c1cc12be2385f5a7e6d0bad0a47d85e5e2385a5658d4`.

`mypy-2.4.0/mypyc/lib-rt/str_ops.c` lines 756–756 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/str_ops.c#L756-L756))

```
    return CPyStr_ChangeCase(self, CPy_ASCII_Upper, _PyUnicode_ToUpperFull);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.

## K0125: StringWriter_repr

**Disposition:** static use; `wrapper_call`; `handwritten`.

**Kind:** implementation_defined; expression `None`.

**Input:** `None` — wrapper_parameter_handoff. Exact invocation arguments passed to inventoried constructor-owning helper; no independent buffer interpretation at this site.

**Length:** `None`; defined by downstream constructor implementation.

**Confirmed:** Actual wrapper invocation in retained source. (mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:548–548)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Implementation cases retain separate immediate/upstream provenance.

**Migration implication:** Wrapper invocation reaches the inventoried constructor/emitter only under recorded activation; constructor arguments/provenance are established in implementation, not these wrapper argument positions.

**Activation / tracing:** 

**Source:** `mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c:546–560`; SHA-256 `3288ec85ef0e7d6d406fb8d32041c449f1fce94d120389fc6484997d8f52f804`.

`mypy-2.4.0/mypyc/lib-rt/strings/librt_strings.c` lines 548–548 ([verified immutable source](https://github.com/python/mypy/blob/935ba8afba7ceacca0651579450c74339f343016/mypyc/lib-rt/strings/librt_strings.c#L548-L548))

```
    PyObject *value = StringWriter_getvalue_internal((PyObject *)self);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/34/4e/64300736cf0a0373a27b94a91b664ee7382e36f77b0621bae6381da3e180/mypy-2.4.0.tar.gz); archive SHA-256 `77bdaebd452f43fcfc4cc3ba94352a3ea537cd01e3f2d0879f48673d2ec00d6e`.
