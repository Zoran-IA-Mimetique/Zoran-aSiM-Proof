# Demande — Benchmark GlyphNet vs Codecs — v47
Date : 2025-09-16T00:26:47.297165Z

## Portée
- **Fichier** : `bench_glyphnet_vs_codecs.py` (v34)  
- **Corpus plat** : `corpus_text1.txt`, `corpus_text2.txt`, `corpus_text3.txt` (v44) + possibilité d’ajouter WikiText‑2 (lien sous DATA_SOURCES.csv)

## Tâches demandées à AE Studio
- Exécuter le bench sur **corpus plat** et, si licence OK, sur un sous‑ensemble public (WikiText‑2).  
- Produire `BENCH_GLYPHNET_REPORT.json` + un tableau consolidé **size / enc_ms / dec_ms** pour glyphnet/gzip/xz.  
- Commenter les **limites** (textes non répétitifs, overhead header, etc.) et proposer améliorations.

## Livrables
- `glyphnet_bench_report.pdf` + `BENCH_GLYPHNET_REPORT.json` (+ CSV si possible).
