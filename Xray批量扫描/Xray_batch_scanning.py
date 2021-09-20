import os
import hashlib
import re
from concurrent.futures import ThreadPoolExecutor

class Xray_batch_scanning():

    def __init__(self):
        pass

# 报告
    def do_scan(self,targeturl,outputfilename="test"):
        scan_command="xray webscan --basic-crawler {} --html-output {}.html".format(targeturl,outputfilename)
        # print(scan_command)
        os.system(scan_command)
        return

if __name__ == '__main__':
    xray_batch_scanning = Xray_batch_scanning()
    pool = ThreadPoolExecutor(10)
    fp = open('./xray_url.txt','r')
    lines = fp.readlines()
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                targeturl = "http://" + line.strip()
            else:
                targeturl = line.strip()
            # print(targeturl.strip())
            outputfilename = hashlib.md5(targeturl.encode("utf-8"))
            # xray_batch_scanning.do_scan(targeturl.strip(), outputfilename.hexdigest())
            pool.submit(xray_batch_scanning.do_scan,targeturl.strip(),outputfilename.hexdigest())
            # pool.shutdown()
        except Exception as e:
            print(e)
            pass
    fp.close()


