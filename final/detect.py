#encoding=utf-8
import cv2
import sys
import numpy as np
#cascPath = sys.argv[1]
path = sys.argv[1]
if path=='0':
    path = 0
#分类器
cascPath = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
#获取视频或者摄像头
video_capture = cv2.VideoCapture(path)
while True:
    #获取每一帧
    ret, frame = video_capture.read()
    if ret==False:
        break
    #去噪处理
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(frame, kernel, iterations=1)
    #转化成灰度值方便进行人脸识别
    gray = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    print faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
