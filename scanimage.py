from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt
from getimage import *
import cv2
import mxnet as mx
from mxnet import nd
import os

target="banana"

def selectID(class_IDs):
    b=0
    a={}
    while True:
        
        ID=int(class_IDs[0][b].asscalar())
        if (ID)>=0:
            a[b]=ID
        elif ID==-1:
            break
        b+=1
    return a
    

def scan(dir):
    net = model_zoo.get_model('yolo3_darknet53_coco', pretrained=True, root='D:\AI_project\gluoncv\model')
    try:
        x, img = data.transforms.presets.yolo.load_test(dir, short=512)
        print('Shape of pre-processed image:', x.shape)
        class_IDs, scores, bounding_boxs = net(x)
        # print('class:', class_IDs[0][0])
        # print('scores:', scores[0][0])
        # print('bounding_box:', bounding_boxs[0][0])
        with open("D:/Desktop/animal_follower/PC/target.txt","r",encoding="utf-8") as f: 
            target=f.read()
        print("我在找"+target)
        targetIDs=selectID(class_IDs)
        for key in targetIDs:
            if net.classes[targetIDs[key]]==target:
                print("我看到了",target)
                return class_IDs[0][key],scores[0][key],bounding_boxs[0][key]
        # plt.show()
        print("没有找到目标")
        return class_IDs[0][50],scores[0][50],bounding_boxs[0][50]
    except:
        print("刚刚那张图片损坏了")
    return 0
    
    
    #ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0], class_IDs[0], class_names=net.classes)
    #plt.show()
    
    


if __name__ == '__main__':
    scan(r'C:\Users\13079\Desktop\demo.png')
