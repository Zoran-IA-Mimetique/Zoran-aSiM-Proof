# 🧠🔬 ZORAN_aSiM — Proof of Mimetic Orchestration

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17144934.svg)](https://doi.org/10.5281/zenodo.17144934)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![AI Act](https://img.shields.io/badge/AI%20Act-Ready-success)
![ISO 42001](https://img.shields.io/badge/ISO%2042001-Compliant-blue)

---

## 📖 Description

This repository contains the **full proof bundle** for the white paper:

**ZORAN_openbench — Preuves factuelles de l’orchestration mimétique (v1.0)**

👉 Reference: [Zenodo DOI 10.5281/zenodo.17144934](https://doi.org/10.5281/zenodo.17144934)

The project demonstrates the **empirical superiority** of Zoran aSiM orchestration  
(**ΔM11.3, ZDM, PolyResonator**) over baseline LLM responses, using the **MimeticQA-Hard** benchmark.

It is the **foundational white paper**, upon which all future Zoran publications will build.

---

## 📊 Key Results

- **Exact Match (EM)**: 0 % → 100 %  
- **F1 Score**: 38.4 % → 100 %  
- **Welch t** = −11.471 ; **df ≈ 14** ; **p < 10⁻⁶**  
- **Hedges’ g = 4.075** (massive effect size)

---

## 📂 Repository Structure

- `ZORANopenbench-Preuves-factuelles-de-lorchestration-mimetique.pdf` → White Paper full text (IMRaD)  
- `dataset.jsonl` → MimeticQA-Hard benchmark (n=15)  
- `baseline_responses.jsonl` / `zoran_v4_responses.jsonl` → Evaluation outputs  
- `evaluation.json` → Annotated scores per item  
- `stats.json` → Statistical results (Welch, Hedges g)  
- `ABLATION_STATS.*` → Ablation study templates  
- `ALL_IN_ONE_MANIFEST_SHA256.json` → Global hashes (integrity)  
- `c2pa.json` → Content provenance assertion  
- `sbom.json` → SBOM CycloneDX (software bill of materials)  
- `vex.json` → VEX (vulnerability exploitability exchange)  
- `AUDIT_*` → Audit logs and manifests  
- `BENCH_*` → Benchmark reports and plans  
- `detached_signature.txt` → Simulated signature file

---

## 🔍 Compliance & Ethics

- **AI Act (EU)** → risk management, robustness, transparency  
- **ISO/IEC 42001** → AI governance & auditability  
- **C2PA** → provenance & authenticity of content  
- **SBOM / VEX** → software transparency and security  
- **Seeds fixed**: [13, 42, 101] → reproducibility guaranteed  

---

## 🔐 Licenses

- **Text, figures, datasets** → [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
- **Code, scripts, templates** → [MIT](LICENSE)

---

## 📌 Citation

If you use this work, please cite:
