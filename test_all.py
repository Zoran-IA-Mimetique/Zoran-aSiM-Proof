# test_all.py (v32) — run all available tests
import os, subprocess, glob

def run(cmd):
    print("RUN", " ".join(cmd))
    return subprocess.run(cmd, check=False).returncode

def main():
    # injector total
    if os.path.isfile("injector_total_test.py"):
        run(["python","injector_total_test.py"])
    # glyphnet/hyper/quanta tests
    for f in ["tests_glyphnet.py","tests_hyperglottal.py","tests_quanta.py"]:
        if os.path.isfile(f):
            run(["python", f])
    # mimetic analyzer (if data present)
    if os.path.isfile("mimetic_experiment.py"):
        run(["python","mimetic_experiment.py"])
        if os.path.isfile("mimetic_analyzer.py"):
            run(["python","mimetic_analyzer.py"])
    print("test_all done")

if __name__=="__main__":
    main()
