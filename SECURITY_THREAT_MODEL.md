# Security Threat Model (light)

- **Spoofed artifacts** → SHA/manifest & signature check (CI fail).
- **Prompt injection** → validator rules; whitelist sources; sanitize; logs.
- **Key misuse** → KMS least‑privilege, rotation, audit trail.
- **Supply chain** → SBOM CycloneDX, pinned deps, CI caching off for sensitive steps.
