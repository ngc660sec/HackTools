import os
from concurrent.futures import ThreadPoolExecutor
import hashlib

class Sqlmap_batch_scan():

    def __init__(self):
        pass

    def run_sqlmap(self,sqlmap_url,url_name):
        print(f"[*]>>>正在测试URL:{sqlmap_url}")
        new_url_name = hashlib.md5(url_name.encode("utf-8")).hexdigest()
        #存放报告的路径
        report_path = 'E:/python/HACK/Sqlmap批量扫描/'
        os_command = r'sqlmap.py -u "{}" --batch > "{}{}.txt"'.format(sqlmap_url,report_path,new_url_name)
        # print(os_command)
        os.system(os_command)
        print(f'[+]>>>已生成报告:{new_url_name}.txt')

    def run(self,sqlmap_url,url_name):
        self.run_sqlmap(sqlmap_url,url_name)

if __name__ == '__main__':
    sqlmap_batch_scan = Sqlmap_batch_scan()
    #线程池数量
    sqlmap_pool = ThreadPoolExecutor(10)
    sqlmap_file = open('./sqlmap_url.txt','r')
    sqlmap_urls = sqlmap_file.readlines()
    for url in sqlmap_urls:
        sqlmap_url = url.strip()
        url_name = sqlmap_url
        sqlmap_pool.submit(sqlmap_batch_scan.run,sqlmap_url,url_name)
    sqlmap_file.close()
