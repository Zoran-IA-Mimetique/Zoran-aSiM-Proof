from semantic_crypto_v37 import embed,detect
def test_gap():
    wm,_=embed("We start and end small big work","K")
    ok=detect(wm,"K"); bad=detect(wm,"wrong")
    assert ok['rate']>0.5 and bad['rate']<0.6
if __name__=='__main__': test_gap(); print('semcrypto tests OK')
