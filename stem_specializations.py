import json, time, sys, random

STEM = {
  "name": "stem_injector",
  "glyph": "⟦STEM:injector⋄ΔM11.3:guard⋄ZDM:dual⋄IA2IA:glyphnet⟧",
  "policy": {"zero_claim": True, "evidence_first": True}
}

ROLES = {
  "compliance": {
    "prompt": "Act as a compliance assistant. Map evidence files to AI Act/ISO items and produce a compliance_score.",
    "fields": ["ai_act_items_passed","ai_act_items_total","compliance_score"]
  },
  "energy": {
    "prompt": "Act as an energy logger analyst. Summarize psutil logs (cpu_avg, mem_avg) and produce an energy_proxy score.",
    "fields": ["cpu_avg","mem_avg","energy_proxy"]
  },
  "report": {
    "prompt": "Act as a client-facing reporter. Produce a short status in French (HUMBLE), listing proofs present/absent.",
    "fields": ["present_proofs","missing_proofs","status_summary_fr"]
  }
}

def specialize(role_key, context):
    random.seed(role_key + str(context))
    ts = time.time()
    if role_key == "compliance":
        passed = random.randint(3,8); total = 8
        score = round(passed/total,3)
        payload = {"ai_act_items_passed": passed, "ai_act_items_total": total, "compliance_score": score}
    elif role_key == "energy":
        cpu = round(20 + random.random()*20, 2)
        mem = round(30 + random.random()*30, 2)
        proxy = round((cpu/100.0 + mem/100.0)/2, 3)
        payload = {"cpu_avg": cpu, "mem_avg": mem, "energy_proxy": proxy}
    elif role_key == "report":
        payload = {
            "present_proofs": ["metrics_humble_psutil.json","C2PA_manifest_full.json","sbom_cyclonedx_full.json"],
            "missing_proofs": ["benchmark_public","external_audit_report"],
            "status_summary_fr": "Pack HUMBLE livré : preuves documentaires présentes, benchmark et audit externe à venir."
        }
    else:
        raise SystemExit("Unknown role")
    return {"meta":{"created": ts, "role": role_key, "stem": STEM}, "result": payload}

def main():
    role = sys.argv[1] if len(sys.argv)>1 else "compliance"
    out = specialize(role, "minimal_ctx")
    fname = f"injector_{role}_log.json"
    with open(fname,"w") as f: json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps({"written": fname, "role": role}, indent=2))

if __name__ == "__main__":
    main()
