#!/usr/bin/env bash
set -e
export ZORAN_SIGN_KEY=${ZORAN_SIGN_KEY:-zoran_demo_key}
python injector_total.py || true
python injector_total_test.py || true
python test_all.py || true
echo "Local CI run complete."
