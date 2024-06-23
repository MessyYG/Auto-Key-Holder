import time
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox
import threading

# Initial configuration
hold_duration = 0.7
release_duration = 0.5
key_to_hold = 'e'
running = False
controller = keyboard.Controller()

def on_press(key):
    global running
    try:
        if key.char == ',':
            running = not running
            if running:
                print("Starting the program.")
            else:
                print("Stopping the program.")
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def update_key(new_key):
    global key_to_hold
    key_to_hold = new_key
    messagebox.showinfo("Key Updated", f"The key to hold has been updated to '{new_key}'")

def update_hold_duration(new_duration):
    global hold_duration
    try:
        hold_duration = float(new_duration)
        messagebox.showinfo("Hold Duration Updated", f"The hold duration has been updated to {hold_duration} seconds")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def update_release_duration(new_duration):
    global release_duration
    try:
        release_duration = float(new_duration)
        messagebox.showinfo("Release Duration Updated", f"The release duration has been updated to {release_duration} seconds")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def create_ui():
    root = tk.Tk()
    root.title("Key Holder")

    tk.Label(root, text="Key to Hold:").pack(pady=5)
    key_entry = tk.Entry(root)
    key_entry.pack(pady=5)
    key_entry.insert(0, key_to_hold)

    def on_update_key():
        new_key = key_entry.get()
        if new_key:
            update_key(new_key)

    tk.Button(root, text="Update Key", command=on_update_key).pack(pady=10)

    tk.Label(root, text="Hold Duration (seconds):").pack(pady=5)
    hold_duration_entry = tk.Entry(root)
    hold_duration_entry.pack(pady=5)
    hold_duration_entry.insert(0, str(hold_duration))

    def on_update_hold_duration():
        new_duration = hold_duration_entry.get()
        update_hold_duration(new_duration)

    tk.Button(root, text="Update Hold Duration", command=on_update_hold_duration).pack(pady=10)

    tk.Label(root, text="Release Duration (seconds):").pack(pady=5)
    release_duration_entry = tk.Entry(root)
    release_duration_entry.pack(pady=5)
    release_duration_entry.insert(0, str(release_duration))

    def on_update_release_duration():
        new_duration = release_duration_entry.get()
        update_release_duration(new_duration)

    tk.Button(root, text="Update Release Duration", command=on_update_release_duration).pack(pady=10)

    tk.Label(root, text="Press ',' to start/stop the program.").pack(pady=5)
    tk.Label(root, text="Press 'ESC' to exit the listener.").pack(pady=5)

    root.mainloop()

# Main loop
def main_loop():
    global running, key_to_hold
    try:
        while True:
            if running:
                controller.press(key_to_hold)
                print(f"Key '{key_to_hold}' is being held down")
                time.sleep(hold_duration)
                controller.release(key_to_hold)
                print(f"Key '{key_to_hold}' is released")
                time.sleep(release_duration)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program interrupted by user")

def start_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

if __name__ == "__main__":
    # Start the keyboard listener in a separate thread
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.daemon = True
    listener_thread.start()

    # Start the UI in the main thread
    ui_thread = threading.Thread(target=create_ui)
    ui_thread.start()

    # Start the main loop in a separate thread
    main_thread = threading.Thread(target=main_loop)
    main_thread.start()
