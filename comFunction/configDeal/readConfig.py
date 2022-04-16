"""
readconfig file
"""
"""
    author: kawi
    time: 22/04/16
    update: 
"""

import os
from configparser import ConfigParser
from comFunction.logingDeal import log

# 定位到配置文件位置
configPath = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "config\config.ini")
log.info("get config.ini information")


class ReadConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(configPath, encoding="UTF-8")

    def get_test_url(self):
        """获取测试地址路径"""
        try:
            url = self.config.get("TESTSERVER", "url")
            if url:
                return url
            else:
                raise Exception("未获取到URL地址，请检查配置文件是否配置测试url地址信息")
        except Exception as e:
            log.error("ERROR : {}".format(e))
            print("ERROR : {}".format(e))

    def get_database(self):
        try:
            DBtype = self.config.get("DATABASE", "type")
            DBuser = self.config.get("DATABASE", "user")
            DBpassword = self.config.get("DATABASE", "password")
            DBdatabase = self.config.get("DATABASE", "database")
            DBhost = self.config.get("DATABASE", "host")
            DBport = self.config.get("DATABASE", "port")
            if DBtype and DBuser and DBpassword and DBdatabase and DBhost and DBport:
                value = {'type': DBtype, 'user': DBuser, 'password': DBpassword, 'database': DBdatabase, 'host': DBhost,
                         'port': DBport}
                return value
            else:
                raise Exception("请检查数据库配置是否配置正常")
        except Exception as e:
            log.error("ERROR : {}".format(e))
            print("ERROR : {}".format(e))


if __name__ == '__main__':
    ReadConfig().get_database()
