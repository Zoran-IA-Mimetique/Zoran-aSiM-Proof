import time, json, sys
try:
    import psutil
except ImportError:
    psutil = None

def main(duration=10, interval=0.5, out='energy_log.json'):
    duration = float(duration); interval = float(interval)
    samples = []
    t0 = time.time()
    if psutil is None:
        data = {'meta':{'created': time.time(), 'method':'fallback', 'note':'psutil not installed'},
                'samples': []}
        with open(out,'w') as f: json.dump(data, f, indent=2)
        print(json.dumps(data, indent=2)); return
    while time.time()-t0 < duration:
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory().percent
        samples.append({'t': time.time(), 'cpu_pct': cpu, 'mem_pct': mem})
        time.sleep(interval)
    data = {'meta':{'created': time.time(), 'method':'psutil', 'duration_s': duration, 'interval_s': interval},
            'samples': samples}
    with open(out,'w') as f: json.dump(data, f, indent=2)
    print(json.dumps({'written': out, 'n_samples': len(samples)}, indent=2))

if __name__=='__main__':
    args = sys.argv[1:]
    duration = args[0] if len(args)>0 else 10
    interval = args[1] if len(args)>1 else 0.5
    out = args[2] if len(args)>2 else 'energy_log.json'
    main(duration, interval, out)
