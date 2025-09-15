import json, time

def run():
    out={
        "meta":{"created": time.time(),"note":"HUMBLE ONLY demo"},
        "reasoning":{"baseline":80.0,"zoran":90.0,"n":72,"energy_proxy":1.05},
        "stability":{"baseline":0.30,"zoran":0.18},
        "glyphnet":{"ratio":1.2,"note":"mixed non-repetitive corpus"},
        "compliance":{"score":0.0,"requires_files":{}},
        "pertinence_composite":None
    }
    with open("metrics_humble.json","w") as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))

if __name__=="__main__": run()
