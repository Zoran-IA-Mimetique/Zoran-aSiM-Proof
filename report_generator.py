# report_generator.py (v23)
# Generate SCIENTIFIC_REPORT_v23.md from bench + multi_ia results + EURO5 checklist.
import json, os, datetime

def md_table_glyphnet(report):
    out = ["## GlyphNet vs Codecs Results"]
    out.append("| File | Codec | Size | Enc ms | Dec ms |")
    out.append("|------|-------|------|--------|--------|")
    for f,v in report.items():
        if "error" in v: continue
        for codec,res in v.items():
            out.append(f"| {f} | {codec} | {res['size']} | {res['enc_ms']:.2f} | {res['dec_ms']:.2f} |")
    return "\n".join(out)

def md_multi(stats):
    out=["## Multi-IA Agreement"]
    o=stats.get("overall",{})
    out.append(f"- Total: {o.get('total')} ; OK: {o.get('ok')} ; Rate: {o.get('rate'):.2f}")
    for ag,v in stats.get("agents",{}).items():
        out.append(f"- Agent {ag}: {v['ok']}/{v['total']} ({v['rate']:.2f})")
    return "\n".join(out)

def main():
    now=datetime.datetime.utcnow().isoformat()+"Z"
    lines=[f"# Scientific Report v23", f"Date: {now}"]
    if os.path.isfile("BENCH_GLYPHNET_REPORT.json"):
        g=json.load(open("BENCH_GLYPHNET_REPORT.json"))
        lines.append(md_table_glyphnet(g))
    if os.path.isfile("MULTI_IA_STATS.json"):
        s=json.load(open("MULTI_IA_STATS.json"))
        lines.append(md_multi(s))
    if os.path.isfile("EURO5_CHECKLIST_FILLED.md"):
        lines.append("## EURO-5 Checklist (example)")
        lines.append(open("EURO5_CHECKLIST_FILLED.md").read())
    open("SCIENTIFIC_REPORT_v23.md","w").write("\n\n".join(lines))

if __name__=="__main__":
    main()
