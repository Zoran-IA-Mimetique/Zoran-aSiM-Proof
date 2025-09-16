# make_all_reports.py — v46
import os, json, datetime
parts = ["# ZORAN_DEMO_REPORT_v46", "Date: "+datetime.datetime.utcnow().isoformat()+"Z"]
def add(title, path):
    parts.append(f"## {title}")
    if os.path.isfile(path):
        parts.append("```json")
        parts.append(open(path).read())
        parts.append("```")
    else:
        parts.append(f"_missing: {path}_")
for title, path in [
    ("Injector log", "injector_total_full_log.json"),
    ("GlyphNet bench", "BENCH_GLYPHNET_REPORT.json"),
    ("Multi‑IA stats", "MULTI_IA_STATS.json"),
    ("Mimetic stats", "MIMETIC_STATS.json"),
    ("Semcrypto verification", "verification_report.json")
]:
    add(title, path)
open("ZORAN_DEMO_REPORT_v46.md","w").write("\n\n".join(parts))
print("Wrote ZORAN_DEMO_REPORT_v46.md")
