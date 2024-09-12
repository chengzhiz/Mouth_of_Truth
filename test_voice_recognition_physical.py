import unittest
from voice_recognition import recognize_speech_from_mic, text_to_speech


class TestVoiceRecognitionPhysical(unittest.TestCase):

    def test_recognize_speech_from_mic_physical(self):
        """Physically test the microphone input for speech recognition."""
        print("Please say something into the microphone...")

        # This test will listen to the user's physical voice input
        recognized_text = recognize_speech_from_mic()

        if recognized_text:
            print(f"Recognized Speech: {recognized_text}")
            self.assertTrue(True)  # Test passes if speech was recognized
        else:
            print("No speech recognized.")
            self.fail("Failed to recognize speech.")

    def test_text_to_speech_physical(self):
        """Test the physical TTS output by converting text to speech."""
        test_text = "This is a test for text to speech."
        print(f"Converting text to speech: {test_text}")

        # Physically test the text-to-speech output
        text_to_speech(test_text)

        # For the physical test, we assume that if no exceptions are raised, the test passes.
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()