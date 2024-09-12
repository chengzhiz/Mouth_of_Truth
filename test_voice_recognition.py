import unittest
from unittest.mock import patch, MagicMock
from voice_recognition import recognize_speech_from_mic, text_to_speech


class TestVoiceRecognition(unittest.TestCase):

    @patch('voice_recognition.sr.Microphone')
    @patch('voice_recognition.sr.Recognizer')
    def test_recognize_speech_from_mic(self, mock_recognizer, mock_microphone):
        """Test speech recognition from microphone with mocked recognizer."""

        # Create a mock instance of the recognizer and microphone
        mock_instance = mock_recognizer.return_value
        mock_instance.listen.return_value = MagicMock()  # Mock the audio data
        mock_instance.recognize_google.return_value = "hello world"

        # Call the function under test
        result = recognize_speech_from_mic()

        # Assert that the function correctly recognized the speech
        self.assertEqual(result, "hello world")

        # Test handling of unknown value error (couldn't understand speech)
        mock_instance.recognize_google.side_effect = sr.UnknownValueError
        result = recognize_speech_from_mic()
        self.assertIsNone(result)

        # Test handling of request error (API/service failure)
        mock_instance.recognize_google.side_effect = sr.RequestError
        result = recognize_speech_from_mic()
        self.assertIsNone(result)

    @patch('voice_recognition.pyttsx3.init')
    def test_text_to_speech(self, mock_pyttsx3_init):
        """Test text to speech function with mocked pyttsx3."""

        # Mock the pyttsx3 engine
        mock_engine = mock_pyttsx3_init.return_value
        mock_engine.say = MagicMock()
        mock_engine.runAndWait = MagicMock()

        # Call the function under test
        text = "Hello, this is a test."
        text_to_speech(text)

        # Assert that the engine's say and runAndWait methods were called
        mock_engine.say.assert_called_once_with(text)
        mock_engine.runAndWait.assert_called_once()


if __name__ == "__main__":
    unittest.main()