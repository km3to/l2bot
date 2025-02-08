import pytesseract
from PIL import Image
import difflib

# ✅ Your expected words
expected_words = ["attack", "buff", "follow", "heal", "dot"]

def best_match(ocr_text):
    matches = difflib.get_close_matches(ocr_text.strip().lower(), expected_words, n=1, cutoff=0.5)
    return matches[0] if matches else None  # Return best match or None

# ✅ Load image
image = Image.open("giran4.png")

# ✅ Define the region of interest (ROI) - Adjust these values
left, top, right, bottom =  60, 990, 200, 1005 # Example coordinates

# ✅ Crop the image to focus only on the relevant area
cropped_image = image.crop((left, top, right, bottom))

# ✅ Run OCR on the cropped region
recognized_text = pytesseract.image_to_string(cropped_image).strip()

# ✅ Find the closest match from your list
matched_word = best_match(recognized_text)

print(f"Recognized: {recognized_text} | Best Match: {matched_word if matched_word else 'No match'}")
