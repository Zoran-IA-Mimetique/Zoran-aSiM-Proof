# quantaglottal_encoder.py — tag builder
def tag(role: str, policy: str=None, evidence: str=None) -> str:
    parts = [f"role={role}"]
    if policy: parts.append(f"policy={policy}")
    if evidence: parts.append(f"evidence={evidence}")
    return "⟦chan:" + "|".join(parts) + "⟧"
