# -*- coding:utf-8 -*-
# created by xiehelin

class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("该对象被释放", self.name)


p1 = Person("aaa")
print(p1.__class__.__name__)
print("aaaa")
print("aaaa")
print("aaaa")
del p1
print("aaaa")
print("aaaa")
print("aaaa")
print("aaaa")
