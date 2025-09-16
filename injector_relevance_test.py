from injector_relevance import relevance_scores, decide
def test_basic():
    s=relevance_scores("define audit","definition is ... with evidence and sha")
    d=decide(s,{"quality":0.1,"coherence":0.1,"utility":0.1,"objectivity":0.1})
    assert d["accepted"]
if __name__=="__main__":
    test_basic(); print("relevance tests OK")
