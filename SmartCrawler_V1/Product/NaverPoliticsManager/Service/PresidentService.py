'''
Created on 2016. 5. 8.

Information : Naver President Service

@author: yunjae
'''

import requests

from bs4 import BeautifulSoup

from Common.Language import Resources
from Common.CommonClass.BaseClass import BaseClass

from Product.NaverPoliticsManager.Common import NaverResources
from Product.NaverPoliticsManager.Common import CommonNaver
from Product.NaverPoliticsManager.Model.President import PresidentModel


class PresidentService(BaseClass):

    def __init__(self):
        self.ListNaverPs = []
    
    def GetPresidentList(self, item_url):
        index = 1;
    
        # Get Text HTML
        soup = CommonNaver.GetTextHTMLPARSER(item_url)
        
        for li in soup.find('ul', {'class':'type06_headline'}).findAll('li'):    
            
            # PresidentModel
            naver_ps = PresidentModel()
            
            for dt in li.findAll('dt'):
                try:
                    Dtclass = dt["class"]
                    title = str(Dtclass)
                
                except KeyError:
                    title = NaverResources.CONST_NAVER_LIST
                    
                if(title == NaverResources.CONST_NAVER_LIST):
                   
                    # index
                    naver_ps.SetIndex(index)
                    # Link Text
                    naver_ps.SetLink(CommonNaver.GetClassLink(dt))
                    # Title Text
                    naver_ps.SetTitle(CommonNaver.GetClassTitle(dt))
                    
                    
            dd = li.find('dd')
            
            naver_ps.SetWriter(CommonNaver.GetClassWriting(dd))
            naver_ps.SetDate(CommonNaver.GetClassDate(dd))
            
            # Index ++
            index = index + 1
            
            # List Add
            self.ListNaverPs.append(naver_ps)
            
        for li in soup.find('ul', {'class':'type06'}).findAll('li'):    
            
            # PresidentModel
            naver_ps = PresidentModel()
            
            for dt in li.findAll('dt'):
                try:
                    Dtclass = dt["class"]
                    title = str(Dtclass)
                
                except KeyError:
                    title = NaverResources.CONST_NAVER_LIST
                    
                if(title == NaverResources.CONST_NAVER_LIST):
                   
                    # index
                    naver_ps.SetIndex(index)
                    # Link Text
                    naver_ps.SetLink(CommonNaver.GetClassLink(dt))
                    # Title Text
                    naver_ps.SetTitle(CommonNaver.GetClassTitle(dt))
                    
                    
            dd = li.find('dd')
            
            naver_ps.SetWriter(CommonNaver.GetClassWriting(dd))
            naver_ps.SetDate(CommonNaver.GetClassDate(dd))
            
            # Index ++
            index = index + 1
            
            # List Add
            self.ListNaverPs.append(naver_ps)
            
        return self.ListNaverPs

        