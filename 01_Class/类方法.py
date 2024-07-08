# -*- coding:utf-8 -*-
# created by xiehelin

class Student(object):
    __stu_num = 0
    student_name = []

    def __init__(self, name):
        self.name = name
        self.add_stu(self)

    @classmethod
    def add_stu(cls, obj):
        if obj.name not in obj.student_name:
            cls.student_name.append(obj.name)
            cls.__stu_num += 1

    def print_stu_num(self):
        print("现在的学生人数是：%s" % self.__stu_num)



s1 = Student("aaa")
s2 = Student("bbb")
s3 = Student("ccc")
s4 = Student("ccc")
s5 = Student("ccc")
print(s3.print_stu_num())
