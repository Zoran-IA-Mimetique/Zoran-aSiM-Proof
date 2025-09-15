#!/bin/sh
# Demo runner for injector_bifurcate
python injector_bifurcate.py compliance,energy,report demo_ctx 42
python validate_bifurcate.py bifurcate_42.json || true
