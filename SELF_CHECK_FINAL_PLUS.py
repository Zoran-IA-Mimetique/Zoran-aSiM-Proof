import json, os, hashlib, glob

REQ = [
 'README_CLIENT_SUMMARY.md','README_CLIENT_FINAL.md','README_AUDIT_FINAL.md',
 'AUDIT_READY_MANIFEST.json','SELF_CHECK_FINAL.py'
]

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for ch in iter(lambda: f.read(8192), b''):
            h.update(ch)
    return h.hexdigest()

def main():
    report={'present':[],'missing':[],'notes':[]}
    for f in REQ:
        (report['present'] if os.path.isfile(f) else report['missing']).append(f)
    # if manifest present, verify two or three entries exist
    try:
        man=json.load(open('AUDIT_READY_MANIFEST.json'))
        files=[e['name'] for e in man.get('files',[])][:5]
        report['notes'].append({'manifest_entries_sample':files})
    except Exception as e:
        report['notes'].append({'manifest_error':str(e)})
    json.dump(report, open('SELF_CHECK_FINAL_PLUS_REPORT.json','w'), indent=2)
    print(json.dumps(report, indent=2))

if __name__=='__main__':
    main()
