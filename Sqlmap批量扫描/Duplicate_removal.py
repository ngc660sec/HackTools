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
            ok_url_file.write(ok_url)
        for flase_url in self.new_flase_url_text:
            flase_url_file.write(flase_url)
        flase_url_file.close()
        ok_url_file.close()

    def run(self):
        self.main()
        self.stroge_url()
        print("[*]>>>去重完成")

if __name__ == '__main__':
    duplicate_removal = Duplicate_removal()
    duplicate_removal.run()
