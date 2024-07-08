# -*- coding:utf-8 -*-
# created by xiehelin

class Person():
    a_type = "傻逼"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def message(self):
        print("name : %s \t age : %s" % (self.name, self.age))


class Person1(Person):
    a_type = "聪明的人"  # 重写父类的全局属性

    def talk(self):  # 继承后可以添加新的子类方法
        print("%s is talking ..." % self.name)

    def message(self):  # 重新定义父类的方法
        print("%s 这个人可以说话" % self.name)


class Person2(Person):
    def chouyan(self):  # 继承后可以添加新的子类方法
        print("%s 在抽烟" % self.name)


p1 = Person1("xiehelin", 26)
p1.message()
p1.talk()
print(p1.a_type)  # 输出的是重写的父类的全局属性

p2 = Person2("aaa", 30)
p2.chouyan()
print(p2.a_type)  # 输出的是原来的父类全局属性
