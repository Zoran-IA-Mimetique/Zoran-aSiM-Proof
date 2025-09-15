import json, time, random, os
try:
    import psutil
except Exception:
    psutil = None

def energy_proxy(duration=2.0):
    if psutil is None:
        return {'method':'fallback','cpu_avg':None,'duration':duration}
    samples=[]; t0=time.time()
    while time.time()-t0<duration:
        samples.append(psutil.cpu_percent(interval=0.2))
    return {'method':'psutil','cpu_avg': sum(samples)/len(samples),'duration':duration}

def main():
    random.seed(13)
    # simulate baseline and zoran metrics
    base= random.uniform(60,80)
    zoran= base + random.uniform(0,10)
    energy= energy_proxy(2.0)
    out = {'meta':{'time':time.time(),'note':'HUMBLE ALLIN v1'}, 'reasoning':{'baseline':base,'zoran':zoran}, 'energy':energy}
    with open('metrics_humble_psutil.json','w') as f:
        json.dump(out,f,indent=2)
    print('Wrote metrics_humble_psutil.json')

if __name__=='__main__':
    main()
