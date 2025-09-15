
# PRODUCTION HARDENING — v17
Date: 2025-09-15T22:43:28.841776Z

Steps to reach production-grade signing and release:
1) Choose KMS provider (AWS KMS or other). Create an asymmetric signing key (RSA/ECDSA) for signing manifests.
2) In CI set environment variables: SIGN_MODE=kms, AWS_KMS_KEY_ID, AWS_REGION.
3) Ensure least-privilege IAM role for CI to call kms:Sign only.
4) Replace demo HMAC usage in tests with calls to tools/sign_kms_wrapper.py when signing manifests.
5) Use tools/generate_release.py in CI to produce signed release zips (includes release_manifest.json).
6) Perform key rotation policy, auditing of KMS usage, and record of signer identity.

Requirements: set `ZORAN_SIGN_KEY` (for hmac fallback) and/or AWS creds for KMS in CI secrets.
