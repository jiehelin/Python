# 装饰器可以有参数


class Decorator(object):
    def __init__(self, double):
        self.double = double

    def __call__(self, func):
        def print_val(a, b):
            c = func(a, b) * self.double
            print("函数的名字叫:%s,输出：%s" % (func.__name__, c))
            return c

        return print_val


@Decorator(2)
def add(a, b):
    return a + b


add(1, 2)