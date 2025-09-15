import gzip, lzma, time, base64, zlib, os, json

MAGIC="Z5::"
def glyphnet_encode(text:str)->str:
    return MAGIC+base64.b64encode(zlib.compress(text.encode("utf-8"),9)).decode("ascii")
def glyphnet_decode(s:str)->str:
    assert s.startswith(MAGIC)
    return zlib.decompress(base64.b64decode(s[len(MAGIC):].encode("ascii"))).decode("utf-8")

def compress_gzip(data:bytes)->bytes: return gzip.compress(data,9)
def decompress_gzip(data:bytes)->bytes: return gzip.decompress(data)
def compress_xz(data:bytes)->bytes: return lzma.compress(data,preset=9)
def decompress_xz(data:bytes)->bytes: return lzma.decompress(data)

def bench_bytes(name, raw):
    text=raw.decode("utf-8","ignore")
    report={}
    # GlyphNet
    t0=time.time(); enc=glyphnet_encode(text); t1=time.time()
    dec=glyphnet_decode(enc); t2=time.time()
    ok = dec==text
    report["glyphnet"]={"size":len(enc.encode("utf-8")),"enc_ms":(t1-t0)*1000,"dec_ms":(t2-t1)*1000,"ok":ok}
    # gzip
    t0=time.time(); g=compress_gzip(raw); t1=time.time(); dr=decompress_gzip(g); t2=time.time()
    report["gzip"]={"size":len(g),"enc_ms":(t1-t0)*1000,"dec_ms":(t2-t1)*1000,"ok":dr==raw}
    # xz
    t0=time.time(); x=compress_xz(raw); t1=time.time(); dx=decompress_xz(x); t2=time.time()
    report["xz"]={"size":len(x),"enc_ms":(t1-t0)*1000,"dec_ms":(t2-t1)*1000,"ok":dx==raw}
    return name, report

def main():
    files=[f for f in os.listdir(".") if f.endswith(".txt") or f.endswith(".md")]
    out={}
    for f in files:
        try:
            raw=open(f,"rb").read()
            k,v = bench_bytes(f, raw)
            out[k]=v
        except Exception as e:
            out[f]={"error":str(e)}
    json.dump(out, open("BENCH_GLYPHNET_REPORT.json","w"), indent=2)
    print(json.dumps(out, indent=2))

if __name__=="__main__":
    main()
