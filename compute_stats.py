# compute_stats.py (v55) — compare baseline vs injected (accuracy & pertinence)
import json, math

def read(path):
    return json.load(open(path,"r",encoding="utf-8"))

def welch(m1,s1,n1,m2,s2,n2):
    se=((s1*s1)/n1 + (s2*s2)/n2)**0.5
    t=(m2-m1)/se if se>0 else 0.0
    num=((s1*s1)/n1 + (s2*s2)/n2)**2
    den=((s1*s1)/n1)**2/(n1-1) + ((s2*s2)/n2)**2/(n2-1) if n1>1 and n2>1 else 1.0
    df=num/den if den>0 else (n1+n2-2)
    return t, df

def cohend(m1,s1,n1,m2,s2,n2):
    if n1+n2-2<=0: return 0.0
    sp2=(((n1-1)*s1*s1 + (n2-1)*s2*s2)/(n1+n2-2))
    return (m2-m1)/(sp2**0.5) if sp2>0 else 0.0

def summarize(rows, field):
    xs=[r[field] for r in rows]
    n=len(xs)
    mu=sum(xs)/n if n else 0.0
    var=sum((x-mu)**2 for x in xs)/(n-1) if n>1 else 0.0
    sd=var**0.5
    return mu, sd, n

def main():
    base=read("BENCH_RESULTS_BASELINE.json"); inj=read("BENCH_RESULTS_INJECTED.json")
    out={"metrics":[]}
    for field in ["ok","pertinence"]:
        m1,s1,n1=summarize(base, field)
        m2,s2,n2=summarize(inj, field)
        t,df=welch(m1,s1,n1,m2,s2,n2)
        d=cohend(m1,s1,n1,m2,s2,n2)
        out["metrics"].append({"field":field,"baseline":{"mean":m1,"sd":s1,"n":n1},
                               "injected":{"mean":m2,"sd":s2,"n":n2},
                               "delta":m2-m1,"t":t,"df":df,"cohen_d":d})
    json.dump(out, open("BENCH_STATS.json","w"), indent=2)
    print(json.dumps(out, indent=2))

if __name__=="__main__":
    main()
