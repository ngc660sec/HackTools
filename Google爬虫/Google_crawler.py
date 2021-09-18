from selenium import webdriver
from lxml import etree
import re
from urllib.parse import quote,unquote

class Google_crawler():
    def __init__(self):
        self.fp = open('./Google_crawler_url.txt','a+')
        self.google_url = 'https://www.google.com.hk'
        self.google_grammar = input('请输入你的谷歌语法，空格用+代替:')
        self.crawl_num = int(input('请输入你要爬取的页数:'))
        self.search_url = 'https://www.google.com.hk/search?q='+self.google_grammar+'&hl=en&start=10'
        self.pattern = '(?<=q=).*?(?=&)'
        self.empty_list = []

    def Initialize_the_browser(self):
        self.bro = webdriver.Chrome(executable_path='chromedriver.exe')
        self.bro.get(self.search_url)
        self.Perform_signal = input('请输入【S】进行下一步操作:')

    def Analytical_data(self,etree_text):
        tree_data = etree_text.xpath('//*[@class="kCrYT"]')
        next_click = self.bro.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/a[2]/span')
        for own_tree_data in tree_data:
            new_own_tree_data = own_tree_data.xpath('./a/@href')
            # print(new_own_tree_data)
            if new_own_tree_data == self.empty_list:
                # print(new_own_tree_data)
                continue
            else:
                old_tree_list_url = new_own_tree_data[0]
                tree_url = re.findall(self.pattern, old_tree_list_url)
                crawl_url = unquote(tree_url[0])
                self.fp.write(crawl_url+'\n')
                print('[*]>>>'+crawl_url+' 写入完成!')
        return next_click

    def Crawl_data(self):
        if self.Perform_signal == 'S':
            start_page = self.bro.page_source
            start_tree = etree.HTML(start_page)
            next_click = self.Analytical_data(start_tree)
            next_click.click()
            for i in range(self.crawl_num):
                page_text= self.bro.page_source
                page_tree = etree.HTML(page_text)
                next_click = self.Analytical_data(page_tree)
                next_click.click()

    def run(self):
        self.Initialize_the_browser()
        self.Crawl_data()

if __name__ == '__main__':
    #使用前先安装最上方的第三方库，再安装自己Google版本对应的chromedriver.exe
    #使用过程中需要手动禁止浏览器的JS，完成之后输入[S]即可
    introduce = """
            ------【Se37安全团队——山屿.EQr开发】------
            ------【使用前请先查看源代码，以寻求帮助】------
    """
    print(introduce)
    google_crawler = Google_crawler()
    google_crawler.run()


