import re

with open('./泰戈尔的诗a.txt', 'r', encoding='gbk') as f:
    while line := f.readline():
        if re.match(r'^[^#].*[\u4e00-\u9fa5].*$', line):
            print(line, end='')
