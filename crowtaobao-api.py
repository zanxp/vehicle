import requests
import json


# def getHTMLText(url):
#     try:
#         r = requests.get(url,timeout = 30)
#         r.rasie_for_status()
#         r.encoding= r.apparent_encoding
#         return r.text
#     except:
#         return ""

def parsePage(ilt,html):
    try:
        data = json.loads(html)
        list = data['API.CustomizedApi']['itemlist']['auctions']
        for n in list:
            raw_title = n ['raw_title']
            view_price = n ['view_price']
            ilt.append([raw_title,view_price])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))



def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/api?&m=customized&q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(36 * i)
            # html = getHTMLText(url)
            wbdata = requests.get(url).text
            parsePage(infoList, wbdata)
        except:
            continue
    printGoodsList(infoList)

main()