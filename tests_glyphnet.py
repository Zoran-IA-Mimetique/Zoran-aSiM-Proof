from glyphnet_codec import encode,decode
def test_roundtrip():
    s="The quick brown fox "*10
    assert decode(encode(s))==s
if __name__=="__main__":
    test_roundtrip(); print("glyphnet roundtrip OK")
