import os
import sys
from comFunction.timeDeal.timeDeal import TimeDeal
from loguru import logger
from bean.baseConfig import BaseConfig

"""可以复用的路径生成写法"""
# stack_t = inspect.stack()
# ins = inspect.getframeinfo(stack_t[1][0])
# print(ins)
# file_dir = os.path.dirname(os.path.abspath(ins.filename))
# print(file_dir)
# report_dir = os.path.join(file_dir, "reports")
# print(report_dir)
# if os.path.exists(report_dir) is False:
#     os.mkdir(report_dir)

"""固定路径生成写法"""
logPath = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'logs')
if os.path.exists(logPath) is False:
    os.mkdir(logPath)

reportPath = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'reports')
if os.path.exists(reportPath) is False:
    os.mkdir(reportPath)

now_time = TimeDeal.getNowTime("%Y-%m-%d %H_%M_%S")
if BaseConfig.LOG_PATH is None:
    BaseConfig.LOG_PATH = os.path.abspath(os.path.join(logPath, now_time + "_log.log"))
if BaseConfig.REPORT_PATH is None:
    BaseConfig.REPORT_PATH = os.path.abspath(os.path.join(reportPath, now_time + "_result.html"))

logger.add(BaseConfig.LOG_PATH, encoding="utf-8")


def debug(msg):
    now = TimeDeal.getNowTime("%Y-%m-%d %H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [DEBUG] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.debug(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.debug(msg)


def info(msg):
    now = TimeDeal.getNowTime("%Y-%m-%d %H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [INFO] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.info(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)


def error(msg):
    now = TimeDeal.getNowTime("%Y-%m-%d %H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [ERROR] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.error(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)


def warn(msg):
    now = TimeDeal.getNowTime("%Y-%m-%d %H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [WARNING] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.warning(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.warning(msg)


def printf(msg):
    if BaseConfig.LOG_COLOR is True:
        return logger.success(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.success(msg)

# if __name__ == '__main__':
