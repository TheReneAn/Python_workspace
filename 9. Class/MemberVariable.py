# Class 내에서 정의 된 변수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} unit has created." .format(self.name))
        print("HP {0}, Damage {1}" .format(self.hp, self.damage))

# Wraith - Airborne unit. Cloaking (Enemy can not see it)
wraith1 = Unit("Wraith1", 80, 5)
print("Unit Name: {0}, Damage{1}" .format(wraith1.name, wraith1.damage))

# Mindcontrol - Making another unity mine
wraith2 = Unit("Plunder wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} is in a clinking state." .format(wraith2.name))

