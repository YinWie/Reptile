import requests
from lxml import etree

def link(url):
    hd ={
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    }
    rst=requests.get(url,headers=hd)
    rst.encoding ="utf-8"
    html = etree.HTML(rst.text)
    return html
def cutting(House):#输入一串带|的列表
    House_type=[]
    for i in range(len(House)):#提取单个字符串
        x=House[i]
        y=x.split("|")#以|分割变成新字列表
        House_type.append(y[0])#新列表的第一个值追加到返回列表
    return House_type
def format(html):
    name = html.xpath('//div[@class="title"]/a//text()')
    money= html.xpath('//div[@class="totalPrice"]//text()')
    Unit_Price= html.xpath('//div[@class="unitPrice"]//text()')
    House= html.xpath('//div[@class="houseInfo"]//text()')
    House_type=cutting(House)
    Data=[]
    cv1=open("./LinkHome.csv", "a", encoding='utf-8')
    for i in range(len(name)):
        Data.append(name[i]+","+money[i]+","+Unit_Price[i]+","+House_type[i])
        cv1.write(name[i]+","+money[i]+","+Unit_Price[i]+","+House_type[i]+"\n")
    cv1.close()
    return Data
def main():
    for i in range(1,100):
        url="https://bj.lianjia.com/ershoufang/pg"+str(i)
        html=link(url)
        data=format(html)
        print(data)
if __name__ == '__main__':
    main()