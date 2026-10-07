# apsw 3.53.4.0

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0159: jsonb_decode_one_actual: JT_INT

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `(const char *)(buf->buffer + value_offset)` — external byte/buffer data. Validated numeric ASCII or text proven max_char == 127. For fixed1, byte elements denote Latin1 values, here ASCII; no UTF8 multibyte payload passed to this call.

**Length:** `buf->offset - value_offset`; 1-byte elements; ASCII byte count equals codepoint count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/jsonb.c:1268–1289) Raw byte buffer type (apsw-3.53.4.0/src/jsonb.c:1131–1143) Tag payload length establishes value_offset and end offset (apsw-3.53.4.0/src/jsonb.c:1203–1249) Hex integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1557–1583) External Python buffer acquisition/decode/release (apsw-3.53.4.0/src/jsonb.c:2318–2335) Integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1502–1554) Float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1637–1660) JSON5 float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1740–1763) ASCII text/max_char fast-path validation (apsw-3.53.4.0/src/jsonb.c:2145–2181)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** alloc branch builds temporary numeric string for parsing/hooks or ASCII output text. Non-ASCII text uses UTF8 constructor instead. Fault macro can intercept when APSW_FAULT_INJECT enabled.

**Source:** `apsw-3.53.4.0/src/jsonb.c:1275–1276`; SHA-256 `4ded8b192f0072405debfec9a8b60fb4df2a0b2675f0ed48b78bd1ad206643f1`.

`apsw-3.53.4.0/src/jsonb.c` lines 1268–1283 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1268-L1283))

```
  case JT_INT:
    if (!jsonb_check_int(buf, value_offset, buf->offset))
      return malformed(buf, "not a valid int");
    if (!buf->alloc)
      return DecodeSuccess;
    {
      /* we cant use PyLong_FromString because the end of the string can't be passed in */
      PyObject *text = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, (const char *)(buf->buffer + value_offset),
                                                 buf->offset - value_offset);
      if (!text)
        return NULL;
      PyObject *result = NULL;
      if (buf->parse_int)
      {
        PyObject *vargs[] = { NULL, text };
        result = PyObject_Vectorcall(buf->parse_int, vargs + 1, 1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
```

Closing lines 1284–1289 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1284-L1289))

```
      }
      else
        result = PyLong_FromUnicodeObject(text, 10);
      Py_DECREF(text);
      return result;
    }
```

Original reviewed range 1268–1289 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0160: jsonb_decode_one_actual: JT_INT5

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `(const char *)(buf->buffer + value_offset)` — external byte/buffer data. Validated numeric ASCII or text proven max_char == 127. For fixed1, byte elements denote Latin1 values, here ASCII; no UTF8 multibyte payload passed to this call.

**Length:** `buf->offset - value_offset`; 1-byte elements; ASCII byte count equals codepoint count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/jsonb.c:1291–1317) Raw byte buffer type (apsw-3.53.4.0/src/jsonb.c:1131–1143) Tag payload length establishes value_offset and end offset (apsw-3.53.4.0/src/jsonb.c:1203–1249) Hex integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1557–1583) External Python buffer acquisition/decode/release (apsw-3.53.4.0/src/jsonb.c:2318–2335) Integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1502–1554) Float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1637–1660) JSON5 float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1740–1763) ASCII text/max_char fast-path validation (apsw-3.53.4.0/src/jsonb.c:2145–2181)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** alloc branch builds temporary numeric string for parsing/hooks or ASCII output text. Non-ASCII text uses UTF8 constructor instead. Fault macro can intercept when APSW_FAULT_INJECT enabled.

**Source:** `apsw-3.53.4.0/src/jsonb.c:1300–1301`; SHA-256 `4ded8b192f0072405debfec9a8b60fb4df2a0b2675f0ed48b78bd1ad206643f1`.

`apsw-3.53.4.0/src/jsonb.c` lines 1291–1306 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1291-L1306))

```
  case JT_INT5:
    /* JSON5 allows leading +, regular numbers (JT_INT), and hex.  SQLite
       only allows hex .*/
    if (!jsonb_check_int5hex(buf, value_offset, buf->offset))
      return malformed(buf, "not a valid int5");
    if (!buf->alloc)
      return DecodeSuccess;
    {
      /* we cant use PyLong_FromString because the end of the string can't be passed in */
      PyObject *text = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, (const char *)(buf->buffer + value_offset),
                                                 buf->offset - value_offset);
      if (!text)
        return NULL;
      PyObject *result = NULL;
      if (buf->parse_int)
      {
```

Closing lines 1312–1317 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1312-L1317))

```
      }
      else
        result = PyLong_FromUnicodeObject(text, 0);
      Py_DECREF(text);
      return result;
    }
```

Original reviewed range 1291–1317 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0161: jsonb_decode_one_actual: JT_FLOAT/JT_FLOAT5

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `(const char *)(buf->buffer + value_offset)` — external byte/buffer data. Validated numeric ASCII or text proven max_char == 127. For fixed1, byte elements denote Latin1 values, here ASCII; no UTF8 multibyte payload passed to this call.

**Length:** `buf->offset - value_offset`; 1-byte elements; ASCII byte count equals codepoint count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/jsonb.c:1319–1341) Raw byte buffer type (apsw-3.53.4.0/src/jsonb.c:1131–1143) Tag payload length establishes value_offset and end offset (apsw-3.53.4.0/src/jsonb.c:1203–1249) Hex integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1557–1583) External Python buffer acquisition/decode/release (apsw-3.53.4.0/src/jsonb.c:2318–2335) Integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1502–1554) Float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1637–1660) JSON5 float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1740–1763) ASCII text/max_char fast-path validation (apsw-3.53.4.0/src/jsonb.c:2145–2181)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** alloc branch builds temporary numeric string for parsing/hooks or ASCII output text. Non-ASCII text uses UTF8 constructor instead. Fault macro can intercept when APSW_FAULT_INJECT enabled.

**Source:** `apsw-3.53.4.0/src/jsonb.c:1327–1328`; SHA-256 `4ded8b192f0072405debfec9a8b60fb4df2a0b2675f0ed48b78bd1ad206643f1`.

`apsw-3.53.4.0/src/jsonb.c` lines 1319–1334 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1319-L1334))

```
  case JT_FLOAT:
  case JT_FLOAT5:
    if ((tag == JT_FLOAT) ? !jsonb_check_float(buf, value_offset, buf->offset)
                          : !jsonb_check_float5(buf, value_offset, buf->offset))
      return malformed(buf, (tag == JT_FLOAT) ? "not a valid float" : "not a valid float5");
    if (!buf->alloc)
      return DecodeSuccess;
    {
      PyObject *text = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, (const char *)(buf->buffer + value_offset),
                                                 buf->offset - value_offset);
      if (!text)
        return NULL;
      PyObject *result = NULL;
      if (buf->parse_float)
      {
        PyObject *vargs[] = { NULL, text };
```

Closing lines 1336–1341 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1336-L1341))

```
      }
      else
        result = PyFloat_FromString(text);
      Py_DECREF(text);
      return result;
    }
```

Original reviewed range 1319–1341 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0162: jsonb_decode_one_actual: JT_TEXT/JT_TEXTRAW ASCII branch

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_1; expression `PyUnicode_1BYTE_KIND`.

**Input:** `(const char *)(buf->buffer + value_offset)` — external byte/buffer data. Validated numeric ASCII or text proven max_char == 127. For fixed1, byte elements denote Latin1 values, here ASCII; no UTF8 multibyte payload passed to this call.

**Length:** `buf->offset - value_offset`; 1-byte elements; ASCII byte count equals codepoint count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/jsonb.c:1343–1370) Raw byte buffer type (apsw-3.53.4.0/src/jsonb.c:1131–1143) Tag payload length establishes value_offset and end offset (apsw-3.53.4.0/src/jsonb.c:1203–1249) Hex integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1557–1583) External Python buffer acquisition/decode/release (apsw-3.53.4.0/src/jsonb.c:2318–2335) Integer ASCII validation (apsw-3.53.4.0/src/jsonb.c:1502–1554) Float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1637–1660) JSON5 float ASCII validation (apsw-3.53.4.0/src/jsonb.c:1740–1763) ASCII text/max_char fast-path validation (apsw-3.53.4.0/src/jsonb.c:2145–2181)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** alloc branch builds temporary numeric string for parsing/hooks or ASCII output text. Non-ASCII text uses UTF8 constructor instead. Fault macro can intercept when APSW_FAULT_INJECT enabled.

**Source:** `apsw-3.53.4.0/src/jsonb.c:1365–1366`; SHA-256 `4ded8b192f0072405debfec9a8b60fb4df2a0b2675f0ed48b78bd1ad206643f1`.

`apsw-3.53.4.0/src/jsonb.c` lines 1343–1358 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1343-L1358))

```
  case JT_TEXT:
  case JT_TEXTJ:
  case JT_TEXT5:
  case JT_TEXTRAW:
    /* zero length? */
    if (value_offset == buf->offset)
      return (buf->alloc) ? PyUnicode_New(0, 0) : DecodeSuccess;
    /* this is the length in codepoints */
    size_t length = 0;
    Py_UCS4 max_char = 0;
    if (!jsonb_decode_utf8_string(buf->buffer + value_offset, buf->offset - value_offset, NULL, tag, &length,
                                  &max_char))
      return malformed(buf, "not a valid string");
    assert(max_char > 0);
    if (!buf->alloc)
      return DecodeSuccess;
```

Closing lines 1365–1370 ([verified immutable source](https://github.com/rogerbinns/apsw/blob/09b6a89e13e1c49f13bfb92fdb8725d1a0f03b5a/src/jsonb.c#L1365-L1370))

```
                ? PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, (const char *)(buf->buffer + value_offset),
                                            buf->offset - value_offset)
                : PyUnicode_FromStringAndSize((const char *)(buf->buffer + value_offset), buf->offset - value_offset);
      if (retval)
        assert((size_t)PyUnicode_GET_LENGTH(retval) == length);
      return retval;
```

Original reviewed range 1343–1370 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0163: Generated APSW FromKindAndData fault interception macro

**Disposition:** non-use context; `generated_macro_forwarding_provider`; `generated_other`.

**Kind:** forwarded; expression `forwarded/dynamic; see snippets`.

**Input:** `__VA_ARGS__: buffer` — forwarded application arguments. Generated header: never-taken conditional expression probes API result type; two runtime branches may forward same application arguments. Controlled fake/error return is test plumbing.

**Length:** `__VA_ARGS__: length`; forwarded element count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/faultinject.h:1812–1826) Compiler and fault enable/clear guards (apsw-3.53.4.0/src/faultinject.h:4–20) Clear mode undefines macro (apsw-3.53.4.0/src/faultinject.h:116–122) Build activation condition (apsw-3.53.4.0/src/apsw.c:141–167) Macro suppression/restoration around source helper code before consumer (apsw-3.53.4.0/src/jsonb.c:638–651)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** Provider forwards application arguments under optional fault mode; preserve interception/type inference when API contracts change. This is not a separate input construction algorithm.

**Activation / tracing:** APSW_FAULT_INJECT gating. 0?API(...):0 branch not evaluated; runtime forwarding at1819 and1822 not independent constructor algorithms. #undef in clear mode line120.

**Source:** `apsw-3.53.4.0/src/faultinject.h:1812–1826`; SHA-256 `0674c0f997f5a51eccdf5f6b20ae5e2bfbf7cd9293707257102ad6bf7cd9c7fd`.

`apsw-3.53.4.0/src/faultinject.h` lines 1812–1826 (GitHub mapping not verified in saved evidence)

```
#define PyUnicode_FromKindAndData(...) \
({                                                                                                                                                                              \
    __auto_type _res_PyUnicode_FromKindAndData = 0 ? PyUnicode_FromKindAndData(__VA_ARGS__) : 0;                                                                                \
                                                                                                                                                                                \
    _res_PyUnicode_FromKindAndData = (typeof (_res_PyUnicode_FromKindAndData))APSW_FaultInjectControl("PyUnicode_FromKindAndData", __FILE__, __func__, __LINE__, #__VA_ARGS__); \
                                                                                                                                                                                \
    if ((typeof (_res_PyUnicode_FromKindAndData))0x1FACADE == _res_PyUnicode_FromKindAndData)                                                                                   \
       _res_PyUnicode_FromKindAndData = PyUnicode_FromKindAndData(__VA_ARGS__);                                                                                                 \
    else if ((typeof(_res_PyUnicode_FromKindAndData))0x2FACADE == _res_PyUnicode_FromKindAndData)                                                                               \
    {                                                                                                                                                                           \
        PyUnicode_FromKindAndData(__VA_ARGS__);                                                                                                                                 \
        _res_PyUnicode_FromKindAndData = (typeof (_res_PyUnicode_FromKindAndData))18;                                                                                           \
    }                                                                                                                                                                           \
    _res_PyUnicode_FromKindAndData;                                                                                                                                             \
})
```

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0192: Generated APSW FromKindAndData fault interception macro; constant-false type probe at line 1814

**Disposition:** non-use context; `unevaluated_type_probe`; `test`.

**Kind:** forwarded; expression `forwarded/dynamic; see snippets`.

**Input:** `__VA_ARGS__: buffer` — forwarded application arguments. Generated header: never-taken conditional expression probes API result type; two runtime branches may forward same application arguments. Controlled fake/error return is test plumbing.

**Length:** `__VA_ARGS__: length`; forwarded element count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/faultinject.h:1812–1826) Compiler and fault enable/clear guards (apsw-3.53.4.0/src/faultinject.h:4–20) Clear mode undefines macro (apsw-3.53.4.0/src/faultinject.h:116–122) Build activation condition (apsw-3.53.4.0/src/apsw.c:141–167) Macro suppression/restoration around source helper code before consumer (apsw-3.53.4.0/src/jsonb.c:638–651)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Generic test instrumentation; application input is described at its concrete constructor site.

**Migration implication:** Provider forwards application arguments under optional fault mode; preserve interception/type inference when API contracts change. This is not a separate input construction algorithm.

**Activation / tracing:** APSW_FAULT_INJECT gating. 0?API(...):0 branch not evaluated; runtime forwarding at1819 and1822 not independent constructor algorithms. #undef in clear mode line120.

**Source:** `apsw-3.53.4.0/src/faultinject.h:1814–1814`; SHA-256 `0674c0f997f5a51eccdf5f6b20ae5e2bfbf7cd9293707257102ad6bf7cd9c7fd`.

`apsw-3.53.4.0/src/faultinject.h` lines 1814–1814 (GitHub mapping not verified in saved evidence)

```
    __auto_type _res_PyUnicode_FromKindAndData = 0 ? PyUnicode_FromKindAndData(__VA_ARGS__) : 0;                                                                                \
```

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0193: Generated APSW FromKindAndData fault interception macro; executable forwarding at line 1819

**Disposition:** static use; `forwarding_api_call`; `test`.

**Kind:** forwarded; expression `forwarded/dynamic; see snippets`.

**Input:** `__VA_ARGS__: buffer` — forwarded application arguments. Generated header: never-taken conditional expression probes API result type; two runtime branches may forward same application arguments. Controlled fake/error return is test plumbing.

**Length:** `__VA_ARGS__: length`; forwarded element count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/faultinject.h:1812–1826) Compiler and fault enable/clear guards (apsw-3.53.4.0/src/faultinject.h:4–20) Clear mode undefines macro (apsw-3.53.4.0/src/faultinject.h:116–122) Build activation condition (apsw-3.53.4.0/src/apsw.c:141–167) Macro suppression/restoration around source helper code before consumer (apsw-3.53.4.0/src/jsonb.c:638–651)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Generic test instrumentation; application input is described at its concrete constructor site.

**Migration implication:** Provider forwards application arguments under optional fault mode; preserve interception/type inference when API contracts change. This is not a separate input construction algorithm.

**Activation / tracing:** APSW_FAULT_INJECT gating. 0?API(...):0 branch not evaluated; runtime forwarding at1819 and1822 not independent constructor algorithms. #undef in clear mode line120.

**Source:** `apsw-3.53.4.0/src/faultinject.h:1819–1819`; SHA-256 `0674c0f997f5a51eccdf5f6b20ae5e2bfbf7cd9293707257102ad6bf7cd9c7fd`.

`apsw-3.53.4.0/src/faultinject.h` lines 1819–1819 (GitHub mapping not verified in saved evidence)

```
       _res_PyUnicode_FromKindAndData = PyUnicode_FromKindAndData(__VA_ARGS__);                                                                                                 \
```

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.

## K0194: Generated APSW FromKindAndData fault interception macro; executable forwarding at line 1822

**Disposition:** static use; `forwarding_api_call`; `test`.

**Kind:** forwarded; expression `forwarded/dynamic; see snippets`.

**Input:** `__VA_ARGS__: buffer` — forwarded application arguments. Generated header: never-taken conditional expression probes API result type; two runtime branches may forward same application arguments. Controlled fake/error return is test plumbing.

**Length:** `__VA_ARGS__: length`; forwarded element count.

**Confirmed:** Exact retained source snippet included (apsw-3.53.4.0/src/faultinject.h:1812–1826) Compiler and fault enable/clear guards (apsw-3.53.4.0/src/faultinject.h:4–20) Clear mode undefines macro (apsw-3.53.4.0/src/faultinject.h:116–122) Build activation condition (apsw-3.53.4.0/src/apsw.c:141–167) Macro suppression/restoration around source helper code before consumer (apsw-3.53.4.0/src/jsonb.c:638–651)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Generic test instrumentation; application input is described at its concrete constructor site.

**Migration implication:** Provider forwards application arguments under optional fault mode; preserve interception/type inference when API contracts change. This is not a separate input construction algorithm.

**Activation / tracing:** APSW_FAULT_INJECT gating. 0?API(...):0 branch not evaluated; runtime forwarding at1819 and1822 not independent constructor algorithms. #undef in clear mode line120.

**Source:** `apsw-3.53.4.0/src/faultinject.h:1822–1822`; SHA-256 `0674c0f997f5a51eccdf5f6b20ae5e2bfbf7cd9293707257102ad6bf7cd9c7fd`.

`apsw-3.53.4.0/src/faultinject.h` lines 1822–1822 (GitHub mapping not verified in saved evidence)

```
        PyUnicode_FromKindAndData(__VA_ARGS__);                                                                                                                                 \
```

[Frozen source distribution](https://files.pythonhosted.org/packages/3b/a3/404d93429ad78385158b277ddd4929137eb279b047d892c24b8d75237119/apsw-3.53.4.0.tar.gz); archive SHA-256 `4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625`.
