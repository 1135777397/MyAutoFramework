# -*- coding:utf-8 -*-

import datetime
import time
import calendar

"""
    时间处理方法.不断补充
    author: kawi
    time: 22/04/16
    update:
"""


class TimeDeal:
    # 修饰符对应的函数不需要实例化，不需要 self 参数
    @classmethod
    def getNowTime(cls, format='%Y-%m-%d %H:%M:%S'):
        # strftime(format) 获取格式化的时间
        # 获取当前时间
        return time.strftime(format)
