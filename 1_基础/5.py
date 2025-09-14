work = 1
sleep = 1
for _ in range(365):
    work = work * 1.01
    sleep = sleep * 0.99
print(f'天天向上: {work}')
print(f'天天向下: {sleep}')
