#!/usr/bin/env python3
# coding: utf8
import json
import xmltodict
import feedparser
class FileReader:
    @classmethod
    def text(cls, path):
        with open(path, mode='r', encoding='utf-8') as f: return f.read().rstrip('\n')
    @classmethod
    def json(cls, path):
        with open(path, mode='r', encoding='utf-8') as f: return json.load(f)
    @classmethod
    def feed(cls, path): # RSS1.0, RSS2.0, Atom
        return feedparser.parse(path)
    @classmethod
    def xml(cls, path):
        with open(path, mode='r', encoding='utf-8') as f: return xmltodict.parse(f.read())
    @classmethod
    def csv(cls, path):
        return cls.dsv(path, ',')
    @classmethod
    def tsv(cls, path):
        return cls.dsv(path, '\t')
    @classmethod
    def dsv(cls, path, delimiter=' '):
        with open(path, mode='r', encoding='utf-8') as f: return csv.reader(f, delimiter=delimiter)

