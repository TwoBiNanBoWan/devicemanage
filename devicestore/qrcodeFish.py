# -*- coding: UTF-8 -*-
'''
@Project ：devicemanage 
@File    ：qrcodeFish.py
@IDE     ：PyCharm 
@Author  ：dengyunpeng16605
@Date    ：2021/8/9 下午8:04 
'''

import os
import django.utils
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from urllib3.packages.six import BytesIO

os.environ.setdefault('DJANGO_SETTING_MODULE', 'devicemanage.settings')
django.setup()
from devicestore.views import index


import qrcode
import json
import requests



# def qrcodeStop():
#
#     data = '人生苦短,我用python'
#     image = qrcode.make(data)
#
#     with open('test.png','wb') as f:
#         image.save(f)


# if __name__ == '__main__':
#     qrCodeFinsh()



def qrCodeFinsh():
    propery_id = "2a7f9d2ef50711eba0d0acde48001122"


    response = requests.get("http://127.0.0.1:8000/devicestore/showdevices",params={"propery_id":propery_id})
    # print(json.loads(response.content))
    # image = qrcode.make(response.content)
    #
    # with open('test.png','wb') as f:
    #     image.save(f)



    img = qrcode.make(response.content)      #传入网址计算出二维码图片字节数据
    buf = BytesIO()                                 #创建一个BytesIO临时保存生成图片数据
    img.save(buf)                                   #将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()                   #在BytesIO临时保存拿出数据
    response2 = HttpResponse(image_stream, content_type="image/jpg")
    print(response2.content)

if __name__ == '__main__':
    qrCodeFinsh()
