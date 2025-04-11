import os
import json
import argparse
import re
from jsonschema import Draft7Validator, exceptions

# --- Casing Helpers ---

def is_snake_case(s): return re.fullmatch(r'[a-z]+(_[a-z]+)*', s or "") is not None
def is_pascal_case(s): return re.fullmatch(r'[A-Z][a-zA-Z0-9]*', s or "") is not None
def is_camel_case(s): return re.fullmatch(r'[a-z]+([A-Z][a-z0-9]*)*', s or "") is not None

# --- Schema Validation ---

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def validate_schema(plm_data, schema_data):
    validator = Draft7Validator(schema_data)
    return sorted(validator.iter_errors(plm_data), key=lambda e: e.path)

# --- Soft Metadata Warnings ---

def get_components_from_plm(plm_data):
    if "components" in plm_data:
        return plm_data["components"]
    elif "component" in plm_data:
        return [plm_data["component"]]
    return []

def check_metadata_warnings(plm_data):
    warnings = []
    KNOWN_TYPES = [
        "input", "button", "link", "select", "checkbox", "form",
        "modal", "text", "icon_button", "numeric_input"
    ]
    components = get_components_from_plm(plm_data)

    for component in components:
        cid = component.get("id", "<unknown>")
        ctype = component.get("type")
        page_name = plm_data.get("page")
        
        if not is_snake_case(cid):
            warnings.append(f"Component ID '{cid}' should be snake_case")

        if ctype and not is_snake_case(ctype):
            warnings.append(f"Component type '{ctype}' should be snake_case")

        if page_name and not is_pascal_case(page_name):
            warnings.append(f"Page name '{page_name}' should be PascalCase")

        if ctype and ctype not in KNOWN_TYPES:
            warnings.append(f"Component '{cid}' has unknown type: '{ctype}'")

        for field in ["description", "intent"]:
            if field not in component:
                warnings.append(f"Component '{cid}' is missing: {field}")

        if component.get("type") in ["button", "modal", "form"]:
            if "llmHint" not in component:
                warnings.append(f"Component '{cid}' is missing: llmHint")

        if component.get("type") in ["input", "select"]:
            if "exampleInput" not in component:
                warnings.append(f"Component '{cid}' is missing: exampleInput")

    return warnings

# --- Run Validation on a Single File ---

def validate_file(file_path, schema):
    try:
        plm = load_json(file_path)

        if "component" in plm:
            print("🔧 Standalone component PLM detected.")
        elif "page" in plm:
            print(f"🧩 Page PLM detected: {plm.get('page')}")

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