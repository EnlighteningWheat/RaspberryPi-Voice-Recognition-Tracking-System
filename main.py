from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt
from getimage import *
import cv2
from scanimage import *
from mxnet import nd

while True:

    socket_service()
    result.send_txt()


# person(人) bicycle(自行车)  car(汽车)  motorbike(摩托车)  aeroplane(飞机)  bus(公共汽车)  train(火车)  truck(卡车)  boat(船) traffic
# light(信号灯)  fire hydrant(消防栓)  stop sign(停车标志)  parking meter(停车计费器)  bench(长凳) bird(鸟)  cat(猫)  dog(狗)  horse(马)
# sheep(羊)  cow(牛)  elephant(大象)  bear(熊)  zebra(斑马)  giraffe(长颈鹿) backpack(背包)  umbrella(雨伞)  handbag(手提包)  tie(领带)
# suitcase(手提箱) frisbee(飞盘)  skis(滑雪板双脚)  snowboard(滑雪板)  sports ball(运动球)  kite(风筝) baseball bat(棒球棒)  baseball
# glove(棒球手套)  skateboard(滑板)  surfboard(冲浪板)  tennis racket(网球拍) bottle(瓶子)  wine glass(高脚杯)  cup(茶杯)  fork(叉子)
# knife(刀) spoon(勺子)  bowl(碗) banana(香蕉)  apple(苹果)  sandwich(三明治)  orange(橘子)  broccoli(西兰花)  carrot(胡萝卜)  hot dog(
# 热狗)  pizza(披萨)  donut(甜甜圈)  cake(蛋糕) chair(椅子)  sofa(沙发)  pottedplant(盆栽植物)  bed(床)  diningtable(餐桌)  toilet(厕所)
# tvmonitor(电视机) laptop(笔记本)  mouse(鼠标)  remote(遥控器)  keyboard(键盘)  cell phone(电话) microwave(微波炉)  oven(烤箱)  toaster(
# 烤面包器)  sink(水槽)  refrigerator(冰箱) book(书)  clock(闹钟)  vase(花瓶)  scissors(剪刀)  teddy bear(泰迪熊)  hair drier(吹风机)
# toothbrush(牙刷)
#
#