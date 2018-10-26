#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UrlManager(object): #建立URL管理类，实现对未爬URL和已爬URL的管理
    def __init__(self):  #初始化UrlManager属性，创建未爬集合和已爬集合
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url): #定义新加url是否为未读url方法
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls): #定义获取新url方法
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self): #返回是否还有未爬取url
        return len(self.new_urls) != 0

    def get_new_url(self): #将未爬取url逐个弹出
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url