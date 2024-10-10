# sensors.py
import RPi.GPIO as GPIO
import time

# PIR Motion Sensor Pin
PIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
print("Waiting for the PIR sensor to initialize...")


def user_interaction_detected():
    """Detect if motion is detected and hand is placed on the statue's mouth."""
    print("Checking for user interaction...")
    return GPIO.input(PIR_PIN) == GPIO.HIGH