import json, time, hashlib, hmac, os, sys, uuid
from datetime import datetime

HMAC_KEY = os.environ.get('ZORAN_SIGN_KEY', 'zoran_demo_key').encode('utf-8')

STEM_TEMPLATE = {
    "name": "stem_injector",
    "glyph": "⟦STEM:injector⋄ΔM11.3:guard⋄ZDM:dual⋄IA2IA:glyphnet⟧",
    "meta_policy": {"zero_claim": True, "evidence_first": True, "version":"v16"}
}

ROLE_TEMPLATES = {
    "compliance": {"desc":"Map evidence to regulatory checklist", "fields":["ai_act_items_passed","ai_act_items_total","compliance_score"]},
    "energy": {"desc":"Summarize psutil logs and compute energy proxy", "fields":["cpu_avg","mem_avg","energy_proxy"]},
    "report": {"desc":"Produce client-facing French status", "fields":["present_proofs","missing_proofs","status_summary_fr"]},
    "audit": {"desc":"Produce ERRATA candidates and claims mismatches", "fields":["errata_candidates","claims_mismatch"]},
    "bench": {"desc":"Produce protocol steps, datasets, seeds, metrics", "fields":["datasets","seeds","metrics","ablations"]},
    "summary": {"desc":"Produce IMRaD style summary", "fields":["imrad_sections","limits"]}
}

def uuid5(namespace: str, name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{namespace}:{name}"))

def sign_bytes(b: bytes) -> str:
    return hmac.new(HMAC_KEY, b, hashlib.sha256).hexdigest()

def build(stem, roles, context, seed:int):
    prov = {"created_at": time.time(), "created_iso": datetime.utcnow().isoformat()+"Z", "seed": seed, "context": context, "stem": stem}
    runs = []
    ns = prov["created_iso"]
    for r in roles:
        tmpl = ROLE_TEMPLATES.get(r, {"desc":"custom","fields":[]})
        rid = uuid5(ns, f"{stem.get('name','stem')}.{r}.{seed}")
        values = {}
        for f in tmpl["fields"]:
            material = f"{rid}:{f}:{seed}:{context}".encode('utf-8')
            h = hashlib.sha256(material).hexdigest()
            if 'score' in f or 'avg' in f or 'proxy' in f:
                num = (int(h[:8],16) % 1000)/1000.0
                values[f] = round(num,3)
            elif 'items' in f:
                values[f] = (int(h[:6],16) % 8) + 1
            elif f in ('datasets','seeds','metrics','ablations'):
                values[f] = {"note":"placeholder","example":["sudoku_small"],"seed":seed}
            else:
                values[f] = f"auto:{h[:12]}"
        entry = {
            "role_id": rid,
            "role": r,
            "generated_at": time.time(),
            "generated_iso": datetime.utcnow().isoformat()+"Z",
            "payload": {"role": r, "desc": tmpl["desc"], "values": values}
        }
        entry["signature"] = sign_bytes(json.dumps(entry, sort_keys=True).encode('utf-8'))
        runs.append(entry)
    out = {"provenance": prov, "runs": runs}
    out["signature"] = sign_bytes(json.dumps(out, sort_keys=True).encode('utf-8'))
    return out

def main():
    roles = sys.argv[1].split(",") if len(sys.argv)>1 else ["compliance","energy","report"]
    context = sys.argv[2] if len(sys.argv)>2 else "strict_demo_ctx"
    seed = int(sys.argv[3]) if len(sys.argv)>3 else 16
    out = build(STEM_TEMPLATE, roles, context, seed)
    fname = f"bifurcate_strict_{seed}.json"
    with open(fname,"w",encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps({"written": fname, "roles": roles}, indent=2))

if __name__ == "__main__":
    main()
