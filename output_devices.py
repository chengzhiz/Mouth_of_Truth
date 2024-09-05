import os

def display_on_tv(text):
    """Display text on the TV screen."""
    os.system(f"echo '{text}' > /dev/tty1")  # Replace with the appropriate command to display on your TV setup

def play_on_speaker(text):
    """Convert text to speech and play it through the speaker."""
    os.system(f'espeak "{text}"')  # You can replace 'espeak' with another TTS library if needed.

def control_led(mode):
    """Control LED strip for different modes like 'off', 'breathing', etc."""
    if mode == "breathing":
        # Example: Activate PWM-controlled breathing light (replace with actual implementation)
        print("Breathing light activated")
    elif mode == "off":
        print("LED turned off")