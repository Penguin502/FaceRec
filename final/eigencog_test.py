# -*- coding: utf-8 -*-

from numpy import *
import sys,os
from pca import *
import cv2
reload(sys)
sys.setdefaultencoding('utf-8')
test = int(sys.argv[1])

ef = Eigenfaces()
ef.dist_metric=ef.distEclud
ef.loadimgs("train_faces/")
ef.compute()
# 创建测试集
testImg = ef.X[test]

cv2.imshow('image', testImg)

print "实际值 =", ef.y[test], " ", "预测值 =",ef.predict(testImg)

cv2.waitKey(0)

cv2.destroyAllWindows()
