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
    :param base_url:针对HTTP接口测试的参数，设置全局的URL。
    :param implicitly_wait:隐式等待时间设置，默认8秒，全局可用
    """
    driver = None
    base_url = None
    implicitly_wait = 8
