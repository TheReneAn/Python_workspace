from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit has created." .format(self.name))

    def move(self, location):
        print("{0} : Moving in the {1} direction. [Speed {2}]" \
         .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} damage got." .format(self.name, damage))
        self.hp -= damage
        print("{0} : I'm {1} now." .format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : It has destroyed." .format(self.name))

# Attck Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : attack in the {1} direction. [Damage {2}]" \
         .format(self.name, location, self.damage))

# Marine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    # Stimpack - Increase movement and attack speed over a period of time  
    #            Decrease hp -10         
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Use the stimpack. (HP -10) " .format(self.name))
        else:
            print("{0} : No HP. Can not use stimpack " .format(self.name))

# Tank
class Tank(AttackUnit):
    # Siege mode - Can attack more powerful. Can not move 
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seiz_mode(self):
        if Tank.seize_developed == False:
            return
        
        # If the status is not seige mode -> Turn on Siege mode
        if self.seize_mode == False:
            print("{0} : Turn on Siege mode." .format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # If the status is seige mode -> Turn off Siege mode 
        else:
            print("{0} : Turn off Siege mode." .format(self.name))
            self.damage /= 2
            self.seize_mode = False
        
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
        self.fly(self.name, location)

# Wraith
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : Turn off Clocing mode." .format(self.name))
            self.clocked = False
        else:
            print("{0} : Turn on Clocing mode." .format(self.name))
            self.clocked = True

def game_start():
    print("[Notice] Start game now.")

def game_over():
    print("Player: Good Game")
    print("[Player] left this game")

''' ----------------------------------------------------------------'''

# Start Game
game_start()

# Create Marine 3 
m1 = Marine()
m2 = Marine()
m3 = Marine()

# Create Tank 2
t1 = Tank()
t2 = Tank()

# Create Wraith 1
w1 = Wraith()

## Unit organization
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# All unit move
for unit in attack_units:
    unit.move("1 o'clock")

# Developed Tank seize mode
Tank.seize_developed = True
print("[Notice] Tank seize mode development completed")

# Prepare to fight 
# (Marine: stimpack, Tank: seiz mode, Wraith: clocking)
for unit in attack_units:
    # Is it "unit" instance from the "Marine" class?
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seiz_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# All units attack
for unit in attack_units:
    unit.attack("1 o'clock")

# All units are damaged
for unit in attack_units:
    # random damage (5~20)
    unit.damaged(randint(5, 21))

# End Game
game_over()


