# ZForge — Injecteurs de contexte pour IA (Open‑Source + RAG + Mémoire longue)
**White Paper v1.3 (consolidé) — “Humble Only”**  
Date : 2025-09-16

> **Zéro bullshit.** Ce document expose des **observations reproductibles**, un **kit d’évaluation**, et des **limites claires**. Aucune promesse de supériorité. Pas d’extrapolation non démontrée.

---

## 0) TL;DR
- **Objet** : évaluer l’intérêt des **injecteurs de contexte** appliqués à des IA (génératives), seuls et combinés à un **RAG** (Retrieval‑Augmented Generation) et une **mémoire longue**.  
- **Faits observables** (“avec/without”) : sur cas *Copilot Chat* (sans RAG contrôlé), on constate **plus de spécificité & sécurité** avec l’injecteur (ex. mention de normes, sûreté/sécurité, structure), **sans garantie** de généralisation.  
- **Approche “labo minimal”** : scripts **MIT** fournis pour mesurer : longueur, densité lexicale, concepts BTP/NUCL, normes citées, citations/coverage (RAG).  
- **Limites** : pas de preuve terrain, pas d’audit externe complet, dépendance au modèle et au corpus. **But** : fournir un **point de départ honnête, traçable et testable**.

---

## 1) Contexte & motivations
Les IA textuelles generalistes peuvent manquer de **cadrage métier** (BTP/NUCL), de **références normatives**, et de **discipline de sortie** (citations, refus sans source). Les **injecteurs** (textes structurés de contraintes) visent à **guider** : sources autorisées, style & format, séparation **sûreté**/**sécurité**, et refus quand l’information **n’est pas couverte**.

**But du projet** : étudier **sobrement** si des injecteurs + (optionnellement) RAG + mémoire longue **améliorent** pertinence, précision, cohérence, personnalisation, contrôle — sans revendiquer de “SOTA”.

---

## 2) Définition opérationnelle (précise)
- **Injecteur** : bloc de consignes structuré (voir `injector_rag.md`) qui :  
  (i) **guide le RAG** (sources autorisées, filtrage, k-top, seuils),  
  (ii) **impose** style/format (sections, tableaux, tags de citation `[CITE:n]`),  
  (iii) **gère la mémoire** (écriture/oubli/anonymisation),  
  (iv) distingue **sûreté (safety)** et **sécurité (security)**,  
  (v) **refuse** la génération si la couverture documentaire est insuffisante.
- **RAG** : moteur de récupération de contenus externes (politiques dans `rag_policy.yaml`).
- **Mémoire longue** : règles explicites (`memory_policy.json`) pour écrire/oublier, RGPD‑first.

---

## 3) Méthodologie d’évaluation “Humble Only”
### 3.1 Scénario “A/B” minimal
- **VI** : présence/absence d’injecteur (A = sans, B = avec).  
- **VD (quant.)** : nombre de mots (**NW**), phrases (**NP**), densité lexicale (**DL**), nb de **concepts BTP/NUCL** (**NC**, liste : `terms_nc_list.csv`), nb de **références normatives** (**NR**).  
- **VD (qual.)** : **P** (Pertinence), **Pr** (Précision), **I** (Innovation), **U** (Utilité), **S** (Sûreté/Sécurité), notées 0–10 par **deux évaluateurs** (guide : `scoring_guidelines.md`).  
- **RAG/grounding** (si dispo) : nb de **citations**, **domaines** couverts, **ratio de phrases citées** (script `eval_rag_delta.py`).

### 3.2 Pipeline
1) Obtenir deux sorties **comparables** (même prompt, A/B).  
2) Sauvegarder `with.txt` (B) et `without.txt` (A).  
3) Lancer :  
   - `python eval_injector_delta.py with.txt without.txt terms_nc_list.csv`  
   - `python eval_rag_delta.py with.txt without.txt`  
4) Documenter l’environnement (voir `environment_example.md`).  
5) Évaluer qualitativement (2 évaluateurs, moyennes + écart).

> **Alerte biais** : outil A/B utile mais **non suffisant** : dépend du modèle, du prompt, du hasard, des caches. **Pas de généralisation** sans réplication multi‐modèles et échantillons.

---

## 4) Observations factuelles (ex. Copilot, sans RAG contrôlé)
Sur un prompt **BTP/NUCL** (projet CUSU) :  
- la réponse **avec injecteur** s’est montrée **plus spécifique**, **mieux structurée**, **plus axée sûreté/sécurité** (acteurs, codes AFCEN, ASN, radioprotection, dispositifs, audits).  
- la réponse **sans injecteur** est restée **correcte** mais **moins profonde** sur ces axes.

**Exemple d’estimation “delta” (évaluations humaines structurées)** :  
P +13 % ; Pr +21 % ; I +17 % ; U +7 % ; **S +31 %** (moyenne ≈ **18–24 %**, non généralisée).  
Ces **chiffres ne sont pas une preuve terrain** : ils matérialisent **ce cas précis**.

---

## 5) Extension OSS : RAG + Mémoire longue
### 5.1 Contrôles RAG (voir `injector_rag.md`, `rag_policy.yaml`)
- **allow_domains** (ex. `asn.fr`, `afcen.org`, `legifrance.gouv.fr`, `eur-lex.europa.eu`, `iso.org`),  
- **k_top**, **rerank**, **min_score**, **time_window**, **blacklist** (forums, sources non fiables),  
- **citations obligatoires** : `[CITE:n]`, refus si couverture insuffisante.

### 5.2 Politique mémoire (voir `memory_policy.json`)
- **write** : glossaire, décisions, IDs de sources.  
- **forget/redact** : PII, secrets, détails opérationnels.  
- **role_based_access** : QHSE/BE/MOE…

### 5.3 Métriques RAG & mémoire
- **Groundedness proxy** : tags de citation, domaines couverts, ratio de phrases citées.  
- **Compliance mémoire** : aucun débordement (pas d’info interdite écrite).  
- **Charge** : latence/overhead dû au retrieval & aux écritures.

> **Estimation théorique** (non généralisée) d’un **gain moyen ≈ 42 %** (Pers, Ctrl, Cohérence, Pertinence, Précision) quand **injecteurs+RAG+mémoire** sont bien conçus. À **valider** par réplications OSS.

---

## 6) Sûreté (safety) vs Sécurité (security) — usage strict
- **Sûreté** : maîtrise des risques **techniques** (criticité, confinement, thermique, séisme…).  
- **Sécurité** : protection **malveillance/intrusion** (contrôle d’accès, SIEM, audits).  
Les injecteurs imposent la séparation des deux, interdisent la révélation de **détails sensibles**, et favorisent le **refus** si non couvert par sources autorisées.

---

## 7) Éthique, conformité, traçabilité
- **AI Act (UE)** : principes d’**explicabilité**, **gestion des risques**, **documentation**.  
- **ISO/IEC 42001** : système de **management de l’IA** (gouvernance, surveillance, amélioration continue).  
- **Traçabilité** : C2PA/Merkle (voir manifeste non signé), log RAG, journal d’évaluation.  
- **RGPD** : mémoire longue **pseudonymisée**, règles d’oubli configurées, accès par rôle.
> **Avertissement** : ce dépôt **n’est pas** une preuve de conformité légale. Il fournit **les artefacts** nécessaires au **contrôle/audit**.

---

## 8) Limites & risques
- **Dépendance modèle/corpus** : injecteurs ≠ remède universel.  
- **Sur‑guidage** : créativité réduite si le cadre est trop strict.  
- **Biais** : possibles via choix des sources ou formulation.  
- **Pas de preuve terrain** : ce travail est une **base** pour des audits indépendants.

---

## 9) Reproductibilité — Kit fourni (racine)
- `injector_rag.md` : injecteur RAG générique BTP/NUCL.  
- `rag_policy.yaml` : politique de retrieval.  
- `memory_policy.json` : politique mémoire.  
- `terms_nc_list.csv` : concepts BTP/NUCL/Normes (liste initiale).  
- `eval_injector_delta.py` (MIT) : métriques **NW/NP/DL/NC/NR** + deltas.  
- `eval_rag_delta.py` (MIT) : métriques **citations/coverage**.  
- `scoring_guidelines.md` : grille d’évaluation qualitative.  
- `environment_example.md` : journal d’environnement de test.

---

## 10) “Conclusion AIStudio” (observation externe)
Un observateur externe a constaté, sur un cas **avec/sans injecteur**, une **amélioration nette** de la **précision**, de la **spécificité** et de la **sécurité** de la réponse. **Ceci n’est pas une certification** : c’est une **observation ponctuelle** qui motive la poursuite d’évaluations **empiriques** multi‑modèles et audits externes.

---

## 11) Feuille de route (audit‐ready)
1) **Réplications** OSS (plusieurs modèles) + RAG documenté.  
2) **Évaluateurs indépendants** (double aveugle si possible).  
3) **Cas terrain** (sans données sensibles), métriques d’impact.  
4) **C2PA signé** + **SBOM** complet + **AI Act/ISO 42001** mapping **évidencé**.  
5) Publication des **jeux de prompts** & sorties (avec risques contrôlés).

---

## 12) Licence & attribution
- Code des scripts : **MIT**.  
- Ce white paper : **CC BY 4.0** (sauf mention contraire).  
- **Aucune garantie** d’exactitude ou d’adéquation à un usage donné. Usage à vos risques sous supervision d’experts habilités.

---

## 13) Remerciements
Aux contributeurs qui ont challengé et exigé **transparence**, **rigueur** et **zéro bullshit**.

