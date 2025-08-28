# exception - try, except, finally (try, catch, default)

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero! I know, I know, but you can't!")
except ValueError:
    print("Enter only numbers please!")
except Exception:                                                               # all exception, bad practice
    print("Something went wrong!")
finally:
    print("Do some cleanup here!")
