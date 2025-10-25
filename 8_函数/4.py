def func(i):
    if i <= 0:
        return 0
    if i == 1:
        return 1 / 3
    return i / (2 * i + 1) + func(i - 1)


if __name__ == '__main__':
    i = int(input('i = '))
    print(f'm(i) = {func(i)}')
