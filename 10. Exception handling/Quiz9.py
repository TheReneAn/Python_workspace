class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print("[Remain chicken : {0}]" .format(chicken))
        order = int(input("How many chicken do you want to order? "))
        if order > chicken:
            print("Insufficient materials.")
        elif order <= 0:
            raise ValueError
        else:
            print("[Wait number {0}] {1} chickens ordering completed." \
                .format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
        
    except ValueError:
        print("You put wrong number. Please enter a single digit number.")
    except SoldOutError:
        print("We don't take orders anymore because we ran out of ingredients.")
        break

