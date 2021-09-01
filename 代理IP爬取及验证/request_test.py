import requests
import re
from concurrent.futures import ThreadPoolExecutor


wp = open('./ok_ping_ip.txt','r',encoding='utf-8')

def get_response(ip_port_list):

    # for new_ip_port in ip_port_list:
    new_ip_port = str(ip_port_list)
    # print(new_ip_port)
    port = re.findall(r'\d\d\d\d', new_ip_port)
    ip = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', new_ip_port)
    ip = str(ip[0])
    port = str(port[0])
    print(ip,port)
    proxy_headers = {
        'http:':'http://' + str(ip) + str(port),
        'https:':'https://' + str(ip) + str(port),
    }
    try:
        response = requests.get(url='http://icanhazip.com', proxies=proxy_headers, timeout=5)
        if response.status_code == 200:
            print('200 is ok ==>' + response.text+'请求成功!')
            fp = open('./ok_daili.txt', 'a+')
            fp.write(ip+":"+port + '\n')
    except:
        print("[!]==>"+ ip+":"+port+"不可用！")


if __name__ == '__main__':
    pool = ThreadPoolExecutor(100)
    for i in wp.readlines():
        ip_port_list = i.strip().split(':')
        pool.submit(get_response,ip_port_list)


