list_student = [["001", "李元芳", 19], ["002", "刘禅", 20], ["003", "张三丰", 18]]
# (a)
list_student.append(["004", "柯镇恶", 19])
list_student.append(["006", "十三郎", 20])
# (b)
list_student.insert(4, ["005", "唐涤生", 20])
# (c)
data_003 = list_student[2]
print(' '.join(map(str, data_003)))
print('-' * 16)
# (d)
for i in list_student:
    print(i[1])
print('-' * 16)
# (e)
for i in list_student:
    if i[2] > 19:
        print(' '.join(map(str, i)))
