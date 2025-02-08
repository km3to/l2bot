from PIL import Image

# Load the image
image = Image.open("giran4.png")

# Define the region of interest (ROI)
left, top, right, bottom = 60, 990, 200, 1005  # Adjust these values

# Crop the image
cropped_image = image.crop((left, top, right, bottom))

# Show the cropped image (a preview window will open)
cropped_image.show()
