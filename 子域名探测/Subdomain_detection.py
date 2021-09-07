import requests
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue


class Subdomain_detection():
    ok_stat_url = Queue()

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/101"
        }

        self.zu_domain = '.qq.com' #定义根域名
        self.head_domain = 'https://' #http或者https

    def get_url_stat(self, zi_domain):
        # print(zi_domain)
        all_url = self.head_domain+zi_domain+self.zu_domain
        print(all_url)
        domain_stat = requests.get(url=all_url,headers = self.headers,timeout = 10).status_code
        # print('yes')
        if domain_stat == 200:
            self.ok_stat_url.put(all_url)
            print('[*]'+all_url+' '+str(domain_stat)+' OK!!')
        else:
            self.ok_stat_url.put(all_url)
            print('[!]'+all_url+' '+str(domain_stat)+' Flase!!')

    def save_subdomain_url(self):
        while self.ok_stat_url.empty() == False:
            ok_domain = self.ok_stat_url.get()
            with open('./ok_zi_domain.txt','a+',encoding='utf-8') as fp:
                fp.write(ok_domain+'\n')

    def run(self,zi_domain):
        self.get_url_stat(zi_domain)
        self.save_subdomain_url()

if __name__ == '__main__':
  ##使用前创建你的zi_domain.txt，用于存放子域名，在类下的init处定义你的根域名和请求方式
    subdomain_detection = Subdomain_detection()
    pool = ThreadPoolExecutor(1)
    fp = open('./zi_domain.txt','r',encoding='utf-8')
    zi_domain_list = fp.read().splitlines()
    for domain in zi_domain_list:
        # print(domain)
        pool.submit(subdomain_detection.run,domain)


