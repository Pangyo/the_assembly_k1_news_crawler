'''
Created on 2016. 5. 17.

@author: yunjae
'''

class PoliticalPartyModel:
    
    def SetIndex(self, index):
        self.index = index
    
    def SetLink(self, link):
        self.link = link
    
    def SetTitle(self, title):
        self.title = title
        
    def SetWriter(self, writer):
        self.writer = writer
    
    def SetDate(self, date):
        self.date = date
    
    def GetIndex(self, index):
        return self.index
    
    def GetLink(self, link):
        return self.link
    
    def GetTitle(self, title):
        return self.title
        
    def GetWriter(self):
        return self.writer
    
    def GetDate(self):
        return self.date
          
    # Constructor
    def __init__(self):
        pass