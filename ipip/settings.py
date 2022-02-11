#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
配置和全局变量
"""

import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Options(metaclass=Singleton):
    """
    Global options
    """

    def __init__(self):
        self.ipdbfile = os.path.join(os.path.dirname(__file__), "db", "qqwry.ipdb")
        self.fake_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset": "UTF-8,*;q=0.5",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "en-US,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
            "referer": "https://www.google.com",
        }
        self.ipaddrs = []
        self.outfile = ""
        self.infile = ""
        self.proxies = None
        self.debug = False
        self.verbose = False
        self.ipstack_key = ""


opts = Options()
