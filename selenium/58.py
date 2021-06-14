# 需要安装selenium安装包
from selenium import webdriver
from lxml import etree


def open_url(url):
    dricer = webdriver.Chrome()  # 打开谷歌浏览器
    dricer.get(url)  # 设置打开的网址
    data = dricer.page_source  # 获取网页信息
    return data


def clean(money):
    mo = []
    for i in range(0, len(money)):
        if money[i] != '元/月':
            mo.append(money[i])
    return mo


def data_location_format(data):
    html = etree.HTML(data)
    region = html.xpath('//span[@class="address"]//text()')
    name = html.xpath('//span[@class="name"]//text()')
    money = html.xpath('//p[@class="job_salary"]//text()')
    mo = clean(money)
    company = html.xpath('//a[@class="fl"]//text()')
    url = html.xpath('//div[@class="job_name clearfix"]/a/@href')
    data_format = []
    cv1 = open("./58.csv", "a", encoding='utf-8')
    for i in range(0, len(region)):
        data_format.append(region[i] + "," + name[i] + "," + str(mo[i]) + "," + company[i] + "," + url[i])
        cv1.write(region[i] + "," + name[i] + "," + str(mo[i]) + "," + company[i] + "," + url[i] + "\n")
    cv1.close()
    return data_format


def main():
    for i in range(1, 15):
        url = "https://hz.58.com/tech/pn" + str(
            i) + "/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0004-f3d7-3aa9-be2d73c668e3&ClickID=2"
        data = open_url(url)
        dt = data_location_format(data)
        print(dt)


if __name__ == '__main__':
    main()
