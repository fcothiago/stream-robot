from scheduling.task import task
from browser.firefox import firefox
from webscraper.twitch import twitch
from webscraper.youtube import youtube
from threading import Thread
from threading import Event
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
import concurrent.futures
import time
import sys

class sbot(Thread):
    def __init__(self,configs):
        Thread.__init__(self)
        self.__stop__ = False
        self.__runing__ = False
        self.wait = 120
        self.tasks = []
        self.exit = Event()
        for name, site, browser in configs:
            self.add(name, site, browser)

    def run(self):
        self.__runing__ = True
        with ThreadPoolExecutor(4) as executor:
            while(self.__runing__ == True):
                futures =  [executor.submit(t.start) for t in list(self.tasks)]
                for future in concurrent.futures.as_completed(futures):
                    pass
                self.exit.wait(self.wait)
            self.__runing__ = False

    def stop(self):
        self.__runing__ = False
        self.exit.set()
            
    def add(self,name, site, browser,start=False):
        s = twitch(name) if site == 'twitch' else youtube(name) if site == "youtube" else None
        l = firefox(s.url) if browser == 'firefox' else None
        t = task(s,l)
        self.tasks.append(t)
        if start:
            t.start()