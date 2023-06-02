class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, n):
        self.capacity += n


veh1 = Vehicle("Car", 220, 20000, 5)
print("The seating capacity of", veh1.name, "is", veh1.capacity)
# Reducing capacity to that of a Coupé, not part of the assignment
veh1.seating_capacity(-3)
print(veh1.capacity)
print("------------------------")


class Bus(Vehicle):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def seating_capacity(self):
        default_capacity = super().seating_capacity
        default_capacity = 50
        return default_capacity

    def appearance(color="white"):
        return color


# testing, if Bus inherited all variables/methods from Vehicle
bus1 = Bus("Schoolbus", 180, 500000, 48)
print(bus1.mileage)
print(bus1.capacity)
# testing bus default capacity of 50
# print(bus1.seating_capacity)
# can't do task 4

print(bus1.appearance())
