class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} unit has created." .format(self.name))
        print("HP {0}, Damage {1}" .format(self.hp, self.damage))

# Attck Unit
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : attack in the {1} direction. [Damage {2}]" \
         .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} damage got." .format(self.name, damage))
        self.hp -= damage
        print("{0} : I'm {1} now." .format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : It has destroyed." .format(self.name))

# Firebat : Attack Unit, He can shoot fire
firebat1 = AttackUnit("Firebat1", 50, 16)
firebat1.attack("5 o'clock")

firebat1.damaged(50)




