# -*- coding:utf-8 -*-
# created by xiehelin

class Dog():

    def sound(self):
        print("汪汪汪。。。。")


class Cat():

    def sound(self):
        print("喵喵喵。。。。")


def makesound(obj):
    obj.sound()


dog = Dog()
cat = Cat()

makesound(dog)
makesound(cat)
