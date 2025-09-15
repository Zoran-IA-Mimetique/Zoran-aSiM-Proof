# README_INJECTORS — Quickstart (v11)

## Comment utiliser les injecteurs
1) Choisir un injecteur **STEM** puis une **spécialisation** (audit/summary/bench).
2) Ajouter le bloc glyphique dans votre prompt système ou initial :
   `⟦STEM:injector⋄ΔM11.3:guard⋄ZDM:dual⋄IA2IA:glyphnet⟧`
3) Formuler la tâche cible (ex: "audite ce README et propose ERRATA.md").
4) **Tracer** : enregistrer le log JSON (ex: `injector_logs_example.json`) et signer via C2PA.

## Démo
```bash
python injector_stem_demo.py
# -> crée injector_logs_example.json
```
