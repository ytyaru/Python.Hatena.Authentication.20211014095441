#!/usr/bin/env python3
#encoding:utf-8
# http://developer.hatena.ne.jp/ja/documents/auth/apis/oauth/consumer
# https://qiita.com/kosystem/items/7728e57c70fa2fbfe47c
#Temporary Credential Request URL 	https://www.hatena.com/oauth/initiate
#Resource Owner Authorization URL (PC) 	https://www.hatena.ne.jp/oauth/authorize
#Resource Owner Authorization URL (スマートフォン) 	https://www.hatena.ne.jp/touch/oauth/authorize
#Resource Owner Authorization URL (携帯電話) 	http://www.hatena.ne.jp/mobile/oauth/authorize
#Token Request URL 	https://www.hatena.com/oauth/token
import sys
from requests_oauthlib import OAuth1Session
from path import Path
from secret import Secret
import json
import urllib.parse
import webbrowser
import requests
from requests_oauthlib import OAuth1
class OAuth1Token:
    @classmethod
    def from_json(cls, path, schema_path=None):
        secret = Secret.from_json(path, schema_path)
        if 'oauth_token' in secret and 'oauth_token_secret' in secret:
            print('AccessTokenは取得済みです。既存値を返します。', file=sys.stderr)
            return secret
        keys = ['oauth_consumer_key', 'oauth_consumer_secret']
        cls.__has_not_keys(path, secret, keys)
        return cls.from_str(*[secret[key] for key in keys], secret)
    @classmethod
    def __has_not_keys(cls, path, secret, keys):
        for key in keys:
            if key not in secret:
                raise ValueError(f'[ERROR] {key} がありません。指定したファイルにセットしてください。: {path}')
    @classmethod
    def from_str(cls, client_key:str, client_secret:str, secret:dict=None) -> dict:
        return cls.__write_token(*cls.__get_token(client_key, client_secret), secret)
    @classmethod
    def __get_token(self, consumer_key:str, consumer_secret:str) -> dict:
        # リクエストトークンを取得する
        auth = OAuth1(consumer_key, consumer_secret, callback_uri='oob')
        res = requests.post('https://www.hatena.com/oauth/initiate', auth=auth)
        if not res.ok: res.raise_for_status()
        request_token = dict(urllib.parse.parse_qsl(res.text))
        print(request_token)

        # ブラウザを開きOAuth認証確認画面を表示。ユーザーが許可するとPINコードが表示される
        webbrowser.open(f"https://www.hatena.ne.jp/oauth/authorize?oauth_token={request_token['oauth_token']}")

        # 上記PINコードを入力する
        oauth_verifier = input("Please input PIN code:")
        auth = OAuth1(
            consumer_key,
            consumer_secret,
            request_token['oauth_token'],
            request_token['oauth_token_secret'],
            verifier=oauth_verifier)
        res = requests.post('https://www.hatena.com/oauth/token', auth=auth)
        if not res.ok: res.raise_for_status()
        access_token = dict(urllib.parse.parse_qsl(res.text))
        print(access_token)
        return [access_token['oauth_token'], access_token['oauth_token_secret']]
    @classmethod
    def __write_token(self, oauth_token:str, oauth_token_secret:str, secret:dict=None) -> dict:
        if not secret: secret = Secret.from_json(Path.here('secret.json'))
        secret['oauth_token'] = oauth_token
        secret['oauth_token_secret'] = oauth_token_secret
        with open(Path.here('secret.json'), mode='w', encoding='utf-8') as f:
            json.dump(secret, f, ensure_ascii=False, indent=4)
        return secret


if __name__ == '__main__':
    secret = OAuth1Token.from_json(Path.here('secret.json'), Path.here('secret-schema.json'))
    print(secret)

