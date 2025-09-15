import json, random, time
# simulate PolyResonator picking solvers
solvers = ['solver_a','solver_b','solver_c']
random.seed(1)
logs=[]
for i in range(10):
    choice = random.choice(solvers)
    result = {'task':i,'solver':choice,'success': random.random()>0.2}
    logs.append(result)
with open('orchestration_log.json','w') as f:
    json.dump({'meta':{'time':time.time()}, 'logs':logs}, f, indent=2)
print('Wrote orchestration_log.json')
