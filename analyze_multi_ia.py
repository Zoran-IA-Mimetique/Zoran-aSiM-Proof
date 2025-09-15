# analyze_multi_ia.py (v22)
# Aggregate agreement across multiple MULTI_IA_DEMO_LOG.json files in the current directory.
import json, glob, statistics

def load_logs():
    data = []
    for f in glob.glob("MULTI_IA_DEMO_LOG*.json"):
        try:
            data.append(json.load(open(f,"r")))
        except Exception:
            pass
    return data

def analyze_logs(reports):
    total = 0; understood = 0; per_agent = {}
    for r in reports:
        for entry in r.get("logs", []):
            total += 1
            if entry.get("understood"): understood += 1
            ag = entry.get("agent","?")
            per_agent.setdefault(ag, {"total":0,"ok":0})
            per_agent[ag]["total"] += 1
            per_agent[ag]["ok"] += 1 if entry.get("understood") else 0
    overall = {"total": total, "ok": understood, "rate": (understood/total if total else 0.0)}
    agents = {k: {"rate": (v["ok"]/v["total"] if v["total"] else 0.0), **v} for k,v in per_agent.items()}
    return {"overall": overall, "agents": agents}

def main():
    reports = load_logs()
    out = analyze_logs(reports)
    json.dump(out, open("MULTI_IA_STATS.json","w"), indent=2)
    print(json.dumps(out, indent=2))

if __name__=="__main__":
    main()
