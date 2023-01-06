import urllib3
import datetime
import json 
from bs4 import BeautifulSoup

class streamer_infos:
    def __init__(self):
        self.onlive = False
        self.description = ""
        self.lastupdate = None
        self.thumb = ""

class webscraper:
    __base_url__ = "https://www.twitch.tv/"
    __html__ = ""
    __PM__ = urllib3.PoolManager()
    streamer = streamer_infos()

    def __init__(self,name):
        self.name = name
        self.url = f'{self.__base_url__}{self.name}'
    def update(self):
        res = self.__PM__.request('GET',self.url)
        if(res.status != 200):
            raise Exception(f'Failed to open {self.url}')
        self.__html__ = BeautifulSoup(res.data.decode('utf-8'), 'html.parser')
        self.streamer.lastupdate = datetime.datetime.now()
        self.__check_infos__()