import random


def redPacket(totalMoney: float = 100, person: int = 15) -> list[float] | list[str]:
    def getSingleAmount(resMoney: int, resPerson: int) -> int:
        resMoney = int(resMoney * 100)
        while resPerson > 1:
            max_amount = max(min(int(2 * resMoney / resPerson), resMoney - (resPerson - 1)), 1)
            amount = random.randint(1, max_amount)
            resMoney -= amount
            resPerson -= 1
            yield amount / 100
        yield resMoney / 100

    if totalMoney * 100 < person:
        return ['无法分配']

    result = []
    for amount in getSingleAmount(totalMoney, person):
        result.append(amount)
    return result


if __name__ == '__main__':
    money = float(input('请输入总金额：'))
    money = int(money * 100) / 100
    cnt = int(input('请输入总人数：'))
    print(f'红包的分配如下：{', '.join([str(i) for i in redPacket(money, cnt)])}')
