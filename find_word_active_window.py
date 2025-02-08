import pytesseract
import pyautogui

import serial
import time

from PIL import Image
import difflib

# Establish connection with pico
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Give the connection a moment to establish

# ✅ Your expected words
expected_words = ["EXIT_SCRIPT", "START_PARSE", "END_PARSE", "FOLLOW_DWARF", "ATTACK_TARGET", "ENHANCE_DWARF", "CURE_WOUNDS", "DMG_OVER_TIME"]

# ✅ Define Region of Interest (ROI) - Adjust these values for your screen
left, top, right, bottom = 63, 980, 180, 1005  # Adjust as needed

parse_commands = False

def best_match(ocr_text):
    """Find the closest match from the expected words."""
    matches = difflib.get_close_matches(ocr_text.strip(), expected_words, n=1, cutoff=0.5)
    return matches[0] if matches else None  # Return best match or None

# For Alt+Tab
time.sleep(3)

while True:
    # ✅ Capture the active screen
    screenshot = pyautogui.screenshot()

    # ✅ Crop the region of interest (ROI)
    cropped_image = screenshot.crop((left, top, right, bottom))

    # ✅ Run OCR on the cropped region
    recognized_text = pytesseract.image_to_string(cropped_image).strip()

    # ✅ Find the closest match from your list
    matched_word = best_match(recognized_text)

    if matched_word == "EXIT_SCRIPT":
        print("Will TERMINATE the whole script...")

    if matched_word == "START_PARSE":
        parse_commands = True
    
    if matched_word == "END_PARSE":
        ser.close()
        parse_commands = False

    if parse_commands == True:        
        if matched_word == "FOLLOW_DWARF":
            print("Will FOLLOW the DWARF")
            ser.write(b'hello\n')
        elif matched_word == "ATTACK_TARGET":
            print("Will ATTACK the TARGET")
            ser.write(b'f1\n')
        elif matched_word == "ENHANCE_DWARF":
            print("Will ENHANCE the DWARF")
        elif matched_word == "CURE_WOUNDS":
            print("Will CURE WOUNDS")
        elif matched_word == "DMG_OVER_TIME":
            print("DMG_OVER_TIME")

    # print("------------------------------------------------")
    # print(f"Recognized: {recognized_text} | Best Match: {matched_word if matched_word else 'No match'}")
    # print(f"parse_commands = {parse_commands}")

    # ✅ Wait 1 second before capturing again
    time.sleep(2)
