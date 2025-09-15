
# polyresonator.py
# Minimal orchestrator: choose among candidate solvers using a UCB1 bandit.
import math, random
from typing import Callable, List, Tuple

class UCB1:
    def __init__(self, n_arms: int):
        self.n = [0]*n_arms
        self.s = [0.0]*n_arms
        self.t = 0
    
    def select(self) -> int:
        self.t += 1
        # try unpulled arms first
        for i, c in enumerate(self.n):
            if c == 0:
                return i
        # compute UCB
        ucb = [ (self.s[i]/self.n[i]) + math.sqrt(2*math.log(self.t)/self.n[i]) for i in range(len(self.n)) ]
        return max(range(len(self.n)), key=lambda i: ucb[i])
    
    def update(self, arm: int, reward: float):
        self.n[arm] += 1
        self.s[arm] += reward

def orchestrate(task_inputs: List, solvers: List[Callable]) -> Tuple[int,int]:
    bandit = UCB1(len(solvers))
    success = 0
    for x in task_inputs:
        i = bandit.select()
        ok = 1.0 if solvers[i](x) else 0.0
        bandit.update(i, ok)
        success += int(ok)
    return success, len(task_inputs)
