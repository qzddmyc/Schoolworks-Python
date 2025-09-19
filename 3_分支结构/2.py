import re

ch = input("输入一个字符: ")
if re.match(r'^[a-zA-Z]$', ch):
    print('输入的英文字母')
elif re.match(r'^[0-9]$', ch):
    print('输入的是数字')
else:
    print('输入的是什么鬼？')
