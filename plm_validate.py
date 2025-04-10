import os
import json
import argparse
from jsonschema import Draft7Validator, exceptions

# --- Schema Validation ---

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def validate_schema(plm_data, schema_data):
    validator = Draft7Validator(schema_data)
    return sorted(validator.iter_errors(plm_data), key=lambda e: e.path)

# --- Soft Metadata Warnings ---

def check_metadata_warnings(plm_data):
    warnings = []
    KNOWN_TYPES = [
    "input", "button", "link", "select", "checkbox", "form",
    "modal", "text", "icon_button", "numeric_input"
    ]
    components = plm_data.get("components", [])

    for component in components:
        cid = component.get("id", "<unknown>")
        ctype = component.get("type")

        if ctype and ctype not in KNOWN_TYPES:
            warnings.append(f"Component '{cid}' has unknown type: '{ctype}'")

        for field in ["description", "intent"]:
            if field not in component:
                warnings.append(f"Component '{cid}' is missing: {field}")

        if component.get("type") in ["button", "modal", "form"]:
            if "llm_hint" not in component:
                warnings.append(f"Component '{cid}' is missing: llm_hint")

        if component.get("type") in ["input", "select"]:
            if "exampleInput" not in component:
                warnings.append(f"Component '{cid}' is missing: exampleInput")

    return warnings

# --- Run Validation on a Single File ---

def validate_file(file_path, schema):
    try:
        plm = load_json(file_path)
        errors = validate_schema(plm, schema)
        warnings = check_metadata_warnings(plm)

        if not errors:
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            for error in errors:
                path = ".".join([str(p) for p in error.path])
                print(f"  - {path or '<root>'}: {error.message}")

        if warnings:
            print("  Warnings:")
            for w in warnings:
                print(f"    ⚠️  {w}")
        print("")

    except Exception as e:
        print(f"❗ Error in {file_path}: {e}")

# --- Main CLI ---

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a PLM JSON file or folder of files.")
    parser.add_argument("plm_path", help="Path to a PLM JSON file or folder.")
    parser.add_argument("--schema", default="schema/plm.schema.json", help="Path to the PLM schema file.")
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)

        if os.path.isdir(args.plm_path):
            for filename in os.listdir(args.plm_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(args.plm_path, filename)
                    validate_file(file_path, schema)
        else:
            validate_file(args.plm_path, schema)

    except exceptions.SchemaError as e:
        print(f"❗ Schema error: {e}")
    except Exception as e:
        print(f"❗ Unexpected error: {e}")