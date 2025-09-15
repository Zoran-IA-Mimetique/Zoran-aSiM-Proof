import json, sys

SCHEMA_FILE = "injector_log_schema.json"

def load_json(path):
    with open(path,"r") as f:
        return json.load(f)

def validate(obj, schema):
    # Minimal validation: required top-level keys and required meta fields
    errors = []
    if not isinstance(obj, dict):
        return ["Root is not an object"]
    for req in schema.get("required", []):
        if req not in obj:
            errors.append(f"Missing required root key: {req}")
    meta = obj.get("meta", {})
    meta_schema = schema["properties"]["meta"]
    for req in meta_schema.get("required", []):
        if req not in meta:
            errors.append(f"Missing required meta key: {req}")
    return errors

def main():
    if len(sys.argv)<2:
        print("Usage: python validate_injector_log.py <log.json>")
        sys.exit(1)
    schema = load_json(SCHEMA_FILE)
    obj = load_json(sys.argv[1])
    errs = validate(obj, schema)
    out = {"file": sys.argv[1], "valid": len(errs)==0, "errors": errs}
    print(json.dumps(out, indent=2))
    with open("VALIDATION_RESULT.json","w") as f:
        json.dump(out, f, indent=2)

if __name__ == "__main__":
    main()
