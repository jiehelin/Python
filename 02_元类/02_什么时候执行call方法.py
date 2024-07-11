# -*- coding:utf-8 -*-
# created by xiehelin

class Obj(object):

    def __init__(self, name):
        self.name = name
        print("__call__方法")

    def __new__(cls, *args, **kwargs):
        print("__new__方法")
        return super().__new__(cls)  # This works because object.__new__ accepts extra args

    def __call__(self, *args, **kwargs):
        print(1)


# 类名加括号，执行的是__new__和__init__方法

obj1 = Obj("aaa")

# 对象加括号，执行__call__方法
obj1()

# OutPut
# __new__方法
# __call__方法
# 1
