import random

class Dictionary():
    def __init__(self):
        self.res_list = []
        self.Letter_number_list = []
        self.fp = open('./res_list.txt','a+',encoding='utf-8')
        while True:
            Letter_num = input('请输入你要生成的字母或者数字:')
            if Letter_num == 'SE':
                break
            elif Letter_num == 'a-z' or Letter_num == 'A-Z':
                self.Letter_number_list.append(Letter_num)
                break
            else:
                self.Letter_number_list.append(Letter_num)
        self.Digits = int(input('请输入你要生成的位数:'))
        print(self.Letter_number_list)

    def Generate(self):
        global az_letter_number
        if self.Letter_number_list[0] == 'a-z':
            digits = self.Digits
            # print(digits)
            az_letter_number = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            for i in range(int(len(az_letter_number))  ** self.Digits *2):
                print(f'一共需要生成{int(len(az_letter_number)) ** self.Digits *2}条数据')
                res = random.sample(az_letter_number , self.Digits)
                self.Conversion(res)
                # print(f'正在生成{i}')
                print(f'剩余{(int(len(az_letter_number)) ** self.Digits *2) - i}条数据')


        elif self.Letter_number_list[0] == 'A-Z':
            AZ_letter_number = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for i in range(int(len(AZ_letter_number)) ** self.Digits *2):
                print(f'一共需要生成{int(len(AZ_letter_number)) ** self.Digits *2 }条数据')
                res = random.sample(az_letter_number,self.Digits)
                self.Conversion(res)
                print(f'剩余{(int(len(AZ_letter_number)) ** self.Digits *2) - i}条数据')

        else:
            for i in range(self.Digits ** 10 * 100):
                res = random.sample(self.Letter_number_list, 1)
                self.Conversion(res)
            # print(res)
        # print(self.res_list)
        n =0
        for i in self.res_list:
            self.fp.write(i+'\n')
            n+=1


        print('生成完毕！')
        print(f'一共生成{n}条数据！！')

    def Conversion(self,res):
        res = ''.join(res)
        self.res_list.append(res)
        self.res_list = set(self.res_list)
        self.res_list = list(self.res_list)
        return self.res_list


    def run(self):
        # print(self.Letter_number_list)
        self.Generate()

if __name__ == '__main__':

    prompt = '''
            【自定义字典生成】
            【Se37】山屿开发
            1.输入你要生成的字母或者数字，同时输入SE退出【注意大写！】
            2.输入你要生成的位数
            3.若要生成[a-z]字符中的随机位数，则输入[a-z]或者[A-Z]
            
    '''
    print(prompt)
    dictionary = Dictionary()
    dictionary.run()

