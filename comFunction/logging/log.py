import os
import time
import inspect
from loguru import logger
from bean.baseConfig import BaseConfig

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
print(ins)
file_dir = os.path.dirname(os.path.abspath(ins.filename))
print(file_dir)
report_dir = os.path.join(file_dir, "reports")
print(report_dir)
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

now_time = time.strftime("%Y-%m-%d %H:%M:%S")
if BaseConfig.LOG_PATH is None:
    BaseConfig.LOG_PATH = os.path.join(os.getcwd(), "reports", now_time + "_log.log")
if BaseConfig.REPORT_PATH is None:
    BaseConfig.REPORT_PATH = os.path.join(os.getcwd(), "reports", now_time + "_result.html")

logger.add(BaseConfig.LOG_PATH, encoding="utf-8")


def debug(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [DEBUG] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.debug(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.debug(msg)


def info(msg):
    now = time.strftime("%Y-%m-%d_%H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [INFO] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.info(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)


def error(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if BaseConfig.IS_DEBUG is False:
        print(now + " [ERROR] " + str(msg))
    if BaseConfig.LOG_COLOR is True:
        return logger.error(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)


def warn(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
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
