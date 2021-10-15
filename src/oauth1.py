#!/usr/bin/env python3
#encoding:utf-8
import sys
from requests_oauthlib import OAuth1Session
from path import Path
from secret import Secret
class OAuth1:
    @classmethod
    def from_json(cls, path, schema_path=None):
        secret = Secret.from_json(path, schema_path)
        keys = ['oauth_consumer_key', 'oauth_consumer_secret', 'oauth_token', 'oauth_token_secret']
        cls.__has_not_key(path, secret)
        cls.__has_not_token(path, secret)
        return cls.from_str(*[secret[key] for key in keys])
    @classmethod
    def __has_not_key(cls, path, secret):
        for key in ['oauth_consumer_key', 'oauth_consumer_secret']:
            if key not in secret:
                raise ValueError(f'[ERROR] {key} がありません。指定したファイルにセットしてください。: {path}\nJSONキー名は同ディレクトリにある secret-schema.json を参照してください。\nキーの取得は以下サイトを参照してください。\nhttp://developer.hatena.ne.jp/ja/documents/auth/apis/oauth/consumer')
    @classmethod
    def __has_not_token(cls, path, secret):
        for key in ['oauth_token', 'oauth_token_secret']:
            if key not in secret:
                raise ValueError(f'[ERROR] {key} がありません。AccessTokenを取得して次のファイルにセットしてください。：{path}\nこの処理は半自動化できます。oauth1_get_token.py ファイルを実行して指示に従ってください。')
    @classmethod
    def from_str(cls, client_key:str, client_secret:str, resource_owner_key:str, resource_owner_secret:str):
        CREDENTIALS = {}
        CREDENTIALS['client_key'] = client_key
        CREDENTIALS['client_secret'] = client_secret
        CREDENTIALS['resource_owner_key'] = resource_owner_key
        CREDENTIALS['resource_owner_secret'] = resource_owner_secret
        return OAuth1(**CREDENTIALS)
    def __init__(self, **kwargs):
        self.__set_client(**kwargs)
    def __set_client(self, **kwargs):
        self.__client = OAuth1Session(**kwargs)
    def get(self, url):
        res = self.__client.get(url)
        self.__check_response(res)
        return res
    def __check_response(self, res):
        if not res.ok:
            res.raise_for_status()
        print('status code: {}'.format(res.status_code), file=sys.stderr)


if __name__ == '__main__':
    from secret import Secret
    HATENA_ID = 'ytyaru'
    HATENA_BLOG_ID = 'ytyaru.hatenablog.com'
    client = OAuth1.from_json(Path.here('secret.json'), Path.here('secret-schema.json'))
    res = client.get(f'https://blog.hatena.ne.jp/{HATENA_ID}/{HATENA_BLOG_ID}/atom/entry')
    with open(f'{HATENA_BLOG_ID}.entry.xml', mode='w', encoding='utf-8') as f:
        f.write(res.text)
    print(f'{HATENA_BLOG_ID}.entry.xml')

