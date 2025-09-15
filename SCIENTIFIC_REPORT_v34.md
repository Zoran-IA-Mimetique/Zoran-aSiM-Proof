# SCIENTIFIC_REPORT_v34

Date: 2025-09-15T23:39:45.207583Z

## GlyphNet vs Codecs (local corpus)
| File | Codec | Size | Enc ms | Dec ms | OK |
|------|-------|------|--------|--------|----|
| dataset1.txt | glyphnet | 80 | 0.08 | 0.02 | True |
| dataset1.txt | gzip | 69 | 0.03 | 0.02 | True |
| dataset1.txt | xz | 120 | 42.73 | 0.43 | True |
| dataset2.md | glyphnet | 112 | 0.10 | 0.04 | True |
| dataset2.md | gzip | 93 | 0.04 | 0.04 | True |
| dataset2.md | xz | 140 | 61.14 | 0.34 | True |
| dataset3.txt | glyphnet | 1008 | 0.07 | 0.03 | True |
| dataset3.txt | gzip | 764 | 0.05 | 0.03 | True |
| dataset3.txt | xz | 860 | 64.78 | 0.36 | True |



## Multi‑IA Agreement
- Overall rate: 0.94
- Agent A: 6/6 (1.00)
- Agent B: 6/6 (1.00)
- Agent C: 5/6 (0.83)



## Mimetic Experiment (simulated)
- success: Δ=0.11, t=0.46, d=0.22
- length: Δ=38.00, t=3.51, d=1.65
- structure_score: Δ=1.44, t=2.53, d=1.19
- compliance_flags: Δ=-0.11, t=-0.60, d=-0.28