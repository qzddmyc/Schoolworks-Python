import csv

with open('./score.txt', 'r', encoding='utf-8') as f:
    score = csv.DictReader(f)
    all_score = []
    for each in score:
        each['总评成绩'] = round(float(each['平时成绩']) * 0.4 + float(each['期末成绩']) * 0.6)
        all_score.append(each)

all_score.sort(key=lambda x: -x['总评成绩'])

with open('./score.txt', 'r', encoding='utf-8') as f:
    header = f.readline().strip().split(',')
    header.append('总评成绩')

with open('./score_sorted.txt', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(all_score)
