import requests
import json
import re
import pandas as pd
import time


def get_data(name, code, page=11):
    df_list = []
    for index in range(1, page):
        url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18303008568368266129_1623321529841&fundCode={' \
              '}&pageIndex={}&pageSize=20&startDate=&endDate=&_=1623321540754'.format(
            code, index)
        headers = {
            'Referer': 'http://fundf10.eastmoney.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.212 Safari/537.36 '
        }

        resp = requests.get(url, headers=headers)
        html = resp.text
        # print(html)
        res = re.findall('\((.*?)\)', html)  # 正则表达式
        datas = json.loads(res[0])["Data"]["LSJZList"]  # 整理并留下想要的
        df = pd.DataFrame(datas)
        df_list.append(df)

    df_data = pd.concat(df_list)
    # print(df_data)
    print(name)
    if name!='恒越研究精选混合A/B':
        df_data.to_csv('./CSV/{}.csv'.format(name), index=False)  # 下载
    print(name)

def get_fund_ranking(num):
    baes_url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020' \
               '-06-10&ed=2021-06-10&qdii=&tabSubtype=,,,,,&pi={}&pn=50&dx=1&v=0.3234890370768233'.format(
        num)
    headers = {
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.212 Safari/537.36 '
    }
    response = requests.get(baes_url, headers=headers)

    result = re.findall('"(.*?)"', response.text)
    # print(result)
    for i in result:
        code = i.split(',')[0]
        # print(code)
        name = i.split(',')[1]
        # print(name)
        get_data(name, code)


get_fund_ranking(1)
