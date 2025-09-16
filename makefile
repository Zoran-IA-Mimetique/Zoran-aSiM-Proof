SEEDS=13 42 101

.PHONY: reproduce_all helm mmlu agentbench multiagentbench sign sbom

reproduce_all: helm mmlu agentbench multiagentbench sign sbom
	@echo "DONE (placeholders)."

helm:
	@echo "[HELM] Plug your runner here with seeds $(SEEDS)"

mmlu:
	@echo "[MMLU] Plug your runner here with seeds $(SEEDS)"

agentbench:
	@echo "[AgentBench] Add ablations +ΔM11.3,+ZDM,+EthicChain"

multiagentbench:
	@echo "[MultiAgentBench] Scale-out 50+ agents"

sign:
	@bash ./sign_and_rekor.sh report_manifest.json report.pdf || true

sbom:
	@echo '{"bomFormat":"CycloneDX","specVersion":"1.6","components":[]}' > cyclonedx.json
	@echo '{"vexVersion":"1.0","statements":[]}' > vex.json
