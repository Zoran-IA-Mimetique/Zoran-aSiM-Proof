# py_glyphnet_bridge.py — bridge helpers
import json, os
from glyphnet_codec import encode, decode

def wrap_file(path: str, out_json: str):
    payload = open(path,"r",encoding="utf-8").read()
    msg = encode(payload)
    json.dump(msg, open(out_json,"w"), indent=2)

def unwrap_file(in_json: str, out_path: str):
    msg = json.load(open(in_json,"r"))
    text = decode(msg)
    open(out_path,"w",encoding="utf-8").write(text)
