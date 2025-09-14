ls = []
prompts = ['我的名字是：', '我第一个队友的名字是：', '我第二个队友的名字是：', '我第三个队友的名字是：']
for p in prompts:
    ls.append(input(p))
rev = [i[::-1] for i in ls]
heads, *_ = zip(*rev)
print(f'我们的组合是：{''.join(heads)}')
