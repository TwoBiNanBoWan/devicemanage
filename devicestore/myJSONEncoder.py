# -*- coding: UTF-8 -*-
'''
@Project ：devicemanage 
@File    ：myJSONEncoder.py
@IDE     ：PyCharm 
@Author  ：dengyunpeng16605
@Date    ：2021/8/4 上午11:51 
'''

import datetime
import decimal
import json
import uuid

from django.utils.timezone import is_aware
class myJSONEncoder(json.JSONEncoder):
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            r = o.isoformat(sep=" ")   # 关键代码
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, uuid.UUID):
            return str(o)
        else:
            return super(json.JSONEncoder, self).default(o)
