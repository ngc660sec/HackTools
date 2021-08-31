# -*- encoding:utf-8 -*-
import time


def four_code_create():
    # 4位手机验证码生成
    first_num = '0'
    fp = open('./four_code.txt', 'w', encoding='utf-8')
    for phone_code in range(0, 10000):
        if len(str(phone_code)) < 4:
            len_code = len(str(phone_code))
            four_code = 4
            fill_num = four_code - len_code
            new_num = fill_num * first_num + str(phone_code)
            fp.write(new_num + '\n')
        else:
            fp.write(str(phone_code) + '\n')

def six_code_create():
    # 6位手机验证码生成
    first_num = '0'
    fp = open('./six_code.txt', 'w', encoding='utf-8')
    for phone_code in range(0, 1000000):
        if len(str(phone_code)) < 6:
            len_code = len(str(phone_code))
            six_code = 6
            fill_num = six_code - len_code
            new_num = fill_num * first_num + str(phone_code)
            fp.write(new_num + '\n')

if __name__ == '__main__':
    readme = """
            1.生成4位手机验证码
            2.生成6位手机验证码
            (使用请输入序号)
            【Se37-山屿】开发
    """
    print(readme)
    time.sleep(0.3)
    choose = int(input('请输入你的选择：'))
    if choose == 1:
        four_code_create()
        print('生成完毕！！')
    else:
        six_code_create()
        print('生成完毕！！')
