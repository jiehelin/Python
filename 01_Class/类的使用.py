# -*- coding:utf-8 -*-
# created by xiehelin

"""
创建两个类，一个狗类，一个人，
狗类中存在一个咬人的动作
人中存在一个打狗的动作
第三个类作为人使用打狗的武器功能
"""


class Dog():

    def __init__(self, name, attack_val):
        self.name = name
        self.attack_val = attack_val
        self.health = 100

    def bite(self, person_obj):
        person_obj.health -= self.attack_val
        print("[%s]被[%s]狗，咬了[%s]血，还剩[%s]血" % (person_obj.name, self.name, self.attack_val, person_obj.health))


class Person():
    person_international = "China"

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapen = Weapen()


class Weapen():

    def gun(self, obj):
        self.name = "枪"
        self.attack_val = 100
        obj.health -= self.attack_val
        pass

    def gunzi(self,obj):
        pass
