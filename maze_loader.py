# maze_loader.py — simple maze dataset generator
import random,json

def gen_maze(w=10,h=10,seed=13):
    random.seed(seed)
    grid=[["#"]*w for _ in range(h)]
    for r in range(1,h-1):
        for c in range(1,w-1):
            grid[r][c]="." if random.random()>0.3 else "#"
    grid[1][1]="S"; grid[h-2][w-2]="G"
    return ["".join(row) for row in grid]

def gen_dataset(n=5,w=10,h=10,seed=13):
    random.seed(seed)
    return [{"id":i,"maze":gen_maze(w,h,seed+i)} for i in range(n)]

def save_json(data,path="maze_data.json"):
    with open(path,"w") as f: json.dump({"meta":{"n":len(data)},"rows":data},f,indent=2)
    return path

if __name__=="__main__":
    d=gen_dataset()
    p=save_json(d)
    print("Saved",p)
