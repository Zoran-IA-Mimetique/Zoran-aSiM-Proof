# Zoran v22 — Analysis & EU Profile (Flat)
Date: 2025-09-15T23:00:27.077295Z

## New files
- `analyze_multi_ia.py` — computes agreement stats from MULTI_IA_DEMO_LOG*.json → `MULTI_IA_STATS.json`.
- `BENCH_RESULTS_TEMPLATE.md` — template to present GlyphNet vs codecs results.
- `EURO5_CHECKLIST_FILLED.md` — example checklist filled (to be confirmed by auditor).

## How to use
1) Run `multi_ia_demo.py` multiple times (seed variations), rename outputs as MULTI_IA_DEMO_LOG_1.json, _2.json, ... then:
   ```bash
   python analyze_multi_ia.py
   # -> MULTI_IA_STATS.json
   ```
2) Run `bench_glyphnet_vs_codecs.py` and copy numbers into `BENCH_RESULTS_TEMPLATE.md`.
3) Update `EURO5_CHECKLIST_FILLED.md` based on evidence and auditor feedback.
