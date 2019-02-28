__author__ = 'Administrator'
import cv2
import numpy as np
import os.path
from glob import glob
import hashlib

def img_circle(input_img):
    # ---------------------
    # 作者：红薯爱帅
    # 来源：CSDN
    # 原文：https://blog.csdn.net/san1156/article/details/76691841
    # 版权声明：本文为博主原创文章，转载请附上博文链接！
    #剪裁为最大内切圆形，保存png
    img = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)
    rows, cols, channel = img.shape
    # 创建一张4通道的新图片，包含透明通道，初始化是透明的
    img_new = np.zeros((rows,cols,4),np.uint8)
    img_new[:,:,0:3] = img[:,:,0:3]
    # 创建一张单通道的图片，设置最大内接圆为不透明，注意圆心的坐标设置，cols是x坐标，rows是y坐标
    img_circle = np.zeros((rows,cols,1),np.uint8)
    img_circle[:,:,:] = 0  # 设置为全透明
    img_circle = cv2.circle(img_circle,(cols//2,rows//2),min(rows, cols)//2,(255),-1) # 设置最大内接圆为不透明
    # 图片融合
    img_new[:,:,3] = img_circle[:,:,0]
    # 保存图片
    file_dir = os.path.dirname(os.path.realpath(input_img))
    file_name = os.path.splitext(os.path.basename(os.path.realpath(input_img)))[0]
    cv2.imwrite(file_dir+'\\'+file_name+".png", img_new)


def detect(filename,cascade_file="lbpcascade_animeface.xml"):
    # ---------------------
    # 作者：莫凡的博客
    # 来源：CSDN
    # 原文：https://blog.csdn.net/mozf881/article/details/83592977
    # 版权声明：本文为博主原创文章，转载请附上博文链接！
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(
        gray,
        # detector options
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (128,128)
    )
    for i,(x,y,w,h) in enumerate(faces):
        face = image[y: y+h, x:x+w, :]
        face = cv2.resize(face, (144, 144))
        save_filename = hashlib.md5(os.path.basename(os.path.realpath(filename)).encode('utf-8')).hexdigest()
        save_filename = '%s.jpg' % save_filename

        cv2.imwrite("faces/"+save_filename, face)



if __name__ == '__main__':
    if os.path.exists('faces') is False:
        os.makedirs('faces')
    file_list = glob('imgs/*.jpg')
    for filename in file_list:
        detect(filename)

    faces = glob('faces/*.jpg')
    for face in faces:
        img_circle(face)
