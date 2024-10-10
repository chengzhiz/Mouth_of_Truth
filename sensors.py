# sensors.py
import RPi.GPIO as GPIO
import time

# PIR Motion Sensor Pin
PIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def user_interaction_detected():
    """Detect if motion is detected and hand is placed on the statue's mouth."""
    return GPIO.input(PIR_PIN)