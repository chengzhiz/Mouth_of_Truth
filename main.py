from sensors import motion_detected, hand_on_statue
from chatgpt_interface import ask_chatgpt
from output_devices import display_on_tv, play_on_speaker, control_led
import time


def main():
    print("System starting...")

    while True:
        if motion_detected():
            print("User detected. System ready.")
            control_led("off")  # Turn off breathing light when motion is detected.

            if hand_on_statue():
                print("Hand detected on statue's mouth.")
                user_input = input("Ask your question: ")

                # Ask ChatGPT for a response.
                response = ask_chatgpt(user_input)

                # Display the response on the TV and play it through the speaker.
                display_on_tv(response)
                play_on_speaker(response)

        else:
            # No motion, activate breathing light.
            control_led("breathing")

        time.sleep(1)


if __name__ == "__main__":
    main()