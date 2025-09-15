# v33 quick tests
from injector_total import run, seccheck
import json, os
def test_sec():
    assert not seccheck("rm -rf /")["safe"]
def test_det():
    a=run("ctx","hello AI Act","report",seed=33,out="log_a.json")
    b=run("ctx","hello AI Act","report",seed=33,out="log_b.json")
    assert a["signature"]==b["signature"]
def test_thr():
    log=run("c","t","report",seed=33,thr={"quality":0.99,"coherence":0.99,"utility":0.99,"objectivity":0.99},out="log_thr.json")
    assert not log["decision"]["accepted"]
if __name__=="__main__":
    test_sec(); test_det(); test_thr(); print("injector_total v33 tests OK")
