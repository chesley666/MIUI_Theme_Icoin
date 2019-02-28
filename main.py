__author__ = 'Administrator'
from spyder import konachan_spyder
import face
from makeXML import makeXML
import os
from glob import glob

def clean(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            clean(c_path)
            os.rmdir(c_path)
        else:
            os.remove(c_path)
    for file in glob('imgs/*.*'):
        os.remove(file)
    for file in glob('faces/*.*'):
        os.remove(file)


if __name__ =='__main__':
    #http://konachan.net/post?page=1&tags=
    sp = konachan_spyder('li_syaoran')

    print('准备中...')
    clean('result')
    print('(1/3) 爬取k站图片中，需要较长时间，请稍后...')
    sp.konachan_spyder()
    print('(2/3) 人脸识别中，请稍后...')
    if os.path.exists('faces') is False:
        os.makedirs('faces')
    file_list = glob('imgs/*.jpg')
    for filename in file_list:
        face.detect(filename)
    faces = glob('faces/*.jpg')
    for face_img in faces:
        face.img_circle(face_img)
    print('(3/3) 生成动态图标中，请稍后...')
    xml = makeXML()
    xml.deal(face_sf=0.7, base_sf=0.7, mask_sf=1)
    #print('清理工程目录....')
    #clean('result')
    print('全部完成，结果文件在result目录')