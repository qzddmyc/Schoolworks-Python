from random import randint as r
from math import gcd, lcm

RND1, RND2 = r(0, 100), r(0, 100)
print(f"随机整数 RND1 = {RND1}, RND2 = {RND2}")
print(f"最大公约数 = {gcd(RND1, RND2)}")
print(f"最小公倍数 = {lcm(RND1, RND2)}")


# 造个轮子
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def LCM(a, b):
    return a * b // GCD(a, b)
