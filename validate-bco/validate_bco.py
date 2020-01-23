#!/usr/bin/env python3 

import argparse
import json
import jsonref
import jsonschema

def main():
    json_schema_uri = 'https://raw.githubusercontent.com/biocompute-objects/BCO_Specification/1.3.1/schemas/biocomputeobject.json'

    parser = argparse.ArgumentParser()
    parser.add_argument('json_schema_uri', default=json_schema_uri, help="json schema uri")
    parser.add_argument('json', type=argparse.FileType('r'), help="json to validate")
    args = parser.parse_args()

    data = json.load(args.json)
    #schema = jsonref.load(args.json_schema_uri, jsonschema=True)
    schema = jsonref.loads(f'{{ "$ref": "{json_schema_uri}" }}', jsonschema=True)
    return jsonschema.validate(data, schema)

    # Load JSON Schema from the repository by using URL or local file using absolute path and 'file:' prefix
    schema = jsonref.loads(f'{{ "$ref": "{schema_uri}" }}', jsonschema=True)

    data = {}
    # Use the extended validator to fill in `data` with default values from the schema
    for err in DefaultValidatingDraft7Validator(schema).iter_errors(data):
        # print validation errors with a schema path to make them easier to read/trace
        print(f'{err.message} in the schema path {err.schema.get("$id") }#{"/".join(err.schema_path)}')

    # Pretty print `data` showing the assigned default values.
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
