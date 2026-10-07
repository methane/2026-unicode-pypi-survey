# yarl 1.25.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0169: cpython.unicode cimport

**Disposition:** non-use context; `cimport_binding`; `handwritten`.

**Kind:** not_applicable; expression `None`.

**Input:** `None` — not_applicable. None

**Length:** `None`; not_applicable.

**Confirmed:** Cython imports the API under its original spelling; active invocation is in _Unquoter._unquote_from.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Consult buffer provenance and confirmed evidence; no automatic independence claim.

**Migration implication:** No active construction call at this occurrence.

**Activation / tracing:** 

**Source:** `yarl-1.25.1/yarl/_quoting_c.pyx:4–17`; SHA-256 `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

`yarl-1.25.1/yarl/_quoting_c.pyx` lines 4–17 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L4-L17))

```
from cpython.unicode cimport (
    Py_UCS1,
    Py_UCS2,
    PyUnicode_DATA,
    PyUnicode_DecodeASCII,
    PyUnicode_1BYTE_KIND,
    PyUnicode_2BYTE_KIND,
    PyUnicode_4BYTE_KIND,
    PyUnicode_FindChar,
    PyUnicode_FromKindAndData,
    PyUnicode_GET_LENGTH,
    PyUnicode_KIND,
    PyUnicode_READ,
)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz); archive SHA-256 `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.

## K0173: _Unquoter._unquote_from

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `writer.buf` — owned_native_output. UCS4Writer.buf is Py_UCS4*. _do_unquote supplies a local Py_UCS4 stack array, or _init_ucs4_writer allocates length * sizeof(Py_UCS4). Prefixes/literal runs are widened/copied; percent UTF-8 sequences produce code point values. Invalid escapes are preserved or replaced with U+FFFD by configuration.

**Length:** `writer.pos`; Py_UCS4 elements / output code point values, not bytes.

**Confirmed:** _ucs4_write_char assigns buf[pos] and increments pos; _ucs4_write_slice increments pos by its code point length. _unquote_from returns original val when no change occurred; FromKindAndData runs only for a changed assembled result. _do_unquote releases the writer in finally after _unquote_from returns.

**Inference / unresolved:** none recorded

**Upstream representation coupling:** immediate_constructor_buffer_is_python_fsr: False; immediate_buffer_provenance: owned_native_output; scope: Local buffer-production and reader dataflow feeding this constructor; not an assertion about all code in the package.; status: confirmed_upstream_borrowed_fsr; borrowed_fsr_dependency: confirmed; api_symbols: PyUnicode_DATA PyUnicode_KIND PyUnicode_READ; public_owned_export_dependency: False; explanation: Although the constructor receives the owned UCS4 writer, _unquote_from first borrows DATA(val), obtains KIND(val), reads code points via READ and widens/copies width-specific source slices into that writer.; input_paths: path: _Unquoter.__call__ -> _do_unquote -> _unquote_from; borrowed_fsr: True; condition: Changed percent-unquote path reaching the constructor; no-change paths return val before construction.; support_span_refs: package: yarl; path: yarl-1.25.1/yarl/_quoting_c.pyx; source_sha256: ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af; evidence_path: read-access-analysis/sources/yarl/ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af.pyx; start: 645; end: 665; snippet_sha256: 3117701e2a3dd3cfdbc3bf0d72c3a6df4bbabd31def298bc4bacf2eee409817c; verified_permalink: https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L645-L665 package: yarl; path: yarl-1.25.1/yarl/_quoting_c.pyx; source_sha256: ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af; evidence_path: read-access-analysis/sources/yarl/ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af.pyx; start: 531; end: 549; snippet_sha256: 2b707ef836be35be0cc0ba34126beaa91dea8dc621d2010deba2c56e11663242; verified_permalink: https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L531-L549 package: yarl; path: yarl-1.25.1/yarl/_quoting_c.pyx; source_sha256: ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af; evidence_path: read-access-analysis/sources/yarl/ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af.pyx; start: 627; end: 633; snippet_sha256: f367b5e4420c17c2765d8dcdeeed49b0d4fda28d0114e6830711ba708fb3c780; verified_permalink: https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L627-L633

**Migration implication:** FromKindAndData itself can transcode this owned UCS4 output under UTF-8 internals. Upstream PyUnicode_DATA/KIND/READ and width-specific literal-copy paths still need adaptation; these are separate from its constructor operands.

**Activation / tracing:** Synchronous _Unquoter.__call__ -> _do_unquote -> _unquote_from. No output-buffer ownership transfer.

**Source:** `yarl-1.25.1/yarl/_quoting_c.pyx:705–715`; SHA-256 `ba945a5c0adc152921ef02c4c2b7776acdc80a55b74d3498f16999d6c7cf62af`.

`yarl-1.25.1/yarl/_quoting_c.pyx` lines 705–715 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L705-L715))

```
        if not changed:
            return val

        if buflen:
            self._write_invalid(
                writer, kind, data, length - buflen * PCT_ESCAPE_LEN, length
            )

        return PyUnicode_FromKindAndData(
            PyUnicode_4BYTE_KIND, writer.buf, writer.pos
        )
```

`yarl-1.25.1/yarl/_quoting_c.pyx` lines 480–495 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L480-L495))

```
cdef struct UCS4Writer:
    Py_UCS4 *buf
    bint heap_allocated_buf
    Py_ssize_t pos


cdef inline int _init_ucs4_writer(
    UCS4Writer* writer, Py_UCS4* stack_buf, Py_ssize_t length
) except -1:
    writer.pos = 0
    writer.heap_allocated_buf = False
    if length <= UCS4_BUF_SIZE:
        writer.buf = stack_buf
        return 0
    if <size_t>length > <size_t>PY_SSIZE_T_MAX // sizeof(Py_UCS4):
        writer.buf = NULL
```

Closing lines 498–503 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L498-L503))

```
    writer.buf = <Py_UCS4*>PyMem_Malloc(length * sizeof(Py_UCS4))
    if writer.buf == NULL:
        PyErr_NoMemory()
        return -1
    writer.heap_allocated_buf = True
    return 0
```

Original reviewed range 480–503 is recorded in `data/sites.json`; public excerpts are bounded.

`yarl-1.25.1/yarl/_quoting_c.pyx` lines 506–513 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L506-L513))

```
cdef inline void _release_ucs4_writer(UCS4Writer* writer) noexcept:
    if writer.heap_allocated_buf:
        PyMem_Free(writer.buf)


cdef inline void _ucs4_write_char(UCS4Writer* writer, Py_UCS4 ch) noexcept:
    writer.buf[writer.pos] = ch
    writer.pos += 1
```

`yarl-1.25.1/yarl/_quoting_c.pyx` lines 531–546 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L531-L546))

```
cdef inline void _ucs4_write_slice(
    UCS4Writer* writer,
    int kind,
    const void *data,
    Py_ssize_t start,
    Py_ssize_t end,
) noexcept:
    cdef Py_ssize_t length = end - start
    cdef Py_UCS4 *out
    if length <= 0:
        return
    out = writer.buf + writer.pos
    if kind == PyUnicode_1BYTE_KIND:
        _widen_to_ucs4(out, <const Py_UCS1*>data + start, length)
    elif kind == PyUnicode_2BYTE_KIND:
        _widen_to_ucs4(out, <const Py_UCS2*>data + start, length)
```

Closing lines 547–549 ([verified immutable source](https://github.com/aio-libs/yarl/blob/604eb6da83267f4e8faf1512ffeabc23df10052e/yarl/_quoting_c.pyx#L547-L549))

```
    else:
        memcpy(out, <const Py_UCS4*>data + start, length * sizeof(Py_UCS4))
    writer.pos += length
```

Original reviewed range 531–549 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/75/16/e8be8e2fb175bbf41a0680381a319f1199fae256588241a2ac8677eafb49/yarl-1.25.1.tar.gz); archive SHA-256 `03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7`.
