def guess_age_in_2016(lastOfPhoneNumber: int, bornYear: int) -> int:
    ans = (lastOfPhoneNumber * 2 + 5) * 50 + 1766 - bornYear
    return int(str(ans)[-2:])


def guess_age_in_2025(lastOfPhoneNumber: int, bornYear: int) -> int:
    ans = (lastOfPhoneNumber * 2 + 5) * 50 + 1766 - bornYear + (2025 - 2016)
    return int(str(ans)[-2:])


if __name__ == "__main__":
    l = int(input('输入你手机号的最后一位：'))
    b = int(input('输入你的出生年份：'))
    print(f'2016年你的年龄为：{guess_age_in_2016(l, b)}')
    print(f'现在，你的年龄为：{guess_age_in_2025(l, b)}')
