# -*- coding: UTF-8 -*-
'''
@Project ：devicemanage 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：dengyunpeng16605
@Date    ：2021/8/2 下午5:42 
'''

from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'showdevices$',index),
    url(r'adddevices$', create),
    url(r'edit$', edit),
    url(r'delete$', delete),
    url(r'qrcodefish$', qrCodeFinsh,name='image'),
    url(r'queryqrcode$', queryQRCode)

]