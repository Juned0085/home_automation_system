class Light:
    def __init__(self, name):
        self.name = name
        self.status = False

    def turn_on(self):
        self.status = True
        print(f"{self.name} light turned ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name} light turned OFF.")

class Fan:
    def __init__(self, name):
        self.name = name
        self.status = False

    def turn_on(self):
        self.status = True
        print(f"{self.name} fan turned ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name} fan turned OFF.")
