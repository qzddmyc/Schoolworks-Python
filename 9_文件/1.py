with open("./徐公美.txt", 'r', encoding='utf-8') as f:
    txt = f.read()

new_txt = txt.replace('徐公', '徐坤')

with open("./徐公美.txt", 'w', encoding='utf-8') as f:
    f.write(new_txt)
