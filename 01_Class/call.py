# -*- coding:utf-8 -*-
# created by xiehelin

class Person(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(self, *args, **kwargs)


p1 = Person("aaa")
p1()  # 对象名 + （）
Person("aaa")()  # 类名 + （）
