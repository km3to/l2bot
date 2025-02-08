import usb_cdc
import time
import usb_hid
import random
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode

# Create the keyboard object
kbd = Keyboard(usb_hid.devices)

# Create the mouse object
mouse = Mouse(usb_hid.devices)

# Use the main console for serial communication
serial = usb_cdc.console

# Function to simulate a keypress with random delay
def press_key(key):
    kbd.press(key)
    kbd.release(key)
    time.sleep(random.uniform(0.5, 1))  # Convert ms to seconds

def type_hello():
    time.sleep(5)
    # Press Enter
    press_key(Keycode.ENTER)

    # Type "hello" with random delays
    press_key(Keycode.H)
    press_key(Keycode.E)
    press_key(Keycode.L)
    press_key(Keycode.L)
    press_key(Keycode.O)

def type_attack():
    time.sleep(5)
    press_key(Keycode.A)
    press_key(Keycode.T)
    press_key(Keycode.T)
    press_key(Keycode.A)
    press_key(Keycode.C)
    press_key(Keycode.K)

def type_F1():
    time.sleep(5)
    press_key(Keycode.F1)

def type_sit_stand():
    time.sleep(5)
    press_key(Keycode.F10)

def mouse_move():
    mouse.move(50, 50)
    time.sleep(1)

def mouse_click():
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1)



while True:
    if serial.in_waiting > 0:
        command = serial.readline().decode("utf-8").strip()

        if command == "hello":
            type_hello()
        elif command == "attack":
            type_attack()
        elif command == "f1":
            type_F1()
        elif command == "sit_stand":
            type_sit_stand()
        elif command == "mouse_move":
            mouse_move()
        elif command == "mouse_click":
            mouse_click()
        else:
            print(f"Unknown command: {command}")

