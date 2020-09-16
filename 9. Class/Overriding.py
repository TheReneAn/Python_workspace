class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[Ground unit is moving]")
        print("{0} : Moving in the {1} direction. [Speed {2}]" \
         .format(self.name, location, self.speed))

# Attck Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : Flying in the {1} direction. [Speed {2}]" \
         .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        # Ground speed = 0
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[Airborne unit is moving]")
        self.fly(self.name, location)

# Vulture - Ground unit. Fast Speed 
vulture = AttackUnit("Vulture", 80, 10, 20)

# Battlecruiser - Airborne unit. Good HP, damage
battlecruiser = FlyableAttackUnit("Battlecruiser", 500, 25, 3)

vulture.move("11 o'clock")
# battlecruiser.fly(battlecruiser.name, "9 o'clock")
battlecruiser.move("9 o'clock")




