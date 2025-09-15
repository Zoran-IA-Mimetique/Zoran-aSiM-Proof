import json, glob
def load_logs():
    data=[]
    for f in glob.glob("MULTI_IA_DEMO_LOG*.json"):
        try: data.append(json.load(open(f)))
        except: pass
    return data
def analyze(reports):
    total=0; ok=0; per={}
    for r in reports:
        for e in r.get("logs",[]):
            total+=1; ok+=1 if e.get("understood") else 0
            a=e.get("agent","?"); per.setdefault(a,{"total":0,"ok":0})
            per[a]["total"]+=1; per[a]["ok"]+=1 if e.get("understood") else 0
    overall={"total":total,"ok":ok,"rate":(ok/total if total else 0)}
    agents={k:{"total":v["total"],"ok":v["ok"],"rate":(v["ok"]/v["total"] if v["total"] else 0)} for k,v in per.items()}
    return {"overall":overall,"agents":agents}
def main():
    r=load_logs()
    out=analyze(r)
    json.dump(out,open("MULTI_IA_STATS.json","w"),indent=2)
    print(json.dumps(out,indent=2))
if __name__=="__main__":
    main()
