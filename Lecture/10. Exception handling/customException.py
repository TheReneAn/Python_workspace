class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("It's a single digit calculator.")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("Input value: {0}, {1}" .format(num1, num2))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1 / num2)))

except ValueError:
    print("You put wrong number. Please enter a single digit number.")
except BigNumberError as err:
    print("There was a error. Please enter a single digit number.")
    print(err)
finally:
    print("Thank you for using this calculator.")

