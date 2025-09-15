# bench_runner_all.py (v23)
import subprocess, json, os

def run(cmd, outfile=None):
    print("RUN", " ".join(cmd))
    p = subprocess.run(cmd, capture_output=True, text=True)
    if outfile and p.stdout:
        open(outfile,"w").write(p.stdout)
    return p.returncode

def main():
    results = {}
    if os.path.isfile("bench_glyphnet_vs_codecs.py"):
        run(["python","bench_glyphnet_vs_codecs.py"])
        if os.path.isfile("BENCH_GLYPHNET_REPORT.json"):
            results["glyphnet"] = json.load(open("BENCH_GLYPHNET_REPORT.json"))
    if os.path.isfile("multi_ia_demo.py"):
        for i in range(3):
            run(["python","multi_ia_demo.py"])
            os.rename("MULTI_IA_DEMO_LOG.json", f"MULTI_IA_DEMO_LOG_{i}.json")
        run(["python","analyze_multi_ia.py"])
        if os.path.isfile("MULTI_IA_STATS.json"):
            results["multi_ia"] = json.load(open("MULTI_IA_STATS.json"))
    json.dump(results, open("BENCH_RUNNER_ALL_RESULTS.json","w"), indent=2)
    print(json.dumps(results, indent=2))

if __name__=="__main__":
    main()
