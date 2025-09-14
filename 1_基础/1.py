x = 5
y = 2
sx, sy = str(x), str(y)
symbols = ['+', '-', '*', '/', '//', '%', '**']
for i in symbols:
    print(f'{x} {i} {y} = {eval(sx + i + sy)}')
execs = [
    f'{x} > {y}', f'{x} == {y}', f'{x} and {y}', f'{x} or {y}', f'not {x}',
    f'({x} and {y}) and ({x} or {y})', f'({x} and {y}) or ({x} or {y})'
]
for i in execs:
    print(f'{i} is {eval(i)}')
