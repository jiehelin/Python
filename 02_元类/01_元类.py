# -*- coding:utf-8 -*-
# created by xiehelin

class Mytype(type):

    # 1.创建Foo类
    def __new__(cls, *args, **kwargs):
        print("new")
        new_cls = super().__new__(cls, *args, **kwargs)
        return new_cls

    # 2.初始化Foo类
    def __init__(self, *args, **kwargs):
        print("init")
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        # 1.调用Foo类的 __new__方法创建对象
        empty_object = self.__new__(self) # 这里的self指的是Foo类本身
        # 2.调用Foo类的 __init__ 方法去初始化
        self.__init__(empty_object, *args, **kwargs)
        return empty_object


# 由Mytype创建的对象
# Foo类是Mytype创建的一个对象
# Foo() =-> Mytype() 调用Mytype的call方法

class Foo(object, metaclass=Mytype):
    def __init__(self, name):
        self.name = name


v1 = Foo("aaa")
