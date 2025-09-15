# sudoku_loader.py — simple sudoku dataset generator (toy, license-free)
import json, random

def gen_sudoku(n=5, seed=13):
    random.seed(seed)
    puzzles = []
    for i in range(n):
        grid = [[0]*9 for _ in range(9)]
        # Fill diagonal boxes to make solvable puzzles
        for d in range(0,9,3):
            nums=list(range(1,10)); random.shuffle(nums)
            for r in range(3):
                for c in range(3):
                    grid[d+r][d+c]=nums.pop()
        puzzles.append({"id":i,"grid":grid})
    return puzzles

def save_json(data,path="sudoku_data.json"):
    with open(path,"w") as f: json.dump({"meta":{"n":len(data)},"rows":data},f,indent=2)
    return path

if __name__=="__main__":
    d=gen_sudoku()
    p=save_json(d)
    print("Saved",p)
