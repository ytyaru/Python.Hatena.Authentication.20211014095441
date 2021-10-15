#!/usr/bin/env python3
#encoding:utf-8
import xmltodict
import feedparser
import sys
from requests_oauthlib import OAuth1Session
from path import Path
from secret import Secret
from collections import namedtuple
from FileReader import FileReader
class HatenaBlogResponseParser:
    def __init__(self):
        self.__Blog = namedtuple('Blog', 'id title sub_title url updated author')
        self.__Entry = namedtuple('Entry', 'id title summary url updated published edited draft contents')
        self.__Content = namedtuple('Content', 'type content')
        self.__next_url = None
        self.__blog = None
        self.__entries = None
    def from_file(self, path):
        self.__feed = FileReader.feed(path)
    def from_str(self, xml):
        self.__feed = feedparser.parse(xml)
    @property
    def NextUrl(self):
        if self.__next_url: return self.__next_url
        self.__next_url = [link['url'] for link in self.__feed['feed']['links'] if 'next' == link['rel']][0]
        return self.__next_url
    @property
    def Blog(self):
        if self.__blog: return self.__blog
        self.__parse_blog()
        return self.__blog
    @property
    def Entries(self):
        if self.__entries: return self.__entries
        self.__parse_entries()
        return self.__entries
    def __parse_blog(self):
        self.__blog = self.__Blog(
            self.__feed['feed']['id'],
            self.__feed['feed']['title'],
            self.__feed['feed']['subtitle'],
            self.__feed['feed']['link'],
            self.__feed['feed']['updated'],
            self.__feed['feed']['author']
        ) 
    def __parse_contents(self, entry):
        contents = []
        for content in entry['content']:
            contents.append(self.__Content(content['type'], content['value']))
        if 'hatena_formatted-content' in entry and \
           'value' in entry['hatena_formatted-content'] and \
           'type' in entry['hatena_formatted-content']:
            contents.append(self.__Content(entry['hatena_formatted-content']['type'], entry['hatena_formatted-content']['value']))
        return contents
    def __parse_entries(self):
        self.__entries = []
        for entry in self.__feed['entries']:
            self.__entries.append(
                self.__Entry(
                    entry['id'],
                    entry['title'],
                    entry['summary'],
                    entry['link'],
                    entry['updated'],
                    entry['published'],
                    entry['app_edited'],
                    entry['app_draft'],
                    self.__parse_contents(entry),
                )
            )

if __name__ == '__main__':
    parser = HatenaBlogResponseParser()
    parser.from_file('/tmp/work/ytyaru.hatenablog.com.entry.xml')
    print(parser.NextUrl)
    print(parser.Blog)
    print(len(parser.Entries))
    print(parser.Entries)

