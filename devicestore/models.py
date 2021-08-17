import datetime

import django
from django.db import models

# Create your models here.


class DevicesInfo(models.Model):
    system = models.CharField(max_length=30,help_text='系统') #必填
    model = models.CharField(max_length=50,help_text='型号') #必填
    version = models.CharField(max_length=30,help_text='版本') #必填
    propery_admin = models.CharField(max_length=30,help_text='资产管理员') #必填
    borrow_people = models.CharField(max_length=30,help_text='借用人') #必填
    desc = models.TextField(blank=True,null=True,help_text='备注') #选填
    qr_code = models.ImageField(max_length=6000,null=True,help_text='二维码')
    ct = models.DateTimeField(default=django.utils.timezone.now,help_text='创建时间')
    ut = models.DateTimeField(default=django.utils.timezone.now,help_text='更新时间')
    operator = models.CharField(max_length=30,help_text='操作人')
    # 通过uuid生成
    propery_id = models.CharField(default="",max_length=100,db_index=True,help_text='资产id')

    # Django自动生成id主健
    # id = models.IntegerField(db_column='propery_id',unique=True)