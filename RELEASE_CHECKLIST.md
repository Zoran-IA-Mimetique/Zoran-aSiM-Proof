# Release Checklist — v25

- [ ] Update ROADMAP.md
- [ ] Update DATA_SOURCES_TEMPLATE.csv with real sources & checksums
- [ ] Run all tests (tests/test_all.py or equivalent)
- [ ] Recompute ROOT_SHA256_MANIFEST.json
- [ ] Run CI workflows (matrix, strict injectors)
- [ ] Generate release with tools/generate_release.py
- [ ] Attach release_summary.json
- [ ] Tag version (vX.Y)
