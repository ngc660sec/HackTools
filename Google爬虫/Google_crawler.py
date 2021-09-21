import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

class Google_crawler():

    def __init__(self,):

        self.Google_crawler_txt = open('./Google_crawler.txt','a+')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/101'
        }

    def Request_data(self,search_q,stop_page):

        self.request_url = f'https://g.luciaz.me/search?q={search_q}&start={stop_page}'
        self.page_data = requests.get(url=self.request_url,headers=self.headers).text

    def Analytical_data(self):
        page_html = etree.HTML(self.page_data)
        page_html_xpath = page_html.xpath('//*[@class="yuRUbf"]')
        for page_url in page_html_xpath:
            url = page_url.xpath('./a/@href')[0]
            self.Google_crawler_txt.write(url+'\n')
            print(f'[*]>>>{url}写入完成!!')

    def run(self,search_q,stop_page):
        self.Request_data(search_q,stop_page)
        self.Analytical_data()

if __name__ == '__main__':
    google_crawler = Google_crawler()
    #定义线程数量
    pool = ThreadPoolExecutor(2)
    #定义谷歌语法
    search_q = 'inurl:asp?id=2 公司'
    #爬取页数
    stop_page = 2
    for page in range(stop_page):
        page *=10
        pool.submit(google_crawler.run,search_q,page)
    pool.shutdown()



