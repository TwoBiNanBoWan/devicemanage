# -*- coding: UTF-8 -*-
'''
@Project ：devicemanage
@File    ：qrcodeFish.py
@IDE     ：PyCharm
@Author  ：dengyunpeng16605
@Date    ：2021/8/9 下午8:04
'''

# Create your views here.

import os
from typing import List

import MySQLdb
import uuid


from django.views.decorators.http import require_http_methods
from pkg_resources._vendor.six import BytesIO

from devicestore.models import DevicesInfo
import json
from devicestore.myJSONEncoder import myJSONEncoder
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
import time
import requests
import qrcode


# from urllib3.packages.six import BytesIO
from django.http import HttpResponse



@require_http_methods(["GET"])
def index(request):
    system = request.GET.get("system",'')
    model = request.GET.get("model", '')
    version = request.GET.get("version", '')
    propery_admin = request.GET.get("propery_admin", '')
    borrow_people = request.GET.get("borrow_people", '')
    propery_id = request.GET.get("propery_id", "")

    response = {}
    devicesInfos = DevicesInfo.objects.filter(system__icontains=system) \
        .filter(model__icontains=model) \
        .filter(version__icontains=version) \
        .filter(propery_admin__icontains=propery_admin) \
        .filter(borrow_people__icontains=borrow_people) \
        .filter(propery_id__icontains=propery_id)  # TODO 实现精确查询,使用__exact后查询不到数据，提示propery_id是必传项
    response['list'] = json.loads(serializers.serialize("json", devicesInfos, cls=myJSONEncoder))
    return JsonResponse(response)

    '''
    DTL方法实现
    
    sql = "SELECT * FROM devicestore.devicestore_devicesinfo WHERE 1=1 "
    if system.strip() != '':
        sql = sql + "and system = '" + system + "'"
    if model.strip() != '':
        sql = sql + "and model = '" + model + "'"
    if version.strip() != '':
        sql = sql + "and version = '" + version + "'"
    if propery_admin.strip() != '':
        sql = sql + "and propery_admin = '" + propery_admin + "'"
    if borrow_people.strip() != '':
        sql = sql + "and borrow_people = '" + borrow_people + "'"
    if id.strip() != '':
        sql = sql + "and id = '" + id + "'"
    print("查询SQL-----\n %s" % sql)

    conn = MySQLdb.connect(host="10.106.68.1", port=4000, user="product", passwd="banyu2017@TESTMYSQL", db="devicestore", charset='utf8')

    with conn.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
    devices = []
    columnNames = [column[0] for column in cursor.description]
    for i in results:
        devices.append(dict(zip(columnNames,i)))
    
    return render(request,"index.html",{"system":system,
                      "model":model,
                      "version":version,
                      "propery_admin":propery_admin,
                      "borrow_people":borrow_people,
                      "id":id,
                      "devices":devices})
    '''

@require_http_methods(["GET"])
def create(request):
    system = request.GET.get("system")
    model = request.GET.get("model")
    version = request.GET.get("version")
    propery_admin = request.GET.get("propery_admin")
    borrow_people = request.GET.get("borrow_people")
    desc = request.GET.get("desc")
    qr_code = None
    operator = "邓运鹏"
    propery_id = uuid.uuid1().hex
    # TODO 实现propery_id、ct、ut自动生成/创建


    DevicesInfos = DevicesInfo.objects.create(system=system,
                                       model=model,
                                       version=version,
                                       propery_admin=propery_admin,
                                       borrow_people=borrow_people,
                                       desc=desc,
                                       qr_code=qr_code,
                                       propery_id=propery_id,
                                       operator=operator)

    print(DevicesInfos,type(DevicesInfos))
    response = {}
    response["code"] = 200
    response["msg"] = "添加成功"

    return JsonResponse(response)





@require_http_methods(["GET"])
def edit(request):
    system = request.GET.get("system")
    model = request.GET.get("model")
    version = request.GET.get("version")
    propery_admin = request.GET.get("propery_admin")
    borrow_people = request.GET.get("borrow_people")
    desc = request.GET.get("desc")
    propery_id = request.GET.get("propery_id")
    qr_code = request.GET.get("qr_code")
    operator = "邓运鹏"
    ut = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


    devicesInfos = DevicesInfo.objects.filter(propery_id=propery_id).update(system=system,
                                       model=model,
                                       version=version,
                                       propery_admin=propery_admin,
                                       borrow_people=borrow_people,
                                       desc=desc,
                                       qr_code=qr_code,
                                       operator=operator,
                                       ut=ut)

    print(devicesInfos,type(devicesInfos))
    response = {}
    response["code"] = 200
    response["msg"] = "修改成功"

    return JsonResponse(response)




@require_http_methods(["GET"])
def delete(request):
    propery_id = request.GET.get("propery_id")
    DevicesInfo.objects.filter(propery_id=propery_id).delete()

    response = {}
    response["code"] = 200
    response["msg"] = "删除成功"

    return JsonResponse(response)

@require_http_methods(["GET"])
def qrCodeFinsh(request):
    propery_id = request.GET.get("propery_id", "")
    # devicesInfo = requests.get("http://127.0.0.1:8000/devicestore/showdevices",params={"propery_id":propery_id})

    img = qrcode.make("http://127.0.0.1:8000/devicestore/showdevices?propery_id=" + propery_id)      #传入网址计算出二维码图片字节数据
    buf = BytesIO()                                 #创建一个BytesIO临时保存生成图片数据
    img.save(buf)                                   #将图片字节数据放到BytesIO临时保存
    image_stream = buf.getvalue()                   #在BytesIO临时保存拿出数据
    result = HttpResponse(image_stream,content_type="image/jpg")

    # 更新数据库
    qr_code = result.content
    # safads <class 'bytes'>
    print("safads",type(qr_code))
    operator = "邓运鹏"
    ut = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    DevicesInfo.objects.filter(propery_id=propery_id).update(
                                                            qr_code=qr_code,
                                                            operator=operator,
                                                            ut=ut)
    response = {}
    response["code"] = 200
    response["msg"] = "生成成功"
    response["qr_code"] = qr_code
    return response

@require_http_methods(["GET"])
def queryQRCode(request):
    propery_id = request.GET.get("propery_id", "")

    resultQRCode = DevicesInfo.objects.filter(propery_id=propery_id)
    qrcode = None
    for i in resultQRCode:
        qrcode = i.qr_code

    response = {}
    response["code"] = 200
    response["msg"] = "获取成功"
    response["qr_code"] = qrcode
    return response


