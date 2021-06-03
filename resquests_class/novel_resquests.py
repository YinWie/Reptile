import requests
from lxml.html import etree
hd ={
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}#伪装浏览器
def pageNumber():#获取页数
    rst = requests.get("http://www.ijjxsw.com/txt/Xuanhuan/index_1.html", headers=hd)
    wb_data = rst.text
    html = etree.HTML(wb_data)
    number = html.xpath('//a[@title="总数"]/b//text()')#总数
    title = html.xpath('//span[@class="title"]//text()')#标题
    num=int(number[0])#列表变整形
    ls = len(title)#每页长度
    page =num//ls#计算页数
    nm = num%ls#计算是否有余数
    if nm>=0:#如果有余数页数+1
        page=page+1
    return page
def main():#分页爬取
    pg=pageNumber()
    for i in range(1,pg+1):
        number=str(i)
        page = "index_"+number+".html"
        rst = requests.get("http://www.ijjxsw.com/txt/Xuanhuan/"+page, headers=hd)
        wb_data = rst.text
        html = etree.HTML(wb_data)
        title = html.xpath('//span[@class="title"]//text()')#标题
        introduce = html.xpath('//div[@class="listbg"]//div[1]//text()')#简介
        informationList = html.xpath('//span[@class="mainGreen"]//text()')#未选取作者信息
        print("{0:=^20}".format(i))#打印当前爬取页数
        format(title,introduce,informationList)
def format(title,introduce,informationList):#格式化以及写入
    i=2
    author=[]#作者列表
    while i <= len(informationList):#筛选出作者并保存到author
        name=informationList[i]
        i=i+9
        author.append(name.replace('\r','').replace('\n',''))#过滤掉转义字符
    for i in range(0,len(title)):#文件写入与打印
        list = open('novel.txt', 'a', encoding='UTF-8')
        list.write(title[i]+"|"+introduce[i]+"|"+author[i])#存入文件
        list.write("\n")#换行
        text=title[i]+"|"+introduce[i]+"|"+author[i]
        print(text)#打印到控制台
    list.close()
if __name__ == '__main__':
   main()