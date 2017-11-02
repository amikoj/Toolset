# !/usr/bin/env python
# -*- encoding:utf-8 -*-

import  socket,sys,urllib2




class TcpClient:
    port = 80     # 默认http请求


    def __init__(self,host,params=None):
        #初始化基本配置参数
        #请求信息头部
        self.requestBody=""       #请求信息内容
        self.responseHeader=""
        self.responseBody=""
        self.host=host
        self.params=params

    def getResponse(self):
        '''
        :return: 请求返回的数据,通过字典的方式
        '''

        # print "getResponse,and address is:%s"%(str(self.address))
        # if self.params is None:
        #     '''
        #      请求参数为空的时候，返回页面请求
        #     '''
        #     print "请求参数为空"
        #     requestStr=self.requestHeader
        #     print requestStr
        # else:
        #     '''
        #     请求信息不为空
        #
        #     '''
        #     requestStr=''.join(self.requestHeader,self.requestBody) #字符串链接
        # print "requestStr:%s"%requestStr
        responseStr = urllib2.urlopen("http://www.baidu.com").read()
        return responseStr









