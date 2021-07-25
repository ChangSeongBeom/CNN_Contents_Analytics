import easyocr
import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
import os
from PIL import ImageFont, ImageDraw, Image
import natsort
beforeResult=[]
textResult=[]

tmpResult=[]

arr = os.listdir("C:/Users/iwsl1/CNN_Contents_Analytics/data/olim/")
arr=natsort.natsorted(arr)

for i in range(0,len(arr.length)):



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

#원본
print(beforeResult)

#자막 부분만 자른부분
print(textResult)

