# -*- coding:utf-8 -*-
# created by xiehelin


class Person():
    def __init__(self, name, age):
        self.name = name  # 实例属性，成员变量
        self.age = age
        self.__health = 100  # 私有属性

    def get_health(self):
        # 在类的内部是可以被访问的，通过函数能访问属性，但是不能在类的外部去修改它
        print(self.__health)
        return self.__health

    def attack(self):
        # 封装的过程，通过一个方法去操作一个私有属性
        self.__health -= 20
        print("被攻击了，掉血%s" % self.__health)
        self.__breath()
        return self.__health

    def __breath(self):
        # 只能在类的內部去调用
        print("%s 正在呼吸。。。" % self.name)


p = Person("aaa", 10)
p.get_health()  # 只能通过函数去访问属性
p.attack()  # 只能通过函数去修改属性的值

# 强制访问 实例名._类名 + 方法(__方法名)
p._Person__breath()
# 强制修改私有属性
p._Person__health = 50
p.get_health()

# 从外部创建私有属性。
p.__val = 100 # 在外部创建的私有属性，将不具有私有性。在外部是可以直接访问的，例如下面的print可以直接访问。只有在类的初始化下面创建的私有属性才具有私有性
print(p.__val)
