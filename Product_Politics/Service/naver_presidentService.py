'''
Created on 2016. 5. 8.

Information : Naver President Service

@author: yunjae
'''

import requests

from bs4 import BeautifulSoup

from Common import str_resources
from Common import str_naver

from Product_Politics.Model import naver_presidentModel

ListNaverPs = []

def GetPresidentList(item_url):
    index = 1;
    
    # Get Text HTML
    soup = GetTextHTMLPARSER(item_url)
    
    for li in soup.find('ul', {'class':'type06_headline'}).findAll('li'):    
        naver_ps = naver_presidentModel.president()
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
                naver_ps.setLink(GetClassLink(dt))
                # Title Text
                naver_ps.setTitle(GetClassTitle(dt))
                
                
        dd = li.find('dd')
        
        naver_ps.setWriter(GetClassWriting(dd))
        naver_ps.setDate(GetClassDate(dd))
        
        # Index ++
        index = index + 1
        
        # List Add
        ListNaverPs.append(naver_ps)
        
    return ListNaverPs

def GetTextHTMLPARSER(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, str_resources.CONST_HTML_PARSER)
    return soup

def GetClassLink(dt):
    link =dt.find('a')['href']
    return str(link)
    
def GetClassTitle(dt):
    title = dt.find('a')
    return title.string.strip()

def GetClassWriting(dd):
    person_writing = dd.find('span' , {'class' : 'writing'})
    return person_writing.string

def GetClassDate(dd):
    person_time = dd.find('span' , {'class' : 'date'})
    return person_time.string
    