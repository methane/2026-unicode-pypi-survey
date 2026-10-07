# aiocsv — non-simple Unicode reads

[All packages](README.md)

Version: 1.4.1. **2 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`Dialect_init`](#case-001)
- [`Parser_get_char_and_increment_line_num`](#case-002)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `Dialect_init`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, a scalar or single-character check. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Character initialization macros read index0 of delimiter/quotechar/escapechar values; count one consuming function, not two forwarding macro definitions.

The single-character or scalar check is counted as B because it is not a complete traversal. A read at one fixed position does not demonstrate unrestricted random indexing.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9c/18/bc63651e9d716f388678d5bf58fc004dd719a623b0ca7f4f401573883a89/aiocsv-1.4.1.tar.gz). Archive SHA-256: `bb663f9eabf88402ca2c325fd0df836eee7da34cf7c5476b5e6cf7d098cdebda`.

**Function source:** `aiocsv-1.4.1/aiocsv/_parser.c`, lines 251–260. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`.

[Verified immutable function link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L251-L260).

### Read sites

- Site 1: lines 251–259; macro scalar; index expression `0`. dialect_init_char and dialect_init_optional_char expand ReadChar at 197 and 213.

### Contextual source excerpts

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 251–260. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L251-L260).

```c
int Dialect_init(Dialect* d, PyObject* o) {
    dialect_init_char(d, o, delimiter);
    dialect_init_optional_char(d, o, quotechar);
    dialect_init_optional_char(d, o, escapechar);
    dialect_init_quoting(d, o);
    dialect_init_bool(d, o, doublequote);
    dialect_init_bool(d, o, skipinitialspace);
    dialect_init_bool(d, o, strict);
    return 1;
}
```

### Callee analysis

- `dialect_init_char / dialect_init_optional_char` in `aiocsv-1.4.1/aiocsv/_parser.c`, lines 194–222: ReadChar(attr_name,0), with API error propagated. B scalar index0

Available source context:

- [`dialect_init_char / dialect_init_optional_char`](#helper-001) (`aiocsv-1.4.1/aiocsv/_parser.c`, lines 194–222).

<a id="case-002"></a>

## 2. `Parser_get_char_and_increment_line_num`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

Reads saved buffer_idx rather than a zero-start full loop. Caller may stop at record boundary and reread same index when DECISION_DONE_WITHOUT_CONSUMING; resumed calls start partway.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/9c/18/bc63651e9d716f388678d5bf58fc004dd719a623b0ca7f4f401573883a89/aiocsv-1.4.1.tar.gz). Archive SHA-256: `bb663f9eabf88402ca2c325fd0df836eee7da34cf7c5476b5e6cf7d098cdebda`.

**Function source:** `aiocsv-1.4.1/aiocsv/_parser.c`, lines 464–480. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`.

[Verified immutable function link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L464-L480).

### Read sites

- Site 1: lines 464–479; saved index; index expression `self->buffer_idx`. Bounded read from persistent parser state.

### Contextual source excerpts

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 464–479. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L464-L479).

```c
static Py_UCS4 Parser_get_char_and_increment_line_num(Parser* self) {
    assert(self->buffer_str);
    assert(self->buffer_idx < PyUnicode_GET_LENGTH(self->buffer_str));
    Py_UCS4 c = PyUnicode_READ_CHAR(self->buffer_str, self->buffer_idx);

    if (c == '\r') {
        ++self->line_num;
        self->last_char_was_cr = true;
    } else if (c == '\n') {
        self->line_num += !self->last_char_was_cr;  // increment if not part of a CRLF
        self->last_char_was_cr = false;
    } else {
        self->last_char_was_cr = false;
    }

    return c;
```

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 482–485. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L482-L485).

```c
static Decision Parser_process_char_in_eat_newline(Parser* self, Py_UCS4 c) {
    self->state = STATE_START_RECORD;
    return c == '\n' ? DECISION_DONE : DECISION_DONE_WITHOUT_CONSUMING;
}
```

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 625–642. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L625-L642).

```c
static PyObject* Parser_try_parse(Parser* self) {
    Decision decision = DECISION_CONTINUE;
    while (decision == DECISION_CONTINUE && Parser_has_char(self)) {
        Py_UCS4 c = Parser_get_char_and_increment_line_num(self);
        decision = Parser_process_char(self, c);

        if (decision == DECISION_ERROR) {
            if (!PyErr_Occurred()) {
                PyErr_Format(PyExc_SystemError,
                             "Parser_process_char (state %d) returned DECISION_ERROR without "
                             "setting an exception",
                             (int)self->state);
            }
            return NULL;
        }

        if (decision != DECISION_DONE_WITHOUT_CONSUMING) ++self->buffer_idx;
    }
```

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 684–716. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L684-L716).

```c
static int Parser_finalize_read(Parser* self, PyObject* unicode) {
    int result = 1;

    // Clear any existing str
    self->buffer_idx = 0;
    if (self->buffer_str) {
        Py_DECREF(self->buffer_str);
        self->buffer_str = NULL;
    }

    // Ensure the result is a valid unicode object in canonical form
    if (!PyUnicode_Check(unicode)) {
        PyErr_Format(PyExc_TypeError, "reader.read() returned %R, expected str", Py_TYPE(unicode));
        FINISH_WITH(0);
    }

#if PY_VERSION_HEX < 0x030C0000
    // PyUnicode_READY is a guaranteed no-op starting with 3.12, but before that other
    // modules may produce strings using the deprecated path that requires preparation.
    if (PyUnicode_READY(unicode)) {
        FINISH_WITH(0);
    }
#endif

    Py_ssize_t len = PyUnicode_GET_LENGTH(unicode);
    assert(len >= 0);
    if (len == 0) {
        // No more data - hit EOF
        self->eof = true;
    } else {
        // More data - move it to buffer_str
        self->buffer_str = unicode;
        unicode = NULL;
```

### Callee analysis

- `Parser_try_parse` in `aiocsv-1.4.1/aiocsv/_parser.c`, lines 625–654: Increments buffer_idx except DONE_WITHOUT_CONSUMING. May reread a character on next record request.
- `Parser_finalize_read` in `aiocsv-1.4.1/aiocsv/_parser.c`, lines 684–716: Sets buffer_idx=0 for a new chunk. Forward within each chunk, but paused/repeated index accesses.

Available source context:

- [`Parser_try_parse`](#helper-002) (`aiocsv-1.4.1/aiocsv/_parser.c`, lines 625–654).
- [`Parser_finalize_read`](#helper-003) (`aiocsv-1.4.1/aiocsv/_parser.c`, lines 684–716).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `dialect_init_char / dialect_init_optional_char`

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 194–222. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L194-L222).

```c
#define dialect_init_char(d, o, attr_name)                                                  \
    PyObject* attr_name = PyObject_GetAttrString((o), #attr_name);                          \
    if (attr_name) {                                                                        \
        (d)->attr_name = PyUnicode_ReadChar(attr_name, 0);                                  \
        if (PyErr_Occurred()) {                                                             \
            Py_DECREF(attr_name);                                                           \
            return 0;                                                                       \
        }                                                                                   \
    } else {                                                                                \
        PyErr_SetString(PyExc_AttributeError, "dialect has no attribute '" #attr_name "'"); \
        return 0;                                                                           \
    }                                                                                       \
    Py_DECREF(attr_name);

#define dialect_init_optional_char(d, o, attr_name)                                         \
    PyObject* attr_name = PyObject_GetAttrString((o), #attr_name);                          \
    if (attr_name == Py_None) {                                                             \
        (d)->attr_name = NO_CHAR;                                                           \
    } else if (attr_name) {                                                                 \
        (d)->attr_name = PyUnicode_ReadChar(attr_name, 0);                                  \
        if (PyErr_Occurred()) {                                                             \
            Py_DECREF(attr_name);                                                           \
            return 0;                                                                       \
        }                                                                                   \
    } else {                                                                                \
        PyErr_SetString(PyExc_AttributeError, "dialect has no attribute '" #attr_name "'"); \
        return 0;                                                                           \
    }                                                                                       \
    Py_DECREF(attr_name);
```

<a id="helper-002"></a>

### 2. `Parser_try_parse`

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 625–654. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L625-L654).

```c
static PyObject* Parser_try_parse(Parser* self) {
    Decision decision = DECISION_CONTINUE;
    while (decision == DECISION_CONTINUE && Parser_has_char(self)) {
        Py_UCS4 c = Parser_get_char_and_increment_line_num(self);
        decision = Parser_process_char(self, c);

        if (decision == DECISION_ERROR) {
            if (!PyErr_Occurred()) {
                PyErr_Format(PyExc_SystemError,
                             "Parser_process_char (state %d) returned DECISION_ERROR without "
                             "setting an exception",
                             (int)self->state);
            }
            return NULL;
        }

        if (decision != DECISION_DONE_WITHOUT_CONSUMING) ++self->buffer_idx;
    }

    if (decision != DECISION_CONTINUE || (self->eof && !state_is_end_of_record(self->state))) {
        if (self->dialect.strict && state_is_unexpected_at_eof(self->state)) {
            PyErr_SetString(parser_get_module_state(self)->csv_error, "unexpected end of data");
            return NULL;
        }

        Parser_add_field_at_eof(self);
        return Parser_extract_record(self);
    }
    return NULL;
}
```

<a id="helper-003"></a>

### 3. `Parser_finalize_read`

Archive member `aiocsv-1.4.1/aiocsv/_parser.c`, lines 684–716. Member SHA-256: `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`. [Verified immutable source link](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L684-L716).

```c
static int Parser_finalize_read(Parser* self, PyObject* unicode) {
    int result = 1;

    // Clear any existing str
    self->buffer_idx = 0;
    if (self->buffer_str) {
        Py_DECREF(self->buffer_str);
        self->buffer_str = NULL;
    }

    // Ensure the result is a valid unicode object in canonical form
    if (!PyUnicode_Check(unicode)) {
        PyErr_Format(PyExc_TypeError, "reader.read() returned %R, expected str", Py_TYPE(unicode));
        FINISH_WITH(0);
    }

#if PY_VERSION_HEX < 0x030C0000
    // PyUnicode_READY is a guaranteed no-op starting with 3.12, but before that other
    // modules may produce strings using the deprecated path that requires preparation.
    if (PyUnicode_READY(unicode)) {
        FINISH_WITH(0);
    }
#endif

    Py_ssize_t len = PyUnicode_GET_LENGTH(unicode);
    assert(len >= 0);
    if (len == 0) {
        // No more data - hit EOF
        self->eof = true;
    } else {
        // More data - move it to buffer_str
        self->buffer_str = unicode;
        unicode = NULL;
```
