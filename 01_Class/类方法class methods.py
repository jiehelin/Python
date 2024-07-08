# -*- coding:utf-8 -*-
# created by xiehelin
class Dog(object):
    a_type = "a"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s吃东西。。。。" % self.name)

    @classmethod
    def attack(cls):
        print("%s咬人。。。。" % cls.a_type)
