# MIT License
# Copyright (c) 2025
# eval_rag_delta.py : mesure simple des citations/grounding dans deux sorties
import re, sys, json, urllib.parse
def load(p): return open(p,"r",encoding="utf-8").read()

def extract_citations(s):
    # cherche [CITE:n] et "(source: ...)" et URLs
    tags = re.findall(r"\[CITE:(\d+)\]", s)
    urls = re.findall(r"https?://[^\s\)\]]+", s)
    domains = set()
    for u in urls:
        try:
            domains.add(urllib.parse.urlparse(u).netloc.lower())
        except: pass
    return {"tags": set(tags), "urls": urls, "domains": sorted(domains)}

def sentence_split(s):
    return [x.strip() for x in re.split(r"[.!?]\s+", s) if x.strip()]

def cited_sentence_ratio(s):
    sents = sentence_split(s)
    if not sents: return 0.0
    cited = sum(1 for x in sents if "[CITE:" in x or "http" in x or "(source:" in x.lower())
    return round(cited/len(sents),4)

def metrics(s):
    cit = extract_citations(s)
    return {
        "num_citation_tags": len(cit["tags"]),
        "num_urls": len(cit["urls"]),
        "num_domains": len(cit["domains"]),
        "domains": cit["domains"],
        "cited_sentence_ratio": cited_sentence_ratio(s)
    }

def main():
    if len(sys.argv)!=3:
        print("usage: python eval_rag_delta.py with.txt without.txt"); sys.exit(1)
    w, wo = load(sys.argv[1]), load(sys.argv[2])
    mw, mwo = metrics(w), metrics(wo)
    delta = {k: (mw[k]-mwo[k]) if isinstance(mw[k], (int,float)) else None for k in mw if k!="domains"}
    pct = {k: ((delta[k]/mwo[k]*100.0) if isinstance(mwo[k], (int,float)) and mwo[k]!=0 else None) for k in delta}
    out = {"with":mw,"without":mwo,"delta_abs":delta,"delta_pct":pct}
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__=="__main__": main()
