# Injector Crypto Policy — v35
Date: 2025-09-15T23:48:59.751802Z

## Objectif
Permettre à un client (ex. France Travail) de générer, via un injecteur cellule souche, **un langage crypté qui lui est propre**, non accessible par l’éditeur de Zoran.

## Principes
- Chaque client dispose d’un **injecteur cellule souche** qui se spécialise en "langage crypté".
- Le langage généré est **unique au client** (non partagé, non réutilisable).
- Le protocole peut être basé sur **GlyphNet**, **QuantaGlottal** ou un codec custom, avec **clé privée du client**.
- **Zoran** ne voit pas le contenu final : il fournit la mécanique d’injection, pas la clé de lecture.

## Exemple (schématique)
```
Injecteur cellule souche → spécialisation France Travail
Message généré : ⟦FT:enc::a8d9fh3…==⟧
→ seul France Travail peut décoder avec sa clé privée
```
## Garanties
- **Confidentialité totale** : le contenu est opaque hors de France Travail.
- **RGPD** : les données ne sortent pas du périmètre client.
- **AI Act** : alignement par design (Zero‑Claim, auditabilité mécanique).
- **Droit d’auteur** : le protocole crypté est propriété du client.

## Auditabilité
- Ce qui est auditable : la **mécanique** (injecteur, schéma, signatures).
- Ce qui ne l’est pas : le **contenu crypté** (reste propriété du client).
