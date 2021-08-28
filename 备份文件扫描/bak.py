import time
import requests
from multiprocessing import Pool
def Conventional_detection(path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/101'
    }
    url = 'http://www.baidu.com'
    boop_url = url+path
    boop = requests.get(url=boop_url, headers=headers)
    ok_line = []
    try:
        if boop.status_code == 404:
            print('没有此地址文件:' + boop_url)
        else:
            waf_url = boop_url
            print(waf_url)
            time.sleep(3)
            ok_line.append(waf_url)
            result = waf_url + ' 探测结果：' + str(boop.status_code)
            result_path = open('./result.txt', 'w', encoding='utf-8')
            result_path.write(result + '\n')
    except:
        print('连接错误！')
        for i in ok_line:
            print(i)
        quit()

def Custom_Scan(dic_file):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/101'
    }
    #存放url地址
    url = 'http://www.baidu.com'
    houzui = {
        #备份文件后缀存放
        'zip':'.zip',
        'rar':'.rar',
    }
    #'请输入你要选择的扫描类型  (zip/rar)'
    choose = 'zip'
    bak_houzui = str(houzui[choose])
    path_bak = dic_file + bak_houzui
    new_url = url+path_bak
    boop = requests.get(url=new_url,headers=headers)
    if boop.status_code == 404:
        print('没有此地址文件:' + new_url)
    else:
        waf_url = new_url
        result = waf_url + ' 探测结果：' + str(boop.status_code)
        result_path = open('./result.txt', 'w', encoding='utf-8')
        result_path.write(result + '\n')


if __name__ == '__main__':


    # 放置字典
    file_name = './bak.txt'
    Feature_list = """
        1.常规目录字典扫描
        2.固定后缀自定义字典内容扫描
        (使用请输入序号!!)
        【Se37一山屿】开发
        (暂时只有两个功能)
    """
    print(Feature_list)
    time.sleep(0.4)
    choose_num = int(input('请输入你要选择的功能:'))
    # url = input('输入你要探测的url地址,后面不可接"/" :')
    kong = []
    #线程池数量，需要和下方end_num保持一致

    if choose_num  == 1:
        fp= open(file_name, 'r', encoding='utf-8')
        line = fp.read()
        line = line.strip().split('\n')
        start_num = 0
        #线程数量
        end_num = 20
        pool = Pool(20)
        while True:
            new_line = line[start_num:end_num]
            if new_line == kong:
                break
            # print(new_line)
            del line[start_num:end_num]
            pool.map(Conventional_detection, new_line)
    elif choose_num ==2 :
        #自定义文件字典
        file_name_two = './bak.txt'
        fp = open(file_name_two,'r',encoding='utf-8')
        line = fp.read()
        line = line.strip().split('\n')
        start_num = 0
        end_num = 20
        pool = Pool(20)
        while True:
            new_line = line[start_num:end_num]
            if new_line == kong:
                break
            # print(new_line)
            del line[start_num:end_num]
            pool.map(Custom_Scan, new_line)


