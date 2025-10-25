def dialogueWithPenguin(i) -> None:
    def not_douDou(n):
        print(f'记者问第{n}只企鹅：你每天都干什么？')
        print(f'第{n}只企鹅：吃饭 睡觉 打豆豆！')

    def douDou(n):
        print(f'记者问第{n}只企鹅：你每天都干什么？')
        print(f'第{n}只企鹅：吃饭，睡觉。')
        print(f'记者惊奇地问：你怎么不打豆豆？')
        print(f'第{n}只企鹅：我就是豆豆！！！！')

    if i <= 99:
        not_douDou(i)
        return
    douDou(i)


if __name__ == '__main__':
    for idx in range(1, 101):
        dialogueWithPenguin(idx)
