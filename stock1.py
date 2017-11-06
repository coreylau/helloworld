# -*- coding: utf-8 -*-
 
import urllib.request
import re
from bs4 import BeautifulSoup
from time import ctime

def get_last_info():
    url='http://ggjd.cnstock.com/gglist/search/ggkx/0'
    html=urllib.request.urlopen(url)
    bsobj2=BeautifulSoup(html,"lxml")
    alltext=bsobj2.body.findAll("ul",class_='new-list')
    l_2=len(alltext)
    file_open=open(r'E:\Python36\File\securities_info1.txt','w')
    for i in range(1,l_2):
        t1= alltext[i].get_text()
        i+=1
        t1="<获取信息时间>：%s\n"%ctime()+url+'\n'+"中国证券网->上市公司专区->信息披露与公告解读->公告快讯:"+t1
        print (t1)
        m1=re.findall('东方明珠.*\s',t1)
        m2=re.findall('国泰君安.*\s',t1)
        m3=re.findall('传化.*\s',t1)
        m4=re.findall('幸福蓝海.*\s',t1)
        m5=re.findall('创新股份.*\s',t1)
        m6=re.findall('诚迈.*\s',t1)
        m7=re.findall('华大基因.*\s',t1)
        if m1:
            print (m1)
        elif m2:
            print (m2)
        elif m3:
            print (m3)
        elif m4:
            print (m4)
        elif m5:
            print (m5)
        elif m6:
            print (m6)
        elif m7:
            print (m7)
        else:
            print('not match')
    file_open.write(t1)
    file_open.close()

get_last_info()


    
    

 
