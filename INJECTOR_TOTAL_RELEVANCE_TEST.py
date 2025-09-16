from injector_total_full import run
def test_security_blocks():
    log=run("ctx","rm -rf /","report",seed=45,out="log_sec.json")
    assert not log["decision"]["accepted"]
def test_relevance_thresholds():
    log=run("define","definition is ...","report",seed=45,out="log_rel.json")
    assert log["decision"]["accepted"]
if __name__=="__main__":
    test_security_blocks(); test_relevance_thresholds(); print("injector total basic tests OK")
