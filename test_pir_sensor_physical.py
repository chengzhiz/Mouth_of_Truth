import unittest
import time
import RPi.GPIO as GPIO

PIR_PIN = 17  # GPIO pin connected to the PIR sensor


class TestPIRSensorPhysical(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the GPIO pin for the PIR sensor."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)
        print("Waiting for the PIR sensor to initialize...")
        time.sleep(2)  # Give the sensor some time to initialize

    @classmethod
    def tearDownClass(cls):
        """Clean up the GPIO setup."""
        GPIO.cleanup()

    def test_motion_detected(self):
        """Test motion detection by physically triggering the PIR sensor."""
        print("Move in front of the PIR sensor to trigger it.")

        # Monitor the PIR sensor for motion
        motion_detected = False
        for _ in range(10):  # Check 10 times with a delay
            if GPIO.input(PIR_PIN):
                motion_detected = True
                print("Motion detected!")
                break
            else:
                print("No motion detected.")
            time.sleep(1)  # Wait for 1 second before checking again

        # Assert that motion was detected within 10 seconds
        self.assertTrue(motion_detected, "No motion detected by the PIR sensor.")


if __name__ == "__main__":
    unittest.main()