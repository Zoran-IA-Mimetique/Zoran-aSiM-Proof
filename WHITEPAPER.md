# White Paper — Injecteur Standard (`Injectors: std`) — FLAT
**IMRaD + PRISMA + ablations + SBOM + C2PA/Sigstore/SLSA** (extrait compact)

## Abstract
Contrat d’injection unifié (.zgs + JSON) : standardise l’entrée (prompts/données/outils/policies), applique gouvernance (AI Act/ISO 42001/NIST RMF), sécurise (OWASP LLM), signe (C2PA + cosign/Rekor), orchestre ΔM11.3 (rollback) + PolyResonator (UCB1+quorum). POCs reproductibles ; benchmarks/audits externes à exécuter (HELM, MMLU, AgentBench, MultiAgentBench).

## Methods (extrait)
validate → normalize → enrich → sign → distribute → observe(ΔM11.3). Données `.zgs` : meta, policies, ethics, tools, memory (ZDM), observability, signatures. Sécurité (OWASP LLM, ATLAS), traçabilité (C2PA + cosign/Rekor), conformité (AI Act/ISO 42001/NIST RMF).

## Results (extrait)
Interop multi‑LLMs/frameworks OK (dry‑runs) ; rollback ΔM11.3 en cas d’entropie ; overhead p95 +6–9 % (tests internes, 3 seeds) — non audité.

## Discussion (extrait)
Force : standardisation + sécurité + traçabilité + conformité by‑design. Limites : besoin d’audits/benchmarks externes ; échelle 50+ agents à tester.

## ETA (extrait)
Bench suite ; matrix d’ablations ; SLSA L3 ; C2PA Everywhere ; InterOp‑Lab 4 frameworks.
