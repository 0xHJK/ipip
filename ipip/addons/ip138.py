#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
从IP138获得IP位置信息
"""

import requests
from pyquery import PyQuery as pq
from ..settings import opts

API = "https://2021.ip138.com/"


def myip() -> str:
    """ 查本机IP """
    try:
        r = requests.get(API, headers=opts.fake_headers)
        d = pq(r.text)
        return d(d("p")[0]).text()
    except Exception as e:
        return "0.0.0.0"


def ipinfo(ip) -> str:
    try:
        pass
    except Exception as e:
        return "%s query failed." % ip
