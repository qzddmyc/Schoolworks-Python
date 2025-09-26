print('-' * 5 + ' situation-1 ' + '-' * 5 + '\n')

word = input("请输入一串字符：")
reversedWord = ""
for ch in word:
    reversedWord = ch + reversedWord
print("The reversed word is: " + reversedWord)

print('\n' + '-' * 5 + ' situation-2 ' + '-' * 5 + '\n')

word = input("请输入一串字符：")
reversedWord = ""
for ch in word:
    reversedWord = reversedWord + ch
print("The reversed word is: " + reversedWord)
