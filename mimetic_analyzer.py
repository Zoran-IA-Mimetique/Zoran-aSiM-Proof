import json, math
def mean_sd(xs):
    n=len(xs); mu=sum(xs)/n if n else 0.0
    var=sum((x-mu)**2 for x in xs)/(n-1) if n>1 else 0.0
    return mu, var**0.5, n
def welch(m1,s1,n1,m2,s2,n2):
    se=((s1*s1)/n1 + (s2*s2)/n2)**0.5
    t=(m2-m1)/se if se>0 else 0.0
    num=((s1*s1)/n1 + (s2*s2)/n2)**2
    den=((s1*s1)/n1)**2/(n1-1) + ((s2*s2)/n2)**2/(n2-1) if n1>1 and n2>1 else 1.0
    df=num/den if den>0 else (n1+n2-2)
    return t,df
def cohen_d(m1,s1,n1,m2,s2,n2):
    sp2=(((n1-1)*s1*s1 + (n2-1)*s2*s2)/(n1+n2-2)) if (n1+n2-2)>0 else 0.0
    return (m2-m1)/(sp2**0.5) if sp2>0 else 0.0
def main():
    base=json.load(open("MIMETIC_RUNS_BASELINE.json"))
    inj=json.load(open("MIMETIC_RUNS_INJECTED.json"))
    report={}
    for m in ["success","length","structure_score","compliance_flags"]:
        b=[x[m] for x in base]; i=[x[m] for x in inj]
        m1,s1,n1=mean_sd(b); m2,s2,n2=mean_sd(i)
        t,df=welch(m1,s1,n1,m2,s2,n2); d=cohen_d(m1,s1,n1,m2,s2,n2)
        report[m]={"baseline":{"mean":m1,"sd":s1,"n":n1},"injected":{"mean":m2,"sd":s2,"n":n2},
                   "delta":m2-m1,"t":t,"df":df,"cohen_d":d}
    json.dump(report,open("MIMETIC_STATS.json","w"),indent=2)
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    main()
