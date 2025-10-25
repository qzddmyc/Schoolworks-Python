import math

func = lambda x: (1 + math.log(x)) / (2 * math.pi)
ans = math.e ** 3 + sum([func(i) for i in range(1, 101)])
print(f's = {ans}')
