#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import traceback
import time
import url_manager, html_downloader, html_parser, ip_info_outputer
    

"""
    快代理
    
    https://www.kuaidaili.com/free/
"""


class SpiderMain(object):    # 主调度类
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = ip_info_outputer.IpInfoOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ("craw %d : %s" % (count, new_url))
                # html_cont = self.downloader.download(new_url)
                html_cont = self.downloader.download_by_webdriver(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                # self.outputer.collect_data(new_data)
                self.outputer.output_ip(new_data)
                # if count == 5:
                #     break
                count += 1
            except:
                print ("craw failed")
                print (traceback.format_exc())

            # 休眠 60 秒 * 10
            time.sleep(1*60*30)    

        # self.outputer.output_ip()



if __name__ == '__main__':
	obj_spider = SpiderMain()
	obj_spider.craw('https://www.kuaidaili.com/free/intr/')