# aiocsv 1.4.1

This page separates API expressions, wrapper consumers, emitted calls and non-use context. All counts are static source sites, not executions.

## K0157: Parser_save_field

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `self->field_so_far + offset` — constructed codepoint array. Py_UCS4 heap field buffer filled by Parser_add_char. skipinitialspace selects leading-whitespace-trimmed suffix; other branch whole field. Field length reset only after constructor returns.

**Length:** `self->field_so_far_len - offset`; Py_UCS4 codepoint elements.

**Confirmed:** Exact retained source snippet included (aiocsv-1.4.1/aiocsv/_parser.c:390–409) Buffer type/element length (aiocsv-1.4.1/aiocsv/_parser.c:144–160) Allocation, append and trim (aiocsv-1.4.1/aiocsv/_parser.c:360–388) Upstream Python Unicode read API (aiocsv-1.4.1/aiocsv/_parser.c:464–479)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Parser_get_char_and_increment_line_num reads buffer_str at buffer_idx; parser states append selected scalars to owned field_so_far. UTF8 migration must address upstream character traversal separately from constructor.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Two static target callsites in mutually exclusive whitespace branches. Output constructor copies input; owned field buffer reused.

**Source:** `aiocsv-1.4.1/aiocsv/_parser.c:401–402`; SHA-256 `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`.

`aiocsv-1.4.1/aiocsv/_parser.c` lines 390–405 ([verified immutable source](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L390-L405))

```
static int Parser_save_field(Parser* self) {
    // Ensure parser has a list
    if (!self->record_so_far) {
        self->record_so_far = PyList_New(0);
        if (!self->record_so_far) return 0;
    }

    // Convert field_so_far to a PyUnicode object
    PyObject* field = NULL;
    if (self->dialect.skipinitialspace) {
        Py_ssize_t offset = find_first_non_space(self->field_so_far, self->field_so_far_len);
        field = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, self->field_so_far + offset,
                                          self->field_so_far_len - offset);
    } else {
        field = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, self->field_so_far,
                                          self->field_so_far_len);
```

Closing lines 406–409 ([verified immutable source](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L406-L409))

```
    }
    if (!field) return 0;

    self->field_so_far_len = 0;
```

Original reviewed range 390–409 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9c/18/bc63651e9d716f388678d5bf58fc004dd719a623b0ca7f4f401573883a89/aiocsv-1.4.1.tar.gz); archive SHA-256 `bb663f9eabf88402ca2c325fd0df836eee7da34cf7c5476b5e6cf7d098cdebda`.

## K0158: Parser_save_field

**Disposition:** static use; `direct_api_call`; `handwritten`.

**Kind:** fixed_4; expression `PyUnicode_4BYTE_KIND`.

**Input:** `self->field_so_far` — constructed codepoint array. Py_UCS4 heap field buffer filled by Parser_add_char. skipinitialspace selects leading-whitespace-trimmed suffix; other branch whole field. Field length reset only after constructor returns.

**Length:** `self->field_so_far_len`; Py_UCS4 codepoint elements.

**Confirmed:** Exact retained source snippet included (aiocsv-1.4.1/aiocsv/_parser.c:390–409) Buffer type/element length (aiocsv-1.4.1/aiocsv/_parser.c:144–160) Allocation, append and trim (aiocsv-1.4.1/aiocsv/_parser.c:360–388) Upstream Python Unicode read API (aiocsv-1.4.1/aiocsv/_parser.c:464–479)

**Inference / unresolved:** Migration implication is conditional on retaining an element-buffer construction API; a UTF8 representation does not make these buffers UTF8 bytes. Preserve validation and surrogate semantics. Static source evidence does not measure conversion costs or runtime activation.

**Upstream representation coupling:** Parser_get_char_and_increment_line_num reads buffer_str at buffer_idx; parser states append selected scalars to owned field_so_far. UTF8 migration must address upstream character traversal separately from constructor.

**Migration implication:** The constructor can consume this integer-element buffer and encode a UTF-8 internal result; API compatibility must preserve codepoint and surrogate behavior. Immediate buffer provenance alone does not establish independence from upstream Unicode APIs.

**Activation / tracing:** Two static target callsites in mutually exclusive whitespace branches. Output constructor copies input; owned field buffer reused.

**Source:** `aiocsv-1.4.1/aiocsv/_parser.c:404–405`; SHA-256 `898b2e32de28a0918756ae4f81b36c3450629d8da31867084fc6b7d97c1fba54`.

`aiocsv-1.4.1/aiocsv/_parser.c` lines 390–405 ([verified immutable source](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L390-L405))

```
static int Parser_save_field(Parser* self) {
    // Ensure parser has a list
    if (!self->record_so_far) {
        self->record_so_far = PyList_New(0);
        if (!self->record_so_far) return 0;
    }

    // Convert field_so_far to a PyUnicode object
    PyObject* field = NULL;
    if (self->dialect.skipinitialspace) {
        Py_ssize_t offset = find_first_non_space(self->field_so_far, self->field_so_far_len);
        field = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, self->field_so_far + offset,
                                          self->field_so_far_len - offset);
    } else {
        field = PyUnicode_FromKindAndData(PyUnicode_4BYTE_KIND, self->field_so_far,
                                          self->field_so_far_len);
```

Closing lines 406–409 ([verified immutable source](https://github.com/MKuranowski/aiocsv/blob/0f73ceeb6bfe2ad9e8dbd4202e4abc7a054600ec/aiocsv/_parser.c#L406-L409))

```
    }
    if (!field) return 0;

    self->field_so_far_len = 0;
```

Original reviewed range 390–409 is recorded in `data/sites.json`; public excerpts are bounded.

[Frozen source distribution](https://files.pythonhosted.org/packages/9c/18/bc63651e9d716f388678d5bf58fc004dd719a623b0ca7f4f401573883a89/aiocsv-1.4.1.tar.gz); archive SHA-256 `bb663f9eabf88402ca2c325fd0df836eee7da34cf7c5476b5e6cf7d098cdebda`.
