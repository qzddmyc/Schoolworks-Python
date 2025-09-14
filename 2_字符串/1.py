s1 = "文人独酌当晓月"
s2 = "思者孤形缠林间"
print(s1 + s2)
print(s1 * 2)
print(3 * s2)
try:
    print(s1 * s2)
except Exception as e:
    print(f'Error: {e} in s1 * s2.')
print("眉" in s1)
print(s1[0])
print(s1[0:-1])
print(s1[0:])
print(s2[-3:-1])
print(s1[::-1])
print(s2[::2])
print(s2[1::2])
print(s1 > s2)
print(len(s1))
