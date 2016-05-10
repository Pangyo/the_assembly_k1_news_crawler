'''
Created on 2016. 5. 8.

Information : shell main

@author: yunjae
'''

from Helper import LogHelper

from Product_Politics.Model import naver_presidentModel
from Product_Politics.Service import naver_presidentService


url = 'http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=264'
ListNaverPresident = naver_presidentService.GetPresidentList(url)

#for ps in naver_presidentService.ListNaverPs:
#    print(ps.index)
#    print(ps.link)
#    print(ps.title)
#    print(ps.writer)
#    print(ps.date)

