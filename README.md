# IPIP

## 主要功能

1. 查询本机IP
2. 单个IP多来源查询（联网）
3. 单个IP高精度查询（联网）
4. 单个IP本地查询
5. IP批量本地查询
7. 支持管道查询

## 安装

```
git clone https://github.com/0xHJK/ipip

cd ipip

make install
```

注册 https://ipstack.com 

修改`settings.py`中的`self.ipstack_key`

## 使用方式

查看帮助

```bash
ipip --help
```

```bash
Usage: ipip [OPTIONS] [IPADDRS]...

Options:
  -t, --test          查看本机IP
  -i, --infile TEXT   指定IP列表文件
  -o, --outfile TEXT  指定输出结果文件
  -v, --verbose       详细模式
  --debug             调试模式
  --help              Show this message and exit.
```

查询本机IP（输出mac地址、内网IP、外网IP）

```bash
ipip -t
```

查询指定IP

```bash
ipip 1.1.1.1
```

批量查询IP

```bash
ipip -i ip.txt -o out.txt
```

管道查询IP

```bash
cat ip.txt | ipip
```

```bash
echo "8.8.8.8" | ipip
```