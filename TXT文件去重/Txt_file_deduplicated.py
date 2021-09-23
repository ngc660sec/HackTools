import os

class Txt_file_deduplicated():

    def __init__(self):
        self.file_dir_path = './txt_files/' #定义你要去重文件夹路径，目录中只能包含txt文件

    def Access_file(self):
        for root, dirs, files in os.walk(self.file_dir_path):
            self.root_path = root # 当前目录路径
            self.files_list = files # 当前路径下所有非目录子文件

    def get_new_path(self):
        for file_path in self.files_list:
            new_file_path = self.root_path+file_path
            print(new_file_path)
            self.duplicate_removal(new_file_path)

    def duplicate_removal(self,new_file_path):
        with open(new_file_path,'r+') as open_files:
            open_files_read = list(set(open_files.readlines()))
            open_files.close()
            new_open_file = open(new_file_path,'w')
            for open_files_line in open_files_read:
                if open_files_line == '':
                    continue
                else:
                    new_open_file.write(open_files_line)
            new_open_file.close()
        print('[*]>>>去重完成!!!')

    def run(self):
        self.Access_file()
        self.get_new_path()

if __name__ == '__main__':
    txt_file_deduplicated = Txt_file_deduplicated()
    txt_file_deduplicated.run()
