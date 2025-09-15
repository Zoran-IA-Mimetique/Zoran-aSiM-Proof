# README_BIFURCATE — Bifurcation Engine (v15)
Date: 2025-09-15T22:36:38.806482Z

This pack implements a deterministic bifurcation engine for STEM injectors.
Goals:
- Make injector specialization deterministic and reproducible (seeded).
- Produce a provenance chain for each specialization run.
- Produce HMAC signatures for integrity (replace stub with KMS for production).
- Provide validation tooling to check signatures and structure.

Files:
- injector_bifurcate.py : core engine
- injector_bifurcate_schema.json : JSON schema
- validate_bifurcate.py : validator and signature checker
- injector_bifurcate_demo.sh : demo runner

Usage (local):
$ python injector_bifurcate.py compliance,energy,report demo_ctx 42
$ python validate_bifurcate.py bifurcate_42.json

Notes:
- The HMAC key is read from env ZORAN_SIGN_KEY; set it in CI before running for deterministic signatures.
- This is a traceable, verifiable step toward making injectors auditable and robust.
