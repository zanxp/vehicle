from bs4 import BeautifulSoup
import requests
import bs4
import re
import codecs
import xlrd
import xlwt

def getHTMLText(url,code="utf-8"):
    try:
        r= requests.get(url,timeout =30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getbrandgroupinitial(blst,html):
    soup = BeautifulSoup(html, "html.parser")
    jump = soup.find_all('div', {"class": "caption","id":re.compile("jump-*")})
    for i in jump:
        try:
            id = i.string
            blst.append(id)
        except:
            continue

def getbrandlist(blst,Brandlist,html):
    for jumpid in blst:
        try:
            # infoDict = {}
            soup = BeautifulSoup(html,"html.parser")
            brandinfo = soup.find('div', {"class": "caption", "id":"jump-" +jumpid}).next_sibling
            for i in brandinfo:
                Brandid = i["id"]
                Brandname = i.find("strong").string
                imglinks = i.find('img')
                if 'src' in imglinks.attrs.keys():
                    imglink = "http:"+imglinks["src"]
                else:
                    imglink = "http:"+imglinks["data-src"]
                infolist=[jumpid,Brandid,Brandname,imglink]
                # infoDict= {"Jumpid":jumpid,"Brandid":Brandid,"Brandname":Brandname,"imglink":imglink}
                Brandlist.append(infolist)

        except:
            return ""


def outputfile(Brandlist,fpath):
    file = xlwt.Workbook()
    sheet1 = file.add_sheet(u'sheet1', cell_overwrite_ok=True)
    row0 = [u'Jumpid',u'Brandid',u'Brandname',u'imglink']
    for i in range(len(row0)):
        sheet1.write(0, i, row0[i])
    for i, p in enumerate(Brandlist):
        for j, q in enumerate(p):
            sheet1.write(i + 1, j, q)

    file.save(fpath)


def main():
    blst = []
    Brandlist= []
    output_file = 'crowchexingku.xls'
    url = 'http://car.m.autohome.com.cn'
    html= getHTMLText(url)
    getbrandgroupinitial(blst,html)
    getbrandlist(blst,Brandlist,html)
    outputfile(Brandlist,output_file)




main()