#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests ##导入requests
import re
import os
import time
from bs4 import BeautifulSoup
from zcy_fun import get_format_filename
from zcy_fun import get_inner_link
from proxytest import get_random_IP
from proxytest import get_image_header

from zcy_fun import Process_SubPage

# file_path='D:\MyProjectFile\Python\studyproject\Python3\StudyPro1\datebase'#存储的地址

# file_path = 'D:\1024\日本骑兵'

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding':'gzip',
           }#初始使用的header
# URL_1024='github已自动隐藏该信息'#网站地址中‘日本骑兵’系列，别的系列我没有测试，不保证正确 #刚测试了，‘亚洲无码’也可以，估计所有系列的网页HTML格式是一样的
# URL_1024='http://1024.91lulea.click/pw/thread.php?fid=22&page='#日本骑兵
URL_1024_1 = 'http://1024.91lulea.click/pw/thread.php?fid=3&page='   #最新合集
URL_1024_2 = 'http://1024.91lulea.click/pw/thread.php?fid=5&page='   #亚洲无码
URL_1024_3 = 'http://1024.91lulea.click/pw/thread.php?fid=22&page='  #日本骑兵
URL_1024_4 = 'http://1024.91lulea.click/pw/thread.php?fid=7&page='   #欧美新片
URL_1024_5 = 'http://1024.91lulea.click/pw/thread.php?fid=18&page='  #三级写真
URL_Arr = (URL_1024_1, URL_1024_2, URL_1024_3, URL_1024_4, URL_1024_5)


file_path_1 = '/Users/liusen/Desktop/1024/1'
file_path_2 = '/Users/liusen/Desktop/1024/2'
file_path_3 = '/Users/liusen/Desktop/1024/3'
file_path_4 = '/Users/liusen/Desktop/1024/4'
file_path_5 = '/Users/liusen/Desktop/1024/5'
file_path_Arr = [file_path_1, file_path_2, file_path_3, file_path_4, file_path_5]


seed_path_1 = '/Users/liusen/Desktop/seed/seed_1.txt'
seed_path_2 = '/Users/liusen/Desktop/seed/seed_2.txt'
seed_path_3 = '/Users/liusen/Desktop/seed/seed_3.txt'
seed_path_4 = '/Users/liusen/Desktop/seed/seed_4.txt'
seed_path_5 = '/Users/liusen/Desktop/seed/seed_5.txt'
seed_Arr = (seed_path_1, seed_path_2, seed_path_3, seed_path_4, seed_path_5)


for i in range(5):
    for x in range(1, 20):
        # 翻页
        print(x)
        url_for_1024 = URL_Arr[i] + str(x+1)
        filePath = file_path_Arr[i]

        start_html = requests.get(url_for_1024, headers=headers)
        start_html.encoding = 'utf-8'
        bsObj = BeautifulSoup(start_html.text, 'html.parser')
        for a in bsObj.find("tbody", {"style": "table-layout:fixed;"}).findAll("h3"):
            attrs = a.find("a").attrs['href']
            # if re.match(r'^htm_data/.+.html', attrs):
            print(attrs)
            # 取种子名
            seedStr = get_inner_link(attrs)
            seed_html = requests.get(seedStr, headers=get_image_header())
            seed_html.encoding = 'utf-8'
            seedObj = BeautifulSoup(seed_html.text, 'html.parser')
            for seed_a in seedObj.find("div", {"id": "read_tpc"}).findAll("a"):
                if re.match(r'^http://www?\d+.+.html$', seed_a.attrs['href']):
                    seedUrl = seed_a.attrs['href']
                    seedNum = seedUrl[-12: -5]
                    print(seedNum)

                    a_path = get_format_filename(a.text)  # 构建本地文件路径,影片名

                    if not os.path.exists(os.path.join(filePath, seedNum)):
                        os.makedirs(os.path.join(filePath, seedNum))
                    os.chdir(filePath + '/' + seedNum)  # 切换到上面创建的文件夹
                    f = open(seedNum + '.txt', 'w')  # r只读，w可写，a追加
                    f.write(a_path)
                    f.close()
                    Process_SubPage(filePath + '/' + seedNum, attrs)  # 处理子页面，包括下载图片，种子
                    print(get_inner_link(attrs))
                    print(a_path + '：处理完毕')
                    time.sleep(0.5)  # 设置等待还是会被服务器封禁


                    # # 种子页网址 爬取种子
                        # seedStr = get_inner_link(a.attrs['href'])
                        # seed_html = requests.get(seedStr, headers=get_image_header())
                        # seed_html.encoding = 'utf-8'
                        # seedObj = BeautifulSoup(seed_html.text, 'html.parser')
                        # for seed_a in seedObj.find("div", {"id": "read_tpc"}).findAll("a"):
                        #     if re.match(r'^http://www?\d+.+.html$',seed_a.attrs['href']):
                        #
                        #
                        #         print(seed_a.attrs['href'])
                        #         # f = open(seed_path,'w')
                        #         # f.write(seed_a.attrs['href'])
                        #         with open(seed_Arr[i], 'a', newline='\r') as seed_f:
                        #             seed_f.write(seed_a.attrs['href'] + '\r')







