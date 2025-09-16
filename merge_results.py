import json,glob,math
def summ(rows,field):
    xs=[r[field] for r in rows]; n=len(xs); mu=sum(xs)/n if n else 0.0; var=sum((x-mu)**2 for x in xs)/(n-1) if n>1 else 0.0
    return mu,(var**0.5),n
base=[]; inj=[]
for f in glob.glob('BASE_*.json'): base+=json.load(open(f))
for f in glob.glob('INJ_*.json'): inj+=json.load(open(f))
def welch(m1,s1,n1,m2,s2,n2):
    se=((s1*s1)/n1 + (s2*s2)/n2)**0.5; t=(m2-m1)/se if se>0 else 0.0; return {'t':t,'df':n1+n2-2}
out={'metrics':[]}
for field in ['ok','pertinence']:
    m1,s1,n1=summ(base,field); m2,s2,n2=summ(inj,field); stat=welch(m1,s1,n1,m2,s2,n2)
    out['metrics'].append({'field':field,'baseline':{'mean':m1,'sd':s1,'n':n1},'injected':{'mean':m2,'sd':s2,'n':n2},'delta':m2-m1,**stat})
json.dump(out,open('BENCH_STATS_GLOBAL.json','w'),indent=2); print('wrote BENCH_STATS_GLOBAL.json')
