__author__ = 'Administrator'
from glob import glob
import cv2
import numpy as np
#import face
import os
from shutil import copyfile

file_list = glob('temp_baseicoin/*.*')
for file in file_list:
    img = cv2.imread(file)
    img = cv2.resize(img, (182, 182))
    file = os.path.splitext(os.path.basename(os.path.realpath(file)))[0]
    cv2.imwrite('temp_baseicoin/'+file+'.jpg', img)
imgs = glob('temp_baseicoin/*.jpg')
for input_img in imgs:
    #face.img_circle(img)
    img = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)
    rows, cols, channel = img.shape
    # 创建一张4通道的新图片，包含透明通道，初始化是透明的
    img_new = np.zeros((rows,cols,4),np.uint8)
    img_new[:,:,0:3] = img[:,:,0:3]
    # 创建一张单通道的图片，设置最大内接圆为不透明，注意圆心的坐标设置，cols是x坐标，rows是y坐标
    img_circle = np.zeros((rows,cols,1),np.uint8)
    img_circle[:,:,:] = 0  # 设置为全透明
    img_circle = cv2.circle(img_circle, (cols//2,rows//2), min(rows-40, cols-40)//2, (255), -1)  # 设置最大内接圆为不透明
    # 图片融合
    img_new[:,:,3] = img_circle[:,:,0]
    # 保存图片
    file_dir = os.path.dirname(os.path.realpath(input_img))
    file_name = os.path.splitext(os.path.basename(os.path.realpath(input_img)))[0]
    cv2.imwrite(file_dir+'\\'+file_name+".png", img_new)

pngs = glob('temp_baseicoin/*.png')
for png in pngs:
    png_name = os.path.basename(os.path.realpath(png))
    copyfile(png, 'baseIcoin/'+png_name)