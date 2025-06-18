from devices import Light, Fan

class HomeAutomationController:
    def __init__(self):
        self.living_room_light = Light("Living Room")
        self.bedroom_fan = Fan("Bedroom")

    def control_device(self, device, action):
        if hasattr(self, device):
            dev = getattr(self, device)
            if action == "on":
                dev.turn_on()
            elif action == "off":
                dev.turn_off()
            else:
                print("Invalid action!")
        else:
            print("Device not found!")
