# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup


def getPage(url):
    res = requests.get(url)
    # res.encoding = res.apparent_encoding
    res.encoding = 'EUC-JP'
    html = res.text
    # print(res.encoding)
    return html


def getPageBySerial(serial, page=2):
    url = 'https://db.netkeiba.com'
    params = {
        'pid': 'horse_list',
        'sort_key': 'prize',
        'sort_type': 'desc',
        'page': page,
        'serial': serial.encode('euc-jp')}
    res = requests.post(url, data=params)
    res.encoding = res.apparent_encoding
    html = res.text
    return html


def getSerial(html):
    soup = BeautifulSoup(html, "html.parser")
    serial = soup.select('input[name="serial"]')
    return serial[0].get('value')


def checkIfNextPageExists(html):
    soup = BeautifulSoup(html, "html.parser")
    # next_page_elms = soup.select("div.common_pager a[title='次']")
    next_page_elms = soup.select('div.common_pager a[title="次"]')  # 上のコードだとうまく動かなくなった
    if len(next_page_elms) == 0:
        return None
    return True


def searchHorse(**kwargs):
    url = 'https://db.netkeiba.com'
    params = {
        'pid': 'horse_list',
        'word': '',
        'sire': '',
        'keito': '',
        'mare': '',
        'bms': '',
        'trainer': '',
        'owner': '',
        'breeder': '',
        'under_age': '',
        'over_age': '',
        'sex': '',
        'sort': "prize",
        'list': "100"
    }

    for k, v in kwargs.items():
        if type(v) is str:
            params[k] = v.encode('euc-jp')
        elif type(v) is list:
            params[k + '[]'] = ','.join([str(i) for i in v])
        else:
            params[k] = v

    res = requests.post(url, data=params)
    res.encoding = res.apparent_encoding
    html = res.text
    return html
