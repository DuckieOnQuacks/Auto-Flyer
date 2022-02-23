import keyboard
import time

while True:
    keyboard.wait("=")
    keyboard.press("w")
    keyboard.press("shift")
    keyboard.wait("s")
    keyboard.release("shift")
    keyboard.release("w")