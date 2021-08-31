# -*- encoding:utf-8 -*-


from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import time

#爬取代理ip，并且保存
fp = open('未校验代理.txt', 'a+', encoding='utf-8')
def down_load_ip_port(url):
    print(f"开始下载{url}....")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/101'
    }
    get_url_page = requests.get(url= url,headers=headers,timeout=5).text
    print(f"{url} 请求完成")
    tree = etree.HTML(get_url_page)
    all_ip_port = tree.xpath('//*[@id="list"]/table')
    # print(all_ip_port)
    return all_ip_port

def write_ip_port(all_ip_port):
    all_ip_port = all_ip_port.result()
    # print(all_ip_port)
    for ip_port in all_ip_port:
        ip_list = ip_port.xpath('./tbody/tr/td[@data-title="IP"]/text()')
        port_list = ip_port.xpath('./tbody/tr/td[@data-title="PORT"]/text()')
        print(f"{url} 解析完成!!")
        # print("下载完成!!")
        for ip, port in zip(ip_list, port_list):
            new_ip_port = ip + ":" + port
            fp.write(new_ip_port+'\n')
            # print(new_ip_port)
        print('爬取成功!!!')

if __name__ == '__main__':
    # down_load_ip_port('https://www.kuaidaili.com/free/inha/1')
    #此处限定一个线程，因为快了被ban
    pool = ThreadPoolExecutor(1)
    #定义要爬取的页数
    num = 10
    for i in range(num):
        #别尝试改这个，被ban了不怪我
        time.sleep(1)
        url = f'https://www.kuaidaili.com/free/inha/{i}/'
        pool.submit(down_load_ip_port,url).add_done_callback(write_ip_port)
        # print(res)
