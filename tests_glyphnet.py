# tests_glyphnet.py — roundtrip & corpus tests
from glyphnet_codec import encode, decode, encode_to_str, decode_from_str
import random, string

def rt(s): 
    return decode(encode(s))==s and decode_from_str(encode_to_str(s))==s

def test_roundtrip():
    s = "The quick brown fox jumps over the lazy dog"*5
    assert rt(s)

def test_mixed_corpus():
    rnd = "".join(random.choice(string.ascii_letters+" ") for _ in range(200))
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    assert rt(rnd) and rt(lorem)

if __name__=="__main__":
    test_roundtrip(); test_mixed_corpus(); print("GLYPHNET OK")
