# oracledb — non-simple Unicode reads

[All packages](README.md)

Version: 26.0.1. **24 B function records.** The count includes scalar checks and range continuations where present; overlapping subtypes are not additional function counts.

## Contents

- [`BaseParser.get_current_char`](#case-001)
- [`BaseParser.parse_keyword`](#case-002)
- [`BaseParser.parse_quoted_string`](#case-003)
- [`BaseParser.skip_spaces`](#case-004)
- [`ConnectStringParser._parse_descriptor_key_value_pair`](#case-005)
- [`ConnectStringParser._parse_easy_connect_host`](#case-006)
- [`ConnectStringParser._parse_easy_connect_hosts`](#case-007)
- [`ConnectStringParser._parse_easy_connect_parameter`](#case-008)
- [`ConnectStringParser._parse_easy_connect_parameters`](#case-009)
- [`ConnectStringParser._parse_easy_connect_port`](#case-010)
- [`ConnectStringParser._parse_easy_connect_protocol`](#case-011)
- [`ConnectStringParser._parse_easy_connect_service_name`](#case-012)
- [`ConnectStringParser._parse_easy_connect_instance_name`](#case-013)
- [`ConnectStringParser.parse`](#case-014)
- [`TnsnamesFileParser._skip_to_end_of_line`](#case-015)
- [`TnsnamesFileParser._parse_key`](#case-016)
- [`TnsnamesFileParser._parse_value_part`](#case-017)
- [`NameParser.parse_simple_sql_name`](#case-018)
- [`is_qualified_sql_name`](#case-019)
- [`StatementParser._parse_bind_name`](#case-020)
- [`StatementParser._parse_multiple_line_comment`](#case-021)
- [`StatementParser._parse_qstring`](#case-022)
- [`StatementParser._parse_single_line_comment`](#case-023)
- [`StatementParser.parse`](#case-024)
- [Shared callee excerpts](#callee-excerpts)

<a id="case-001"></a>

## 1. `BaseParser.get_current_char`

**Classification:** B. **Subtypes:** caller-provided start or range, arbitrary or fixed-position indexing. **Early exit recorded:** no.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** primitive helper.

Reads caller-managed cursor temp_pos, which can start partway and be reset by parser helpers.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** No risk was identified in this case.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L176-L181).

### Read sites

- Site 1: lines 181–181; derived read; index expression `self.temp_pos`. Stateful arbitrary cursor

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L176-L181).

```cython
    cdef Py_UCS4 get_current_char(self):
        """
        Returns the current character in the data being parsed. This method
        assumes that the end of the stream has not been encountered.
        """
        return cpython.PyUnicode_READ(self.data_kind, self.data, self.temp_pos)
```


<a id="case-002"></a>

## 2. `BaseParser.parse_keyword`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 194–205. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L194-L205).

### Read sites

- Site 1: lines 200–200; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 194–205. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L194-L205).

```cython
    cdef int parse_keyword(self) except -1:
        """
        Parse a keyword from the data to parse.
        """
        cdef Py_UCS4 ch
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not cpython.Py_UNICODE_ISALPHA(ch) \
                    and not cpython.Py_UNICODE_ISDIGIT(ch) \
                    and ch != '_' and ch != '.':
                break
            self.temp_pos += 1
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-003"></a>

## 3. `BaseParser.parse_quoted_string`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 207–224. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L207-L224).

### Read sites

- Site 1: lines 215–215; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 207–224. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L207-L224).

```cython
    cdef int parse_quoted_string(self, Py_UCS4 quote_type,
                                 bint raise_exception=True) except -1:
        """
        Parses a quoted string with the given quote type. All characters until
        the quote type is detected are discarded.
        """
        cdef Py_UCS4 ch
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            self.temp_pos += 1
            if ch == quote_type:
                self.pos = self.temp_pos
                return 0
        if raise_exception:
            if quote_type == "'":
                errors._raise_err(errors.ERR_MISSING_ENDING_SINGLE_QUOTE)
            else:
                errors._raise_err(errors.ERR_MISSING_ENDING_DOUBLE_QUOTE)
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-004"></a>

## 4. `BaseParser.skip_spaces`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 226–235. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L226-L235).

### Read sites

- Site 1: lines 232–232; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 226–235. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L226-L235).

```cython
    cdef int skip_spaces(self) except -1:
        """
        Skip any spaces that are present in the string.
        """
        cdef Py_UCS4 ch
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not cpython.Py_UNICODE_ISSPACE(ch):
                break
            self.temp_pos += 1
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-005"></a>

## 5. `ConnectStringParser._parse_descriptor_key_value_pair`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 384–461. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L384-L461).

### Read sites

- Site 1: lines 409–409; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference
- Site 2: lines 418–418; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference
- Site 3: lines 451–451; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`: lines 388–404, 423–446, 456–458. The original contextual region was lines 384–461.

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 384–387. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L384-L387).

```cython
    cdef int _parse_descriptor_key_value_pair(self, dict args) except -1:
        """
        Parses a key-value pair from the connect string. At this point it is
        assumed that the character previously read was an opening parenthesis.
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 405–422. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L405-L422).

```cython

        # look for equals sign
        self.skip_spaces()
        if self.temp_pos < self.num_chars:
            ch = self.get_current_char()
        if ch != '=':
            errors._raise_err(errors.ERR_INVALID_CONNECT_DESCRIPTOR,
                              data=self.data_as_str)
        self.temp_pos += 1
        self.skip_spaces()

        # parse value
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch == '"':
                if is_simple_value:
                    errors._raise_err(errors.ERR_INVALID_CONNECT_DESCRIPTOR,
                                      data=self.data_as_str)
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 447–455. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L447-L455).

```cython
        if is_simple_value:
            value = self.data_as_str[start_pos:self.temp_pos].strip()
        self.skip_spaces()
        if self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch != ')':
                errors._raise_err(errors.ERR_INVALID_CONNECT_DESCRIPTOR,
                                  data=self.data_as_str)
            self.temp_pos += 1
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 459–461. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L459-L461).

```cython
        # store value in dictionary
        if value is not None:
            self._set_descriptor_arg(args, name, value)
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-006"></a>

## 6. `ConnectStringParser._parse_easy_connect_host`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 488–513. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L488-L513).

### Read sites

- Site 1: lines 497–497; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 488–513. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L488-L513).

```cython
    cdef int _parse_easy_connect_host(self, Address address) except -1:
        """
        Parses a host name from the easy connect string.
        """
        cdef:
            bint found_bracket = False, found_host = False
            ssize_t start_pos = self.temp_pos
            Py_UCS4 ch
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not found_bracket and not found_host and ch == '[':
                found_bracket = True
                start_pos = self.temp_pos + 1
            elif found_bracket and ch == ']':
                address.host = self.data_as_str[start_pos:self.temp_pos]
                self.temp_pos = self.temp_pos + 1
                self.pos = self.temp_pos
                break
            elif found_bracket or self._is_host_or_service_name_char(ch):
                self.temp_pos += 1
                found_host = True
            else:
                if found_host:
                    address.host = self.data_as_str[start_pos:self.temp_pos]
                    self.pos = self.temp_pos
                break
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-007"></a>

## 7. `ConnectStringParser._parse_easy_connect_hosts`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end. Cursor reset to committed self.pos before trial parse.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 515–554. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L515-L554).

### Read sites

- Site 1: lines 536–536; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference
- Site 2: lines 547–547; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`: lines 519–531, 541–542. The original contextual region was lines 515–554.

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 515–518. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L515-L518).

```cython
    cdef int _parse_easy_connect_hosts(self) except -1:
        """
        Parses the list of hosts from an easy connect string. This should be a
        series of host names separated by commas or semicolons.
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 532–540. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L532-L540).

```cython
            if self.temp_pos != self.pos or self.pos >= self.num_chars:
                break
            self.pos = self.temp_pos
            address_list.children.append(address)
            ch = self.get_current_char()
            if ch == ':':
                self.temp_pos += 1
                self._parse_easy_connect_port(address)
                self.pos = self.temp_pos
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 543–554. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L543-L554).

```cython
                for i in range(port_index, len(address_list.children) - 1):
                    temp_address = address_list.children[i]
                    temp_address.port = address.port
                port_index = len(address_list.children)
                ch = self.get_current_char()
            if ch == ';':
                address_list = AddressList()
                self.description.children.append(address_list)
                port_index = 0
            elif ch != ',':
                break
            self.temp_pos += 1
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-008"></a>

## 8. `ConnectStringParser._parse_easy_connect_parameter`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 556–622. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L556-L622).

### Read sites

- Site 1: lines 587–587; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference
- Site 2: lines 597–597; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`: lines 560–582, 592, 602–619. The original contextual region was lines 556–622.

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 556–559. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L556-L559).

```cython
    cdef int _parse_easy_connect_parameter(self) except -1:
        """
        Parses a single parameter from the easy connect string. This is
        expected to be a keyword followed by a value seprated by an equals
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 583–591. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L583-L591).

```cython
        # look for the equals sign
        self.skip_spaces()
        if self.temp_pos >= self.num_chars:
            return 0
        ch = self.get_current_char()
        if ch != '=':
            return 0
        self.temp_pos += 1

```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 593–601. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L593-L601).

```cython
        found_value = False
        self.skip_spaces()
        start_pos = self.temp_pos
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch == '"':
                # if the quote is not the first character in the value, this is
                # not a valid easy connect parameter
                if self.temp_pos > start_pos:
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 620–622. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L620-L622).

```cython
                self.parameters[name] = value
        self.skip_spaces()
        self.pos = self.temp_pos
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-009"></a>

## 9. `ConnectStringParser._parse_easy_connect_parameters`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end. Cursor reset to committed self.pos before trial parse.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 624–641. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L624-L641).

### Read sites

- Site 1: lines 636–636; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 624–641. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L624-L641).

```cython
    cdef int _parse_easy_connect_parameters(self) except -1:
        """
        Parses the parameters from the easy connect string. This is expected to
        be a question mark followed by a series of key-value pairs separated by
        ampersands.
        """
        cdef:
            Py_UCS4 ch, expected_sep
            Address address
        expected_sep = '?'
        self.temp_pos = self.pos
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch != expected_sep:
                break
            expected_sep = '&'
            self.temp_pos += 1
            self._parse_easy_connect_parameter()
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-010"></a>

## 10. `ConnectStringParser._parse_easy_connect_port`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 643–659. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L643-L659).

### Read sites

- Site 1: lines 653–653; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 643–659. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L643-L659).

```cython
    cdef int _parse_easy_connect_port(self, Address address) except -1:
        """
        Parses a port number from the easy connect string. This consists of one
        or more digits.
        """
        cdef:
            ssize_t pos = self.temp_pos
            bint found_port = False
            Py_UCS4 ch
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not cpython.Py_UNICODE_ISDIGIT(ch):
                break
            found_port = True
            self.temp_pos += 1
        if found_port:
            address.port = int(self.data_as_str[pos:self.temp_pos])
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-011"></a>

## 11. `ConnectStringParser._parse_easy_connect_protocol`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end. Cursor reset to committed self.pos before trial parse.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 661–694. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L661-L694).

### Read sites

- Site 1: lines 678–678; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 661–694. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L661-L694).

```cython
    cdef str _parse_easy_connect_protocol(self):
        """
        Parses the protocol from an easy connect string. This should be a
        series of alphanumeric characters, underscores or dashes, followed by a
        colon and two slashes. If such a string is found, it is saved on the
        template address associated with the parser; otherwise, the default
        protocol of "tcp" is saved on the template address associated with the
        parser. If no protocol is found, the separator (two slashes) may still
        be found and will be discarded.
        """
        cdef:
            ssize_t start_sep_pos = self.pos
            int num_sep_chars = 0
            str protocol = None
            Py_UCS4 ch
        self.temp_pos = self.pos
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch == ':':
                protocol = self.data_as_str[self.pos:self.temp_pos].lower()
                start_sep_pos = self.temp_pos + 1
            elif ch == '/' and self.temp_pos - start_sep_pos == num_sep_chars:
                num_sep_chars += 1
                if num_sep_chars == 2:
                    self.temp_pos += 1
                    self.pos = self.temp_pos
                    break
            elif not cpython.Py_UNICODE_ISALPHA(ch) \
                    and not cpython.Py_UNICODE_ISDIGIT(ch) \
                    and ch not in ('-', '_'):
                break
            self.temp_pos += 1
        if protocol is not None and num_sep_chars == 2:
            return protocol
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-012"></a>

## 12. `ConnectStringParser._parse_easy_connect_service_name`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end. Cursor reset to committed self.pos before trial parse.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 696–733. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L696-L733).

### Read sites

- Site 1: lines 710–710; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`: lines 700–705, 715–730. The original contextual region was lines 696–733.

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 696–699. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L696-L699).

```cython
    cdef str _parse_easy_connect_service_name(self):
        """
        Parses the service name from an easy connect string. This is expected
        to be a slash followed by a series of alphanumeric characters. If such
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 706–714. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L706-L714).

```cython
            Py_UCS4 ch
            str value
        self.temp_pos = self.pos
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not found_slash and ch == '/':
                found_slash = True
            elif found_service_name and not found_colon and ch == ':':
                found_colon = True
```

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 731–733. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L731-L733).

```cython
        if found_server_type:
            value = self.data_as_str[service_name_end_pos + 1:self.temp_pos]
            self.description.set_server_type(value)
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-013"></a>

## 13. `ConnectStringParser._parse_easy_connect_instance_name`

**Classification:** B. **Subtypes:** caller-provided start or range, reset or backtracking. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end. Cursor reset to committed self.pos before trial parse.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 735–761. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L735-L761).

### Read sites

- Site 1: lines 749–749; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 735–761. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L735-L761).

```cython
    cdef str _parse_easy_connect_instance_name(self):
        """
        Parses the instance name from an easy connect string. This is expected
        to be a slash followed by a series of alphanumeric characters. If such
        a string is found, it is returned.
        """
        cdef:
            ssize_t instance_name_end_pos = 0
            bint found_instance_name = False
            bint found_slash = False
            Py_UCS4 ch
            str value
        self.temp_pos = self.pos
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not found_slash and ch == '/':
                found_slash = True
            elif found_slash and self._is_host_or_service_name_char(ch):
                found_instance_name = True
                instance_name_end_pos = self.temp_pos + 1
            else:
                break
            self.temp_pos += 1
        if found_instance_name:
            self.description.instance_name = \
                    self.data_as_str[self.pos + 1:instance_name_end_pos]
            self.pos = self.temp_pos
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-014"></a>

## 14. `ConnectStringParser.parse`

**Classification:** B. **Subtypes:** arbitrary or fixed-position indexing, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Initial single read at0 chooses descriptor vs easy-connect parser; subsequent helper pipeline consumes token ranges.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 825–848. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L825-L848).

### Read sites

- Site 1: lines 838–838; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 825–848. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L825-L848).

```cython
    cdef int parse(self, str connect_string) except -1:
        """
        Parses a connect string. If the first character is an opening
        parenthesis, the connect string is assumed to be a connect descriptor
        and any failures to parse the string as a connect descriptor will
        result in an exception. If the connect string contains key elements
        identifying it as an easy connect string, any failures to parse the
        connect string as an easy connect string will result in an exception.
        If the connect string doesn't seem to be either option, the value None
        is returned.
        """
        cdef Py_UCS4 ch
        self.initialize(connect_string)
        ch = self.get_current_char()
        if ch == '(':
            self.temp_pos += 1
            self._parse_descriptor()
        else:
            self._parse_easy_connect()
        if self.description_list is not None and self.pos != self.num_chars:
            if self.pos > 0:
                errors._raise_err(errors.ERR_CANNOT_PARSE_CONNECT_STRING,
                                  data=connect_string)
            self.description_list = None
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-015"></a>

## 15. `TnsnamesFileParser._skip_to_end_of_line`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 853–865. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L853-L865).

### Read sites

- Site 1: lines 860–860; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 853–865. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L853-L865).

```cython
    cdef int _skip_to_end_of_line(self) except -1:
        """
        Skips all characters until the next line break is found and then
        discards all whitespace after that.
        """
        cdef Py_UCS4 ch
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            self.temp_pos += 1
            if cpython.Py_UNICODE_ISLINEBREAK(ch):
                break
        self.pos = self.temp_pos
        self.skip_spaces()
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-016"></a>

## 16. `TnsnamesFileParser._parse_key`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 867–896. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L867-L896).

### Read sites

- Site 1: lines 881–881; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 867–896. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L867-L896).

```cython
    cdef str _parse_key(self):
        """
        Parses a key from the file and returns it. This consists of any number
        of non-whitespace characters until an equals sign is found. Any
        comments are discarded. If no characters are found before the equals
        sign, the line is discarded. Similarly, if an opening or closing
        parenthesis is discovered, the line is discarded.
        """
        cdef:
            bint found_key = False
            ssize_t start_pos = 0
            Py_UCS4 ch
        self.skip_spaces()
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch in ('(', ')', '#'):
                self._skip_to_end_of_line()
                found_key = False
                continue
            elif ch == '=':
                if not found_key:
                    self._skip_to_end_of_line()
                    continue
                self.temp_pos += 1
                self.pos = self.temp_pos
                return self.data_as_str[start_pos:self.temp_pos - 1].strip()
            elif not found_key:
                found_key = True
                start_pos = self.temp_pos
            self.temp_pos += 1
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-017"></a>

## 17. `TnsnamesFileParser._parse_value_part`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 898–931. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L898-L931).

### Read sites

- Site 1: lines 910–910; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 898–931. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L898-L931).

```cython
    cdef str _parse_value_part(self, ssize_t* num_parens):
        """
        Parses part of a value. This consists of all characters from the first
        non-whitespace character to the end of the value or the first comment.
        The number of parentheses are updated.
        """
        cdef:
            ssize_t start_pos = 0, end_pos = 0
            bint found_part = False
            Py_UCS4 ch
        self.skip_spaces()
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if ch == '#':
                end_pos = self.temp_pos
                self._skip_to_end_of_line()
                if found_part:
                    break
                continue
            if found_part and num_parens[0] == 0:
                if cpython.Py_UNICODE_ISLINEBREAK(ch):
                    end_pos = self.temp_pos
                    break
            elif ch == '(':
                num_parens[0] += 1
            elif ch == ')' and num_parens[0] > 0:
                num_parens[0] -= 1
            if not found_part:
                found_part = True
                start_pos = self.temp_pos
            self.temp_pos += 1
            end_pos = self.temp_pos
        if found_part:
            return self.data_as_str[start_pos:end_pos].strip()
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-018"></a>

## 18. `NameParser.parse_simple_sql_name`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 974–1006. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L974-L1006).

### Read sites

- Site 1: lines 985–985; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference
- Site 2: lines 997–997; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 974–1006. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L974-L1006).

```cython
    cdef bint parse_simple_sql_name(self) except *:
        """
        Parses a simple SQL name from the string and returns it. If no simple
        SQL name can be parsed, None is returned. A simple SQL name consists of
        a quoted value or an alphabetic character followed by any number of
        alphanumeric characters or one of the characters '_', '$' and '#'.
        """
        cdef:
            ssize_t start_pos
            Py_UCS4 ch
        if self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            self.temp_pos += 1
            if ch == '"':
                start_pos = self.temp_pos
                self.parse_quoted_string(ch, raise_exception=False)
                if self.pos <= start_pos:
                    return False
                elif self.temp_pos > start_pos + 1:
                    return True
            if cpython.Py_UNICODE_ISALPHA(ch):
                start_pos = self.temp_pos - 1
                while self.temp_pos < self.num_chars:
                    ch = self.get_current_char()
                    if not cpython.Py_UNICODE_ISALPHA(ch) \
                            and not cpython.Py_UNICODE_ISDIGIT(ch) \
                            and ch != '_' \
                            and ch != '$' \
                            and ch != '#':
                        break
                    self.temp_pos += 1
                return True
        return False
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-019"></a>

## 19. `is_qualified_sql_name`

**Classification:** B. **Subtypes:** caller-provided start or range, mixed access patterns. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** owning reader.

Reads get_current_char at caller/parser-managed temp_pos; consumes only the current token/range and may stop at a delimiter rather than traverse start0 through end. Mixes simple-name, whitespace and separator reads.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

BaseParser retains FSR pointer and original Python str in object across calls. Dedicated FSR getter must guarantee view lifetime; callbacks/hooks require view stability or reacquisition.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 1009–1032. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L1009-L1032).

### Read sites

- Site 1: lines 1024–1024; derived read; index expression `self.temp_pos via get_current_char`. Codepoint cursor dereference

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 1009–1032. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L1009-L1032).

```cython
def is_qualified_sql_name(str name):
    """
    Internal method for determining if a name is a qualified SQL name.
    """
    cdef:
        NameParser parser = NameParser.__new__(NameParser)
        bint found_db_link = False
        ssize_t num_parts = 0
        Py_UCS4 ch
    parser.initialize(name.strip())
    while parser.parse_simple_sql_name():
        num_parts += 1
        parser.skip_spaces()
        if parser.temp_pos == parser.num_chars:
            break
        ch = parser.get_current_char()
        parser.temp_pos += 1
        parser.skip_spaces()
        if not found_db_link and ch == '@':
            found_db_link = True
            num_parts = 0
        elif ch != '.':
            return False
    return num_parts > 0 and parser.temp_pos == parser.num_chars
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: PyUnicode_READ(self.data_kind,self.data,self.temp_pos) caller-managed codepoint index

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-020"></a>

## 20. `StatementParser._parse_bind_name`

**Classification:** B. **Subtypes:** caller-provided start or range, multiple passes. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Begins at pos+1, reads current bind token only; on delimiter commits pos=temp_pos-1 so outer parser revisits delimiter.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Inherits BaseParser.DATA/KIND capture and retains input str. Owning parser/helper reader; cursor codepoint offsets, original buffer lifetime across parser calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 62–112. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L62-L112).

### Read sites

- Site 1: lines 80–80; derived read; index expression `self.get_current_char() at self.temp_pos`. Begins at pos+1, reads current bind token only; on delimiter commits pos=temp_pos-1 so outer parser revisits delimiter.

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`: lines 66–75, 85–109. The original contextual region was lines 62–112.

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 62–65. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L62-L65).

```cython
    cdef int _parse_bind_name(self, Statement stmt) except -1:
        """
        Bind variables are identified as follows:
        - Quoted and non-quoted bind names are allowed.
```

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 76–84. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L76-L84).

```cython
            str bind_name
            Py_UCS4 ch
        self.temp_pos = self.pos + 1
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not in_bind:
                if cpython.Py_UNICODE_ISSPACE(ch):
                    self.temp_pos += 1
                    continue
```

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 110–112. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L110-L112).

```cython
            else:
                bind_name = stmt._sql[start_pos:self.temp_pos].upper()
            stmt._add_bind(bind_name)
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ retained DATA at temp_pos

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-021"></a>

## 21. `StatementParser._parse_multiple_line_comment`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Starts at pos+1, reads only comment after first slash until terminator or failed asterisk trial.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Inherits BaseParser.DATA/KIND capture and retains input str. Owning parser/helper reader; cursor codepoint offsets, original buffer lifetime across parser calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 114–139. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L114-L139).

### Read sites

- Site 1: lines 127–127; derived read; index expression `self.get_current_char() at self.temp_pos`. Starts at pos+1, reads only comment after first slash until terminator or failed asterisk trial.

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 114–139. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L114-L139).

```cython
    cdef int _parse_multiple_line_comment(self) except -1:
        """
        Multiple line comments consist of the characters /* followed by all
        characters up until */. This method is called when the first slash is
        detected and checks for the subsequent asterisk. If found, the comment
        is traversed and the current position is updated; otherwise, the
        current position is left untouched.
        """
        cdef:
            bint in_comment = False, exiting_comment = False
            Py_UCS4 ch
        self.temp_pos = self.pos + 1
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not in_comment:
                if ch != '*':
                    break
                in_comment = True
            elif ch == '*':
                exiting_comment = True
            elif exiting_comment:
                if ch == '/':
                    self.pos = self.temp_pos
                    break
                exiting_comment = False
            self.temp_pos += 1
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ retained DATA at temp_pos

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-022"></a>

## 22. `StatementParser._parse_qstring`

**Classification:** B. **Subtypes:** caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Starts after current quote, reads separator-delimited body until closing quote; token subset of original SQL.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Inherits BaseParser.DATA/KIND capture and retains input str. Owning parser/helper reader; cursor codepoint offsets, original buffer lifetime across parser calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 141–180. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L141-L180).

### Read sites

- Site 1: lines 158–158; derived read; index expression `self.get_current_char() at self.temp_pos`. Starts after current quote, reads separator-delimited body until closing quote; token subset of original SQL.

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`: lines 145–153, 163–177. The original contextual region was lines 141–180.

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 141–144. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L141-L144).

```cython
    cdef int _parse_qstring(self) except -1:
        """
        Parses a q-string which consists of the characters "q" and a single
        quote followed by a start separator, any text that does not contain the
```

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 154–162. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L154-L162).

```cython
            bint exiting_qstring = False, in_qstring = False
            Py_UCS4 ch, sep = 0
        self.temp_pos += 1
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not in_qstring:
                if ch == '[':
                    sep = ']'
                elif ch == '{':
```

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 178–180. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L178-L180).

```cython
                    exiting_qstring = False
            self.temp_pos += 1
        errors._raise_err(errors.ERR_MISSING_ENDING_SINGLE_QUOTE)
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ retained DATA at temp_pos

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-023"></a>

## 23. `StatementParser._parse_single_line_comment`

**Classification:** B. **Subtypes:** caller-provided start or range, lookahead or lookbehind. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Starts pos+1, checks second dash then reads until linebreak or end; token subset and early return.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Inherits BaseParser.DATA/KIND capture and retains input str. Owning parser/helper reader; cursor codepoint offsets, original buffer lifetime across parser calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 182–203. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L182-L203).

### Read sites

- Site 1: lines 195–195; derived read; index expression `self.get_current_char() at self.temp_pos`. Starts pos+1, checks second dash then reads until linebreak or end; token subset and early return.

### Contextual source excerpts

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 182–203. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L182-L203).

```cython
    cdef int _parse_single_line_comment(self) except -1:
        """
        Single line comments consist of two dashes and all characters up to the
        next line break (or the end of the data). This method is called when
        the first dash is detected and checks for the subsequent dash. If
        found, the single line comment is traversed and the current position is
        updated; otherwise, the current position is left untouched.
        """
        cdef:
            bint in_comment = False
            Py_UCS4 ch
        self.temp_pos = self.pos + 1
        while self.temp_pos < self.num_chars:
            ch = self.get_current_char()
            if not in_comment:
                if ch != '-':
                    return 0
                in_comment = True
            elif cpython.Py_UNICODE_ISLINEBREAK(ch):
                break
            self.temp_pos += 1
        self.pos = self.temp_pos
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ retained DATA at temp_pos

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="case-024"></a>

## 24. `StatementParser.parse`

**Classification:** B. **Subtypes:** mixed access patterns, multiple passes, caller-provided start or range. **Early exit recorded:** yes.

**Scope:** `fsr_read`; canonical-default included; handwritten source. **Origin:** `handwritten_candidate`.

**Role:** helper consumer.

Main forward SQL scan invokes token/quote/comment readers; bind-name helper returns pos=temp_pos-1, causing delimiter reread in outer loop; keyword/bind substrings also revisit prior ranges.

This function is B because of the access pattern described below. B alone does not prove that migration needs an FSR view: an iterator, retained cursor, buffering or an algorithm rewrite may cover some patterns.

**Offsets and character semantics:** codepoint indices in fixed-width PEP393 units

**FSR lifetime assessment:** A possible risk is recorded. This is not proof of an invalidation event; a future materializing or fallible getter must define buffer stability and owner lifetime.

Inherits BaseParser.DATA/KIND capture and retains input str. Owning parser/helper reader; cursor codepoint offsets, original buffer lifetime across parser calls.

**Archive:** [source distribution](https://files.pythonhosted.org/packages/8c/f3/22113415f48b6608ada31ebb46047b3b8ac361dba393d1b5ed1f768d8f6a/oracledb-26.0.1.tar.gz). Archive SHA-256: `786397a6b37e94ebfa6c1c6cd026755eb8fccfd39e15bcb64cb5879491882aef`.

**Function source:** `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 205–281. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`.

[Verified immutable function link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L205-L281).

### Read sites

- Site 1: lines 226–226; derived read; index expression `self.get_current_char() at self.temp_pos`. Main forward SQL scan invokes token/quote/comment readers; bind-name helper returns pos=temp_pos-1, causing delimiter reread in outer loop; keyword/bind substrings also revisit prior ranges.

### Contextual source excerpts

Omitted from `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`: lines 209–221, 231–278. The original contextual region was lines 205–281.

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 205–208. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L205-L208).

```cython
    cdef int parse(self, Statement stmt) except -1:
        """
        Parses the SQL stored in the statement in order to determine the
        keyword that identifies the type of SQL being executed as well as a
```

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 222–230. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L222-L230).

```cython

        # scan all characters in the string
        while self.pos < self.num_chars:
            self.temp_pos = self.pos
            ch = self.get_current_char()

            # look for certain keywords (initial keyword and the ones for
            # detecting DML returning statements
            is_alpha = cpython.Py_UNICODE_ISALPHA(ch)
```

Archive member `oracledb-26.0.1/src/oracledb/impl/thin/statement.pyx`, lines 279–281. Member SHA-256: `f2c02a4559e730c3d07f1a3c6bfd8743db8851bb42a020734745f0398735fde3`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/thin/statement.pyx#L279-L281).

```cython
            self.pos += 1
            last_was_alpha = is_alpha
            last_ch = ch
```

### Callee analysis

- `BaseParser.get_current_char` in `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181: Exact frozen sdist source recovered and manually inspected B PyUnicode_READ retained DATA at temp_pos

Available source context:

- [`BaseParser.get_current_char`](#helper-001) (`oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181).

<a id="callee-excerpts"></a>

## Shared callee excerpts

These excerpts are shared by the function records linked above. Each is reproduced once on this package page.

<a id="helper-001"></a>

### 1. `BaseParser.get_current_char`

Archive member `oracledb-26.0.1/src/oracledb/impl/base/parsers.pyx`, lines 176–181. Member SHA-256: `d01bca0b418ddd719c7e15a2c4445dba045d3366b24cff0acff2b9525244e262`. [Verified immutable source link](https://github.com/oracle/python-oracledb/blob/cf7d2aa8909543513d25b0fdbc5daa03031e5b17/src/oracledb/impl/base/parsers.pyx#L176-L181).

```cython
    cdef Py_UCS4 get_current_char(self):
        """
        Returns the current character in the data being parsed. This method
        assumes that the end of the stream has not been encountered.
        """
        return cpython.PyUnicode_READ(self.data_kind, self.data, self.temp_pos)
```
