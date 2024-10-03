from sensors import motion_detected, hand_on_statue
from chatgpt_interface import ask_chatgpt
from output_devices import display_on_tv, play_on_speaker, control_led, play_sound
from voice_recognition import recognize_speech_from_mic, text_to_speech  # Import the voice recognition functions
import time


def main():
    print("System starting...")

    while True:
        if motion_detected():
            print("User detected. System ready.")
            control_led("off")  # Turn off breathing light when motion is detected.

            user_input = recognize_speech_from_mic()

            if user_input:
                # Ask ChatGPT for a response
                response = ask_chatgpt(user_input)
                # f"Answer: {answer}\nCategory: {category_name}\nJustification: {justification}"
                # Display the response on the TV and play it through the speaker
                # display_on_tv(response)
                # play sound with the response
                answer = response['answer'] + ".wav"
                play_sound(answer)

                # Optionally, use text-to-speech to provide audio feedback
                text_to_speech(f"You asked: {user_input}. Here is the answer: {response}")
        else:
            # No motion, activate breathing light
            control_led("breathing")
            # play loop sound to attract attention
            play_sound("none.wav", loop=True)

        time.sleep(1)


if __name__ == "__main__":
    main()
