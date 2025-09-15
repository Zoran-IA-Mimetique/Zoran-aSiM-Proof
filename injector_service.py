import requests, hashlib, json, os, time

TRUSTED_HASHES = set()  # populate via C2PA manifest check in production

def fetch_and_verify(url):
    # naive fetch, verify by hash if provided
    r = requests.get(url, timeout=10)
    content = r.text
    # in production: compute hash and compare to C2PA manifest
    return content

def produce_signed_prompt(content):
    # sanitize minimal: remove control characters, limit length
    s=''.join(ch for ch in content if ord(ch)>=32)
    s = s[:8000]
    # attach timestamp and simple integrity token (demo)
    token = hashlib.sha256((s+str(time.time())).encode('utf-8')).hexdigest()
    prompt = f"""⟦INJECTOR:timestamp={time.time()}⋄token={token}⟧\n{s}"""
    return prompt

if __name__=='__main__':
    print('Injector service ready (demo).')
