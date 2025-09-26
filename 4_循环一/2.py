sum = 0
cnt = 0
for i in range(1, 9, 2):
    sum = sum + i
    cnt += 1
    print(f"第{cnt}次循环，当前 i = {i}, sum = {sum}")
print('-' * 30)
print("sum=", sum)
