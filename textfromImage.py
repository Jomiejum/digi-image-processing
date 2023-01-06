# An OCR tool for python which will recognize and read texts embedded in images
import pytesseract as tess 
# An environment variable which is essential for the code to work
tess.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# A function that  imports loaded image from a specified path
from PIL import Image

# This section loads image from its path
img = Image.open('sample-image.png')
# This section extracts text from the selected image
text = tess.image_to_string(img)

# Prints extracted text from the image to the terminal
print(text)
