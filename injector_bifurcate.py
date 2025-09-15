"""injector_bifurcate.py
Deterministic bifurcation engine for STEM injectors.
- Takes a STEM definition and a list of target roles.
- Produces signed, traceable logs with provenance chain and role-specific payloads.
- Uses deterministic UUIDs (seeded) so runs can be reproduced given same seed+inputs.
"""
import json, time, hashlib, hmac, os, sys
from datetime import datetime
from typing import Dict, Any, List
import random, uuid

# Simple HMAC-based signature stub (replace with real key management for production)
HMAC_KEY = os.environ.get('ZORAN_SIGN_KEY', 'zoran_demo_key')

STEM_TEMPLATE = {
    "name": "stem_injector",
    "glyph": "⟦STEM:injector⋄ΔM11.3:guard⋄ZDM:dual⋄IA2IA:glyphnet⟧",
    "meta_policy": {"zero_claim": True, "evidence_first": True}
}

ROLE_TEMPLATES = {
    "compliance": {"desc":"Map evidence to regulatory checklist", "fields":["ai_act_items_passed","ai_act_items_total","compliance_score"]},
    "energy": {"desc":"Summarize psutil logs and compute energy proxy", "fields":["cpu_avg","mem_avg","energy_proxy"]},
    "report": {"desc":"Produce client-facing French status", "fields":["present_proofs","missing_proofs","status_summary_fr"]},
    "audit": {"desc":"Produce ERRATA candidates and claims mismatches", "fields":["errata_candidates","claims_mismatch"]},
    "bench": {"desc":"Produce protocol steps, datasets, seeds, metrics", "fields":["datasets","seeds","metrics","ablations"]},
    "summary": {"desc":"Produce IMRaD style summary", "fields":["imrad_sections","limits"]}
}

def deterministic_uuid(namespace: str, name: str) -> str:
    # deterministic UUIDv5-like using namespace+name
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{namespace}:{name}"))

def sign_payload(payload: bytes) -> str:
    # HMAC-SHA256 signature stub
    return hmac_sha256_hex(HMAC_KEY.encode('utf-8'), payload)

def hmac_sha256_hex(key: bytes, payload: bytes) -> str:
    import hmac, hashlib
    return hmac.new(key, payload, hashlib.sha256).hexdigest()

def bifurcate(stem: Dict[str,Any], roles: List[str], context: str="", seed:int=13) -> Dict[str,Any]:
    random.seed(seed)
    provenance = {"created_at": time.time(), "created_iso": datetime.utcnow().isoformat()+"Z", "stem": stem, "context": context, "seed": seed}
    runs = []
    namespace = provenance["created_iso"]
    for r in roles:
        role_template = ROLE_TEMPLATES.get(r, {"desc":"custom", "fields":[]})
        name = f"{stem.get('name','stem')}.{r}"
        rid = deterministic_uuid(namespace, name)
        # deterministic pseudo-output generation for fields
        payload = {"role": r, "desc": role_template["desc"], "values": {}}
        for f in role_template["fields"]:
            # simple deterministic numeric or example values
            val_seed = f"{rid}:{f}:{seed}:{context}"
            h = hashlib.sha256(val_seed.encode('utf-8')).hexdigest()
            # create pseudo-values: numeric for known metrics, list for others
            if 'score' in f or 'avg' in f or 'proxy' in f:
                num = (int(h[:8],16) % 1000) / 1000.0
                payload["values"][f] = round(num,3)
            elif 'items' in f or 'n' in f:
                payload["values"][f] = (int(h[:6],16) % 9) + 1
            elif f in ('datasets','seeds','metrics','ablations'):
                payload["values"][f] = {"note":"placeholder", "example":["sudoku_small"], "seed":seed}
            else:
                payload["values"][f] = f"auto:{h[:12]}"
        # provenance chain entry
        entry = {
            "role_id": rid,
            "role": r,
            "payload": payload,
            "generated_at": time.time(),
            "generated_iso": datetime.utcnow().isoformat()+"Z"
        }
        # sign entry
        raw = json.dumps(entry, sort_keys=True).encode('utf-8')
        entry["signature"] = sign_payload(raw)
        runs.append(entry)
    out = {"provenance": provenance, "runs": runs}
    # overall signature
    raw_all = json.dumps(out, sort_keys=True).encode('utf-8')
    out["signature"] = sign_payload(raw_all)
    return out

def save(out: Dict[str,Any], path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

def main():
    stem = STEM_TEMPLATE
    roles = sys.argv[1].split(",") if len(sys.argv)>1 else "compliance,energy,report".split(",")
    ctx = sys.argv[2] if len(sys.argv)>2 else "demo_context"
    seed = int(sys.argv[3]) if len(sys.argv)>3 else 13
    out = bifurcate(stem, roles, context=ctx, seed=seed)
    fname = f"bifurcate_{seed}.json"
    save(out, fname)
    print(json.dumps({"written": fname, "roles": roles}, indent=2))

if __name__=='__main__':
    main()
