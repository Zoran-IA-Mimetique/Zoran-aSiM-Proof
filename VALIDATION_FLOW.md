# Validation Flow — v26

1. Developer commit → CI triggers
2. CI runs injectors strict tests, SHA check, artifacts upload
3. Auditor downloads pack → runs SELF_CHECK_FINAL.py
4. Auditor fills CHECKLIST_AUDITOR.md
5. Auditor writes AUDIT_LOG.json (using template)
6. Ethics board fills ETHICS_REVIEW_TEMPLATE.md
7. Security team fills SECURITY_CHECKLIST.md
8. EURO‑5 checklist filled & signed
9. Release packaged with generate_release.py + signed manifest
10. Publication with PAPER_TEMPLATE_IMRAD.md or equivalent
