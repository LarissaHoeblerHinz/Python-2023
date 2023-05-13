x = pow(3, 2)
print(x)

number = int(input("say any number -> "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


def even_or_odd():
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


number = int(input("say any number -> "))
print("The number", number, "is", even_or_odd_arg())
