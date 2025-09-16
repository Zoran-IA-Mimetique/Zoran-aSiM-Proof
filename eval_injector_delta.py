# MIT License
# Copyright (c) 2025
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# eval_injector_delta.py : mesures NW/NP/DL/NC/NR + deltas
import sys, re, json, csv
from collections import Counter

def load(p):
    return open(p, "r", encoding="utf-8").read()

def tokenize_words(s):
    # basic word tokenizer (letters/digits/+accent)
    tokens = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9\-]+", s.lower())
    return tokens

def count_sentences(s):
    # naive sentence split
    return len([x for x in re.split(r"[.!?]+", s) if x.strip()])

def density_lexicale(tokens):
    if not tokens: return 0.0
    return round(len(set(tokens))/len(tokens), 4)

def load_terms(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows

def count_terms(text, terms):
    counts = Counter()
    t = text.lower()
    for row in terms:
        term = row["term"].strip()
        if not term: continue
        # count overlapping occurrences naive
        counts[term] += len(re.findall(re.escape(term.lower()), t))
    return counts

def nr_from_categories(term_counts, terms, categories=("regulatory","code")):
    cat_terms = [r["term"] for r in terms if r["category"] in categories]
    return sum(term_counts.get(t,0) for t in cat_terms)

def metrics(text, terms):
    tokens = tokenize_words(text)
    nw = len(tokens)
    np_ = count_sentences(text)
    dl = density_lexicale(tokens)
    term_counts = count_terms(text, terms)
    nc = sum(term_counts.values())
    nr = nr_from_categories(term_counts, terms)
    return {
        "NW": nw, "NP": np_, "DL": dl,
        "NC": nc, "NR": nr
    }

def delta(mw, mwo):
    d = {k: (mw[k]-mwo[k]) for k in mw}
    pct = {}
    for k,v in d.items():
        base = mwo[k]
        pct[k] = (v/base*100.0) if isinstance(base,(int,float)) and base!=0 else None
    return d, pct

def main():
    if len(sys.argv) not in (3,4):
        print("usage: python eval_injector_delta.py with.txt without.txt [terms_nc_list.csv]")
        sys.exit(1)
    with_path, without_path = sys.argv[1], sys.argv[2]
    terms_path = sys.argv[3] if len(sys.argv)==4 else "terms_nc_list.csv"
    terms = load_terms(terms_path)
    with_text, without_text = load(with_path), load(without_path)
    mw = metrics(with_text, terms)
    mwo = metrics(without_text, terms)
    d, pct = delta(mw, mwo)
    out = {"with": mw, "without": mwo, "delta_abs": d, "delta_pct": pct}
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
