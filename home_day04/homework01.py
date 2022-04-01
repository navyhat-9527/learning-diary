"""
    homework - 输入一段话, 统计每个英文字母的出现次数
 Author : Iven
 Date : 2022/3/9
"""
import string

sentence = input('please input your sentence:').lower()

counter = {letter : 0 for letter in string.ascii_lowercase}
print(counter)

for ch in sentence:
    if ch in counter:
        counter[ch] += 1

for key, value in counter.items():
    print(key, value)



