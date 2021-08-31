# -*- encoding:utf-8 -*-

import requests
import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue
import re

fp = open('./未校验代理.txt','r',encoding='utf-8')
ip_put = Queue()
port_put = Queue()
ok_ping_ip = Queue()

def det_ip_port():

    ip_port = fp.read().splitlines()

    # print(ip_port)
    for ip in ip_port:
        ip = ip.strip()
        port = re.findall(r'\d\d\d\d', ip)
        ip = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', ip)
        for new_ip,new_Port in zip(ip,port):
            ip_put.put(new_ip)
            port_put.put(new_Port)
            # print(new_ip,new_port)

def set_ping():
    while ip_put.empty() == False:
        ip = ip_put.get()
        # port = port_put.get()
        ip_amd = os.system(u'ping ' + str(ip)+'')
        if ip_amd == 0:
            print(str(ip) + '>>>' + 'YES!!')
            # ok_ping_ip.put(ip)
        else:
            print(ip + '>>>' + "False!!")

def get_response():
    while ip_put.empty() == False:
        ip = ip_put.get()
        port = port_put.get()
        proxy_headers = {
            'http:':'http://' + ip + port,
            'https:':'https://' + ip + port,
        }
        try:
            response = requests.get(url='http://icanhazip.com', proxies=proxy_headers, timeout=5)
            if response.status_code == 200:
                print('200 is ok ==>' + response.text+'请求成功!')
                fp = open('ok_daili.txt', 'a+')
                fp.write(ip+":"+port + '\n')
        except:
            print("[!]==>"+ ip+":"+port+"不可用！")




if __name__ == '__main__':
    det_ip_port()
    #不想内存溢出就调小一点,50刚好
    pool = ThreadPoolExecutor(50)
    while ip_put.empty() == False:
        pool.submit(set_ping)
        pool.submit(get_response)

