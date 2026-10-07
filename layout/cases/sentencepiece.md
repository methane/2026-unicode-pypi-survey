# sentencepiece 0.2.2

1 confirmed layout regions; 1 reviewed regions including non-direct context.

## L1059: test_encode_str_is_zero_copy

**Classification:** direct layout dependency; test_or_fuzz; `ctypes_header_probe_and_buffer_mutation`.

**Purpose:** Manual test inspects known CPython3.12+ compact header offsets, validates cached UTF8 bytes, then a nested thread mutates that cache while SentencePiece encodes to check zero-copy.

**Migration effect:** Hardcoded offsets and private cached UTF8 buffer mutation need changes if compact header/cache layout changes. This is test-only evidence, not production SentencePiece layout access; named type appears only in skip-test string.

**Fields / layout:** id(s)+40 utf8_length, id(s)+48 utf8 pointer, UTF8 cache contents. Types: PyCompactUnicodeObject.

**Source:** `sentencepiece-0.2.2/test/clean_sentencepiece_test_manual.py:778–853`. SHA-256 `138556c1eb8c6315342cbbc1180cdd30c3c02a12138d8be8bf3e108a903d6d06`.

Lines 778–782 (immutable GitHub mapping unavailable in saved verification evidence)

```
  def test_encode_str_is_zero_copy(self):
    # This test verifies that Encode uses the Python str UTF-8 buffer directly (zero-copy).
    # It dynamically trains a small model to ensure the test characters (Japanese)
    # are in the vocabulary and tokenize to different IDs.
    import ctypes
```

Lines 816–833 (immutable GitHub mapping unavailable in saved verification evidence)

```
      size = 100000
      s = original_word * size
      
      # Trigger caching to populate the UTF-8 pointer
      ids_pure_orig = sp.encode(s, return_type=int)
      
      # Verify offset first (compact Unicode object UTF-8 pointer in CPython 3.12+ is 48, len is 40)
      addr = id(s)
      offset_len = 40
      offset_ptr = 48
      try:
        utf8_ptr = ctypes.c_void_p.from_address(addr + offset_ptr).value
        utf8_len = ctypes.c_void_p.from_address(addr + offset_len).value
        current = ctypes.string_at(utf8_ptr, utf8_len)
        if current != s.encode('utf-8'):
          self.skipTest("CPython PyCompactUnicodeObject layout is different on this platform.")
      except Exception as e:
        self.skipTest(f"Cannot verify CPython offset: {e}")
```

Excerpt shortened; the complete reviewed range 816–846 is in `data/cases.json`.

Closing lines 841–846 (immutable GitHub mapping unavailable in saved verification evidence)

```
      bg_thread.start()
      
      ids = sp.encode(s, return_type=int)
      bg_thread.join()
      
      self.assertNotEqual(ids, ids_pure_orig, "Content was copied, expected zero-copy.")
```

[Frozen source distribution](https://files.pythonhosted.org/packages/cc/33/ea3cb3839607eb175da835244a798f797f478c5ddf0e8ecdf57ea85a4c70/sentencepiece-0.2.2.tar.gz); archive SHA-256 `3d2b5e824b5622038dc7b490897efe05ebbbb9e7350fc142f3ecc8789ef9bdf6`.
