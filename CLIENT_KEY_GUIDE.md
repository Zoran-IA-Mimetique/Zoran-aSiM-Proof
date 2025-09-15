# Client Key Guide — v37 (Flat)
Date: 2025-09-15T23:55:51.147027Z

## Goal
Let the client (e.g., France Travail) **own the key** to generate/verify their **semantic watermark** without exposing the content to Zoran.

## Options
- **Env var**: `ZORAN_CLIENT_KEY` set in their infra (server/local).  
- **KMS**: store key in AWS KMS (or GCP KMS), inject via CI/secret manager, never in repo.

## Workflow
1) Client sets `ZORAN_CLIENT_KEY`.
2) Run `INJECTOR_CRYPTO_CLIENT_DEMO.py` to produce watermarked text + `FT_semantic_crypto_report.json`.
3) Verification: run `detect(watermarked, key)` → check `rate ≥ θ` (e.g. 0.7).

⚠️ This is **provenance watermarking**, not confidentiality. Use standard crypto for secrecy.
