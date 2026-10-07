# pyahocorasick — non-simple Unicode reads

[All packages](README.md)

Version: 2.3.1. **5 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`automaton_find_all`](#case-001)
- [`automaton_items_create`](#case-002)
- [`automaton_search_iter_next`](#case-003)
- [`automaton_search_iter_long_next`](#case-004)
- [`trie_remove_word`](#case-005)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `automaton_find_all`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Read input.word[i] over caller-provided start/end range; returns matches through Python callbacks while retaining input pointer.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Python callbacks can run arbitrary code on same owner while FSR pointer remains borrowed; repeat-call/eviction getter design must preserve borrowed view lifetime.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz). Archive SHA-256: `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

**Function source:** `pyahocorasick-2.3.1/src/Automaton.c`, lines 653–719. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`.

[Verified immutable function link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L653-L719).

### Read sites

- Site 1: lines 687–713; range; index expression `i=start..end-1`. Codepoint-offset input range.

### Contextual source excerpts

Omitted from `pyahocorasick-2.3.1/src/Automaton.c`: lines 673–689, 703–715. The original contextual region was lines 669–718.

Archive member `pyahocorasick-2.3.1/src/Automaton.c`, lines 669–672. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L669-L672).

```c
    // arg 1
    if (!prepare_input_from_tuple(self, args, 0, &input)) {
        return NULL;
    }
```

Archive member `pyahocorasick-2.3.1/src/Automaton.c`, lines 690–702. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L690-L702).

```c
        return NULL;
    }

    state = automaton->root;
    for (i=start; i < end; i++) {
        state = tmp = ahocorasick_next(state, automaton->root, input.word[i]);

        // return output
        while (tmp) {
            if (tmp->eow) {
                if (automaton->store == STORE_ANY)
                    callback_ret = F(PyObject_CallFunction)(callback, "iO", i, tmp->output.object);
                else
```

Archive member `pyahocorasick-2.3.1/src/Automaton.c`, lines 716–718. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L716-L718).

```c

    destroy_input(&input);
    Py_RETURN_NONE;
```


<a id="case-002"></a>

## 2. `automaton_items_create`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check, mixed access patterns. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Wildcard argument scalar tmp[0], plus raw prefix pointer handed to iterator constructor for bulk copy.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

arg1/arg2 can be same Unicode object: second pymod_get_string call must not invalidate first borrowed view.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz). Archive SHA-256: `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

**Function source:** `pyahocorasick-2.3.1/src/Automaton.c`, lines 722–848. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`.

[Verified immutable function link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L722-L848).

### Read sites

- Site 1: lines 740–775; scalar and handoff; index expression `tmp[0]; word[0:wordlen]`. Requires wildcard length1; prefix copied later.

### Contextual source excerpts

Omitted from `pyahocorasick-2.3.1/src/Automaton.c`: lines 744–766. The original contextual region was lines 740–778.

Archive member `pyahocorasick-2.3.1/src/Automaton.c`, lines 740–743. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L740-L743).

```c
    // arg 1: prefix/prefix pattern
    if (args)
        arg1 = F(PyTuple_GetItem)(args, 0);
    else
```

Archive member `pyahocorasick-2.3.1/src/Automaton.c`, lines 767–778. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L767-L778).

```c
        if (arg2 == NULL) {
            goto error;
        } else {
            if (len == 1) {
                wildcard = tmp[0];
                use_wildcard = true;
            }
            else {
                PyErr_SetString(PyExc_ValueError, "Wildcard must be a single character.");
                goto error;
            }
        }
```

Archive member `pyahocorasick-2.3.1/src/Automaton.c`, lines 819–828. Member SHA-256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L819-L828).

```c
    //
    iter = (AutomatonItemsIter*)automaton_items_iter_new(
                    automaton,
                    word,
                    wordlen,
                    use_wildcard,
                    wildcard,
                    matchtype);

    maybe_decref(word_is_copy, arg1)
```

### Callee analysis

- `automaton_items_iter_new` in `pyahocorasick-2.3.1/src/AutomatonItemsIter.c`, lines 70–78: memcpy pattern from word (borrowed DATA4/UCS4Copy). C bulk copy; later B pattern depth indexing

Available source context:

- [`automaton_items_iter_new`](#helper-001) (`pyahocorasick-2.3.1/src/AutomatonItemsIter.c`, lines 70–78).

<a id="case-003"></a>

## 3. `automaton_search_iter_next`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Input word read at persistent iter->index constrained by caller start/end; resumed iteration starts partway. Optional whitespace check reads same index before automaton transition.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

PEP393 Unicode branch uses UCS4 codepoints; legacy VARIABLE_LEN_CHARCODES path handled separately. Owner incref retained until iterator destruction.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz). Archive SHA-256: `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

**Function source:** `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`, lines 244–300. Member SHA-256: `c0e94d24881f38281da0e9a23d7a21741244b5f03ae958400b470a6a0c76da51`.

[Verified immutable function link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L244-L300).

### Read sites

- Site 1: lines 263–295; persistent index; index expression `iter->index`. Forward range traversal across next() calls; whitespace condition may reread first nonspace index.

### Contextual source excerpts

Omitted from `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`: lines 247–264, 276, 286–289. The original contextual region was lines 243–298.

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`, lines 243–246. Member SHA-256: `c0e94d24881f38281da0e9a23d7a21741244b5f03ae958400b470a6a0c76da51`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L243-L246).

```c
static PyObject*
automaton_search_iter_next(PyObject* self) {
    PyObject* output;

```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`, lines 265–275. Member SHA-256: `c0e94d24881f38281da0e9a23d7a21741244b5f03ae958400b470a6a0c76da51`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L265-L275).

```c
    if (!automaton_search_iter_advance_index(self)) {
        return NULL;
    }
#else
    iter->index += 1;
    if (iter->ignore_white_space) {
        while ((iter->index < iter->end) and iswspace(iter->input.word[iter->index])) {
            iter->index += 1;
        }
    }
#endif
```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`, lines 277–285. Member SHA-256: `c0e94d24881f38281da0e9a23d7a21741244b5f03ae958400b470a6a0c76da51`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L277-L285).

```c
        // process single char
        iter->state = ahocorasick_next(
                        iter->state,
                        iter->automaton->root,
                        iter->input.word[iter->index]
                        );

        ASSERT(iter->state);

```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIter.c`, lines 290–298. Member SHA-256: `c0e94d24881f38281da0e9a23d7a21741244b5f03ae958400b470a6a0c76da51`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIter.c#L290-L298).

```c
        if (!automaton_search_iter_advance_index(self)) {
            return NULL;
        }
#else
        iter->index += 1;
#endif

    } // while

```


<a id="case-004"></a>

## 4. `automaton_search_iter_long_next`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking, lookahead or lookbehind, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Longest nonoverlapping matcher resets input index to last_index after lookahead and fail_index on failover, plus repeated same-index edge checks.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Source explicitly says quadratic worst-case when restart at last_index; start/end provided in iterator constructor. Retained pointer lifetime spans next() calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz). Archive SHA-256: `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

**Function source:** `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`, lines 90–170. Member SHA-256: `7680d82a91c47fb22c98ca76057f6a84704df5cb00024f2db8f54e52455b6abb`.

[Verified immutable function link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIterLong.c#L90-L170).

### Read sites

- Site 1: lines 102–141; index reset; index expression `iter->index=last_index/fail_index; word[index]`. Restarts after best match or failover.
- Site 2: lines 142–163; same index retry; index expression `word[iter->index]`. Retries fail edges using same codepoint.

### Contextual source excerpts

Omitted from `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`: lines 94–105, 115–123, 133–136, 146. The original contextual region was lines 90–170.

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`, lines 90–93. Member SHA-256: `7680d82a91c47fb22c98ca76057f6a84704df5cb00024f2db8f54e52455b6abb`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIterLong.c#L90-L93).

```c
automaton_search_iter_long_next(PyObject* self) {
    PyObject* output = NULL;
    TrieNode* next;
    TrieNode* fail_node = NULL; //< the node to fail over
```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`, lines 106–114. Member SHA-256: `7680d82a91c47fb22c98ca76057f6a84704df5cb00024f2db8f54e52455b6abb`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIterLong.c#L106-L114).

```c

        // start over, as we don't want overlapped results
        // Note: this leads to quadratic complexity in the worst case
        iter->state      = iter->automaton->root;
        iter->index      = iter->last_index;

        iter->last_node  = NULL;
        iter->last_index = -1;

```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`, lines 124–132. Member SHA-256: `7680d82a91c47fb22c98ca76057f6a84704df5cb00024f2db8f54e52455b6abb`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIterLong.c#L124-L132).

```c
            fail_node = NULL;
            fail_index = -1;
            fail_flag = false;
        } else {
            next = trienode_get_next(iter->state, iter->input.word[iter->index]);
        }
        if (next) {
            if (next->eow) {
                // save the last node on the path
```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`, lines 137–145. Member SHA-256: `7680d82a91c47fb22c98ca76057f6a84704df5cb00024f2db8f54e52455b6abb`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIterLong.c#L137-L145).

```c
                fail_index = iter->index;
            }

            iter->state = next;
            iter->index += 1;
        } else {
            if (iter->last_node) {
                goto return_output;
            } else {
```

Archive member `pyahocorasick-2.3.1/src/AutomatonSearchIterLong.c`, lines 147–170. Member SHA-256: `7680d82a91c47fb22c98ca76057f6a84704df5cb00024f2db8f54e52455b6abb`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonSearchIterLong.c#L147-L170).

```c
                  // failover
                  fail_flag = true;
                  continue;
                }
                while (true) {
                    iter->state = iter->state->fail;
                    if (iter->state == NULL) {
                        iter->state = iter->automaton->root;
                        iter->index += 1;
                        break;
                    } else if (trienode_get_next(iter->state, iter->input.word[iter->index])) {
                        break;
                    }
                }
            }
        }
    } // while 

    if (iter->last_node) {
        goto return_output;
    }
    
    return NULL;    // StopIteration
}
```


<a id="case-005"></a>

## 5. `trie_remove_word`

**Classification:** B. **Subtypes:** multiple passes, a subset starting after position zero, arbitrary or fixed-position indexing. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

First forward search records last branch; removal then rereads word[last_multiway_index] and a suffix starting last_multiway_index+1.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz). Archive SHA-256: `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

**Function source:** `pyahocorasick-2.3.1/src/trie.c`, lines 67–136. Member SHA-256: `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`.

[Verified immutable function link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L67-L136).

### Read sites

- Site 1: lines 84–98; first pass; index expression `i=0..wordlen-1`. Find last multiway trie node.
- Site 2: lines 107–129; suffix replay; index expression `last_multiway_index; i=last_multiway_index+1..wordlen-1`. Rereads suffix to delete path.

### Contextual source excerpts

Omitted from `pyahocorasick-2.3.1/src/trie.c`: lines 71–79, 90–103, 126. The original contextual region was lines 67–129.

Archive member `pyahocorasick-2.3.1/src/trie.c`, lines 67–70. Member SHA-256: `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L67-L70).

```c
trie_remove_word(Automaton* automaton, const TRIE_LETTER_TYPE* word, const size_t wordlen) {

    PyObject* object;
    TrieNode* node;
```

Archive member `pyahocorasick-2.3.1/src/trie.c`, lines 80–89. Member SHA-256: `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L80-L89).

```c
    node = automaton->root;

    last_multiway = node;
    last_multiway_index = 0;
    for (i=0; i < wordlen; i++) {
        const TRIE_LETTER_TYPE letter = word[i];

        node = trienode_get_next(node, letter);
        if (node == NULL) {
            return NULL;
```

Archive member `pyahocorasick-2.3.1/src/trie.c`, lines 104–125. Member SHA-256: `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L104-L125).

```c
    object = node->output.object;

    if (trienode_is_leaf(node)) {
        // Remove a linear list that starts at the last_multiway node
        // and ends at the last [found] one.

        // 1. Unlink the tail from the trie
        node = trienode_get_next(last_multiway, word[last_multiway_index]);
        ASSERT(node != NULL);

        if (UNLIKELY(trienode_unset_next_pointer(last_multiway, node) == MEMORY_ERROR)) {
            PyErr_NoMemory();
            return NULL;
        }

        // 2. Free the tail (reference to value from the last element was already saved)
        for (i = last_multiway_index + 1; i < wordlen; i++) {
            tmp = trienode_get_next(node, word[i]);
            ASSERT(tmp->n <= 1);
            trienode_free(node);
            node = tmp;
        }
```

Archive member `pyahocorasick-2.3.1/src/trie.c`, lines 127–129. Member SHA-256: `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L127-L129).

```c
        trienode_free(node);

    } else {
```


<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `automaton_items_iter_new`

Archive member `pyahocorasick-2.3.1/src/AutomatonItemsIter.c`, lines 70–78. Member SHA-256: `b010104775bbe531e249bfa36c00b9b7fe60e14bf1c939245916e805613524c3`. [Verified immutable source link](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/AutomatonItemsIter.c#L70-L78).

```c
    if (word) {
        iter->pattern = (TRIE_LETTER_TYPE*)memory_alloc(wordlen * TRIE_LETTER_SIZE);
        if (UNLIKELY(iter->pattern == NULL)) {
            goto no_memory;
        }
        else {
            iter->pattern_length = wordlen;
            memcpy(iter->pattern, word, wordlen * TRIE_LETTER_SIZE);
        }
```
