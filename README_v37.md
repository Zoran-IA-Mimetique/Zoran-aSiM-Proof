# Zoran — Semantic Cryptography (v37, Flat)
Date: 2025-09-15T23:55:51.147027Z

## Files (flat)
- semantic_crypto_v37.py — embed/detect (deterministic HMAC)
- semantic_demo.py — end-to-end demo + proofs
- INJECTOR_CRYPTO_CLIENT_DEMO.py — client-specific demo (France Travail)
- CLIENT_KEY_GUIDE.md — key management (env/KMS)
- SEMCRYPTO_AUDIT_TEMPLATE.md — audit checklist
- ROBUSTNESS_TESTS.py — mutations & detection stats (JSON+CSV)
- SPEC_SEMANTIC_ENCRYPTION.md — spec
- SEMCRYPTO_REPORT_v37.md — consolidated note

## Quick run
```bash
export ZORAN_CLIENT_KEY='FranceTravail_demo_key'
python semantic_demo.py
python INJECTOR_CRYPTO_CLIENT_DEMO.py
python ROBUSTNESS_TESTS.py
```
