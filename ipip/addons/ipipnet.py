#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
从ipip.net获得ip位置信息
"""

import requests

API = "http://myip.ipip.net"


def myip() -> str:
    """ 查本机IP """
    try:
        r = requests.get(API)
        return r.text.strip()
    except Exception as e:
        return "0.0.0.0"


def ipinfo(ip) -> str:
    """ 查指定IP信息 """
    pass
