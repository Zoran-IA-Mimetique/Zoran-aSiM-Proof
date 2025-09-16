import os,json,hashlib
from semantic_crypto_v37 import embed,detect
key=os.environ.get('ZORAN_CLIENT_KEY','FranceTravail_demo_key')
base='We start to show how an idea can help small teams begin a project and end with a secure summary.'
wm,stats=embed(base,key); open('sample_text_zoranX.txt','w').write(wm)
rep={'embed':stats,'detect_correct':detect(wm,key),'detect_wrong':detect(wm,'wrong')}
json.dump(rep,open('verification_report.json','w'),indent=2); print('wrote verification_report.json')
