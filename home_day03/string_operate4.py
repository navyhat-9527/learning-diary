"""
    string_operate4 - 字符串的操作

凯撒密码 - 通过对应的字符替换, 实现对明文进行加密的一种方式.

abcdefghijklmnopqrstuvwxyz
defghijklmnopqrstuvwxyzabc

明文: attack at dawn
密文: dwwdfn dw gdzq
对称加密: 加密和解密使用相同的密钥 ---AES
非对称加密: 加密和解密使用不同的密钥(公钥, 私钥) ---> 适用于互联网应用---- RSA


 Author : Iven
 Date : 2022/3/7
"""
import random
import string

message = 'attack at dawn'
table = str.maketrans(
    'abcdefghijklmnopqrstuvwxyz',
    'defghijklmnopqrstuvwxyzabc'
)
# print(message.translate(table))


# nums = [i for i in '0123456789']
# big_letters = [chr(i) for i in range(65, 91)]
# small_letters = [chr(i) for i in range(97, 123)]
# all_chars = nums + big_letters + small_letters
all_chars = string.digits + string.ascii_letters

for _ in range(10):
    # 可迭代对象
    select_chars = random.choices(all_chars, k=4)
    print(''.join(select_chars))
