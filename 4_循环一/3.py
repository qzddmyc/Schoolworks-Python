s = odd = even = cnt = 0
while (ipt := input('Integer: ')) != 'A':
    num = int(ipt)
    if num & 1:
        odd += num
    else:
        even += num
    s += num
    cnt += 1
print(f'奇数之和: {odd}')
print(f'偶数之和: {even}')
print(f'所有数平均值: {0 if cnt == 0 else s / cnt}')
