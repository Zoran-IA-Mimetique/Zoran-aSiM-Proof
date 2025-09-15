import json, os, datetime

def glyphnet_table():
    if not os.path.isfile("BENCH_GLYPHNET_REPORT.json"):
        return "No GlyphNet report yet."
    rep=json.load(open("BENCH_GLYPHNET_REPORT.json"))
    lines=["## GlyphNet vs Codecs (local corpus)",
           "| File | Codec | Size | Enc ms | Dec ms | OK |",
           "|------|-------|------|--------|--------|----|"]
    for f,vals in rep.items():
        if "error" in vals: 
            lines.append(f"| {f} | error |  |  |  |  |")
            continue
        for codec in ["glyphnet","gzip","xz"]:
            v=vals.get(codec,{})
            lines.append(f"| {f} | {codec} | {v.get('size','')} | {v.get('enc_ms',0):.2f} | {v.get('dec_ms',0):.2f} | {v.get('ok','')} |")
    return "\n".join(lines)

def multi_ia_section():
    if not os.path.isfile("MULTI_IA_STATS.json"):
        return "No Multi‑IA stats yet."
    s=json.load(open("MULTI_IA_STATS.json"))
    o=s.get("overall",{})
    lines=[f"## Multi‑IA Agreement","- Overall rate: {:.2f}".format(o.get('rate',0))]
    for ag,vals in s.get("agents",{}).items():
        lines.append(f"- Agent {ag}: {vals['ok']}/{vals['total']} ({vals['rate']:.2f})")
    return "\n".join(lines)

def mimetic_section():
    if not os.path.isfile("MIMETIC_STATS.json"):
        return "No mimetic stats yet."
    m=json.load(open("MIMETIC_STATS.json"))
    lines=["## Mimetic Experiment (simulated)"]
    for k,v in m.items():
        lines.append(f"- {k}: Δ={v['delta']:.2f}, t={v['t']:.2f}, d={v['cohen_d']:.2f}")
    return "\n".join(lines)

def main():
    now=datetime.datetime.utcnow().isoformat()+"Z"
    parts=["# SCIENTIFIC_REPORT_v34", f"Date: {now}", glyphnet_table(), "", multi_ia_section(), "", mimetic_section()]
    open("SCIENTIFIC_REPORT_v34.md","w").write("\n\n".join(parts))
    print("Wrote SCIENTIFIC_REPORT_v34.md")

if __name__=="__main__":
    main()
