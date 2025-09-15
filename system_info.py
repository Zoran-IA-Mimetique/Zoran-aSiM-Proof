import platform, json, time, sys
try:
    import psutil
except ImportError:
    psutil = None

def snapshot(out='system_info.json'):
    info = {
        'created': time.time(),
        'python': sys.version,
        'platform': platform.platform(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'psutil': bool(psutil)
    }
    if psutil:
        info.update({
            'cpu_count': psutil.cpu_count(),
            'memory_gb': round(psutil.virtual_memory().total/1e9,2)
        })
    with open(out,'w') as f: json.dump(info, f, indent=2)
    print(json.dumps(info, indent=2))

if __name__=='__main__':
    out = sys.argv[1] if len(sys.argv)>0 else 'system_info.json'
    snapshot(out)
