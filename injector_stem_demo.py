import json, time, random

STEM = {
  "name": "stem_injector",
  "glyph": "⟦STEM:injector⋄ΔM11.3:guard⋄ZDM:dual⋄IA2IA:glyphnet⟧",
  "policy": {"zero_claim": True, "evidence_first": True}
}

ROLES = {
  "audit":   {"prompt": "Act as an ethical auditor. Check claims vs evidence and output ERRATA candidates."},
  "summary": {"prompt": "Act as a scientific summarizer. Produce IMRaD-style summary with limitations."},
  "bench":   {"prompt": "Act as a protocol designer. Propose reproducible steps, seeds, metrics and ablations."}
}

def differentiate(stem, role_key, context):
    role = ROLES[role_key]
    # Simple simulation: attach role prompt, generate a "score" and "notes"
    score = round(0.7 + random.uniform(-0.05, 0.05), 3)
    notes = f"{role_key} specialized from STEM; context_len={len(context or '')}"
    return {"role": role_key, "prompt": role["prompt"], "score": score, "notes": notes}

def main():
    context = "Minimal context for demo"
    logs = {"meta": {"created": time.time(), "stem": STEM}, "steps": []}
    for rk in ["audit", "summary", "bench"]:
        out = differentiate(STEM, rk, context)
        logs["steps"].append(out)
    with open("injector_logs_example.json","w") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)
    print(json.dumps({"written": "injector_logs_example.json", "roles": [s["role"] for s in logs["steps"]]}, indent=2))

if __name__ == "__main__":
    main()
