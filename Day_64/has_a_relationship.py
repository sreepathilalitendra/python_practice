class Battery:
    def charge(self):
        print("Battery is charging")


class Mobile:
    def __init__(self):
        self.battery = Battery()

    def use_mobile(self):
        self.battery.charge()
        print("Mobile is working")


mobile = Mobile()

mobile.use_mobile()