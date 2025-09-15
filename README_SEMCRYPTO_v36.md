# Semantic Encryption Demo — v36 (Flat)
Date: 2025-09-15T23:52:22.689694Z

## Run (end-to-end)
```bash
export ZORAN_CLIENT_KEY='FranceTravail_demo_key'
python semantic_demo.py
# -> sample_text_zoranX.txt, verification_report.json, semantic_demo_log.json
```
- `verification_report.json` montre le **delta** entre la détection **avec la bonne clé** et **avec une mauvaise clé**.
- `semantic_demo_log.json` fournit des **preuves** (SHA des fichiers).

## Notes
- Démo = **watermark sémantique**, pas chiffrement fort de confidentialité.
- Pour confidentialité, utiliser chiffrement standard côté client (AES/KMS).
