import pytesseract
from PIL import Image

# Path to the image file
image_path = 'C:/Users/pgk29/Documents/CPL/image.png'

# Load the image using PIL
image = Image.open(image_path)

# Convert the image to grayscale
gray = image.convert('L')

# Perform OCR on the grayscale image using pytesseract
text = pytesseract.image_to_string(gray)

# Print the extracted text
print(text)