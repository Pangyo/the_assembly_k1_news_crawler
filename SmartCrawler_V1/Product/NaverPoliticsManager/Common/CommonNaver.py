'''
Created on 2016. 5. 17.

@author: yunjae
'''
import requests
from bs4 import BeautifulSoup
from Common.Language import Resources

def GetTextHTMLPARSER(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, Resources.CONST_HTML_PARSER)
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
    #aa = 'empty'
    #return aa