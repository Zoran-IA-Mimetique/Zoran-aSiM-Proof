# Watermark sémantique vs Chiffrement fort (v41, Flat)
Date: 2025-09-16T00:09:06.143086Z

| Propriété        | Watermark sémantique (v37) | Chiffrement fort (AES/KMS) |
|------------------|----------------------------|----------------------------|
| But              | Provenance/identification  | Confidentialité            |
| Lisibilité       | Lisible humain             | Illisible sans clé         |
| Vérification     | Taux de correspondance clé | Déchiffrement              |
| Robustesse bruit | Moyenne (mutations légères)| Haute (intégrité)          |
| Clés             | Client                      | KMS/gestion clés           |
| Cas d'usage      | Traçabilité IA↔IA          | Secret/protection données  |

**Conclusion** : Combiner watermark (provenance) **+** chiffrement (confidentialité) côté client.
