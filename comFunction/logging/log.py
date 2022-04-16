import os
import time
import inspect
from loguru import logger
from bean.driverConfig import DriverConfig

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
print(ins)
file_dir = os.path.dirname(os.path.abspath(ins.filename))
print(file_dir)
report_dir = os.path.join(file_dir, "reports")
print(report_dir)
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

def info(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if DriverConfig.is_debug is False:
        print(now + " [INFO] " + str(msg))
    if colorLog is True:
        return logger.info(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)
