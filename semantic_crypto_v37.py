import re,hmac,hashlib
PAIRS=[("start","begin"),("end","finish"),("big","large"),("small","little")]
WORD_RE=re.compile(r"\b\w+\b")
def _bits(key,text,nbits):
    data=hmac.new(key,text.encode(),hashlib.sha256).digest(); out=[]
    while len(out)<nbits:
        for byte in data:
            for i in range(8):
                out.append((byte>>i)&1); 
                if len(out)>=nbits: break
            if len(out)>=nbits: break
        data=hashlib.sha256(data).digest()
    return out[:nbits]
def embed(text,key):
    keyb=key.encode(); tokens=WORD_RE.findall(text); lower=[t.lower() for t in tokens]
    pos=[]; 
    for i,t in enumerate(lower):
        for pi,(w0,w1) in enumerate(PAIRS):
            if t==w0 or t==w1: pos.append((i,pi)); break
    bits=_bits(keyb,text,len(pos)); out=tokens[:]
    for (i,pi),b in zip(pos,bits):
        w0,w1=PAIRS[pi]; orig=out[i]; des=w0 if b==0 else w1; out[i]=des.capitalize() if orig and orig[0].isupper() else des
    i=0
    def repl(m): 
        nonlocal i
        r=out[i]; i+=1; return r
    import re as _re
    return _re.sub(WORD_RE,repl,text), {"candidates":len(pos),"applied":len(pos)}
def detect(text,key):
    keyb=key.encode(); tokens=WORD_RE.findall(text.lower()); obs=[]
    for t in tokens:
        for w0,w1 in PAIRS:
            if t==w0: obs.append(0); break
            if t==w1: obs.append(1); break
    exp=_bits(keyb,text,len(obs)); matches=sum(1 for o,e in zip(obs,exp) if o==e)
    return {"observed_bits":len(obs),"matches":matches,"rate": (matches/len(obs) if obs else 0.0)}
