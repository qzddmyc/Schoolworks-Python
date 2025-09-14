str1 = "ab,cd"
str2 = "ef,gh"
str3 = str1 + str2
print(str3)
str4 = str3 * 2
print(str4)
str5 = str1.upper()
print(str1, str5)
result = str3 in str4
print(result)
id1 = str4.index('a')
print("{}中出现字母a的位置是{}".format(str4, id1))
id2 = str4.find('a')
print("{}中出现字母a的位置是{}".format(str4, id2))
list1 = str4.split(',')
print(list1)
print("我们一起去{0}, 你,尿了{2}, 我,尿了{1}。".format("尿尿", "一条线", "一个坑"))
