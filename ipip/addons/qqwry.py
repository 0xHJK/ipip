#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
从本地qqwry.ipdb分析IP归属地
"""

import ipdb
from ..settings import opts

DB = ipdb.City(opts.ipdbfile)


def ipinfo(ip) -> str:
    """ 查找单个IP """
    ip = ip.strip()
    try:
        return "%s, %s" % (ip, ", ".join(DB.find(ip.strip(), "CN")))
    except Exception as e:
        return "%s query failed." % ip


def ipbatch(ipaddrs) -> list:
    """ 查找多个IP """
    return [ipinfo(ip) for ip in ipaddrs]
