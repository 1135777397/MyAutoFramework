"""
Exceptions that may happen in all the seldom code.
在所有很少见的代码中可能发生的异常。
"""

"""
    继承异常基础类，webUI会遇到的问题
"""


class NotFindElementError(BaseException):
    """
    No element errors were found
    未发现元素错误
    """
    pass


