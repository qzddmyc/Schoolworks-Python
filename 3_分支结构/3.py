dis = int(input("距离: "))
cost = 10
if dis > 10:
    cost += (dis - 10) * 1.5
    dis = 10
if dis > 3:
    cost += (dis - 3) * 1.2
    dis = 3
print(f'费用: {cost:.1f}')
