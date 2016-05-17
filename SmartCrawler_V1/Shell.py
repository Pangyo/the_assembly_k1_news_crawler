'''
Created on 2016. 5. 14.

@author: yunjae
'''

from Helper.LogHelper import LOG

from Common.CommonClass.BaseClass import BaseClass

from Product.NaverPoliticsManager.Common import str_naver
from Product.NaverPoliticsManager.Service.presidentService import PresidentService


class ShellMain(BaseClass):
    
    def __init__(self):
        self._president = None

    def Pre_Initialize(self):
        LOG.DEBUG("Pre-initialize.")
        self._president = PresidentService()
    
    def Startup(self):
        self.Pre_Initialize()
        
        for ps in self._president.GetPresidentList(str_naver.CONST_NAVER_POLITICS_URL):
            print(ps.index)
            print(ps.link)
            print(ps.title)
            print(ps.writer)
            print(ps.date)
    
        

if __name__ == '__main__':
    
    sm = ShellMain()
    sm.Startup()
    
    
    
    