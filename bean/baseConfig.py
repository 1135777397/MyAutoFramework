"""
BaseConfig bean file
"""
"""
    author: kawi
    time: 22/04/15
    update: 
"""

class BaseConfig:
    """
    BaseConfig
    :param REPORT_PATH:报告路径
    :param REPORT_TITLE:报告标题
    :param LOG_PATH:日志路径
    :param LOG_COLOR: 默认True，显示带有色彩图案的日志
    :param IS_DEBUG: 测试模式（debug）模式，设置为True不生成测试HTML测试报告，默认为False
    """
    REPORT_PATH = None
    REPORT_TITLE = "Test Report"
    LOG_PATH = None
    LOG_COLOR = True
    IS_DEBUG = False

