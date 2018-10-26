#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import telnetlib

class IpInfoOutputer(object):     # 将ip信息输出到服务
    def __init__(self):
        self.datas = set()
        self.count = 0

    def collect_data(self, new_data):
        if new_data is None:
            return
        # print new_data    
        self.datas = self.datas | new_data
        # print 'collect_data: -------------------------------->'
        print (self.datas)

    def output_ip(self,new_data):
        if new_data is None:
            return    
        for ip in new_data:
            print ('IP ---> ' + str(ip))
            try:
                arry = ip.split(':')
                telnetlib.Telnet(arry[0], port=arry[1], timeout=20)
            except Exception as e:
                print(e)
            else:
                self.count +=1
                print ('upload successful count %s ,,, IP: %s' % (str(self.count), ip))