# pyahocorasick 2.3.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0151: automaton_items_iter_next

**Disposition:** static use; `macro_dispatch_actual_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `(void *)(iter->buffer + 1)` — constructed codepoint array. Trie traversal writes letters at depth into uint32_t TRIE_LETTER_TYPE buffer; skip root slot0. Depth counts letters/elements, not bytes. KEY_STRING letters are codepoints; KEY_SEQUENCE can supply integer values, so do not assume every uint32_t is a valid Unicode codepoint.

**Length:** `depth`; uint32_t codepoint elements.

**Confirmed:** Exact retained source snippet included (pyahocorasick-2.3.1/src/AutomatonItemsIter.c:180–225) Iterator key buffer allocation (pyahocorasick-2.3.1/src/AutomatonItemsIter.c:26–60) Typed owned key buffer (pyahocorasick-2.3.1/src/AutomatonItemsIter.h:36–43) PEP393 and uint32_t/4-byte letter configuration (pyahocorasick-2.3.1/src/common.h:35–66) Normal versus fault F dispatch (pyahocorasick-2.3.1/src/common.h:90–94) Token-pasting fault macro (pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:1–5) Variadic forwarding provider (pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:50–55) Upstream Unicode key representation (pyahocorasick-2.3.1/src/utils.c:144–168) prepare_input dispatches Python key through pymod_get_string (pyahocorasick-2.3.1/src/utils.c:354–408) add_word input preparation and trie insertion (pyahocorasick-2.3.1/src/Automaton.c:202–258)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** KEY_STRING preparation accepts borrowed 4-byte FSR or converted UCS4 copy, then add_word inserts letters into trie. KEY_SEQUENCE instead supplies copied integer letters. Constructor reconstructs persisted trie letters into its own iterator buffer; it does not pass original key FSR.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Real macro-dispatch call F(PyUnicode_FromKindAndData)(...). ITER_KEYS and PEP393_UNICODE branch. Normal F(name)=name; injection F(name)=name##_custom forwards variadic args.

**Source:** `pyahocorasick-2.3.1/src/AutomatonItemsIter.c:126–225`; SHA-256 `b010104775bbe531e249bfa36c00b9b7fe60e14bf1c939245916e805613524c3`.

`pyahocorasick-2.3.1/src/AutomatonItemsIter.c` lines 180–195 ([verified immutable source](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonItemsIter.c#L180-L195))

```
            for (i=0; i < n; i++) {
                StackItem* new_item = (StackItem*)list_item_new(sizeof(StackItem));
                if (UNLIKELY(new_item == NULL)) {
                    PyErr_NoMemory();
                    return NULL;
                }

                new_item->node   = trienode_get_ith_unsafe(iter->state, i);
                new_item->letter = trieletter_get_ith_unsafe(iter->state, i);
                new_item->depth  = depth + 1;
                list_push_front(&iter->stack, (ListItem*)new_item);
            }
        }
        else {
            // process single letter
            TrieNode* node = trienode_get_next(iter->state, iter->pattern[depth]);
```

Closing lines 220–225 ([verified immutable source](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonItemsIter.c#L220-L225))

```
            PyObject* val;

            switch (iter->type) {
                case ITER_KEYS:
#if defined PEP393_UNICODE
                    return F(PyUnicode_FromKindAndData)(PyUnicode_4BYTE_KIND, (void*)(iter->buffer + 1), depth);
```

Original reviewed range 180–225 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz); archive SHA-256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

## K0152: PyUnicode_FromKindAndData_custom

**Disposition:** non-use context; `macro_forwarding_provider`; `handwritten`.

**Kind:** forwarded; expression `forwarded/dynamic; see snippets`.

**Input:** `__VA_ARGS__: data` — forwarded application arguments. Fault macro does not construct an independent buffer. Same fixed4 argument triple as iterator application call.

**Length:** `__VA_ARGS__: length`; forwarded codepoint element count.

**Confirmed:** Exact retained source snippet included (pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:1–5) Exact retained source snippet included (pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:50–55)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Input path described by confirmed evidence.

**Migration implication:** Provider forwards application arguments under optional fault mode; preserve interception/type inference when API contracts change. This is not a separate input construction algorithm.

**Activation / tracing:** Fault dispatch enabled by PYCALLS_INJECT_FAULTS && PY3K, otherwise F resolves original API. Error injection can suppress forwarding.

**Source:** `pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:53–53`; SHA-256 `954d913b176276141056cdd28865f9765134a5c440d7840b3aeb746e56498ebb`.

`pyahocorasick-2.3.1/src/pycallfault/pycallfault.h` lines 1–5 (GitHub mapping not verified in saved evidence)

```
#ifndef PYCALLFAULT_H_
#define PYCALLFAULT_H_

#define F(name) name##_custom

```

`pyahocorasick-2.3.1/src/pycallfault/pycallfault.h` lines 50–55 (GitHub mapping not verified in saved evidence)

```

#define PyNumber_Index_custom(arg) (check_and_set_error() ? NULL : PyNumber_Index(arg))

#define PyUnicode_FromKindAndData_custom(...) (check_and_set_error() ? NULL : PyUnicode_FromKindAndData(__VA_ARGS__))

#define PyUnicode_AsUTF8String_custom(...) (check_and_set_error() ? NULL : PyUnicode_AsUTF8String(__VA_ARGS__))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz); archive SHA-256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

## K0191: PyUnicode_FromKindAndData_custom; executable forwarding at line 53

**Disposition:** static use; `forwarding_api_call`; `test`.

**Kind:** forwarded; expression `forwarded/dynamic; see snippets`.

**Input:** `__VA_ARGS__: data` — forwarded application arguments. Fault macro does not construct an independent buffer. Same fixed4 argument triple as iterator application call.

**Length:** `__VA_ARGS__: length`; forwarded codepoint element count.

**Confirmed:** Exact retained source snippet included (pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:1–5) Exact retained source snippet included (pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:50–55)

**Inference / unresolved:** none recorded

**Upstream representation coupling:** Generic test instrumentation; application input is described at its concrete constructor site.

**Migration implication:** Provider forwards application arguments under optional fault mode; preserve interception/type inference when API contracts change. This is not a separate input construction algorithm.

**Activation / tracing:** Fault dispatch enabled by PYCALLS_INJECT_FAULTS && PY3K, otherwise F resolves original API. Error injection can suppress forwarding.

**Source:** `pyahocorasick-2.3.1/src/pycallfault/pycallfault.h:53–53`; SHA-256 `954d913b176276141056cdd28865f9765134a5c440d7840b3aeb746e56498ebb`.

`pyahocorasick-2.3.1/src/pycallfault/pycallfault.h` lines 53–53 (GitHub mapping not verified in saved evidence)

```
#define PyUnicode_FromKindAndData_custom(...) (check_and_set_error() ? NULL : PyUnicode_FromKindAndData(__VA_ARGS__))
```

[Frozen source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz); archive SHA-256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.
