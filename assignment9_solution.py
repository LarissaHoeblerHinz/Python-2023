class Vehicle:
    # part 1
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


# part 2
def seating_capacity(self, capacity):
    return f"The seating capacity of {self.name} is {capacity}."


# part 3
class Bus(Vehicle):
    # part 4
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    # part 5
    color = "white"

    # bonus
    numberOfBuses = 0

    def __init__(self, max_speed, mileage, name):
        super().__init__(max_speed, mileage, name)
        Bus.numberOfBuses += 1
        if Bus.numberOfBuses >= 5:
            Bus.color = "red"
