"""
    example03 -ABCDE无人去捕鱼,补了不计其数的鱼,然后累了睡去
    第二天,A第一个醒来,把鱼分为五份,扔掉多余的一条鱼,然后拿走了自己的一份;
    B第二个醒来,以为鱼没有分过,又把鱼分为五份,扔掉多余的一条鱼,然后拿走了自己的一份;
    CDE依次醒来按照相同的方式分鱼,问他们最少补了多少条鱼.

 Author : Iven
 Date : 2021/12/28
"""


fish = 1  # 假设开始鱼只有一条
while True:   #因为不知道到底有多少条,采用while循环穷举
    is_enough = True
    total = fish
    for i in range(5):
        if (total -1 ) % 5 ==0:  #如果扔掉一条后不够平分5分责可以直接跳过检验
            total = (total -  1)//5*4  #检验是否能够满足题意
        else:
            is_enough = False
            break
    if is_enough:
        print(fish)
        break


    fish += 1 # 如果循环检验出鱼不够分,责加一条鱼继续测试