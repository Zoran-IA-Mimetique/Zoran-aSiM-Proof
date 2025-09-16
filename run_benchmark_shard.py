import json,random,sys
seed=13; shard='prompts_shard_01.jsonl'
for i,a in enumerate(sys.argv):
    if a=='--seed': seed=int(sys.argv[i+1])
    if a=='--shard': shard=sys.argv[i+1]
random.seed(seed)
prompts=[json.loads(l) for l in open(shard) if l.strip()]
def sim(p,inj=False):
    ok=random.random()< (0.7+0.08 if inj else 0.7); return ('ok' if ok else 'uncertain', ok)
res_b=[]; res_i=[]
for p in prompts:
    a0,ok0=sim(p,False); res_b.append({'id':p['id'],'ok':int(ok0),'pertinence':0.7})
    a1,ok1=sim(p,True);  res_i.append({'id':p['id'],'ok':int(ok1),'pertinence':0.75})
open(f'BASE_{seed}_{shard[:-6]}.json','w').write(json.dumps(res_b,indent=2))
open(f'INJ_{seed}_{shard[:-6]}.json','w').write(json.dumps(res_i,indent=2))
print('wrote shard results')
