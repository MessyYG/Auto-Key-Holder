import time
from pynput import keyboard

# Duration to hold the key down (in seconds)
hold_duration = 0.7

# Duration to release the key (in seconds)
release_duration = 0.5

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
        # Handle the case where the key does not have a char attribute (e.g., special keys)
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start a listener for the keyboard events
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# The main loop
try:
    while True:
        if running:
            # Press and hold the "e" key
            controller.press('e')
            print("Key 'e' is being held down")
            time.sleep(hold_duration)
            controller.release('e')
            print("Key 'e' is released")
            time.sleep(release_duration)
        time.sleep(0.1)  # Adding a short delay to avoid high CPU usage
except KeyboardInterrupt:
    print("Program interrupted by user")