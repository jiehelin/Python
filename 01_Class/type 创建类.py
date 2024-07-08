# -*- coding:utf-8 -*-
# created by xiehelin

# 动态创建类

def __init__(self, name, age):
    self.name = name
    self.age = age


cat_class = type("Cat", (object,), {"class_var": "cat", "__init__": __init__})
c1 = cat_class("aaa", 10)
print(c1)









