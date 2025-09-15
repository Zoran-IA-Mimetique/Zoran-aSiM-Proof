# README_GLYPHNET (v20)
Usage:
```python
from glyphnet_codec import encode, decode
msg = encode("hello")
assert decode(msg) == "hello"
```
CLI-ish:
```python
from glyphnet_codec import encode_to_str, decode_from_str
s = encode_to_str("data"); assert decode_from_str(s) == "data"
```
