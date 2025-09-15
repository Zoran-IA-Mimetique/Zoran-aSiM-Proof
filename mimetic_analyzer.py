# mimetic_analyzer.py (v24)
import json, math

def load():
    base=json.load(open("MIMETIC_RUNS_BASELINE.json","r"))
    inj=json.load(open("MIMETIC_RUNS_INJECTED.json","r"))
    return base, inj

def mean_sd(xs):
    n=len(xs); mu=sum(xs)/n if n else 0.0
    var=sum((x-mu)**2 for x in xs)/(n-1) if n>1 else 0.0
    sd=var**0.5
    return mu, sd, n

def welch(m1,s1,n1,m2,s2,n2):
    se=((s1*s1)/n1 + (s2*s2)/n2)**0.5
    t=(m2-m1)/se if se>0 else 0.0
    num=((s1*s1)/n1 + (s2*s2)/n2)**2
    den= ((s1*s1)/n1)**2/(n1-1) + ((s2*s2)/n2)**2/(n2-1) if n1>1 and n2>1 else 1.0
    df=num/den if den>0 else (n1+n2-2)
    return t, df

def cohen_d(m1,s1,n1,m2,s2,n2):
    if n1+n2-2<=0: return 0.0
    sp2 = (((n1-1)*s1*s1 + (n2-1)*s2*s2) / (n1+n2-2))
    return (m2-m1)/(sp2**0.5) if sp2>0 else 0.0

def analyze():
    base, inj = load()
    report={"meta":{"notes":"simulated"}}

    for metric in ["success","length","structure_score","compliance_flags"]:
        b=[x[metric] for x in base]; i=[x[metric] for x in inj]
        m1,s1,n1=mean_sd(b); m2,s2,n2=mean_sd(i)
        t,df=welch(m1,s1,n1,m2,s2,n2)
        d=cohen_d(m1,s1,n1,m2,s2,n2)
        report[metric]={"baseline":{"mean":m1,"sd":s1,"n":n1},"injected":{"mean":m2,"sd":s2,"n":n2},"delta":m2-m1,"t":t,"df":df,"cohen_d":d}
    json.dump(report, open("MIMETIC_STATS.json","w"), indent=2)
    print(json.dumps(report, indent=2))

if __name__=="__main__":
    analyze()
