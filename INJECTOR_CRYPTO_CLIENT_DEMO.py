# INJECTOR_CRYPTO_CLIENT_DEMO.py — France Travail demo (flat)
import os, json, time
from semantic_crypto_v37 import embed, detect

CLIENT_KEY = os.environ.get("ZORAN_CLIENT_KEY","FranceTravail_demo_key")

def build_hyper_block(role="auditor", task="check claims", policy=("zero-claim","evidence-first"), evidence="CLAIMS_AUDIT.md"):
    lines=["#HG v20", f"ROLE: {role}", f"TASK: {task}"]
    if policy: lines.append("POLICY: "+",".join(policy))
    if evidence: lines.append("EVIDENCE: "+evidence)
    lines.append("END")
    return "\n".join(lines)

def build_quanta(role="audit", policy="zero-claim", evidence="CLAIMS_AUDIT.md"):
    parts=[f"role={role}"]
    if policy: parts.append(f"policy={policy}")
    if evidence: parts.append(f"evidence={evidence}")
    return "⟦chan:" + "|".join(parts) + "⟧"

def main():
    base_text = (
        "We start this report to show how an idea can help small teams begin a big project.\n"
        "We try to use simple words and demonstrate the goal with a clear summary.\n"
        "If you need to get results fast, we assist you to make the right choices and finish on time."
    )
    hyper = build_hyper_block()
    quanta = build_quanta()
    msg = hyper + "\n\n" + quanta + "\n\n" + base_text
    watermarked, stats = embed(msg, CLIENT_KEY)
    open("FT_message_watermarked.txt","w",encoding="utf-8").write(watermarked)
    ok = detect(watermarked, CLIENT_KEY)
    wrong = detect(watermarked, "wrong_key")
    report = {
        "meta":{"created": time.time(),"client":"France Travail","mechanism":"Hyper/Quanta + semantic watermark"},
        "embed":{"applied": stats["applied"], "candidates": stats["candidates"]},
        "detect_correct": ok,
        "detect_wrong": wrong
    }
    json.dump(report, open("FT_semantic_crypto_report.json","w"), indent=2)
    print(json.dumps(report, indent=2))

if __name__=="__main__":
    main()
