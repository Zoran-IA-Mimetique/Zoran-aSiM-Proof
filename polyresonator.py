
import math
class UCB1:
    def __init__(self, k:int):
        self.n=[0]*k; self.s=[0.0]*k; self.t=0
    def select(self)->int:
        self.t+=1
        for i,c in enumerate(self.n):
            if c==0: return i
        ucb=[(self.s[i]/self.n[i])+math.sqrt(2*math.log(self.t)/self.n[i]) for i in range(len(self.n))]
        return max(range(len(self.n)), key=lambda i: ucb[i])
    def update(self, i:int, reward:float):
        self.n[i]+=1; self.s[i]+=reward
def orchestrate(inputs, solvers):
    bandit=UCB1(len(solvers)); succ=0; decisions=[]
    for x in inputs:
        i=bandit.select()
        ok=float(solvers[i](x))
        bandit.update(i, ok)
        succ+=int(ok); decisions.append(i)
    return succ, len(inputs), decisions
