class Dog():
    def __init__(self, name, bread, attack_val):
        self.name = name
        self.bread = bread
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self, person):
        person.life_val -= self.attack_val
        print("狗[%s]咬了[%s],人掉血[%s],还剩[%s]" % (self.name, person.name, self.attack_val, person.life_val))


class Person():
    def __init__(self, name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 100
        self.weapon = Weapon()

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print("人[%s]打了狗[%s]，狗掉血[%s],还剩[%s]血..." % (self.name, dog.name, self.attack_val, dog.life_val))


class Weapon():
    def stick(self, obj):
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        # print(obj.name + "被" + self.name + "攻击了，掉了" + self.attack_val + "血，还剩" + obj.life_val + "血")
        print("[%s]使用[%s]打了,掉血[%s],还剩[%s]" % (obj.name, self.name, self.attack_val, obj.life_val))


d = Dog("dog", "二哈", 30)
p = Person("aaa", "M", 50)
d.bite(p)
p.weapon.stick(d)
