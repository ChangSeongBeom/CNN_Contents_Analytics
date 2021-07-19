import easyocr
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

beforeResult=[]
textResult=[]


img = cv2.imread("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")
im=Image.open("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")

w,h=im.size
tmph=(int)(h*0.75)
dst=img[tmph:h,0:w].copy()


reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")

# for i in range(0,len(result)):
#     if result[i]

for i in range(0,len(result)):
    beforeResult.append(str(result[i][1]))
for i in range(0,len(result)):
    if not ((result[i][0][0][0]>0 and result[i][0][0][0]<w) and (result[i][0][0][1]) > tmph and (result[i][0][0][1] < h)
    and (result[i][0][1][0]>0 and result[i][0][1][0]<w) and (result[i][0][1][1]) > tmph and (result[i][0][1][1] < h)
    and (result[i][0][2][0]>0 and result[i][0][2][0]<w) and (result[i][0][2][1]) > tmph and (result[i][0][2][1] < h)
    and (result[i][0][3][0]>0 and result[i][0][3][0]<w) and (result[i][0][3][1]) > tmph and (result[i][0][3][1] < h)):
        continue
    print(result[i][1])
    textResult.append(str(result[i][1]))

print(beforeResult)
print(textResult)

cv2.imshow('sdf,',img)
cv2.waitKey(0)
