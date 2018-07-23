try:
    # value = 10 / 0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError as e:
    print("divided by zero")
    print(e)
except ValueError as e:
    print("invalid input")
    print(e)
else:
    pass
finally:
    pass
