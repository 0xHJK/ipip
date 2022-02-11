#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
从IPSTACK获得IP位置信息
"""

import requests
from ..settings import opts

ACCESS_KEY = opts.ipstack_key
API = "http://api.ipstack.com/"


def ipinfo(ip) -> str:
    """ 获得单个IP的信息 """
    ip = ip.strip()
    try:
        r = requests.get("%s/%s?access_key=%s&language=zh" % (API, ip, ACCESS_KEY))
        j = r.json()
        ret = "%s, %s, %s, %s, %s" % (
            ip,
            j.get("country_name", "-"),
            j.get("region_name", "-"),
            j.get("city", "-"),
            j.get("connection", {}).get("isp", "-"),
        )
        return ret
    except Exception as e:
        return "%s query failed." % ip
