import requests
import sys
import json


def request(url, head=''):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Connection": "close",
    }
    headers.update(head)
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code != 200:
            return None
        return r.content.decode("utf-8")
    except Exception:
        return None


def msg(data):
    print("\033[1;32m%s\033[0m" % data.strip())


def youdao(words):
    url = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=" + words
    r = request(url)
    if r is None:
        return
    r = json.loads(r)
    msg(r["translateResult"][0][0]["tgt"])


def by360(words):
    url = "http://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=" + words
    head = {"pro": "fanyi"}
    r = request(url, head)
    if r is None:
        return
    r = json.loads(r)
    try:
        for i, j in r["data"]["explain"]["phonetic"].items():
            print("\033[1;34m%s %s\033[0m" % (i, j))
        msg(r["data"]["explain"]["translation"][0])
        for i in r["data"]["explain"]["web_translations"]:
            msg(i["translation"])
    except Exception:
        pass


data = ''
for i in sys.argv[1:]:
    data += i + ' '

print("\033[1;31m****************************************************************************\033[0m")
by360(data)
youdao(data)
print("\033[1;31m****************************************************************************\033[0m")
