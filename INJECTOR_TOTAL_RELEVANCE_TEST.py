# INJECTOR_TOTAL_RELEVANCE_TEST.py (v45)
from injector_total_full import run, seccheck, relevance_scores, decide
import json

def test_security_blocks():
    log=run("ctx","rm -rf /","report",seed=45,out="log_sec.json")
    assert not log["decision"]["accepted"] and "forbidden" in ",".join(log["decision"]["reasons"])

def test_relevance_threshold_accept():
    ctx="define plan"
    txt="Definition is ... Steps roadmap checklist sha"
    log=run(ctx, txt, "report", seed=45, thresholds={"quality":0.2,"coherence":0.2,"utility":0.2,"objectivity":0.2}, out="log_rel_ok.json")
    assert log["decision"]["accepted"]

def test_relevance_threshold_reject():
    ctx="define"
    txt="amazing!!! awesome!!! terrible???"
    log=run(ctx, txt, "report", seed=45, thresholds={"quality":0.9,"coherence":0.5,"utility":0.5,"objectivity":0.8}, out="log_rel_bad.json")
    assert not log["decision"]["accepted"]

def test_determinism():
    a=run("ctx","content","report",seed=45,out="log_a.json")
    b=run("ctx","content","report",seed=45,out="log_b.json")
    assert a["signature"]==b["signature"]

if __name__=="__main__":
    test_security_blocks(); test_relevance_threshold_accept(); test_relevance_threshold_reject(); test_determinism()
    print("INJECTOR TOTAL FULL tests OK")
