#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib

class HtmlParser(object):  # 创建html解析类，实现对html的解析
    def parse(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls = self.get_new_urls(new_url, soup)
        new_data = self.get_new_data(new_url, soup)
        return new_urls, new_data

    def get_new_urls(self, new_url, soup):  # 获取解析后的新url
        # <a href="?stype=1&amp;page=3">3</a>
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/inha/\d+/'))
        if links == None or len(links) == 0:
            links = soup.find_all('a', href=re.compile(r'/intr/\d+/'))
        for link in links:
            new_parse_url = link['href']
            new_full_url = urllib.parse.urljoin(new_url, new_parse_url)
            # print('new_full_url: ' + new_full_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, new_url, soup):  # 获取解析后新数据
        # 
        res_data = set()
        # table_node = soup.find('div', attrs={'class':'containerbox boxindex'}).find('table')
        table_node = soup.find('table', class_ = 'table table-bordered table-striped')
       	if table_node is None:
       		return res_data
		# print table_node.encode('GBK')
        for index, tr in enumerate(table_node.find_all('tr')):
        	if index != 0:
        		tds = tr.find_all('td')
        		# print 'item_data:' + ''+ tds[0].contents[0]+':' + tds[1].contents[0]
        		res_data.add(''+ tds[0].contents[0]+':' + tds[1].contents[0])
        # print res_data
        return res_data