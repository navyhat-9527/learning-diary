"""
    homework02 -  找到1- 10000内的所有完美数(除自身外的所有因子的和等于这个数)
    例:6 =1 + 2 + 3
    28 = 1 + 2 + 4 + 7 + 14
 Author : Iven
 Date : 2021/12/26
 """
for num in range (1 , 10001):
    total = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            total += i
            if i != num//i and num != num // i:
                total += num // i
    if num == total :
        print(num)
