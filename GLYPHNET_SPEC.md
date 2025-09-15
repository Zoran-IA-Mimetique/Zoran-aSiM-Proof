# GLYPHNET — SPEC (v20)
Date: 2025-09-15T22:54:20.015942Z

Goal: Minimal, deterministic, lossless IA↔IA container with visible header and safe payload.
- Header: `Z5::` (magic)
- Payload: zlib‑compressed bytes, base64 encoded (ASCII‑safe)
- Round‑trip guarantee: decode(encode(x)) == x
- Deterministic: zlib level 9; no metadata; newline normalized.

Security notes:
- No code execution; pure data container.
- For untrusted inputs, size‑limit before decode and base64 validation.
