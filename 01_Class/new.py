# -*- coding:utf-8 -*-
# created by xiehelin

"""
单列模式，确保类只有一个实例
"""


class Person(object):
    _only_class = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls._only_class is None:
            Person._only_class = super(Person, cls).__new__(cls)
        return cls._only_class  # 必须要由return


p1 = Person("aaa")
p2 = Person("bbb")
print(p1, p2)
