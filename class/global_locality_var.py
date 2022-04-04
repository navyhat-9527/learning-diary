"""
    global_locality_var - 全局变量 和 局部变量
全局变量:没有定义在在任何函数里面
局部变量:定义在在函数内的变量
python程序搜索一个变量是安装LEGB顺序搜索

Local ---> Embed(嵌套作用域) ---> Global ---> build-in ---> NameError: name ... not defined


 Author : Iven
 Date : 2022/3/16
"""

x = 100  # 全局变量


def foo():
    # 不定义局部变量,直接使用全局变量
    global x
    x = 200
    def bar():
        # nonlocal x
        x = 300
        print(x)
    bar()
    print(x)

foo()
print(x)




