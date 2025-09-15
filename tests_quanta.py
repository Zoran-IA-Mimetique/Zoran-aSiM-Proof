# tests_quanta.py
from quantaglottal_encoder import tag
t = tag("audit","zero-claim","CLAIMS_AUDIT.md")
assert t.startswith("⟦chan:") and "role=audit" in t
print("QUANTA-GLOTTAL OK")
