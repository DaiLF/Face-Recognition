#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: kang_liu
from aip import AipFace
import base64

dic = {}

def Mactch(img1, img2):
    """ 你的 APPID AK SK """
    APP_ID = '11646884'
    API_KEY = '6r28pUXhHB4Z42zbalhLPmYU'
    SECRET_KEY = 'fkfKASiTmLwYoLGn4ENdrZzBDwsRnsfM'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    name = img2[9:-4] # 获取文件名
    dic[name] = 0    # 创建一个容器来存放已知照片的人物名称

    f1 = open(img1, 'rb')   # 打开图片1
    f2 = open(img2, 'rb')
    #参数image：图像base64编码 分别base64编码后的2张图片数据
    img1 = base64.b64encode(f1.read()) # 编码
    img2 = base64.b64encode(f2.read())
    image_1 = str(img1,'utf-8') # 变成字符串
    image_2 = str(img2,'utf-8')


    #数据打包上传到百度AI开放平台
    ptr = client.match([
                          {
                            'image': image_1,
                            'image_type': 'BASE64',
                          },
                          {
                            'image': image_2,
                            'image_type': 'BASE64',
                           }
                        ])
    ptr = ptr['result']
    # print(ptr)
    dic[name] = ptr['score'] #给名称打分并存在容器里面
    sort = list(sorted(dic.items(), key= lambda x:x[1])) #对分数进行排列，从小到大顺序
    print(sort)
    return sort




