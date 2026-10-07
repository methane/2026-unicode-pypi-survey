# pyahocorasick: lifetime witnesses

[Summary](../LIFETIME.md) · [Complete per-package reasoning](README.md#pyahocorasick)

Strong conditional borrowed-FSR repeat case: repeated exists/match/get/longest_prefix calls with same kind4 str cannot infer last future query from local Input destruction. Lease through one iterator solves that iterator lifetime but not unrelated synchronous future calls.

These are disjoint exact contextual source excerpts. Lines outside each stated range are omitted; no ellipsis or replacement text is inserted into the quoted source. They are static evidence, not executed tests.

## utils.c: 146–170

Kind4 borrowed ownership versus lower-kind owned copy; Input preparation/destruction.

Archive member: `pyahocorasick-2.3.1/src/utils.c`

Member SHA256: `65469c0f2300135739ecac734c3bc9784b5307cf3ec3f6bf45be945d0e24832c`

[Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz); archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

[Verified permanent source](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/utils.c#L146-L170).

```
pymod_get_string(PyObject* obj, TRIE_LETTER_TYPE** word, Py_ssize_t* wordlen, bool* is_copy) {

#ifdef INPUT_KEEPS_COPY
    Py_ssize_t i;
    char* bytes;
#endif

#if defined PEP393_UNICODE
    if (F(PyUnicode_Check)(obj)) {
    PyUnicode_READY(obj);
    if (PyUnicode_KIND(obj) == PyUnicode_4BYTE_KIND) {
            *word = (TRIE_LETTER_TYPE*)(PyUnicode_4BYTE_DATA(obj));
            *wordlen = PyUnicode_GET_LENGTH(obj);
            *is_copy = false;
            Py_INCREF(obj);

        return obj;
    } else {
        *word = PyUnicode_AsUCS4Copy(obj);
        *wordlen = PyUnicode_GET_LENGTH(obj);
        *is_copy = true;
        // No INCREF - we have our copy
        return obj;
    }
    }
```

## trie.c: 140–154

Missing edge ends find/longest at prefix.

Archive member: `pyahocorasick-2.3.1/src/trie.c`

Member SHA256: `e9864211483837edf684b5664f33792859b7f88ce733269c4c10548c967d60d5`

[Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz); archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

[Verified permanent source](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/trie.c#L140-L154).

```
trie_find(TrieNode* root, const TRIE_LETTER_TYPE* word, const size_t wordlen) {
    TrieNode* node;
    size_t i;

    node = root;

    if (node != NULL) {
        for (i=0; i < wordlen; i++) {
            node = trienode_get_next(node, word[i]);
            if (node == NULL)
                return NULL;
        }
    }

    return node;
```

## Automaton.c: 419–440

Synchronous providers release Input; selected-range find_all.

Archive member: `pyahocorasick-2.3.1/src/Automaton.c`

Member SHA256: `5a293c377174102861896a2f9d83c0f50a9f1aeca68417ae2019b18d7903938f`

[Frozen sdist](https://files.pythonhosted.org/packages/b0/3c/dc9e31a0f004eabe2ef5d31456766555a02e2af29e159daa31266934af79/pyahocorasick-2.3.1.tar.gz); archive SHA256 `9d0f6bb522237ed7f111ed59c9e8baea7d1e75813587b6773babd43bda35db9f`.

[Verified permanent source](https://github.com/WojciechMula/pyahocorasick/blob/4e28d29898f1019d9706485b2a06026466814d9d/src/Automaton.c#L419-L440).

```

static int
automaton_contains(PyObject* self, PyObject* args) {
#define automaton ((Automaton*)self)
    TrieNode* node;
    struct Input input;

    if (!prepare_input(self, args, &input)) {
        return -1;
    }

    node = trie_find(automaton->root, input.word, input.wordlen);

    destroy_input(&input);

    return (node and node->eow);
#undef automaton
}


static PyObject*
automaton_exists(PyObject* self, PyObject* args) {
```
