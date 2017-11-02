# !/usr/bin/env python
# -*- encoding:utf-8 -*-

from utils import *


if __name__ == "__main__":
    print "begin request:"
    client=TcpClient("www.enjoytoday.cn")
    client.getResponse()