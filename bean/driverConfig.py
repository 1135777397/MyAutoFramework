"""
DriverConfig bean file
"""
"""
    author: kawi
    time: 22/04/15
    update: 22/04/16
"""


class DriverConfig:
    """
    browser driver
    :param driver: driver
    :param is_debug: 测试模式（debug）模式，设置为True不生成测试HTML测试报告，默认为False
    :param base_url:针对HTTP接口测试的参数，设置全局的URL。
    :param implicitly_wait:隐式等待时间设置，默认8秒，全局可用
    """
    driver = None
    is_debug = False
    base_url = None
    implicitly_wait = 8
