# basic functionality
jules = 0


def start_washing():
    def pump_water():
        global jules
        jules = 5
        print("pumping water -> 10 minutes")
        print(jules)

    pump_water()

    def spin():
        jules = 20
        print("spinning -> 5 minutes")
        print(jules)

    spin()

    def heat_water():
        jules = 1320
        print("heating water -> 20 minutes")
        print(jules)

    heat_water()

    def rinse():
        jules = 1400
        print("rinsing -> 15 minutes")
        print(jules)

    rinse()

    def spin2():
        jules = 1900
        print("spinning -> 40 minutes")
        print(jules)

    spin2()


start_washing()

# extended functionality

jules = 0
minutes = 0
mode = str(input("Please choose eco mode or regular mode ->"))


def start_washing():
    def pump_water():
        global jules
        global minutes
        minutes = 10
        if mode == "eco mode":
            jules = 5
        else:
            jules = 5
        print("pumping water -> 10 minutes")
        print(jules, minutes)

    pump_water()

    def spin():
        minutes = 15
        if mode == "eco mode":
            jules = 20
        else:
            jules = 20
        print("spinning -> 5 minutes")
        print(jules, minutes)

    spin()

    def heat_water():
        minutes = 35
        if mode == "eco mode":
            jules = 920
        else:
            jules = 1320
        print("heating water -> 20 minutes")
        print(jules, minutes)

    heat_water()

    def rinse():
        minutes = 50
        if mode == "eco mode":
            jules = 960
        else:
            jules = 1400
        print("rinsing -> 15 minutes")
        print(jules, minutes)

    rinse()

    def spin2():
        minutes = 90
        if mode == "eco mode":
            jules = 1760
        else:
            jules = 1900
        print("spinning -> 40 minutes")
        print(jules, minutes)

    spin2()


start_washing()
