# PR — Semantic Cryptography (v38, Flat)

**What’s included**
- End‑to‑end demo (`semantic_demo.py`) — produces watermarked text + verification report
- Client demo France Travail (`INJECTOR_CRYPTO_CLIENT_DEMO.py`) — client‑key detection gap
- Robustness tests (`ROBUSTNESS_TESTS.py`) — JSON/CSV with rate stats under perturbations
- CI workflow (`GITHUB_WORKFLOW_semcrypto.yml`) — runs demo + robustness, uploads artifacts

**Proofs**
- `verification_report.json` — correct‑key vs wrong‑key detection rates
- `semantic_demo_log.json` — SHA of generated files
- `FT_semantic_crypto_report.json` — client‑specific report
- `ROOT_SHA256_MANIFEST_v37.json` or newer

**Zero‑Claim**
- Watermark = provenance, **not** confidentiality
- For secrecy, use client‑side crypto (KMS/AES)

**Next**
- Move workflow to `.github/workflows/` to activate CI
- Add client KMS key in secrets if needed
