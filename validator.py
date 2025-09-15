import re, json

def validate_prompt(p):
    # basic checks: length, forbidden patterns, no exec directives
    if len(p)>10000: return False, 'too long'
    forbidden = ['rm -rf','import os','open(']
    for f in forbidden:
        if f in p: return False, f'forbidden token {f}'
    # simple regex for allowed glyph pattern
    if re.search(r'[^\x20-\x7E\n]', p):
        return False, 'non-ascii or control chars'
    return True, 'ok'

if __name__=='__main__':
    tests = ['safe prompt','rm -rf /', 'normal ⟦Z5::test⟧']
    for t in tests:
        print(t, validate_prompt(t))
