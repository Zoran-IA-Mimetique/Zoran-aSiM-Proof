
"""sign_kms_wrapper.py
Wrapper that prefers AWS KMS signing (asymmetric) if configured via env vars.
Falls back to HMAC signing for demo mode.
Usage:
  export SIGN_MODE=kms  # or 'hmac'
  export AWS_KMS_KEY_ID=...  (for kms)
  export AWS_REGION=...
  export ZORAN_SIGN_KEY=...  (for hmac fallback)
Functions:
  sign_bytes(bytes) -> signature_hex
  verify_bytes(bytes, signature) -> bool   (for HMAC only)
"""
import os, hashlib, hmac
MODE = os.environ.get("SIGN_MODE","hmac")
if MODE=="kms":
    try:
        import boto3, base64
        AWS_REGION = os.environ.get("AWS_REGION")
        KMS_KEY_ID = os.environ.get("AWS_KMS_KEY_ID")
        kms_client = boto3.client("kms", region_name=AWS_REGION) if AWS_REGION else boto3.client("kms")
    except Exception as e:
        kms_client = None
        MODE = "hmac"
        # print fallback
def hmac_sign(key_bytes, payload_bytes):
    return hmac.new(key_bytes, payload_bytes, hashlib.sha256).hexdigest()

def sign_bytes(payload_bytes: bytes) -> str:
    if MODE=="kms" and 'kms_client' in globals() and kms_client is not None:
        # Use KMS Sign API (RSA or ECDSA). Here we simulate: use KMS to sign with KeyId
        resp = kms_client.sign(KeyId=os.environ.get("AWS_KMS_KEY_ID"), Message=payload_bytes, MessageType='RAW', SigningAlgorithm='RSASSA_PSS_SHA_256')
        sig = resp['Signature']
        return base64.b64encode(sig).decode('utf-8')
    else:
        key = os.environ.get("ZORAN_SIGN_KEY","zoran_demo_key").encode('utf-8')
        return hmac_sign(key, payload_bytes)

def verify_hmac(payload_bytes: bytes, signature_hex: str) -> bool:
    key = os.environ.get("ZORAN_SIGN_KEY","zoran_demo_key").encode('utf-8')
    return hmac_sign(key, payload_bytes) == signature_hex

if __name__=='__main__':
    import sys, json
    data = sys.stdin.read().encode('utf-8') if sys.stdin.readable() else b'example'
    sig = sign_bytes(data)
    print(json.dumps({'mode': MODE, 'signature': sig}))
