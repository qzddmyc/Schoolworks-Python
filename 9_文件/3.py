with open('./data.txt', 'r', encoding='utf-8') as f:
    data = list(map(int, f.read().strip().split(',')))

data.sort()
data = [str(i) for i in data]

with open('./data_sorted.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(data))
