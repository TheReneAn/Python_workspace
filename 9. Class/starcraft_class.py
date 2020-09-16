# # Marine: Attack unit. He can shoot

# marine_name = "Marine"
# marine_HP = 40
# marine_damage = 5

# print("{0} unit has created." .format(marine_name))
# print("HP {0}, Damage {1}\n" .format(marine_HP, marine_damage))

# # Tank: Attack unit. It can shoot cannon. General & Siege mode
# tank_name = "Tank"
# tank_HP = 150
# tank_damage = 35

# print("{0} unit has created." .format(tank_name))
# print("HP {0}, Damage {1}\n" .format(tank_HP, tank_damage))

# tank2_name = "Tank2"
# tank2_HP = 150
# tank2_damage = 35

# print("{0} unit has created." .format(tank2_name))
# print("HP {0}, Damage {1}\n" .format(tank2_HP, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : attack in the {1} direction. [Damage {2}]" \
#         .format(name, location, damage))

# attack(marine_name, "1 o'clock", marine_damage)
# attack(tank_name, "2 o'clock", tank_damage)
# attack(tank2_name, "3 o'clock", tank_damage)



''' Many unit can not make this way.
    We can use 'class'.  '''



class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} unit has created." .format(self.name))
        print("HP {0}, Damage {1}\n" .format(self.hp, self.damage))

marine1 = Unit("Marine1", 40, 5)
marine2 = Unit("Marine2", 40, 5)
tank2 = Unit("Tank1", 150, 35)

# __init__
# - Python 생성자
# 즉, marine이나 tank같은 객체가 만들어 질때, 자동으로 호출되는 부분.

# 객체
# - Class 로부터 만들어지는 것들을 객체라고 한다.
# 즉, marine and tank는 객체이며, Unit class의 instance라고 부른다.


