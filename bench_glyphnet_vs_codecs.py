import gzip,lzma,time,base64,zlib,os,json
MAGIC="Z5::"
def glyphnet_encode(t): return MAGIC+base64.b64encode(zlib.compress(t.encode('utf-8'),9)).decode('ascii')
def glyphnet_decode(s): assert s.startswith(MAGIC); return zlib.decompress(base64.b64decode(s[len(MAGIC):].encode('ascii'))).decode('utf-8')
def main():
    files=[f for f in os.listdir('.') if f.startswith('corpus_text')]
    out={}
    for f in files:
        raw=open(f,'rb').read(); txt=raw.decode('utf-8','ignore')
        t0=time.time(); enc=glyphnet_encode(txt); t1=time.time(); dec=glyphnet_decode(enc); t2=time.time()
        out[f]={"glyphnet":{"size":len(enc.encode()),"enc_ms":(t1-t0)*1000,"dec_ms":(t2-t1)*1000,"ok":dec==txt},
                "gzip":{"size":len(gzip.compress(raw,9))}, "xz":{"size":len(lzma.compress(raw,preset=9))}}
    json.dump(out,open('BENCH_GLYPHNET_REPORT.json','w'),indent=2); print("wrote BENCH_GLYPHNET_REPORT.json")
if __name__=='__main__': main()
