# gevent 26.9.0

18 confirmed layout regions; 18 reviewed regions including non-direct context.

## L0574: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_abstract_linkable.c:12331–12397`. SHA-256 `b244fa06ec2301f7a72795ff5ddad36b44ab237b3698269b03cff8c4cb52fbe1`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 12332–12349 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 12332–12382 is in `data/cases.json`.

Closing lines 12377–12382 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0575: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_greenlet_primitives.c:5040–5106`. SHA-256 `0bc4c6bd9374ced16cb4e5df3ba44558a9fdae6eb0593ad39761191a2599a36a`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 5041–5058 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 5041–5091 is in `data/cases.json`.

Closing lines 5086–5091 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0576: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_hub_primitives.c:11441–11507`. SHA-256 `c0a33ebd893abbb9c84e11ac9c7e31d225c728a8d8443fae985db6238199c6c3`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 11442–11459 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 11442–11492 is in `data/cases.json`.

Closing lines 11487–11492 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0577: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_imap.c:9423–9489`. SHA-256 `314d0c76edb4f3e51d9b1cb5e11020c7fc1053167a337daef020aa9c99053652`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 9424–9441 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 9424–9474 is in `data/cases.json`.

Closing lines 9469–9474 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0578: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_semaphore.c:11512–11578`. SHA-256 `ee03eb3809294ff35e33e75fdf0c7f3b95cd4f2937bdcd8d1045e262bcb1adff`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 11513–11530 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 11513–11563 is in `data/cases.json`.

Closing lines 11558–11563 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0579: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_tracer.c:8429–8495`. SHA-256 `d3552cb6a51b3285cbd4f6b0bcbb08b0563ca79b339809f3745b67d93fa1ce5e`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 8430–8447 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 8430–8480 is in `data/cases.json`.

Closing lines 8475–8480 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0580: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_waiter.c:6785–6851`. SHA-256 `0c5420b52f0ccd7a39434c26c634b7104fe751e8956a951b92ce544f95a91832`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 6786–6803 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 6786–6836 is in `data/cases.json`.

Closing lines 6831–6836 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0581: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/event.c:9398–9464`. SHA-256 `08f6350795ab8fefeac2422efffbfb299f5e31a1c8db1ef6ab7360b8b4f8e7ce`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 9399–9416 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 9399–9449 is in `data/cases.json`.

Closing lines 9444–9449 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0582: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/greenlet.c:25430–25496`. SHA-256 `70f2f5cea5e112badf4a7237713d5018f99cffc8ac9809473b8f415d268991bb`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 25431–25448 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 25431–25481 is in `data/cases.json`.

Closing lines 25476–25481 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0583: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/libev/corecext.c:27199–27265`. SHA-256 `d51d50e5d6e0ab7a033c7dc85c692be36e30715bfe2da5f348ed891eba9cb4cb`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 27200–27217 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 27200–27250 is in `data/cases.json`.

Closing lines 27245–27250 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0584: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/local.c:12140–12206`. SHA-256 `afcd26ac45d494464a8c3a5d8008c1ae1654cf1058b75017ca5019506a3c45ed`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 12141–12158 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 12141–12191 is in `data/cases.json`.

Closing lines 12186–12191 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0585: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/queue.c:23221–23287`. SHA-256 `6e51d7bc82add0ba9c63e44b84d9f4829ae6d03767e14ec6cb7a98cf12b3ca3e`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 23222–23239 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 23222–23272 is in `data/cases.json`.

Closing lines 23267–23272 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0586: __Pyx_MatchKeywordArg_str

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Keyword matching reads incoming key hash and precomputed argument-name hashes before equality/duplicate checks.

**Migration effect:** Cached-hash metadata coupling; character comparison helpers are separate API-based FSR context and do not make these named fields payload reads.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/resolver/cares.c:14654–14720`. SHA-256 `f74f768090b378b0968794b129de9e54654a801435cbc3a57843f5a8c6bcd7c3`.

**Activation / context:** CYTHON_USE_UNICODE_INTERNALS; API comparison path in other configurations.

Lines 14655–14672 (immutable GitHub mapping unavailable in saved verification evidence)

```
    PyObject *key,
    PyObject ** const argnames[],
    PyObject ** const *first_kw_arg,
    size_t *index_found,
    const char *function_name)
{
    PyObject ** const *name;
    #if CYTHON_USE_UNICODE_INTERNALS
    Py_hash_t key_hash = ((PyASCIIObject*)key)->hash;
    if (unlikely(key_hash == -1)) {
        key_hash = PyObject_Hash(key);
        if (unlikely(key_hash == -1))
            goto bad;
    }
    #endif
    name = first_kw_arg;
    while (*name) {
        PyObject *name_str = **name;
```

Excerpt shortened; the complete reviewed range 14655–14705 is in `data/cases.json`.

Closing lines 14700–14705 (immutable GitHub mapping unavailable in saved verification evidence)

```
        }
        #else
        #if CYTHON_ASSUME_SAFE_SIZE
        if (PyUnicode_GET_LENGTH(name_str) == PyUnicode_GET_LENGTH(key))
        #endif
        {
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0850: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Class namespace assignment passes private cached name hash to _PyDict_SetItem_KnownHash.

**Migration effect:** Private metadata coupling; regeneration can select normal dictionary API. Does not require codepoint layout.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_hub_local.c:887–888`. SHA-256 `0f1050a4e165b44f2c04bc57076c1cbd56467e34838958a63f9d2f20ba8cbad9`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000; Python3.13+ generated branch uses PyDict_SetItem.

Lines 880–896 (immutable GitHub mapping unavailable in saved verification evidence)

```
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static PyTypeObject *__Pyx_Get_CyFunction_Type(void);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* PyObjectCall2Args.proto (used by Py3ClassCreate) */
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L0851: __Pyx_SetNameInClass macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_metadata_read`.

**Purpose:** Class namespace assignment passes private cached name hash to _PyDict_SetItem_KnownHash.

**Migration effect:** Private metadata coupling; regeneration can select normal dictionary API. Does not require codepoint layout.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/resolver/cares.c:1316–1317`. SHA-256 `f74f768090b378b0968794b129de9e54654a801435cbc3a57843f5a8c6bcd7c3`.

**Activation / context:** CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000; Python3.13+ generated branch uses PyDict_SetItem.

Lines 1309–1325 (immutable GitHub mapping unavailable in saved verification evidence)

```
#define __Pyx_SetItemOnTypeDict(tp, k, v) __Pyx__SetItemOnTypeDict((PyTypeObject*)tp, k, v)

/* SetItemOnTypeDict.export */
static int __Pyx__SetItemOnTypeDict(PyTypeObject *tp, PyObject *k, PyObject *v);

/* SetNameInClass.proto (used by SetNewInClass) */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030d0000
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* SetNewInClass.proto */
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L1042: __Pyx__GetModuleGlobalName

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_read`.

**Purpose:** Generated Cython helper supplies the Unicode name cached hash to _PyDict_GetItem_KnownHash.

**Migration effect:** Generated runtime needs an updated cached-hash accessor if the Unicode header field changes; preserve as generated family, not handwritten application evidence.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_generated_include/GetModuleGlobalName_impl_8222c3ef3e98cb454364bff02f8f87d5421239b0e5243442497828f013d7762f.h:1–43`. SHA-256 `8222c3ef3e98cb454364bff02f8f87d5421239b0e5243442497828f013d7762f`.

Lines 21–38 (immutable GitHub mapping unavailable in saved verification evidence)

```
#elif CYTHON_AVOID_BORROWED_REFS || CYTHON_AVOID_THREAD_UNSAFE_BORROWED_REFS
    if (unlikely(__Pyx_PyDict_GetItemRef(__pyx_mstate_global->__pyx_d, name, &result) == -1)) {
        if (!__Pyx_IgnoreException(PyExc_Exception)) {
            return NULL; // BaseException
        }
    }
    __PYX_UPDATE_DICT_CACHE(__pyx_mstate_global->__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return result;
    }
#else
    result = _PyDict_GetItem_KnownHash(__pyx_mstate_global->__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_mstate_global->__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyObject *exc = PyErr_Occurred();
    if (unlikely(exc) && !__Pyx_IgnoreGivenException(exc, PyExc_Exception)) {
```

Excerpt shortened; the complete reviewed range 21–42 is in `data/cases.json`.

Closing lines 39–42 (immutable GitHub mapping unavailable in saved verification evidence)

```
        return NULL; // BaseException
    }
#endif
    return __Pyx_GetBuiltinName(name);
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L1043: __Pyx_PyDict_GetItemStrWithError macro

**Classification:** direct layout dependency; generated_distribution_code; `cached_hash_read`.

**Purpose:** Cython compatibility macro reads the cached Unicode name hash for known-hash dictionary lookup.

**Migration effect:** Update generated Cython compatibility code if cached-hash layout changes.

**Fields / layout:** hash. Types: PyASCIIObject.

**Source:** `gevent-26.9.0/src/gevent/_generated_include/PythonCompatibility_impl_d461987f0831f7886b9efe1daf595a4e05b454ed1c2035ff85faa33be8de9aa6.h:228–229`. SHA-256 `d461987f0831f7886b9efe1daf595a4e05b454ed1c2035ff85faa33be8de9aa6`.

Lines 228–229 (immutable GitHub mapping unavailable in saved verification evidence)

```
#if CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStrWithError(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.

## L1044: __Pyx_PyUnicode_IS_TRUE pre3.12 macro

**Classification:** direct layout dependency; generated_distribution_code; `legacy_metadata_read`.

**Purpose:** For CPython before3.12, fallback truth test reads compact wstr_length when canonical representation is not ready.

**Migration effect:** Legacy conditional branch depends on wstr_length/ready semantics; current3.12+ path uses public length API. Keep separate from active UTF-8 migration requirements.

**Fields / layout:** wstr_length. Types: PyCompactUnicodeObject.

**Source:** `gevent-26.9.0/src/gevent/_generated_include/PythonCompatibility_impl_d461987f0831f7886b9efe1daf595a4e05b454ed1c2035ff85faa33be8de9aa6.h:298–306`. SHA-256 `d461987f0831f7886b9efe1daf595a4e05b454ed1c2035ff85faa33be8de9aa6`.

Lines 298–306 (immutable GitHub mapping unavailable in saved verification evidence)

```
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
```

[Frozen source distribution](https://files.pythonhosted.org/packages/2b/ac/dd3137ae695aef399373088c84c66398f3eac597fba542f0a22280bc21d6/gevent-26.9.0.tar.gz); archive SHA-256 `4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1`.
