
# benchmarks.py
from typing import List, Tuple
import random

def sudoku_is_valid(grid):
    # grid: 9x9 list of lists
    digits = set(range(1,10))
    for i in range(9):
        row = [x for x in grid[i] if x!=0]
        col = [grid[r][i] for r in range(9) if grid[r][i]!=0]
        if len(row)!=len(set(row)) or len(col)!=len(set(col)):
            return False
    # 3x3 blocks
    for br in range(0,9,3):
        for bc in range(0,9,3):
            vals = []
            for r in range(br,br+3):
                for c in range(bc,bc+3):
                    if grid[r][c]!=0: vals.append(grid[r][c])
            if len(vals)!=len(set(vals)):
                return False
    return True

def sudoku_solve(grid):
    # backtracking minimal
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                for v in range(1,10):
                    grid[r][c]=v
                    if sudoku_is_valid(grid) and sudoku_solve(grid):
                        return True
                    grid[r][c]=0
                return False
    return True

def simple_mazes() -> List[List[str]]:
    # tiny mazes represented as list of strings; S start, G goal, # wall, . free
    return [
        ["S..#G",
         "##.#.",
         "....."],
        ["S#...",
         ".#.#G",
         ".#..."],
    ]

def maze_solve(maze: List[str]) -> bool:
    R,C = len(maze), len(maze[0])
    from collections import deque
    sr=sc=gr=gc=-1
    for r in range(R):
        for c in range(C):
            if maze[r][c]=="S": sr,sc=r,c
            if maze[r][c]=="G": gr,gc=r,c
    q=deque([(sr,sc)])
    seen=set([(sr,sc)])
    while q:
        r,c=q.popleft()
        if (r,c)==(gr,gc): return True
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and maze[nr][nc]!="#" and (nr,nc) not in seen:
                seen.add((nr,nc)); q.append((nr,nc))
    return False

def arc_like_tasks() -> List[Tuple[List[int], List[int]]]:
    # toy: map input vector to its element-wise parity; success if matches expected
    tasks = []
    for _ in range(20):
        v = [random.randint(0,9) for _ in range(8)]
        y = [x%2 for x in v]
        tasks.append((v,y))
    return tasks

def arc_like_solver(vec: List[int]) -> List[int]:
    return [x%2 for x in vec]
