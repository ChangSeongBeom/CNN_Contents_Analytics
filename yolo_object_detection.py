import cv2
import numpy as np
import os
from dataclasses import dataclass
from datetime import datetime
import time
import pymysql

@dataclass
class Item:
    object: str
    percent: str
    time : str
arr = os.listdir("C:/Users/iwsl1/CNN_Contents_Analytics/data")
itemDB=Item("TEST","TEST",str(datetime.now()))

print(arr)

for i in range(0,len(arr)):
    substr=arr[i]
    # Load Yolo
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Loading image
    # img = cv2.imread("C:/Users/iwsl1/yolo_object/CNN_Contents_Analytics/data/frame420.jpg")
    img = cv2.imread("C:/Users/iwsl1/CNN_Contents_Analytics/data/"+substr)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            class_name = classes[class_ids[i]]
            label = f"{class_name} {confidences[i]:.2f}"

            print(class_name)
            print(f"{confidences[i]:.2f}")

            itemDB.object = itemDB.object + " " + str(class_name)
            itemDB.percent = itemDB.percent + " " + str(f"{confidences[i]:.2f}")

            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)


cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


tmpObject=itemDB.object.split()
tmpObject.remove('TEST')

tmpPercent=itemDB.percent.split()
tmpPercent.remove('TEST')

now = time.strftime("%Y-%m-%d %H:%M:%S")

# connection 정보
conn = pymysql.connect(
    host = 'localhost', # host name
    user = 'root', # user name
    password = 'A1b2c3d4e5!', # password
    db='developer',
    charset = 'utf8'
)
cursor = conn.cursor()

print(tmpObject)
print(tmpPercent)
for i in range(0,len(tmpObject)):
    print(tmpObject[i])
    print(tmpPercent[i])
    sql = "INSERT INTO t_cmn_yolo_log VALUES (%s,%s,%s,%s)"
    val = (1,str(tmpObject[i]),str(tmpPercent[i]),now)
    cursor.execute(sql,val)

conn.commit()
conn.close()