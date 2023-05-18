class Car:
    type = "no name"
    name = "unknown"
    constructionyear = 0


car1 = Car()
car1.type = "porsche"
car1.name = "cayenne"
car1.constructionyear = 2019


class Vehicle:
    def __init__(self, brand, modelname, year):
        self.brand = brand
        self.modelname = modelname
        self.year = year

    def __repr__(self):
        return (
            "Brand: "
            + str(self.brand)
            + " Model: "
            + str(self.modelname)
            + " Year: "
            + str(self.year)
        )


c = Vehicle("vw", "golf", "2011")
print(repr(c))
