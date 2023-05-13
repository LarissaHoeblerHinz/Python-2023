temperature = int(input("what will be the temperature today?"))

if temperature > 25:
    print("wear sunglasses")


if temperature < 12 and temperature >= 10:
    print("wear a jacket")


if temperature < 10 and temperature >= 8:
    print("wear a scarf")

if temperature < 8 and temperature >= 6:
    print("wear a hat")


if temperature < 6:
    print("wear gloves")
