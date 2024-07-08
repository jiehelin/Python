# -*- coding:utf-8 -*-
# created by xiehelin
class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        str1 = "str------以字符串的方式展现类的内容 %s " % self.name
        return str1

    def __repr__(self):
        str2 = "repr-----以字符串的方式展现类的内容 %s " % self.name
        return str2


p1 = Person("aaa")
print(p1)
