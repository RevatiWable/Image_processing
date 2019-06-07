'''Python tesseract is an optical character recognition tool for Python that is it will recognise and read the text embedded in the image.
For tesseract to work download it from the following link:
https://github.com/UB-Mannheim/tesseract/wiki
(tesseract-ocr-w64-setup-v5.0.0.20190526 (alpha) (64 bit) resp.)
This is for windows, check for your operating system accordingly. '''

import pytesseract
from PIL import Image
from pytesseract import image_to_string
#to avoid "pytesseract.pytesseract.tesseractnotfounderror"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\tesseract.exe"
#To load an image from a file, use the open() function in the Image module
img=Image.open(r'numb.jpg')
text=image_to_string(img)
#to print the text present in the image
print(text)

