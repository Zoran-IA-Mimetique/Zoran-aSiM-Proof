# Zoran ALL‑IN FINAL — v34 (Flat)
Date: 2025-09-15T23:39:44.430530Z

## What’s inside
- **DATA_SOURCES.csv** — provenance (links/licences/checksums to fill)
- **GlyphNet Bench** — `bench_glyphnet_vs_codecs.py` + local corpus → `BENCH_GLYPHNET_REPORT.json`
- **Multi‑IA** — `multi_ia_demo.py` ×3 + `analyze_multi_ia.py` → `MULTI_IA_STATS.json`
- **Mimetic** — `mimetic_experiment.py` + `mimetic_analyzer.py` → `MIMETIC_STATS.json`
- **Report** — `report_v34.py` → `SCIENTIFIC_REPORT_v34.md`

## Run
```bash
python bench_glyphnet_vs_codecs.py
python multi_ia_demo.py && python analyze_multi_ia.py
python mimetic_experiment.py && python mimetic_analyzer.py
python report_v34.py
```
