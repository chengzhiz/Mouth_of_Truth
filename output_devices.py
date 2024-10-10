import os
import threading
import time
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

# Global flag to control playback
is_playing = False

def play_wav_file(file_name, loop=False):
    """Play a WAV file from the Assets folder with optional looping in a separate thread."""
    def play_audio():
        global is_playing
        try:
            # Construct the full file path
            file_path = os.path.join('Assets', file_name)
            # Load the WAV file
            audio = AudioSegment.from_wav(file_path)

            # Play the audio
            is_playing = True
            while is_playing:
                playback = _play_with_simpleaudio(audio)
                playback.wait_done()
                if not loop:
                    break
                time.sleep(10)  # Delay of 10 seconds before playing again
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            is_playing = False

    # Start the audio playback in a separate thread
    threading.Thread(target=play_audio, daemon=True).start()

def stop_playback():
    """Stop the playback of the WAV file."""
    print("Stopping playback...")
    global is_playing
    is_playing = False