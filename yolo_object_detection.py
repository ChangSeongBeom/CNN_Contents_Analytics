import cv2
import numpy as np
import os

hash_dict={
"person":0,
"bicycle":0,
"car":0,
"motorbike":0,
"aeroplane":0,
"bus":0,
"train":0,
"truck":0,
"boat":0,
"traffic light":0,
"fire hydrant":0,
"stop sign":0,
"parking meter":0,
"bench":0,
"bird":0,
"cat":0,
"dog":0,
"horse":0,
"sheep":0,
"cow":0,
"elephant":0,
"bear":0,
"zebra":0,
"giraffe":0,
"backpack":0,
"umbrella":0,
"handbag":0,
"tie":0,
"suitcase":0,
"frisbee":0,
"skis":0,
"snowboard":0,
"sports ball":0,
"kite":0,
"baseball bat":0,
"baseball glove":0,
"skateboard":0,
"surfboard":0,
"tennis racket":0,
"bottle":0,
"wine glass":0,
"cup":0,
"fork":0,
"knife":0,
"spoon":0,
"bowl":0,
"banana":0,
"apple":0,
"sandwich":0,
"orange":0,
"broccoli":0,
"carrot":0,
"hot dog":0,
"pizza":0,
"donut":0,
"cake":0,
"chair":0,
"sofa":0,
"pottedplant":0,
"bed":0,
"diningtable":0,
"toilet":0,
"tvmonitor":0,
"laptop":0,
"mouse":0,
"remote":0,
"keyboard":0,
"cell phone":0,
"microwave":0,
"oven":0,
"toaster":0,
"sink":0,
"refrigerator":0,
"book":0,
"clock":0,
"vase":0,
"scissors":0,
"teddy bear":0,
"hair drier":0,
"toothbrush":0
}
arr = os.listdir("C:/Users/iwsl1/yolo_object/CNN_Contents_Analytics/data")

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
    img = cv2.imread("C:/Users/iwsl1/yolo_object/CNN_Contents_Analytics/data/"+substr)
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
            label = str(classes[class_ids[i]])
            hash_dict[label]+=1
            print(label)
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)


cv2.imshow("Image", img)
print(hash_dict)
cv2.waitKey(0)
cv2.destroyAllWindows()