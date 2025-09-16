# FAQ France Travail — v51 (Flat)
Date : 2025-09-16T00:34:54.427975Z

## Technique
**Q : L’injecteur peut‑il modifier le LLM sous‑jacent ?**  
R : Non, il agit en **surcouche**. Il filtre, évalue et trace, mais n’altère pas le modèle.  

**Q : Les clés cryptographiques sont‑elles visibles par Zoran ?**  
R : Non. Elles sont gérées côté client (KMS/env).  

## Juridique
**Q : Respectez‑vous le RGPD ?**  
R : Oui. Pas de données personnelles traitées, governance ERRATA+Zero‑Claim intégrée.  

**Q : Quid du droit d’auteur ?**  
R : Corpus = sources publiques/licences ouvertes. Aucun contenu protégé n’est réutilisé.  

## Gouvernance
**Q : Qui valide la pertinence des réponses ?**  
R : L’injecteur applique des seuils déterministes ; l’auditeur externe valide les métriques.  

**Q : Comment tracer la conformité ?**  
R : Tous les artefacts (JSON, SHA, manifests) sont livrés audit‑ready.  
