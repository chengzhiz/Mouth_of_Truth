import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()


def recognize_speech_from_mic():
    """Capture voice input from the microphone and convert it to text."""
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command...")

        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None


def text_to_speech(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    print("Voice recognition test is active.")

    while True:
        command = recognize_speech_from_mic()
        if command:
            print(f"Processing command: {command}")
            # Optionally, you can use text-to-speech to provide audio feedback
            text_to_speech(f"You said: {command}")
        else:
            print("Please try again...")


if __name__ == "__main__":
    main()