'''
Created on 2016. 5. 14.

@author: yunjae
'''

from Helper.LogHelper import LOG

from Common.CommonClass.BaseClass import BaseClass
from Common.Language import Resources
from Helper.FileHelper import CrawlerINI

from Product.NaverPoliticsManager.Service.PresidentService import PresidentService


class ShellMain(BaseClass):
    
    def __init__(self):
        self._president = None

    def Pre_Initialize(self):
        
        LOG.DEBUG("Pre-initialize.")
        # Pre-initialize.
        # 1. Crawler .iniFile Write, if not exist file.
        # 2. Crawler .iniFile Read, if exist file.
        # 3. All Service Instances Init.
        # .....
        # 4. Main Call
        # .....
        
        
        LOG.DEBUG("Crawler INI Write.")
        CrawlerINI.WriteINI()
        
        LOG.DEBUG("Crawler INI Read.")
        CrawlerINI.ReadINI()
        
        LOG.DEBUG("Service Init.")
        self._president = PresidentService()
    
    def Startup(self):
        
        self.Pre_Initialize()
        
        #for ps in self._president.GetPresidentList(Resources.CONST_NAVER_POLITICS_PRESIDENT_URL):
        #    print(ps.index)
        #    print(ps.link)
        #    print(ps.title)
        #    print(ps.writer)
        #    print(ps.date)

if __name__ == '__main__':
    
    sm = ShellMain()
    sm.Startup()
    
    
    
    