#!/usr/bin/env bash
# FLAT signing pipeline (placeholders). Requires c2patool, cosign, rekor-cli.
set -euo pipefail
MANIFEST="${1:-report_manifest.json}"
ARTIFACT="${2:-report.pdf}"

echo "[C2PA] Would attach manifest to ${ARTIFACT} (placeholder)."
# c2patool "$ARTIFACT" -m "$MANIFEST" --out ./

echo "[cosign] Would sign ${ARTIFACT} and create a bundle (placeholder)."
# cosign sign-blob "$ARTIFACT" --bundle cosign.bundle

echo "[Rekor] Would upload signature and artifact to Rekor (placeholder)."
# rekor-cli upload --rekor_server https://rekor.sigstore.dev --artifact "$ARTIFACT" --public-key cosign.pub --signature cosign.sig

echo "Done (dry-run)."
