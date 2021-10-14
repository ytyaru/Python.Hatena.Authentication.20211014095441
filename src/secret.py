#!/usr/bin/env python3
# coding: utf8
import jsonschema
from FileReader import FileReader
class Secret:
    @classmethod
    def from_json(cls, path, schema_path=None):
        secret = FileReader.json(path)
        if schema_path:
            schema = FileReader.json(schema_path)
            try: jsonschema.validate(secret, schema)
            except jsonschema.ValidationError as e:
                print(f'[ERROR] スキーマ違反です。\n{path}\n{schema_path}', file=sys.stderr)
                print(e, file=sys.stderr)
                raise e
        return secret

if __name__ == '__main__':
    from path import Path
    secret = Secret.from_json(
        Path.here('secret.json'),
        Path.here('secret-schema.json')
    )
    print(secret['username'])

