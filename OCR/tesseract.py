import pytesseract
from PIL import Image
import cv2
import os

pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract'
# config=('-l kor+eng --oem3 --psm 11')

image=cv2.imread("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


text=pytesseract.image_to_string(Image.open(filename),lang='kor+eng')
os.remove(filename)

print(text)

cv2.imshow("Image",image)
cv2.waitKey(0)