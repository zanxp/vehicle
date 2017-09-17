import requests
from bs4 import BeautifulSoup
import bs4



def getHTMLText(url):
    try:
        r= requests.get(url,timeout =30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""




def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    sibling= soup.find_all("table",{"cellpadding":"0","cellspacing":"0"})
    table1 = sibling[1]
    for tr in table1:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string])


def printUnivList(ulist,num):
    tplt = "{:^10}\t{:^10}"
    print(tplt.format("Item","数值"))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1]))
def main():
    uinfo =[]
    url = 'http://www.cnev.cn/chexing/jilidihaoEV/canshu.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,5)

main()