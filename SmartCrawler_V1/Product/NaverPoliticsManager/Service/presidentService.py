'''
Created on 2016. 5. 8.

Information : Naver President Service

@author: yunjae
'''

import requests

from bs4 import BeautifulSoup

from Common.Language import Resources
from Common.CommonClass.BaseClass import BaseClass

from Product.NaverPoliticsManager.Common import str_naver
from Product.NaverPoliticsManager.Model.presidentModel import presidentModel


class PresidentService(BaseClass):

    def __init__(self):
        self.ListNaverPs = []
    
    def GetTextHTMLPARSER(self, url):
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, Resources.CONST_HTML_PARSER)
        return soup
    
    def GetClassLink(self, dt):
        link =dt.find('a')['href']
        return str(link)
        
    def GetClassTitle(self, dt):
        title = dt.find('a')
        return title.string.strip()
    
    def GetClassWriting(self, dd):
        person_writing = dd.find('span' , {'class' : 'writing'})
        return person_writing.string
    
    def GetClassDate(self, dd):
        person_time = dd.find('span' , {'class' : 'date'})
        return person_time.string
    
    def GetPresidentList(self, item_url):
        index = 1;
    
        # Get Text HTML
        soup = self.GetTextHTMLPARSER(item_url)
        
        for li in soup.find('ul', {'class':'type06_headline'}).findAll('li'):    
            
            # PresidentModel
            naver_ps = presidentModel()
            
            for dt in li.findAll('dt'):
                try:
                    Dtclass = dt["class"]
                    title = str(Dtclass)
                
                except KeyError:
                    title = str_naver.CONST_NAVER_LIST
                    
                if(title == str_naver.CONST_NAVER_LIST):
                   
                    # index
                    naver_ps.setIndex(index)
                    # Link Text
                    naver_ps.setLink(self.GetClassLink(dt))
                    # Title Text
                    naver_ps.setTitle(self.GetClassTitle(dt))
                    
                    
            dd = li.find('dd')
            
            naver_ps.setWriter(self.GetClassWriting(dd))
            naver_ps.setDate(self.GetClassDate(dd))
            
            # Index ++
            index = index + 1
            
            # List Add
            self.ListNaverPs.append(naver_ps)
            
        return self.ListNaverPs

        