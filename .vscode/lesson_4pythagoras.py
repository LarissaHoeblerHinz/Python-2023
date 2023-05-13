import math

a = 3
b = 5


def pythagoras(a, b):
    c2 = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c2)
    return c


print(pythagoras(a, b))


sum = lambda a1, a2: a1 + a2
print(sum(4, 5))

str1 = "Dear Students"
str2 = "Nice Evening"
str3 = "ReDi to learn"
print(str1, str2, str3)
