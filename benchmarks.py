
from typing import List, Tuple
from collections import deque
import random, time

def sudoku_is_valid(grid):
    for i in range(9):
        row=[x for x in grid[i] if x!=0]; col=[grid[r][i] for r in range(9) if grid[r][i]!=0]
        if len(row)!=len(set(row)) or len(col)!=len(set(col)): return False
    for br in range(0,9,3):
        for bc in range(0,9,3):
            vals=[]; 
            for r in range(br,br+3):
                for c in range(bc,bc+3):
                    if grid[r][c]!=0: vals.append(grid[r][c])
            if len(vals)!=len(set(vals)): return False
    return True

def sudoku_solve(grid, ops):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                for v in range(1,10):
                    ops[0]+=1
                    grid[r][c]=v
                    if sudoku_is_valid(grid) and sudoku_solve(grid, ops): return True
                    grid[r][c]=0
                return False
    return True

def simple_mazes(n=5, w=10, h=6)->List[List[str]]:
    # generate random mazes with start/goal borders; naive DFS carve
    def gen():
        import random
        grid=[["#"]*w for _ in range(h)]
        for r in range(1,h-1):
            for c in range(1,w-1):
                grid[r][c] = "." if random.random()>.35 else "#"
        grid[1][1]="S"; grid[h-2][w-2]="G"
        return ["".join(row) for row in grid]
    return [gen() for _ in range(n)]

def maze_solve(maze: List[str], ops)->bool:
    R,C=len(maze),len(maze[0]); sr=sc=gr=gc=-1
    for r in range(R):
        for c in range(C):
            if maze[r][c]=="S": sr,sc=r,c
            if maze[r][c]=="G": gr,gc=r,c
    q=deque([(sr,sc)]); seen=set([(sr,sc)])
    while q:
        r,c=q.popleft(); ops[0]+=1
        if (r,c)==(gr,gc): return True
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and maze[nr][nc]!="#" and (nr,nc) not in seen:
                seen.add((nr,nc)); q.append((nr,nc))
    return False

def arc_like_tasks(n=60, d=12)->List[Tuple[list,list]]:
    tasks=[]
    for _ in range(n):
        v=[random.randint(0,9) for _ in range(d)]
        y=[x%2 for x in v]
        tasks.append((v,y))
    return tasks

def arc_like_solver(vec: List[int])->List[int]:
    return [x%2 for x in vec]
