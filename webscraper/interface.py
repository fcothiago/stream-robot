import urllib3
import datetime
import json 
from bs4 import BeautifulSoup

class streamer_infos:
    def __init__(self):
        self.onlive = False
        self.description = ""
        self.lastupdate = None
        #self.thumb = ""

class webscraper:
    __PM__ = urllib3.PoolManager()

    def __init__(self,name):
        self.__html__ = ""
        self.streamer = streamer_infos()
        self.name = name
        self.channel_url = f'{self.__base_url__}{self.name}'
        self.live_url = f'{self.__base_url__}{self.name}'
    def update(self):
        res = self.__PM__.request('GET',self.channel_url)
        if(res.status != 200):
            raise Exception(f'Failed to open {self.url}')
        self.__html__ = BeautifulSoup(res.data.decode('utf-8'), 'html.parser')
        self.streamer.lastupdate = datetime.datetime.now()
        self.__check_infos__()