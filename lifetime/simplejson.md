# simplejson: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#simplejson)

The callable scanner is reusable configuration, not a prepared input/view object. scan_once(string,idx) independently gets DATA; successful null needs only four scalar reads.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## _speedups.c: 2263–2283

view macros

Archive member: `simplejson-4.1.2/simplejson/_speedups.c`

Member SHA256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`

[Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz); archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

[Verified permanent source](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2263-L2283).

```
/* -- Generate scan_once_unicode, _parse_object_unicode, _parse_array_unicode,
   _match_number_unicode from the shared template. -- */
#define JSON_SCAN_SUFFIX _unicode
#define JSON_SCAN_DATA_INIT(p) \
    PY2_UNUSED int kind = PyUnicode_KIND(p); \
    void *str = PyUnicode_DATA(p); \
    Py_ssize_t end_idx = PyUnicode_GET_LENGTH(p) - 1
#define JSON_SCAN_READ(i) PyUnicode_READ(kind, str, (i))
#define JSON_SCAN_SCANSTRING_CALL(pos, nextp) \
    scanstring_unicode(state, pystr, (pos), s->strict, (nextp))
#if PY_MAJOR_VERSION >= 3
#define JSON_SCAN_NUMSTR_CREATE(sidx, eidx) \
    PyUnicode_Substring(pystr, (sidx), (eidx))
#else
#define JSON_SCAN_NUMSTR_CREATE(sidx, eidx) \
    PyUnicode_FromUnicode(&((Py_UNICODE *)str)[(sidx)], (eidx) - (sidx))
#endif
#define JSON_SCAN_PARSE_FLOAT_FAST(ns) _match_number_float_fast_unicode(ns)
#define JSON_SCAN_PARSE_INT_FAST(ns)   _match_number_int_fast_unicode(s, ns)
#define JSON_SPEEDUPS_SCAN_INCLUDING 1
#include "_speedups_scan.h"
```

## _speedups.c: 2306–2330

entry and call exit

Archive member: `simplejson-4.1.2/simplejson/_speedups.c`

Member SHA256: `e0681cf41a97d26be4232927215d2486b5b9ff12bbebf69293de733e20be80c2`

[Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz); archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

[Verified permanent source](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups.c#L2306-L2330).

```
static PyObject *
scanner_call(PyObject *self, PyObject *args, PyObject *kwds)
{
    /* Python callable interface to scan_once_{str,unicode} */
    PyObject *pystr;
    PyObject *rval = NULL;
    Py_ssize_t idx;
    Py_ssize_t next_idx = -1;
    static char *kwlist[] = {"string", "idx", NULL};
    PyScannerObject *s;
#if PY_VERSION_HEX < 0x030D0000
    assert(PyScanner_Check(self));
#endif
    s = (PyScannerObject *)self;
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "On:scan_once", kwlist, &pystr, &idx))
        return NULL;

    if (PyUnicode_Check(pystr)) {
        if (PyUnicode_READY(pystr))
            return NULL;
    }
#if PY_MAJOR_VERSION < 3
    else if (!PyString_Check(pystr)) {
#else
    else {
```

## _speedups_scan.h: 437–479

successful four-character null

Archive member: `simplejson-4.1.2/simplejson/_speedups_scan.h`

Member SHA256: `7ee24c08e51074970f2bd7e14ab3afd89e5e7db850b8065a35e8297ce9eff5c3`

[Frozen sdist](https://files.pythonhosted.org/packages/f1/e3/1cc7dbf4deebc16e9dc42db37f473b5b612d021eb10e69974be308425171/simplejson-4.1.2.tar.gz); archive SHA256 `6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394`.

[Verified permanent source](https://github.com/simplejson/simplejson/blob/d1fe71a2b8a4dd307d7010076cd8cc74087df030/simplejson/_speedups_scan.h#L437-L479).

```
    _speedups_state *state = get_speedups_state(s->module_ref);
    JSON_SCAN_DATA_INIT(pystr);
    Py_ssize_t length = end_idx + 1;
    PyObject *rval = NULL;
    int fallthrough = 0;
    if (idx < 0 || idx >= length) {
        raise_errmsg(state, ERR_EXPECTING_VALUE, pystr, idx);
        return NULL;
    }
    switch (JSON_SCAN_READ(idx)) {
        case '"':
            /* string */
            rval = JSON_SCAN_SCANSTRING_CALL(idx + 1, next_idx_ptr);
            break;
        case '{':
            /* object */
            if (Py_EnterRecursiveCall(" while decoding a JSON object "
                                      "from a string"))
                return NULL;
            rval = JSON_SCAN_FN(_parse_object)(s, pystr, idx + 1, next_idx_ptr);
            Py_LeaveRecursiveCall();
            break;
        case '[':
            /* array */
            if (Py_EnterRecursiveCall(" while decoding a JSON array "
                                      "from a string"))
                return NULL;
            rval = JSON_SCAN_FN(_parse_array)(s, pystr, idx + 1, next_idx_ptr);
            Py_LeaveRecursiveCall();
            break;
        case 'n':
            /* null */
            if ((idx + 3 < length)
                && JSON_SCAN_READ(idx + 1) == 'u'
                && JSON_SCAN_READ(idx + 2) == 'l'
                && JSON_SCAN_READ(idx + 3) == 'l') {
                Py_INCREF(Py_None);
                *next_idx_ptr = idx + 4;
                rval = Py_None;
            }
            else
                fallthrough = 1;
            break;
```
