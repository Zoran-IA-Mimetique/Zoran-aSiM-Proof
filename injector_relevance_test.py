# injector_relevance_test.py (v44)
from injector_relevance import relevance_scores, decide

def test_quality_subjective():
    s = relevance_scores("","This is amazing and fantastic!!")
    assert s["quality"] < 0.8

def test_coherence_overlap():
    s = relevance_scores("define audit", "This text includes a definition and an audit checklist")
    assert s["coherence"] > 0.2

def test_utility_intent():
    s = relevance_scores("plan", "Here are the steps: 1) do this 2) do that")
    assert s["utility"] >= 0.66

def test_objectivity_refs():
    s = relevance_scores("","JSON CSV SHA doi http")
    assert s["objectivity"] >= 0.7

def test_decision_thresholds():
    s = relevance_scores("define","definition is ...")
    d = decide(s, {"quality":0.1,"coherence":0.1,"utility":0.1,"objectivity":0.1})
    assert d["accepted"]

if __name__=="__main__":
    test_quality_subjective(); test_coherence_overlap(); test_utility_intent(); test_objectivity_refs(); test_decision_thresholds()
    print("injector_relevance tests OK")
