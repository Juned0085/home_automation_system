from automation_controller import HomeAutomationController

def main():
    controller = HomeAutomationController()

    while True:
        command = input("Enter command (device action) or 'exit': ")
        if command.lower() == 'exit':
            break
        try:
            device, action = command.split()
            controller.control_device(device, action)
        except ValueError:
            print("Invalid input format! Use 'device action'.")

if __name__ == "__main__":
    main()
