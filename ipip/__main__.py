#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
import sys
import re
import uuid
import socket
import logging
import requests
import fileinput
import ipdb
import click
from .settings import opts
from .addons import ip138, ipipnet, ipstack, qqwry


def sprint(*args):
    if not args:
        return
    s = click.style(args[0], fg="yellow")
    s += " ".join(args[1:])
    click.echo(s)


def sformat(*args):
    s = click.style(args[0], fg="yellow")
    s += " ".join(args[1:])
    return s


def myip() -> list:
    """ 输出本机MAC地址、内网地址和外网地址 """
    ret = []
    # MAC地址
    mac = ":".join(re.findall("..", "%012x" % uuid.getnode())).upper()
    sprint("[MAC]: ", mac)
    # 内网地址
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        internal_ip = s.getsockname()[0]
    except Exception:
        internal_ip = "127.0.0.1"
    finally:
        s.close()
    ret.append(sformat("[INTERNAL]: ", internal_ip))
    # 外网地址 TODO: 加代理
    ret.append(sformat("[IPIP.NET]: ", ipipnet.myip()))
    ret.append(sformat("[IP138]: ", ip138.myip()))

    return ret


def ipquery(ipaddrs) -> list:
    """ 联网查询一个或多个IP """
    ret = []
    for ip in ipaddrs:
        ret.append(sformat("[QQWRY]: ", qqwry.ipinfo(ip)))
        ret.append(sformat("[IPSTACK]: ", ipstack.ipinfo(ip)))
    return ret


def ipbatch(ipaddrs) -> list:
    """ 本地库查询多个IP """
    ret = []
    for ip in ipaddrs:
        ret.append(qqwry.ipinfo(ip))
    return ret


def output(result, outfile=None) -> None:
    """ 输出结果 """
    if not outfile:
        for line in result:
            print(line)
    else:
        with open(outfile, "w") as f:
            f.write("\n".join(result))


@click.command()
@click.argument("ipaddrs", nargs=-1)
@click.option("-t", "--test", is_flag=True, help="查看本机IP")
@click.option("-i", "--infile", help="指定IP列表文件")
@click.option("-o", "--outfile", help="指定输出结果文件")
@click.option("-v", "--verbose", is_flag=True, help="详细模式")
@click.option("--debug", is_flag=True, help="调试模式")
def main(ipaddrs, test, infile, outfile, verbose, debug):
    if verbose:
        opts.verbose = verbose
    if debug:
        opts.debug = debug

    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)-8s | %(name)s: %(msg)s ",
        datefmt="%H:%M:%S",
    )


    if test:
        # 查询本机IP
        output(result=myip(), outfile=outfile)
        return

    if ipaddrs:
        # 查询指定IP
        output(result=ipquery(ipaddrs), outfile=outfile)
        return

    if infile:
        # 批量查询文件IP（本地）
        opts.infile = infile
        ipaddrs = open(infile, "r").readlines()
        output(result=ipbatch(ipaddrs), outfile=outfile)
        return
    
    # 管道查询（本地）
    ipaddrs = fileinput.input()
    output(result=ipbatch(ipaddrs), outfile=outfile)


