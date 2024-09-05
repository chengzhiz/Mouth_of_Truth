import unittest
from unittest.mock import patch, MagicMock

# Assuming the PIR detection logic is inside the sensors.py
from sensors import motion_detected


class TestPIRSensor(unittest.TestCase):

    @patch('sensors.GPIO')
    def test_motion_detected(self, mock_gpio):
        """Test if motion is correctly detected when PIR_PIN is high."""
        PIR_PIN = 17  # Assuming PIR_PIN is 17

        # Simulate GPIO input returning HIGH (motion detected)
        mock_gpio.input.return_value = 1  # 1 means motion detected (HIGH)

        # Test if motion_detected() correctly identifies the motion
        self.assertTrue(motion_detected())

        # Simulate GPIO input returning LOW (no motion detected)
        mock_gpio.input.return_value = 0  # 0 means no motion detected (LOW)

        # Test if motion_detected() correctly identifies no motion
        self.assertFalse(motion_detected())


if __name__ == '__main__':
    unittest.main()