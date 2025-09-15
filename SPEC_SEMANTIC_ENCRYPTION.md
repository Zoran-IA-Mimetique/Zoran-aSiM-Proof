# Semantic Encryption / Watermarking — v36 (Flat)
Date: 2025-09-15T23:52:22.689694Z

## Objective
Embed a **client‑specific, cryptographically keyed signature** into natural‑language text using **semantic choices** (synonym preferences & function‑word variants), so that:
- The text remains human‑readable and natural.
- The presence of the signature is **deterministically verifiable** by the client (who holds the key).
- The mechanism is **auditable** (code + logs + manifest), while the embedded signal is **opaque** to third parties.

## Method (lexical watermarking)
- Maintain a list of **controlled synonym pairs** (w0, w1) that are near‑equivalent.
- Derive a **bit‑stream** from HMAC‑SHA256(key, base_text).
- Scan the text left‑to‑right; at each candidate pair occurrence choose **w0 for bit=0** or **w1 for bit=1**.
- Verification recomputes the expected bit‑stream and compares with observed choices → **match‑rate**; above a threshold ⇒ signature present.

## Guarantees (within demo scope)
- **Determinism**: Same (text, key) ⇒ same embedding.
- **Verifiability**: Detector yields match‑rate ≥ θ (e.g. 0.7) for the correct key; near random for wrong keys.
- **Auditability**: We emit `semantic_demo_log.json` (params, HMAC of inputs) and `verification_report.json`.

⚠️ This is **not strong cryptography** for confidentiality; it is a **semantic watermark** for provenance. For confidentiality, use standard crypto and keep data on client side.
