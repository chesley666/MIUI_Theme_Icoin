__author__ = 'Administrator'
import xml.etree.ElementTree as ET
import os
from glob import glob
from shutil import copyfile, copytree, rmtree
from PIL import Image
import random
import math

class makeXML():
    def __makeXML(self, face, face_w, face_h, baseIcoin, pathname, baseIcoinImg_w, baseIcoinImg_h, mask_w, mask_h):
        tree = ET.parse('temple.xml')
        root = tree.getroot()
        for var in root.iter('Var'):
            if var.attrib['name']=='face':
                var.set('expression', '\''+face+'.png\'')
            if var.attrib['name']=='face_w':
                var.set('expression', str(face_w))
            if var.attrib['name']=='face_h':
                var.set('expression', str(face_h))
            if var.attrib['name']=='base_coin':
                var.set('expression', '\''+baseIcoin+'.png\'')
            if var.attrib['name']=='base_coin_w':
                var.set('expression', str(baseIcoinImg_w))
            if var.attrib['name']=='base_coin_h':
                var.set('expression', str(baseIcoinImg_h))
            if var.attrib['name']=='mask':
                var.set('expression', '\'mask.png\'')
            if var.attrib['name']=='mask_w':
                var.set('expression', str(mask_w))
            if var.attrib['name']=='mask_h':
                var.set('expression', str(mask_h))
            if var.attrib['name']=='x':
                var.set('expression', str(int(mask_w/2)))
            if var.attrib['name']=='y':
                var.set('expression', str(int(mask_h/2)))
        rand_time = random.randint(0, 10000)
        for img in root.iter('Image'):
            i = 0
            for item in img.iter('Item'):
                if i == 0:
                    item.set('time', str(0))
                if i == 1:
                    item.set('time', str(rand_time))
                if i == 2:
                    item.set('time', str(rand_time+200))
                if i == 3:
                    item.set('time', str(rand_time+2200))
                if i == 4:
                    item.set('time', str(rand_time+2400))
                if i == 5:
                    item.set('time', str(rand_time+4400))
                i = i+1

        if os.path.exists('result/') is False:
            os.makedirs('result/'+pathname)
        tree.write('result/'+pathname+'/manifest.xml')



    def deal(self, face_sf=1, base_sf=1, mask_sf=1):
        faces = glob('faces/*.*')
        baseIcoins = glob('baseIcoin/*.png')
        num = min(len(faces), len(baseIcoins))

        mask = Image.open('mask.png')
        #print('mask:', mask.size, type(mask.size))
        mask_w = math.ceil(mask.size[0]*mask_sf)
        mask_h = math.ceil(mask.size[1]*mask_sf)
        if num > 0:
            if len(faces)<len(baseIcoins):
                print('注意!!!face:'+str(len(faces))+'张， 小于base:'+str(len(baseIcoins))+'张')
            baseIcoinImg = Image.open(baseIcoins[0])
            baseIcoinImg_w = math.ceil(baseIcoinImg.size[0]*base_sf)
            baseIcoinImg_h = math.ceil(baseIcoinImg.size[1]*base_sf)
            faceImg = Image.open(faces[0])
            face_w = math.ceil(faceImg.size[0]*face_sf)
            face_h = math.ceil(faceImg.size[0]*face_sf)
        #以face、baseicoin最小数量循环
        for i in range(num):
            '''
            0、从目录路径获取文件名
            1、创建对应目录
            2、复制图片资源到对应目录
            3、获取mask、baseicoin大小
            4、从xml模板生成代码文件
            '''
            baseIcoin = os.path.splitext(os.path.basename(os.path.realpath(baseIcoins[i])))[0]
            face = os.path.splitext(os.path.basename(os.path.realpath(faces[i])))[0]
            pathname = baseIcoin

            if os.path.exists('result/'+pathname) is False:
                os.makedirs('result/'+pathname)

            copyfile(faces[i], 'result/'+pathname+'/'+face+'.png')
            copyfile(baseIcoins[i], 'result/'+pathname+'/'+baseIcoin+'.png')
            copyfile('mask.png', 'result/'+pathname+'/mask.png')

            self.__makeXML(face, face_w, face_h, baseIcoin, pathname, baseIcoinImg_w, baseIcoinImg_h, mask_w, mask_h)

        #时钟、日历、天气，3个特殊的图标：把mask拷入，再拷贝整个目录到result
        copyfile('mask.png', '3special/com.android.calendar/mask.png')
        copyfile('mask.png', '3special/com.android.deskclock/mask.png')
        copyfile('mask.png', '3special/com.miui.weather2/mask.png')
        if os.path.exists('result/com.android.calendar') is True:
            rmtree('result/com.android.calendar')
        if os.path.exists('result/com.android.deskclock') is True:
            rmtree('result/com.android.deskclock')
        if os.path.exists('result/com.miui.weather2') is True:
            rmtree('result/com.miui.weather2')
        copytree('3special/com.android.calendar', 'result/com.android.calendar')
        copytree('3special/com.android.deskclock', 'result/com.android.deskclock')
        copytree('3special/com.miui.weather2', 'result/com.miui.weather2')



if __name__ == '__main__':
    xml = makeXML()
    xml.deal(face_sf=0.7, base_sf=0.7, mask_sf=1)