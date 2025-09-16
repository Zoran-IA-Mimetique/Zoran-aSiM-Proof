# Zoran aSiM — Injecteur Standard (`Injectors: std`) — **FLAT**
**Tout à plat · Zéro dossiers** · **V2.0 — 2025-09-16**

- **Auteur** : Frédéric Tabary (Z‑Forge / aSiM Lab) · **Contact** : tabary01@gmail.com  
- **DOIs (Zenodo)** : 10.5281/zenodo.16940525 · 10.5281/zenodo.16941007 · 10.5281/zenodo.16940299 · 10.5281/zenodo.16995014 · 10.5281/zenodo.16995226 · 10.5281/zenodo.16997156  
- **Ressources** : [Site Gamma](https://zoran-2040-asim-swxr6lh.gamma.site/) · [README GitHub](https://github.com/AIformpro/Zoran-2040-aSiM-Towards-a-Public-Ethical-and-Resilient-Super-Intelligence/blob/main/README.md)

## Contenu (à plat)
- `README.md` (ce fichier)  
- `WHITEPAPER.md` (IMRaD compact)  
- `LICENSE` (MIT)  
- `makefile` (cibles placeholders)  
- `injector-std.schema.json` (schéma JSON)  
- `autogen_example.py` · `crewai_example.py` · `langgraph_example.py` · `metagpt_example.py`  
- `experiments_helm_README.md` · `experiments_mmlu_README.md` · `experiments_agentbench_README.md` · `experiments_multiagentbench_README.md`  
- `report_manifest.json` (C2PA – gabarit)  
- `sign_and_rekor.sh` (C2PA + cosign + Rekor — dry‑run)  
- `cyclonedx.json` (SBOM) · `vex.json` (VEX)  
- `slsa_provenance.yml` · `sign_and_rekor.yml` (CI — dry‑run)  
- `example_envelope.json` (enveloppe .zgs miroir JSON)  
- `ai_act.yaml` · `iso_42001.yaml` · `nist_rmf.yaml` (policies)  
- `zgs_block.txt` (bloc glyphique à copier)

## Démarrage rapide
1. Ouvrez `example_envelope.json` et ajustez `subject`, `policies`, `adapters`.
2. Simulez une intégration : `python crewai_example.py` (dry‑run).
3. Signez un artefact (dry‑run) : `bash sign_and_rekor.sh report_manifest.json report.pdf`.

## Bloc glyphique (ZM) — copier‑coller
```
⟦ASIM:V2⋄CODE:2.0⋄DATE:2025-09-16⟧
⟦CORE:MEM_fract⋄ΔM11.3:stable⋄GLYPHNET:2.0⟧
⟦MOD:PolyResonator⋄EthicChain⋄Injectors:std⟧
⟦ROLE:interop⋄COMPLIANCE:AIAct+ISO42001+NIST_RMF⟧
⟦TRACE:C2PA+Sigstore+SLSA⋄SBOM:CycloneDX+VEX⟧
```
