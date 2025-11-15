import csv
from collections import defaultdict

dic = defaultdict(lambda: {'cnt': 0, 'sumFixedAcidity': 0, 'items': []})

with open('./white_wine.csv', 'r', encoding='utf-8') as f:
    score = csv.DictReader(f)
    for s in score:
        q = s['quality']
        dic[q]['items'].append(s)
        dic[q]['cnt'] += 1
        dic[q]['sumFixedAcidity'] += float(s['fixed acidity'])

dic = {k: dic[k] for k in sorted(dic.keys())}

print(f'白葡萄酒总共分为{len(dic)}种品质等级')
for k, v in dic.items():
    print(f'等级{k}的数量为{v['cnt']}, fixed acidity的均值为{v['sumFixedAcidity'] / v['cnt']:.2f}')

# 应当使用 pandas 模块，但是不想学 :(
