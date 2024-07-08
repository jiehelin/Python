# -*- coding:utf-8 -*-
# created by xiehelin

class Flight(object):
    def __init__(self, name):
        self.name = name
        self.value = 0

    def checking_status(self):
        print(self.name)
        return 1

    @property
    def fight_status(self):
        self.value = self.checking_status()
        print(self.value)

    @fight_status.setter
    def fight_status(self, state):
        self.value = state
        print(self.value)

    @fight_status.deleter
    def fight_status(self):
        del self.value

f = Flight("aaa")
f.fight_status
f.fight_status = 3
del f.fight_status
