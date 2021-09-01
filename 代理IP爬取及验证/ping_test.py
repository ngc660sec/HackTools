# -*- encoding:utf-8 -*-

import requests
import os
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue
import re

fp = open('./未校验代理.txt','r',encoding='utf-8')
wp = open('./ok_ping_ip.txt','a+',encoding='utf-8')
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
        port = port_put.get()
        ip_port = [ip,port]
        ip_amd = os.system(u'ping ' + str(ip_port[0])+'')
        if ip_amd == 0:
            new_ip_port_list = ip_port
            print(str(ip) + '>>>' + 'YES!!')
            new_ip_port = new_ip_port_list[0]+':'+new_ip_port_list[1]
            print(new_ip_port)
            wp.write(new_ip_port+'\n')
        else:
            print(ip + '>>>' + "False!!")


if __name__ == '__main__':
    det_ip_port()
    #不想内存溢出就调小一点,50刚好
    pool = ThreadPoolExecutor(300)
    while ip_put.empty() == False:
        pool.submit(set_ping)
        # pool.shutdown()
    # print('[*]ping is OK ....')

