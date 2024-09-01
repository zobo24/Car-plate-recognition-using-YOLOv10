
import cv2
from ultralytics import YOLOv10
import numpy as np
import math
import re
from paddleocr import PaddleOCR
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

#video source
#cap = cv2.VideoCapture(r"C:\Users\bozom\Desktop\registracija\Resources\carLicence4.mp4")
#cap = cv2.VideoCapture(r"C:\Users\bozom\Desktop\registracija\Resources\carLicence1.mp4")
cap = cv2.VideoCapture(r"C:\Users\bozom\Desktop\registracija\Resources\ggollf.jpg")

#initalization
model = YOLOv10(r"C:\Users\bozom\Desktop\registracija\weights\best (1).pt")
count = 0
ocr = PaddleOCR(use_angle_cls = True, use_gpu=False)

#Recognition class
className = ["Registracija"]


#OCR recognition
def paddle_ocr(frame, x1, y1, x2, y2):
    frame = frame[y1:y2, x1:x2]
    result = ocr.ocr(frame, det=False, rec=True, cls= False)
    text = ""
    for i in result:
        #print("OCR", i)
        scores = i[0][1]
        if np.isnan(scores):
            scores = 0
            
        else:
            scores = int(scores * 100)

        if scores > 60:
            text = i[0][0]        
    pattern = re.compile('[W]')
    text = pattern.sub('', text)
    text = text.replace("???", "")
    text = text.replace("O", "0")
    return str(text)
        
#video show and algorithm implementation
while True:
    ret, frame = cap.read()
    if ret: 
        count += 1
        print(f"Frame Number: {count}")
        results = model.predict(frame, conf = 0.45)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1,y1,x2,y2 = int(x1), int(y1),int(x2), int(y2)
                cv2.rectangle(frame, (x1,y1,x2,y2), (255, 0, 0), 2)
                classNameInt = int(box.cls[0])
                clsName = className[classNameInt]
                conf = math.ceil(box.conf[0]*100)/100
                #label = f'{className}:{conf}'
                label = paddle_ocr(frame,x1, y1, x2, y2)
                textSize = cv2.getTextSize(label,0, fontScale=0.5, thickness=2)[0]
                c2 = x1 + textSize[0], y1 - textSize[1] - 3
                cv2.rectangle(frame, (x1,y1), c2, (255,0,0), -1)
                cv2.putText(frame, label, (x1, y1 - 2), 0, 0.5, [255,255,255], thickness = 1, lineType=cv2.LINE_AA)
        
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('1'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()