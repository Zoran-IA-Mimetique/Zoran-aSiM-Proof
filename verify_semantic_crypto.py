import json,os
from semantic_crypto_v37 import detect
w=json.load(open('verification_report.json'))
print(json.dumps({'correct':w['detect_correct'],'wrong':w['detect_wrong']},indent=2))
