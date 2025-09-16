# Zoran aSiM — MASTER RELEASE (v46, FLAT)
Date: 2025-09-16T00:24:00.102685Z

Ce pack rassemble **tout le nécessaire** pour une livraison publique : injecteur TOTAL avec pertinence, CI, benchs, mimétique, cryptage sémantique, gouvernance & conformité — **à la racine**, sans dossiers.

## Démarrage rapide
```bash
# Injecteur TOTAL (sécurité + pertinence)
export ZORAN_SIGN_KEY='zoran_demo_key'
python injector_total_full.py
python INJECTOR_TOTAL_RELEVANCE_TEST.py

# Tests globaux si présents
python test_all.py || true

# Démo cryptage sémantique si présents
export ZORAN_CLIENT_KEY='FranceTravail_demo_key'
python semantic_demo.py || true
python INJECTOR_CRYPTO_CLIENT_DEMO.py || true
```
Consultez `CHECKLIST_LIVRAISON.md` avant publication.
