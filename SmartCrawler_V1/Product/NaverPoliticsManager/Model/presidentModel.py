'''
Created on 2016. 5. 8.

Information : Naver President Class

@author: yunjae
'''

class presidentModel:
    
    def __init__(self):
        pass
    
    def setInit(self, index, link, title, writer, date):
        self.index = index
        self.link = link
        self.title = title
        self.writer = writer
        self.date = date
    
    def setIndex(self, index):
        self.index = index
    
    def setLink(self, link):
        self.link = link
    
    def setTitle(self, title):
        self.title = title
        
    def setWriter(self, writer):
        self.writer = writer
    
    def setDate(self, date):
        self.date = date
    