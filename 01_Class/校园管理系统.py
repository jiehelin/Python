# -*- coding:utf-8 -*-
# created by xiehelin


class School():
    def __init__(self, name, address, course_obj):
        self.name = name
        self.address = address
        self.course_obj = course_obj
        self.money_in = self.money_come()
        self.money_go = self.money_go()

    def course(self):
        print("地址为：%s,开设的课程为%s" % (self.name, self.course_obj.course_name))

    def teacher(self, teacher_obj):
        print("%s他来讲,这个课程%s" % (teacher_obj.staff_name, self.course_obj.course_name))

    def student(self, student_obj):
        print("%s在这个%s学习%s" % (student_obj.name, self.name, self.course_obj.course_name))

    def class_class(self, class_obj):
        pass

    def staff(self, staff_obj):
        pass

    def money_come(self):
        pass

    def money_go(self):
        pass

    def message(self):
        pass


class Course():
    def __init__(self, course_name, course_price):
        self.course_name = course_name
        self.course_price = course_price

    def message(self, teacher_obj):
        print("%s课程为%s钱,%s来讲课" % (self.course_name, self.course_price, teacher_obj.staff_name))


class Staff():
    def __init__(self, staff_name, staff_money, staff_position):
        self.staff_name = staff_name
        self.staff_money = staff_money
        self.staff_position = staff_position


class Teacher(Staff):
    def __init__(self, staff_name, staff_money, staff_position, course_name):
        super().__init__(staff_name, staff_money, staff_position)
        self.course_name = course_name


class Student():
    def __init__(self, name, course_obj):
        self.name = name
        self.course_obj = course_obj

    def message(self):
        print("%s花了%s学习%s" % (self.name, self.course_obj.course_price, self.course_obj.course_name))


teacher1 = Teacher("mjj", 1000, "teacher", "python")
course1 = Course("python", 5000)
student1 = Student("xiehelin", course1)
