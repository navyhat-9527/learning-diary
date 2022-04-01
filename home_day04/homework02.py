"""
    homework02 -  输入一段话, 统计每个单词的出现次数
 Author : Iven
 Date : 2022/3/9
"""

sentence = input('please input your sentence:').lower()
words = sentence.replace('.', ' ').replace(',', ' ').split()

counter = {}


for word in words:
    counter[word] = counter.get(word, 0) + 1  # 取counter的key为word的value, 若没有则赋值为默认值0,使这个值+1

sorted_key = sorted(counter, key=counter.get, reverse=True)

for key in sorted_key:
    print(f'{key}:{counter[key]}', end=',')
