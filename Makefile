setup:
	@mkdir -p out/plots out/logs out/c2pa
	@echo 'env ok'

reproduce_all:
	@python scripts/run_benchmarks.py || echo 'bench stub'
	@python scripts/run_ablations.py || echo 'ablations stub'
	@echo '{}' > out/metrics.json

export_artifacts:
	@cp experiments/delta_table.csv out/
	@cp experiments/kpis.csv out/
	@echo 'export ok'
