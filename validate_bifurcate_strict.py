import json, sys
from jsonschema import validate, Draft202012Validator

SCHEMA_FILE = "injector_bifurcate_schema_strict.json"

def main():
    if len(sys.argv)<2:
        print("usage: python validate_bifurcate_strict.py <file>")
        sys.exit(1)
    schema = json.load(open(SCHEMA_FILE,"r",encoding="utf-8"))
    data = json.load(open(sys.argv[1],"r",encoding="utf-8"))
    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    out = {"file": sys.argv[1], "valid": len(errors)==0, "errors": [str(e.message) for e in errors]}
    print(json.dumps(out, indent=2))
    with open("VALIDATE_STRICT_RESULT.json","w") as f:
        json.dump(out, f, indent=2)
    if errors:
        sys.exit(1)

if __name__ == "__main__":
    main()
