# lxml: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#lxml)

Compiled cleanup_delete invokes mark_unbalanced/tag_name_of_chunk on valid long opening-tag chunks; tag-name extraction reads only through first whitespace or >, yielding a short name while preserving original long chunk in a list. A tag with short name and arbitrarily long nonASCII attributes supports cheap accepted prefix work across independent calls. Objectify also publishes registered int/float type_check functions; invalid first character can reject early, valid numeric text is fully scanned.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## diff.py: 299–315

Public caller and tag-prefix source

Archive member: `lxml-6.1.3/src/lxml/html/diff.py`

Member SHA256: `65ad01cbec9e6254048d4bbb9bbc4a076f3c90a8b2f15052e604f444f39a158d`

[Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
@cython.cfunc
def tag_name_of_chunk(chunk: str) -> str:
    i: cython.Py_ssize_t
    ch: cython.Py_UCS4

    if chunk[0] != '<':
        return ""

    start_pos = 1
    for i, ch in enumerate(chunk):
        if ch == '/':
            start_pos = 2
        elif ch == '>':
            return chunk[start_pos:i]
        elif ch.isspace():
            return chunk[start_pos:i]

```

## diff.c: 9683–9699

Actual public method binding/call chain, compiled tag reader and scoped provider

Archive member: `lxml-6.1.3/src/lxml/html/diff.c`

Member SHA256: `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`

[Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
static PyObject *__pyx_pw_4lxml_4html_4diff_27cleanup_delete(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_4lxml_4html_4diff_26cleanup_delete, " Cleans up any DEL_START/DEL_END markers in the document, replacing\n    them with <del></del>.  To do this while keeping the document\n    valid, it may need to drop some tags (either start or end tags).\n\n    It may also move the del into adjacent tags to try to move it to a\n    similar location where it was originally located (e.g., moving a\n    delete into preceding <div> tag, if the del looks like (DEL_START,\n    'Text</div>', DEL_END)\n    ");
static PyMethodDef __pyx_mdef_4lxml_4html_4diff_27cleanup_delete = {"cleanup_delete", (PyCFunction)(void(*)(void))(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_4lxml_4html_4diff_27cleanup_delete, __Pyx_METH_FASTCALL|METH_KEYWORDS, __pyx_doc_4lxml_4html_4diff_26cleanup_delete};
static PyObject *__pyx_pw_4lxml_4html_4diff_27cleanup_delete(PyObject *__pyx_self, 
#if CYTHON_METH_FASTCALL
PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
) {
  PyObject *__pyx_v_chunks = 0;
```

## diff.c: 11199–11214

Actual public method binding/call chain, compiled tag reader and scoped provider

Archive member: `lxml-6.1.3/src/lxml/html/diff.c`

Member SHA256: `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`

[Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
 *         name = tag_name_of_chunk(chunk)             # <<<<<<<<<<<<<<
 *         if name in empty_tags:
 *             marked.append(('b', chunk))
*/
    if (unlikely(__pyx_v_chunk == Py_None)) {
      PyErr_SetString(PyExc_TypeError, "cannot pass None into a C function argument that is declared 'not None'");
      __PYX_ERR(0, 495, __pyx_L1_error)
    }
    __pyx_t_4 = __pyx_f_4lxml_4html_4diff_tag_name_of_chunk(__pyx_v_chunk); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 495, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_XDECREF_SET(__pyx_v_name, ((PyObject*)__pyx_t_4));
    __pyx_t_4 = 0;

    /* "lxml/html/diff.py":496
 * 
 *         name = tag_name_of_chunk(chunk)
```

## diff.c: 9338–9347

Actual public method binding/call chain, compiled tag reader and scoped provider

Archive member: `lxml-6.1.3/src/lxml/html/diff.c`

Member SHA256: `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`

[Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_v_chunk);
  __pyx_t_4 = __pyx_v_chunk;
  __pyx_t_9 = __Pyx_init_unicode_iteration(__pyx_t_4, (&__pyx_t_6), (&__pyx_t_7), (&__pyx_t_8)); if (unlikely(__pyx_t_9 == ((int)-1))) __PYX_ERR(0, 308, __pyx_L1_error)
  for (__pyx_t_10 = 0; __pyx_t_10 < __pyx_t_6; __pyx_t_10++) {
    __pyx_t_5 = __pyx_t_10;
    __pyx_v_ch = __Pyx_PyUnicode_READ(__pyx_t_8, __pyx_t_7, __pyx_t_5);

    /* "lxml/html/diff.py":309
 *     start_pos = 1
```

## diff.c: 25402–25414

Actual public method binding/call chain, compiled tag reader and scoped provider

Archive member: `lxml-6.1.3/src/lxml/html/diff.c`

Member SHA256: `ba831e039c691f9b67805cc1aba80ca85d3d64f1d4ec3e2b303d4642d16eeb5c`

[Frozen sdist](https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-6.1.3.tar.gz); archive SHA256 `45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21`.

No verified permanent repository link for this range; use the frozen archive and member hash above.

```
static CYTHON_INLINE int __Pyx_init_unicode_iteration(
    PyObject* ustring, Py_ssize_t *length, void** data, int *kind) {
#if CYTHON_COMPILING_IN_LIMITED_API
    *kind   = 0;
    *length = PyUnicode_GetLength(ustring);
    *data   = (void*)ustring;
#else
    if (unlikely(__Pyx_PyUnicode_READY(ustring) < 0)) return -1;
    *kind   = PyUnicode_KIND(ustring);
    *length = PyUnicode_GET_LENGTH(ustring);
    *data   = PyUnicode_DATA(ustring);
#endif
    return 0;
```
