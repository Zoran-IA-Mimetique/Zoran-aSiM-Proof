# INJECTOR_SPEC — v16 (STRICT)

Date: 2025-09-15T22:39:38.574132Z

## Contract (non negotiable)
- Determinism: given (STEM, roles[], context, seed, key), outputs MUST be bit-identical.
- Provenance: output MUST include `provenance.created_iso`, `provenance.seed`, `provenance.context`, and `stem.glyph`.
- Integrity: output MUST be signed (HMAC or better) and MUST be verifiable. Tampering MUST be detected.
- Schema: output MUST validate against `injector_bifurcate_schema_strict.json`.
- Zero-Claim: injector outputs are logs/proofs, NOT performance claims.
