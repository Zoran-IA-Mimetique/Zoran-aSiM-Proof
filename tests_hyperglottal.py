# tests_hyperglottal.py
from hyperglottal_encoder import build
s = build("auditor","check claims",["zero-claim","evidence-first"],"file://CLAIMS_AUDIT.md")
assert s.startswith("#HG v20")
print("HYPERGLOTTAL OK")
