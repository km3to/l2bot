import pyautogui
import time
#from PIL import Image

# ✅ Define Region of Interest (ROI) - Adjust these values!
left, top, right, bottom = 62, 980, 150, 1005  # Screen coordinates

time.sleep(2)
count = 0

while count < 3:
    # ✅ Capture the active screen
    screenshot = pyautogui.screenshot()

    # ✅ Crop the region of interest
    cropped_image = screenshot.crop((left, top, right, bottom))

    # ✅ Show the cropped image (debugging)
    cropped_image.show()

    # ✅ Wait 1 second before capturing again
    time.sleep(1)

    count += 1
