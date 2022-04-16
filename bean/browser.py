"""
Browser bean file
"""
"""
    author: kawi
    time: 22/04/15
    update: 
"""


class Browser:
    """
    Define run browser config
    定义运行浏览器配置
    :param NAME:浏览器种类
    :param REPORT_PATH:针对Web UI测试需要指定浏览器（"chrome"、"firefox" 等）。
    :param REPORT_TITLE:报告标题
    :param LOG_PATH:日志路径

    """
    NAME = None
    REPORT_PATH = None
    REPORT_TITLE = "Test Report"
    LOG_PATH = None
