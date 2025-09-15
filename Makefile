.PHONY: run ci c2pa sbom ablations tests package clean
run:
	python run_all_humble_psutil.py
tests:
	python test_roundtrip_glyphnet.py && python orchestration_e2e_test.py && python adversarial_tests/adversarial_fuzz.py
ablations:
	python run_ablation_suite.py
c2pa:
	python tools/recompute_c2pa.py
sbom:
	python tools/compute_sbom.py
package:
	python tools/recompute_c2pa.py
	zip -r zoran_release.zip . -x .git*
clean:
	rm -f metrics_humble_psutil.json ablation_results.json roundtrip_results.json orchestration_log.json C2PA_manifest_full.json
