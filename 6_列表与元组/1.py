maps = [
    28 if i == 2 else (31 if (i <= 7 and i & 1 or i > 7 and not i & 1) else 30)
    for i in range(1, 13)
]
month = int(input("请输入一个月份："))
if month not in tuple(range(1, 13)):
    print('月份错误')
else:
    print(f'{month}月有{maps[month - 1]}天')
