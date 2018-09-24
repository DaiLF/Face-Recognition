#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: kang_liu
from aip import AipFace
import base64

dic = {}

def Mactch(img1, img2):
    """ APPID AK SK """
    APP_ID = '*******'
    API_KEY = '************'
    SECRET_KEY = '**********************'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    name = img2[9:-4] # obtain image filename
    dic[name] = 0   

    f1 = open(img1, 'rb')   
    f2 = open(img2, 'rb')
   
    img1 = base64.b64encode(f1.read()) 
    img2 = base64.b64encode(f2.read())
    image_1 = str(img1,'utf-8') 
    image_2 = str(img2,'utf-8')


    #update the date to the baidu AI platform
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
    dic[name] = ptr['score'] 
    sort = list(sorted(dic.items(), key= lambda x:x[1])) 
    print(sort)
    return sort




