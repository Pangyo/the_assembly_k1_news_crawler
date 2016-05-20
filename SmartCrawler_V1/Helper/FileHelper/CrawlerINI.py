'''
Created on 2016. 5. 18.

@author: yunjae
'''


import os
import configparser

from Common.Language import Resources

def WriteINI():
    if os.path.exists(Resources.CONST_INI_PATH) == False:
        
        config = configparser.ConfigParser()

        # Path
        config['PATH'] = {}
        CrawlerPath = config['PATH']
        CrawlerPath['Temp'] = './Temp'
        CrawlerPath['Log'] = './Operate.log'
        
        # Url
        config['URL'] = {}
        CrawlerUrl = config['URL']
        CrawlerUrl['POLITICS_PRESIDENT'] = 'None'
        CrawlerUrl['POLITICS_POLITICALPARTY'] = 'None'
        
        # Option
        config['OPTION'] = {}
        CrawlerOption = config['OPTION']
        CrawlerOption['Parser'] = 'html.parser'
        CrawlerOption['Port'] = '0'
        
        with open('Crawler.ini', 'w') as configfile:
            config.write(configfile)       
           
def ReadINI():
    if os.path.exists(Resources.CONST_INI_PATH) == True:
        config = configparser.ConfigParser()
        
        config.read('Crawler.ini')
        
        CrawlerPath = config['PATH']
        Resources.CONST_TEMP_PATH = CrawlerPath['Temp']
        Resources.CONST_LOG_PATH = CrawlerPath['Log']
    
        CrawlerPath = config['URL']
        Resources.CONST_NAVER_POLITICS_PRESIDENT_URL = CrawlerPath['POLITICS_PRESIDENT']
        Resources.CONST_NAVER_POLITICS_POLITICALPARTY_URL = CrawlerPath['POLITICS_POLITICALPARTY']
        
        CrawlerOption = config['OPTION']
        Resources.CONST_HTML_PARSER =  CrawlerOption['Parser']
        CrawlerOption['Port']
    
    
    
    
    