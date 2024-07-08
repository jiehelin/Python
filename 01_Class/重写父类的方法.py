# -*- coding:utf-8 -*-
# created by xiehelin

class Animal():
    a_type = "哺乳动物"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s 正在吃粑粑... " % self.name)

    def talking(self):
        print("%s 正在叫..." % self.name)

    def message_age(self):
        print("%s 年龄是 : %s " % (self.name, self.age))


class Person(Animal):

    def __init__(self, name, age, add_hobbie):
        super(Person, self).__init__(name, age)  # 继承父类的属性
        self.add_hobbie = add_hobbie  # 添加新的属性

    def eat(self):
        # 扩展父类的功能，而不是重新覆盖父类的函数。这样就可以即运行父类的函数又执行了子类的函数，对父类的函数做了补充。
        # Animal.eat(self)  # 这个self是调用的子类的实例，将子类实例的参数关联进这个函数，去运行父类的方法
        super().eat()  # 同上
        print("%s 正在吃好吃的" % self.name)

    def talking(self):
        print("%s 正在说话..." % self.name)


p1 = Person("aaa", 10, "bb")
p1.eat()
