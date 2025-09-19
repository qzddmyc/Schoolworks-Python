x = int(input('x = '))
y = int(input('y = '))
if x == 0:
    print('位于y轴')
elif y == 0:
    print('位于x轴')
elif x > 0 and y > 0:
    print('第一象限')
elif x < 0 and y > 0:
    print('第二象限')
elif x < 0 and y < 0:
    print('第三象限')
else:
    print('第四象限')
