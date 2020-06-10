# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         parser
# Description:  
# Author:       ffish
# Date:         2019/9/25
#-------------------------------------------------------------------------------
from http.server import BaseHTTPRequestHandler,HTTPServer
import urllib
import requests
from bs4 import BeautifulSoup
import datetime

class Parser(BaseHTTPRequestHandler):
    def do_GET(self):
        log("正在获取keyword...")
        if '?' in self.path:
            self.queryString = urllib.parse.unquote(self.path.split('?',1)[1])
            params = urllib.parse.parse_qs(self.queryString)
            code_url = 'https://www.yahaha.online' + params['url'][0]
            cookie = 'PHPSESSID=' + params['PHPSESSID'][0]
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cookie": cookie,
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
            }
            resp = requests.get(url=code_url,headers=headers)
            reditList = resp.history
            location = reditList[len(reditList)-1].headers['Location']

            if location != None:
                sps = location.split("/")
                gif = sps[len(sps)-1]
                keyword = gif.split(".")[0]
                len("keyword 获取成功！")
                isExist,MF = Search(keyword)
                if isExist:
                    log("解析成功。化学式为:"+MF)
                else:
                    log("解析失败。可能该keyword的化学式不存在，可以尝试重新获取...")
            else:
                len("keyword 获取失败！")

        try:
            self.send_response(200)
            self.send_header('Content-type',"image/png")
            self.end_headers()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

def Search(keyword):
    log("正在解析keyword为化学式...")
    url = 'https://www.chemicalbook.com/Search.aspx?keyword='

    isExist = False
    MF = None
    resp = requests.get(url+keyword)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    if len(soup.select('table.mid')[0].find_all('a',href='CAS/GIF/'+keyword+'.gif')) > 0:
        isExist = True
        MF = soup.select('table.mid')[0].select('table.mbox')[0].select('tr')[3].select('td')[1].get_text()
    return isExist,MF

def log(text):
    currTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(currTime,":",text)

def main():
    HOST = "127.0.0.1"
    PORT = 43271
    ADDR = (HOST,PORT)
    try:
        server = HTTPServer(ADDR,Parser)
        print("######################################################################")
        print("#--------------------------------------------------------------------#")
        print("#-----------------------欢迎使用EasyParser工具-----------------------#")
        print("#--------------------------------------------------------------------#")
        print("######################################################################")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == '__main__':
    main()