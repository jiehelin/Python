# -*- coding:utf-8 -*-
# created by xiehelin


class ConnectError(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise ConnectError("连不上网")

except ConnectionError as error:
    print(error)
