# tests_semantic_crypto.py (v36)
import os, json
from semantic_crypto import embed, detect

def test_determinism():
    key="K"
    base="We start to test and end this small work to show an idea and goal."
    a,_=embed(base,key)
    b,_=embed(base,key)
    assert a==b

def test_detection_gap():
    key="K"
    base="We start to test and end this small work to show an idea and goal."
    wm,_=embed(base,key)
    d_ok=detect(wm,key)
    d_bad=detect(wm,"wrong")
    assert d_ok["rate"]>0.6 and d_bad["rate"]<0.6

if __name__=="__main__":
    test_determinism(); test_detection_gap(); print("SEMANTIC CRYPTO TESTS OK")
