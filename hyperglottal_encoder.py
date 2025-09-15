# hyperglottal_encoder.py — simple block builder
def build(role: str, task: str, policy=None, evidence=None) -> str:
    lines = ["#HG v20", f"ROLE: {role}", f"TASK: {task}"]
    if policy: lines.append("POLICY: " + ",".join(policy))
    if evidence: lines.append("EVIDENCE: " + evidence)
    lines.append("END")
    return "\n".join(lines)
