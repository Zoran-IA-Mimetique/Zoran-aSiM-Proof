# Zoran aSiM — Master (Flat)
[![injector_total_full](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_total_full.yml/badge.svg)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_total_full.yml)
[![injector_relevance](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_relevance.yml/badge.svg)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_relevance.yml)
[![semcrypto](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/semcrypto.yml/badge.svg)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/semcrypto.yml)
[![CI: injector_total](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_total_full.yml/badge.svg?branch=main)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_total_full.yml)
[![CI: relevance](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_relevance.yml/badge.svg?branch=main)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/injector_relevance.yml)
[![CI: semcrypto](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/semcrypto.yml/badge.svg?branch=main)](https://github.com/Zoran-IA-Mimetique/Zoran-aSiM-Proof/actions/workflows/semcrypto.yml)

> ⚠️ Pour **activer les badges**, déplacez ces fichiers dans `.github/workflows/` :  
> `GITHUB_WORKFLOW_injector_total_full.yml` → `.github/workflows/injector_total_full.yml`  
> `GITHUB_WORKFLOW_injector_relevance.yml` → `.github/workflows/injector_relevance.yml`  
> `GITHUB_WORKFLOW_semcrypto.yml` → `.github/workflows/semcrypto.yml`

## Démarrage rapide

### Injecteur TOTAL (sécurité + pertinence + rôle + traçabilité)
```bash
export ZORAN_SIGN_KEY='zoran_demo_key'
python injector_total_full.py
python INJECTOR_TOTAL_RELEVANCE_TEST.py
```

### Pertinence (module isolé)
```bash
python injector_relevance.py "define audit" "definition with checklist sha"
python injector_relevance_test.py
```

### GlyphNet (codec IA↔IA) — bench local
```bash
python bench_glyphnet_vs_codecs.py    # utilise corpus_text*.txt
```

### Cryptage sémantique (provenance)
```bash
export ZORAN_CLIENT_KEY='FranceTravail_demo_key'
python semantic_demo.py
python verify_semantic_crypto.py
python tests_semantic_crypto.py
```

### Bench (prompts) & Audit archive
```bash
python run_benchmark_shard.py --seed 13 --shard prompts_shard_01.jsonl
python merge_results.py
python seed_matrix_runner.py
python make_audit_archive.py
```

## Fichiers inclus (plats)
- Injecteur TOTAL : `injector_total_full.py`, `INJECTOR_TOTAL_RELEVANCE_TEST.py`
- Pertinence : `injector_relevance.py`, `injector_relevance_test.py`
- GlyphNet : `glyphnet_codec.py`, `tests_glyphnet.py`, `bench_glyphnet_vs_codecs.py`, `corpus_text*.txt`
- SemCrypto : `semantic_crypto_v37.py`, `semantic_demo.py`, `verify_semantic_crypto.py`, `tests_semantic_crypto.py`
- Bench prompts : `prompts_shard_01.jsonl`, `prompts_shard_02.jsonl`, `prompts_shard_03.jsonl`, `run_benchmark_shard.py`, `merge_results.py`
- Audit run : `seed_matrix_runner.py`, `make_audit_archive.py`, `README_AUDIT_RUN_v57.md`
- CI (à déplacer) : `GITHUB_WORKFLOW_injector_total_full.yml`, `GITHUB_WORKFLOW_injector_relevance.yml`, `GITHUB_WORKFLOW_semcrypto.yml`

## Zero‑Claim
Aucun chiffre public tant que benchmarks publics *réels* et audit externe ne sont pas réalisés.
