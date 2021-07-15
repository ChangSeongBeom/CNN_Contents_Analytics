#
# import cv2
# import math
# import threading
#
# # 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
# vidcap = cv2.VideoCapture('videoplayback.mp4')
#
# count = 0
# timecount=0
#
# def startTimer():
#     global timecount
#     timer = threading.Timer(1, startTimer)
#     timer.start()
#     print(timecount)
#     timecount += 1
#
# startTimer()
#
#
# while (vidcap.isOpened()):
#     # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
#     # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
#     # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
#
#
#     ret, image = vidcap.read()
#     if timecount%3==0:

#         # print('Saved frame number : ' + str(int(vidcap.get(1))))
#         # cv2.imwrite("C:/Users\iwsl1/yolo_object/CNN_Contents_Analytics/data/%d.jpg"%count, image)
#
#
#     count += 1
#
# vidcap.release()
#
#
#
import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))  # added this line
        success, image = vidcap.read()

        cv2.imwrite(pathOut + "\\frame%d.jpg" % count, image)  # save frame as JPEG file
        count = count + 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages("videoplayback.mp4", "C:/Users\iwsl1/yolo_object/CNN_Contents_Analytics/data/")