import random, string, json, time
def fuzz_prompt():
    # generate possibly malicious patterns
    s = ''.join(random.choices(string.printable, k=200))
    return s
tests = [fuzz_prompt() for _ in range(50)]
results = []
for t in tests:
    ok = 'rm -rf' not in t and 'import os' not in t
    results.append({'prompt':t[:80], 'ok':ok})
with open('adversarial_tests_summary.json','w') as f:
    json.dump({'meta':{'time':time.time()}, 'results':results}, f, indent=2)
print('Wrote adversarial_tests_summary.json')
