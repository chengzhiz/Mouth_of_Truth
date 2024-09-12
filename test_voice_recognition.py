import unittest
from unittest.mock import patch, MagicMock
from voice_recognition import recognize_speech_from_mic, text_to_speech


class TestVoiceRecognitionSimulated(unittest.TestCase):

    @patch('voice_recognition.sr.Recognizer')
    @patch('voice_recognition.sr.Microphone')
    def test_recognize_speech_from_mic(self, mock_microphone, mock_recognizer):
        """Test speech recognition with mocked microphone input."""

        # Mock the recognizer and microphone behavior
        mock_recognizer_instance = mock_recognizer.return_value
        mock_recognizer_instance.listen.return_value = "audio data"

        # Simulate successful speech recognition
        mock_recognizer_instance.recognize_google.return_value = "hello world"

        result = recognize_speech_from_mic()

        # Test if the recognized text is as expected
        self.assertEqual(result, "hello world")

    @patch('voice_recognition.pyttsx3.init')
    def test_text_to_speech(self, mock_tts_engine):
        """Test text to speech functionality with mocked TTS engine."""

        # Mock the TTS engine behavior
        mock_engine_instance = mock_tts_engine.return_value
        mock_engine_instance.say = MagicMock()
        mock_engine_instance.runAndWait = MagicMock()

        text_to_speech("hello world")

        # Check if the TTS engine called the appropriate methods
        mock_engine_instance.say.assert_called_once_with("hello world")
        mock_engine_instance.runAndWait.assert_called_once()


if __name__ == '__main__':
    unittest.main()