
.PHONY: run psutil c2pa sbom clean all

run:
	python run_all_humble_psutil.py || true

psutil:
	python -c "import psutil; print('psutil OK')"

c2pa:
	python tools/recompute_c2pa.py

sbom:
	@echo "Generate SBOM here (CycloneDX toolchain if available)."

clean:
	rm -f metrics_humble_psutil.json C2PA_manifest_full.json
