# -*- coding:utf-8 -*-
# created by xiehelin

"""
使用抽象类去实现多态
"""


class Document():
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("必须要在子类中重写此方法")


class PDF(Document):

    def show(self):
        print("使用PDF方法打开文件")


class Word(Document):

    def show(self):
        print("使用Word方式打开文件")


document = PDF("AAA")
document2 = Word("BBB")

objs = [document, document2]

for obj in objs:  # 使用obj这一个接口去调用不同的实例中的相同的方法（这个就是多态）
    obj.show()
