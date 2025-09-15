import os, json, subprocess, shutil

REQUIRED_FILES = [
    "README_CLIENT.md","MODEL_CARD.md","ERRATA.md","CLAIMS_AUDIT.md",
    "C2PA_manifest_full.json","sbom_cyclonedx_full.json",
    "evidence_model_card_full.md","evidence_data_processing_register.md"
]

OPTIONAL_FILES = [
    "metrics_humble_psutil.json","ablation_results.json","ABLATION_STATS.csv",
    "injector_compliance_log.json","injector_energy_log.json","injector_report_log.json",
    "ROOT_SHA256_MANIFEST_v13.json","ROOT_SHA256_MANIFEST_v12.json","ROOT_SHA256_MANIFEST_v11.json"
]

def exists(path): return os.path.isfile(path)

def main():
    report = {"present": [], "missing": [], "optional_present": [], "optional_missing": []}
    for f in REQUIRED_FILES:
        (report["present"] if exists(f) else report["missing"]).append(f)
    for f in OPTIONAL_FILES:
        (report["optional_present"] if exists(f) else report["optional_missing"]).append(f)

    # Try validating a compliance injector log if present
    validation = None
    if exists("injector_compliance_log.json") and exists("validate_injector_log.py"):
        try:
            out = subprocess.run(["python","validate_injector_log.py","injector_compliance_log.json"], capture_output=True, text=True, timeout=30)
            validation = out.stdout.strip()
        except Exception as e:
            validation = f"ERROR: {e}"
    report["injector_validation"] = validation

    with open("SELF_CHECK_REPORT.json","w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
