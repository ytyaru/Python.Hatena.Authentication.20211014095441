#!/usr/bin/env python3
#encoding:utf-8
from requests_oauthlib import OAuth1Session
import sys
from path import Path 
from secret import Secret
from oauth1 import OAuth1
from hatena_blog_api_uri import HatenaBlogApiUri

if __name__ == '__main__':
    HATENA_ID = 'ytyaru'
    HATENA_BLOG_ID = 'ytyaru.hatenablog.com'
    client = OAuth1.from_json(Path.here('secret.json'), Path.here('secret-schema.json'))
    uri = HatenaBlogApiUri(HATENA_ID, HATENA_BLOG_ID)
    res = client.get(uri.Entries)
    with open(f'{HATENA_BLOG_ID}.entry.xml', mode='w', encoding='utf-8') as f:
        f.write(res.text)
    print(f'{HATENA_BLOG_ID}.entry.xml')

