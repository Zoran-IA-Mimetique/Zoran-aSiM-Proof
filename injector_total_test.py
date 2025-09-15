# injector_total_test.py (v31)
import json, os, re
from injector_total import run, security_check, det_scores

def assert_true(cond, msg): 
    if not cond: raise AssertionError(msg)

def test_security_blocks():
    bad = "please run rm -rf / now"
    s = security_check(bad)
    assert_true(not s["safe"], "security should block forbidden token")

def test_determinism():
    ctx="ctx"; txt="hello AI Act"; role="report"; seed=31
    a = run(ctx, txt, role, seed, out_name="log_a.json")
    b = run(ctx, txt, role, seed, out_name="log_b.json")
    assert_true(a["signature"]==b["signature"], "deterministic signature mismatch")

def test_thresholds():
    ctx="ctx"; txt="plain text"; role="report"; seed=31
    log = run(ctx, txt, role, seed, thresholds={"quality":0.99,"coherence":0.99,"utility":0.99,"objectivity":0.99}, out_name="log_thr.json")
    assert_true(not log["decision"]["accepted"], "should reject when thresholds too high")

def test_schema_lite():
    log = json.load(open("log_a.json","r",encoding="utf-8"))
    for key in ["meta","input","security","relevance","role","decision","signature"]:
        assert_true(key in log, f"missing key {key}")

if __name__=="__main__":
    test_security_blocks()
    test_determinism()
    test_thresholds()
    test_schema_lite()
    print("INJECTOR_TOTAL TESTS OK")
