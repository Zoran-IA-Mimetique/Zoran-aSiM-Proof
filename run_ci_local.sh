#!/usr/bin/env bash
export ZORAN_SIGN_KEY=${ZORAN_SIGN_KEY:-zoran_demo_key}
python injector_total.py || true
python injector_total_test.py || true
