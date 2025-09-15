# dataset_loader.py — skeleton for public datasets (ARC-like demo)
# Replace with actual dataset paths/URLs and license notes.

import json, os, random

def load_arc_like(n=100, seed=13):
    random.seed(seed)
    data = []
    for i in range(n):
        # toy parity task
        v = [random.randint(0,9) for _ in range(8)]
        y = [x % 2 for x in v]
        data.append({"x": v, "y": y})
    return data

def save_json(data, path="arc_like_data.json"):
    with open(path, "w") as f:
        json.dump({"meta":{"n":len(data)}, "rows": data}, f, indent=2)
    return path

if __name__ == "__main__":
    d = load_arc_like()
    p = save_json(d)
    print("Saved", p)
