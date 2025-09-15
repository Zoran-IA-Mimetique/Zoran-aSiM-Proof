import json, re, base64, zlib, time

HEADER = "Z5::"

def encode(text: str) -> str:
    comp = zlib.compress(text.encode("utf-8"), 9)
    return HEADER + base64.b64encode(comp).decode("ascii")

def decode(payload: str) -> str:
    assert payload.startswith(HEADER), "Invalid header"
    data = base64.b64decode(payload[len(HEADER):].encode("ascii"))
    return zlib.decompress(data).decode("utf-8")

FORBIDDEN = [r"rm\s+-rf", r"import\s+os", r"open\("]

def validate_prompt(p: str):
    if len(p) > 10000: 
        return False, "too long"
    for pat in FORBIDDEN:
        if re.search(pat, p, flags=re.IGNORECASE):
            return False, f"forbidden: {pat}"
    if re.search(r"[^\x20-\x7E\n]", p):
        return False, "non-ascii/control char"
    return True, "ok"

def main():
    cases = [
        "safe content with glyphs ⟦ΔM11.3:rollback⟧".encode("utf-8","ignore").decode("utf-8"),
        "rm -rf /",
        "import os; os.system('echo hack')",
        "normal ASCII text"
    ]
    results = []
    for c in cases:
        enc = encode(c)
        dec = decode(enc)
        ok, why = validate_prompt(dec)
        results.append({
            "input": c[:80],
            "roundtrip_ok": (dec == c),
            "validate_ok": ok,
            "reason": why
        })
    out = {"meta":{"created": time.time()}, "results": results}
    with open("test_injector_results.json","w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
