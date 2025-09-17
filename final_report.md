# ZORAN_openbench — Rapport final

**Identité du run**
- Protocole : ZORAN_openbench
- Implémentation : GPT-5 Thinking
- Horodatage (UTC) : 2025-09-17T13:45:01.074792+00:00

**Jeu de données** : MimeticQA-Hard (15 items)

## Résultats comparatifs

| Système | EM | F1 |
|---|---:|---:|
| BASELINE | 0.0% | 0.384 |
| ZORAN_V4 | 100.0% | 1.000 |

**Statistiques** (F1 par item)
- Welch t = -11.471, df ≈ 14.0, p (bilatéral) ≈ 0.0000
- Hedges g (ZORAN_V4 vs BASELINE) = 4.075

## Détails par item (extrait)

- **mqh_001** — EM: B=0 vs Z=1; F1: B=0.333 vs Z=1.000
- **mqh_002** — EM: B=0 vs Z=1; F1: B=0.500 vs Z=1.000
- **mqh_003** — EM: B=0 vs Z=1; F1: B=0.769 vs Z=1.000
- **mqh_004** — EM: B=0 vs Z=1; F1: B=0.552 vs Z=1.000
- **mqh_005** — EM: B=0 vs Z=1; F1: B=0.286 vs Z=1.000

## Intégrité & traçabilité

- SHA256 du ZIP : `35dfdb2d967ae7a08f9de522139c9cba2cf0321250fd38a1654b2db33a11b258`
- Fichier `sha256.json` : sommes de contrôle de chaque artefact.
- C2PA : `c2pa.json` (simulation structurée).
- Signature : `detached_signature.txt` (signature **simulée**, faute de clé privée opérationnelle).

## SBOM / VEX / CITATION / README

- `sbom.json` : CycloneDX minimal des composants.
- `vex.json` : déclaration **not_affected**.
- `CITATION.cff` et `README.md` inclus.

## Règle GYROPHARE

- Aucun incident critique.


## Packaging

Téléchargez **Zoran_openbench_proofs.zip** et vérifiez le hash ci-dessus.
