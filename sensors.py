import RPi.GPIO as GPIO
import time

# PIR Motion Sensor Pin
PIR_PIN = 17

# Capacitive touch sensor pin
TOUCH_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(TOUCH_PIN, GPIO.IN)

def motion_detected():
    """Detect motion from PIR sensor."""
    return GPIO.input(PIR_PIN)

def hand_on_statue():
    """Detect if the hand is placed on the statue's mouth using a touch sensor."""
    return GPIO.input(TOUCH_PIN)