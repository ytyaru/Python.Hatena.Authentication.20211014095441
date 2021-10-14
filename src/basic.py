#!/usr/bin/env python3
# coding: utf8
# requests.post(url, auth=Basic.from_json(...))
from secret import Secret
import requests
from requests.auth import HTTPBasicAuth
class Basic:
    @classmethod
    def from_str(cls, username:str, password:str):
        return cls._make_auth(username, password)
    @classmethod
    def from_json(cls, path, schema_path=None):
        secret = Secret.from_json(path, schema_path)
        if 'password' not in secret:
            raise ValueError(f'[ERROR] password がありません。指定したファイルにセットしてください。: {path}')
        return cls._make_auth(secret['username'], secret['password'])
    @classmethod
    def _make_auth(cls, username:str, password:str):
        return requests.auth.HTTPBasicAuth(username, password)

