class Duplicate_removal():

    def __init__(self):
        self.ok_url_file = open('./sqlmap_ok_url.txt','r+',encoding='utf-8')
        self.flase_url_file = open('./sqlmap_flase_url.txt','r+',encoding='utf-8')

    def main(self):
        ok_url_text = self.ok_url_file.readlines()
        flase_url_file = self.flase_url_file.readlines()
        self.ok_url_file.close()
        self.flase_url_file.close()

        self.new_ok_url_text = list(set(ok_url_text))
        self.new_flase_url_text = list(set(flase_url_file))

    def stroge_url(self):
        ok_url_file = open('./sqlmap_ok_url.txt','w')
        flase_url_file = open('./sqlmap_flase_url.txt','w')
        for ok_url in self.new_ok_url_text:
            new_ok_url = ok_url.strip()
            if new_ok_url == '':
                continue
            else:
                ok_url_file.write(new_ok_url + '\n')
        for flase_url in self.new_flase_url_text:
            new_flase_url = flase_url.strip()
            if new_flase_url == '':
                continue
            else:
                flase_url_file.write(new_flase_url + '\n')

    def run(self):
        self.main()
        self.stroge_url()
        print("[*]>>>去重完成")

if __name__ == '__main__':
    # duplicate_removal = Duplicate_removal()
    # run = duplicate_removal.run()
    pass
