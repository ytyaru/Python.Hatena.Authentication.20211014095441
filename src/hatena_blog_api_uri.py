#!/usr/bin/env python3
#encoding:utf-8
from requests_oauthlib import OAuth1Session
import sys
from path import Path 
from secret import Secret
from oauth1 import OAuth1
class HatenaBlogApiUri:
    def __init__(self, hatena_id, blog_id):
        self.__hatena_id = hatena_id
        self.__blog_id = blog_id
    @property
    def Service(self): return f'https://blog.hatena.ne.jp/{self.__hatena_id}/{self.__blog_id}/atom'
    @property
    def Category(self): return f'https://blog.hatena.ne.jp/{self.__hatena_id}/{self.__blog_id}/atom/category'
    @property
    def Entries(self): return f'https://blog.hatena.ne.jp/{self.__hatena_id}/{self.__blog_id}/atom/entry'
    def entries(self, page): return f'https://blog.hatena.ne.jp/{self.__hatena_id}/{self.__blog_id}/atom/entry?page={page}'
    def entry(self, entry_id): return f'https://blog.hatena.ne.jp/{self.__hatena_id}/{self.__blog_id}/atom/entry/{entry_id}'

