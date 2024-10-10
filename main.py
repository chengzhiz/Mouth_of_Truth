import time
import threading
from sensors import user_interaction_detected
from chatgpt_interface import ask_chatgpt
from output_devices import control_led, play_wav_file, stop_playback
from voice_recognition import recognize_speech_from_mic



import tkinter as tk
from tkinter import scrolledtext
class TerminalUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal UI")
        self.root.geometry("480x320")  # Set the resolution to 480x320

        # Create a scrolled text widget
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Courier", 10))
        self.text_area.pack(padx=10, pady=10)

        # Disable editing
        self.text_area.config(state=tk.DISABLED)

    def append_text(self, text, prefix=""):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"{prefix}{text}\n")
        self.text_area.config(state=tk.DISABLED)
        self.text_area.yview(tk.END)  # Auto-scroll to the end

def main():
    root = tk.Tk()
    terminal_ui = TerminalUI(root)

    terminal_ui.append_text("System starting...")

    def run():
        while True:
            if user_interaction_detected():
                terminal_ui.append_text("User interaction detected. System ready.")
                control_led("on")  # Turn on LED light when user interaction is detected.
                stop_playback()  # Stop any ongoing playback
                user_input = recognize_speech_from_mic()
                if user_input:
                    terminal_ui.append_text(user_input, prefix="User: ")
                    # Stop recognition and process the text with GPT
                    terminal_ui.append_text("Processing user input with GPT...")
                    response = ask_chatgpt(user_input)
                    answer = response['answer'].lower() + ".wav"
                    terminal_ui.append_text(response['justification'])
                    play_wav_file(answer)
                time.sleep(1)  # Add a small delay to avoid rapid looping

            else:

                terminal_ui.append_text("No user interaction detected.")
                # make the remain part into thread from control led to play wav file
                def else_run():
                    control_led("breathing")  # Revert to breathing light if no user interaction is detected.
                    stop_playback()  # Stop any ongoing playback
                    # Play loop sound to attract attention
                    play_wav_file("none.wav", loop=True)
                threading.Thread(target=else_run, daemon=True).start()


            print("looping")
            time.sleep(1)

    # Run the main loop in a separate thread to keep the GUI responsive
    import threading
    threading.Thread(target=run, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()
