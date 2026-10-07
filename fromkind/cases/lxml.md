# lxml 6.1.3

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0002: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `lxml-6.1.3/src/lxml/etree.c:295259–295260`; SHA-256 `cff9439b818e1a6faf210ff2cc89800120c31cbd748668eb6b734444b34436ee`.

`lxml-6.1.3/src/lxml/etree.c` lines 295233–295248 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    #if !CYTHON_COMPILING_IN_LIMITED_API
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    #endif
    length = __Pyx_PyUnicode_GET_LENGTH(text);
    #if !CYTHON_ASSUME_SAFE_SIZE
    if (unlikely(length < 0)) return NULL;
    #endif
    if (start < 0) {
        start += length;
        if (start < 0)
            start = 0;
    }
    if (stop < 0)
```

Closing lines 295257–295262 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 295233–295262 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0003: __Pyx_PyUnicode_Substring

**Disposition:** static use; `direct_api_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text)` — existing_python_fsr. Borrowed fixed-width storage of text. PyUnicode_1BYTE_DATA is used as a byte-address cast; start*kind converts a codepoint offset into a byte offset. No bytes encoding is implied.

**Length:** `stop-start`; codepoint_elements.

**Confirmed:** PyUnicode_KIND(text) selects the actual fixed-width representation. PyUnicode_GET_LENGTH, negative-index adjustment and clamping precede stop-start. Empty slices and complete slices return existing singleton/input references; nonempty proper slices construct a new string.

**Inference / unresolved:** A UTF-8 representation would need a compatible fixed-width view or a rewritten Unicode substring operation.

**Upstream representation coupling:** The constructor reads a borrowed FSR slice during the call. Empty/full fast paths or limited-API branches can bypass this expression.

**Migration implication:** The API can still accept fixed-width arrays, but this provider obtains its input from Python internal FSR and must adapt if that storage is no longer directly available.

**Activation / tracing:** Cython reusable substring runtime provider. Saved sources establish presence and caller syntax, not runtime execution frequency. Full API Cython branches call the target; limited API branches use PyUnicode_Substring where provided.

**Source:** `lxml-6.1.3/src/lxml/html/diff.c:28289–28290`; SHA-256 `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`.

`lxml-6.1.3/src/lxml/html/diff.c` lines 28263–28278 (GitHub mapping not verified in saved evidence)

```
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Substring(
            PyObject* text, Py_ssize_t start, Py_ssize_t stop) {
    Py_ssize_t length;
    #if !CYTHON_COMPILING_IN_LIMITED_API
    if (unlikely(__Pyx_PyUnicode_READY(text) == -1)) return NULL;
    #endif
    length = __Pyx_PyUnicode_GET_LENGTH(text);
    #if !CYTHON_ASSUME_SAFE_SIZE
    if (unlikely(length < 0)) return NULL;
    #endif
    if (start < 0) {
        start += length;
        if (start < 0)
            start = 0;
    }
    if (stop < 0)
```

Closing lines 28287–28292 (GitHub mapping not verified in saved evidence)

```
    return PyUnicode_Substring(text, start, stop);
#else
    return PyUnicode_FromKindAndData(PyUnicode_KIND(text),
        PyUnicode_1BYTE_DATA(text) + start*PyUnicode_KIND(text), stop-start);
#endif
}
```

Original reviewed range 28263–28292 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0043: __pyx_f_4lxml_5etree_11_FeedParser_feed

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument ((PyObject*)__pyx_v_data). Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/etree.c:142739–142739`; SHA-256 `cff9439b818e1a6faf210ff2cc89800120c31cbd748668eb6b734444b34436ee`.

`lxml-6.1.3/src/lxml/etree.c` lines 142721–142736 (GitHub mapping not verified in saved evidence)

```
 *                 # Unicode parsing by converting chunks to UTF-8
 *                 buffer_len = 2**19  # len(bytes) <= 4 * (2**19) == 2 MiB             # <<<<<<<<<<<<<<
 *                 bstring = (<unicode> data)[ustart : ustart+buffer_len].encode('UTF-8')
 *                 ustart += buffer_len
*/
      __pyx_v_buffer_len = 0x80000;

      /* "src/lxml/parser.pxi":1445
 *                 # Unicode parsing by converting chunks to UTF-8
 *                 buffer_len = 2**19  # len(bytes) <= 4 * (2**19) == 2 MiB
 *                 bstring = (<unicode> data)[ustart : ustart+buffer_len].encode('UTF-8')             # <<<<<<<<<<<<<<
 *                 ustart += buffer_len
 *                 py_buffer_len -= buffer_len  # may end up < 0
*/
      if (unlikely(__pyx_v_data == Py_None)) {
        PyErr_SetString(PyExc_TypeError, "'NoneType' object is not subscriptable");
```

Closing lines 142742–142747 (GitHub mapping not verified in saved evidence)

```
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF_SET(__pyx_v_bstring, ((PyObject*)__pyx_t_2));
      __pyx_t_2 = 0;

      /* "src/lxml/parser.pxi":1446
```

Original reviewed range 142721–142747 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0044: __pyx_f_4lxml_5etree__escape_cdata_c14n

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_text. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/etree.c:180748–180748`; SHA-256 `cff9439b818e1a6faf210ff2cc89800120c31cbd748668eb6b734444b34436ee`.

`lxml-6.1.3/src/lxml/etree.c` lines 180730–180745 (GitHub mapping not verified in saved evidence)

```
 *         if pos > start:             # <<<<<<<<<<<<<<
 *             substrings.append(text[start:pos])
 *         substrings.append(escape)
*/
    __pyx_t_16 = (__pyx_v_pos > __pyx_v_start);
    if (__pyx_t_16) {

      /* "src/lxml/serializer.pxi":1205
 *             substrings = []
 *         if pos > start:
 *             substrings.append(text[start:pos])             # <<<<<<<<<<<<<<
 *         substrings.append(escape)
 *         start = pos + 1
*/
      if (unlikely(__pyx_v_substrings == Py_None)) {
        PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
```

Closing lines 180751–180756 (GitHub mapping not verified in saved evidence)

```
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      /* "src/lxml/serializer.pxi":1204
 *         if substrings is None:
 *             substrings = []
 *         if pos > start:             # <<<<<<<<<<<<<<
```

Original reviewed range 180730–180756 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0045: __pyx_f_4lxml_5etree__escape_cdata_c14n

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_text. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/etree.c:180839–180839`; SHA-256 `cff9439b818e1a6faf210ff2cc89800120c31cbd748668eb6b734444b34436ee`.

`lxml-6.1.3/src/lxml/etree.c` lines 180821–180836 (GitHub mapping not verified in saved evidence)

```
 *     if pos >= start:             # <<<<<<<<<<<<<<
 *         substrings.append(text[start:pos+1])
 *     return ''.join(substrings)
*/
  __pyx_t_16 = (__pyx_v_pos >= __pyx_v_start);
  if (__pyx_t_16) {

    /* "src/lxml/serializer.pxi":1212
 *         return text
 *     if pos >= start:
 *         substrings.append(text[start:pos+1])             # <<<<<<<<<<<<<<
 *     return ''.join(substrings)
 * 
*/
    if (unlikely(__pyx_v_substrings == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
```

Closing lines 180842–180847 (GitHub mapping not verified in saved evidence)

```
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

    /* "src/lxml/serializer.pxi":1211
 *     if substrings is None:
 *         return text
 *     if pos >= start:             # <<<<<<<<<<<<<<
```

Original reviewed range 180821–180847 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0046: __pyx_f_4lxml_5etree__escape_attrib_c14n

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_text. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/etree.c:181278–181278`; SHA-256 `cff9439b818e1a6faf210ff2cc89800120c31cbd748668eb6b734444b34436ee`.

`lxml-6.1.3/src/lxml/etree.c` lines 181260–181275 (GitHub mapping not verified in saved evidence)

```
 *         if pos > start:             # <<<<<<<<<<<<<<
 *             substrings.append(text[start:pos])
 *         substrings.append(escape)
*/
    __pyx_t_16 = (__pyx_v_pos > __pyx_v_start);
    if (__pyx_t_16) {

      /* "src/lxml/serializer.pxi":1246
 *             substrings = []
 *         if pos > start:
 *             substrings.append(text[start:pos])             # <<<<<<<<<<<<<<
 *         substrings.append(escape)
 *         start = pos + 1
*/
      if (unlikely(__pyx_v_substrings == Py_None)) {
        PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
```

Closing lines 181281–181286 (GitHub mapping not verified in saved evidence)

```
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      /* "src/lxml/serializer.pxi":1245
 *         if substrings is None:
 *             substrings = []
 *         if pos > start:             # <<<<<<<<<<<<<<
```

Original reviewed range 181260–181286 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0047: __pyx_f_4lxml_5etree__escape_attrib_c14n

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_text. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/etree.c:181369–181369`; SHA-256 `cff9439b818e1a6faf210ff2cc89800120c31cbd748668eb6b734444b34436ee`.

`lxml-6.1.3/src/lxml/etree.c` lines 181351–181366 (GitHub mapping not verified in saved evidence)

```
 *     if pos >= start:             # <<<<<<<<<<<<<<
 *         substrings.append(text[start:pos+1])
 *     return ''.join(substrings)
*/
  __pyx_t_16 = (__pyx_v_pos >= __pyx_v_start);
  if (__pyx_t_16) {

    /* "src/lxml/serializer.pxi":1253
 *         return text
 *     if pos >= start:
 *         substrings.append(text[start:pos+1])             # <<<<<<<<<<<<<<
 *     return ''.join(substrings)
 * 
*/
    if (unlikely(__pyx_v_substrings == Py_None)) {
      PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "append");
```

Closing lines 181372–181377 (GitHub mapping not verified in saved evidence)

```
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

    /* "src/lxml/serializer.pxi":1252
 *     if substrings is None:
 *         return text
 *     if pos >= start:             # <<<<<<<<<<<<<<
```

Original reviewed range 181351–181377 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0048: __pyx_f_4lxml_4html_4diff_tag_name_of_chunk

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_chunk. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/html/diff.c:9411–9411`; SHA-256 `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`.

`lxml-6.1.3/src/lxml/html/diff.c` lines 9393–9408 (GitHub mapping not verified in saved evidence)

```
    /* "lxml/html/diff.py":311
 *         if ch == '/':
 *             start_pos = 2
 *         elif ch == '>':             # <<<<<<<<<<<<<<
 *             return chunk[start_pos:i]
 *         elif ch.isspace():
*/
    __pyx_t_2 = (__pyx_v_ch == 62);
    if (__pyx_t_2) {

      /* "lxml/html/diff.py":312
 *             start_pos = 2
 *         elif ch == '>':
 *             return chunk[start_pos:i]             # <<<<<<<<<<<<<<
 *         elif ch.isspace():
 *             return chunk[start_pos:i]
```

Closing lines 9414–9419 (GitHub mapping not verified in saved evidence)

```
      __pyx_t_11 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      goto __pyx_L0;

      /* "lxml/html/diff.py":311
 *         if ch == '/':
```

Original reviewed range 9393–9419 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0049: __pyx_f_4lxml_4html_4diff_tag_name_of_chunk

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_chunk. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/html/diff.c:9445–9445`; SHA-256 `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`.

`lxml-6.1.3/src/lxml/html/diff.c` lines 9427–9442 (GitHub mapping not verified in saved evidence)

```
    /* "lxml/html/diff.py":313
 *         elif ch == '>':
 *             return chunk[start_pos:i]
 *         elif ch.isspace():             # <<<<<<<<<<<<<<
 *             return chunk[start_pos:i]
 * 
*/
    __pyx_t_2 = __Pyx_Py_UNICODE_ISSPACE(__pyx_v_ch); if (unlikely(__pyx_t_2 == ((int)-1))) __PYX_ERR(0, 313, __pyx_L1_error)
    if (__pyx_t_2) {

      /* "lxml/html/diff.py":314
 *             return chunk[start_pos:i]
 *         elif ch.isspace():
 *             return chunk[start_pos:i]             # <<<<<<<<<<<<<<
 * 
 *     return chunk[start_pos:]
```

Closing lines 9448–9453 (GitHub mapping not verified in saved evidence)

```
      __pyx_t_11 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      goto __pyx_L0;

      /* "lxml/html/diff.py":313
 *         elif ch == '>':
```

Original reviewed range 9427–9453 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

## K0050: __pyx_f_4lxml_4html_4diff_tag_name_of_chunk

**Disposition:** static use; `wrapper_call`; `generated_cython`.

**Kind:** dynamic_1_2_4; expression `PyUnicode_KIND(text)`.

**Input:** `PyUnicode_1BYTE_DATA(text) + clamped_start*PyUnicode_KIND(text)` — existing_python_fsr. text is wrapper argument __pyx_v_chunk. Existing Python string storage is borrowed for the substring conversion.

**Length:** `clamped_stop - clamped_start`; codepoint_elements.

**Confirmed:** Actual generated wrapper invocation; exact provider in same file copies a fixed-width slice.

**Inference / unresolved:** The API is reached for nonempty proper slices; full/empty slices return references. Dynamic kind includes non-ASCII-capable widths where permitted by caller input.

**Upstream representation coupling:** Upstream representation depends on the target implementation and its selected input/control-flow branch; see the linked implementation case IDs.

**Migration implication:** Requires adapting the common substring provider or materializing fixed-width data under a UTF-8 migration.

**Activation / tracing:** Statically verified invocation; no runtime frequency claim. Limited API/provider guards and empty/full fast paths can bypass the target.

**Source:** `lxml-6.1.3/src/lxml/html/diff.c:9472–9472`; SHA-256 `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`.

`lxml-6.1.3/src/lxml/html/diff.c` lines 9454–9469 (GitHub mapping not verified in saved evidence)

```
 *             return chunk[start_pos:i]
 *         elif ch.isspace():             # <<<<<<<<<<<<<<
 *             return chunk[start_pos:i]
 * 
*/
    }
    __pyx_L6:;
  }
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  /* "lxml/html/diff.py":316
 *             return chunk[start_pos:i]
 * 
 *     return chunk[start_pos:]             # <<<<<<<<<<<<<<
 * 
 * if not cython.compiled:
```

Closing lines 9475–9480 (GitHub mapping not verified in saved evidence)

```
  __pyx_t_11 = 0;
  goto __pyx_L0;

  /* "lxml/html/diff.py":299
 * 
 * 
```

Original reviewed range 9454–9480 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA-256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.
