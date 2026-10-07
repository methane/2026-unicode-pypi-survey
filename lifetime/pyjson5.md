# pyjson5: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#pyjson5)

decode(data, some=True) can parse a short initial value and stop with a long non-ASCII suffix unconsumed. Reader objects belong to this call, not a persistent scanner.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## _decoder.pyx: 783–802

some=True stop

Archive member: `pyjson5-2.0.1/src/_decoder.pyx`

Member SHA256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`

[Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

[Verified permanent source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L783-L802).

```
    result = _decode_recursive(reader, &c0)
    try:
        if c0 < 0:
            pass
        elif not some:
            start = _reader_tell(reader)
            c1 = cast_to_uint32(c0)
            c0 = _skip_to_data_sub(reader, c1)
            if expect(c0 >= 0, False):
                c1 = cast_to_uint32(c0)
                _raise_extra_data(c1, start)
        elif expect(not _is_ws_zs(c0), False):
            start = _reader_tell(reader)
            c1 = cast_to_uint32(c0)
            _raise_unframed_data(c1, start)
    except _DecoderException as ex:
        (<_DecoderException> ex).result = result
        raise

    return result
```

## _decoder.pyx: 836–857

view and stack lifetime

Archive member: `pyjson5-2.0.1/src/_decoder.pyx`

Member SHA256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`

[Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

[Verified permanent source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L836-L857).

```
cdef object _decode_ucs4(const void *string, Py_ssize_t length,
                         Py_ssize_t maxdepth, boolean some):
    cdef ReaderUCS4 reader = ReaderUCS4(
        ReaderUCS(length, 0, maxdepth),
        <const Py_UCS4*> string,
    )
    return _decode_all(reader, some)


cdef object _decode_utf8(const void *string, Py_ssize_t length,
                         Py_ssize_t maxdepth, boolean some):
    cdef ReaderUTF8 reader = ReaderUTF8(
        ReaderUCS(length, 0, maxdepth),
        <const Py_UCS1*> string,
    )
    return _decode_all(reader, some)


cdef object _decode_unicode(object data, Py_ssize_t maxdepth, boolean some):
    cdef Py_ssize_t length
    cdef int kind
    cdef const char *s
```

## _decoder.pyx: 855–876

view and stack lifetime

Archive member: `pyjson5-2.0.1/src/_decoder.pyx`

Member SHA256: `c0cef53ced6f4e12d07a4088c487ab4e27ffb1bf16eed996440c19fe412b0d78`

[Frozen sdist](https://files.pythonhosted.org/packages/f1/9a/3db19560e968d6e85b2a4ddf4b949c6ebf9dd1dcfb5a9f37736f8adeb927/pyjson5-2.0.1.tar.gz); archive SHA256 `a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39`.

[Verified permanent source](https://github.com/Kijewski/pyjson5/blob/b612b5511dc6a52f55d44aaaa31c86126b985d5e/src/_decoder.pyx#L855-L876).

```
    cdef Py_ssize_t length
    cdef int kind
    cdef const char *s

    PyUnicode_READY(data)

    if CYTHON_COMPILING_IN_PYPY:
        length = 0
        s = PyUnicode_AsUTF8AndSize(data, &length)
        return _decode_utf8(s, length, maxdepth, some)

    length = PyUnicode_GET_LENGTH(data)
    kind = PyUnicode_KIND(data)

    if kind == PyUnicode_1BYTE_KIND:
        return _decode_ucs1(PyUnicode_1BYTE_DATA(data), length, maxdepth, some)
    elif kind == PyUnicode_2BYTE_KIND:
        return _decode_ucs2(PyUnicode_2BYTE_DATA(data), length, maxdepth, some)
    elif kind == PyUnicode_4BYTE_KIND:
        return _decode_ucs4(PyUnicode_4BYTE_DATA(data), length, maxdepth, some)
    else:
        unreachable()
```
