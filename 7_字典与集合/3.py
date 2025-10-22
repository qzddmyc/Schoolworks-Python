import re

s = "Whether the weather be fine, or whether the weather be not. Whether the weather be cold, or whether the weather be hot.We will weather the whether we like it or not."
s = set(re.findall(r'\b[a-z]+\b', s.lower()))

print(f"英文单词个数为：{len(s)}")
