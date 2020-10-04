# Global variables Way 1
gun = 10
def checkpoint(soldiers):
    # It's not good way
    global gun
    gun = gun - soldiers
    print("[Inside function] Remaining gun: {0}" .format(gun))

print("Total guns: {0}" .format(gun))
checkpoint(2) 
print("Remaining gun: {0}" .format(gun))

# Global variables Way 2
gun = 10
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[Inside function] Remaining gun: {0}" .format(gun))
    return gun

print("Total guns: {0}" .format(gun))
gun = checkpoint_ret(gun, 2)
print("Remaining gun: {0}" .format(gun))


