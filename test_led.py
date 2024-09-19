from output_devices import control_led

def main():
    while True:
        user_input = input("Enter 'breathing' to start or 'off' to stop the LED effect: ")
        control_led(user_input)

if __name__ == "__main__":
    main()