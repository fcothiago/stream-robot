from threading import Thread
from scheduling.task import task
from browser.firefox import firefox
from webscraper.twitch import twitch
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
import concurrent.futures
import time

class sbot(Thread):
    def __init__(self,configs):
        Thread.__init__(self)
        self.__stop__ = False
        self.__runing__ = False
        self.wait = 120
        self.tasks = dict()
        for name, site, browser, ops in configs:
            self.add(name, site, browser, ops)

    def run(self):
        self.__runing__ = True
        with ThreadPoolExecutor(4) as executor:
            while(not self.__stop__):
                futures =  [executor.submit(t.start) for t in list(self.tasks.values())]
                for future in concurrent.futures.as_completed(futures):
                    pass
                time.sleep(self.wait)
            self.__runing__ = False
            self.__stop__ = True

    def stop(self):
        self.__stop__ = True
            
    def add(self,name, site, browser, ops):
        s = twitch(name) if site == 'twitch' else None
        l = firefox(s.url) if browser == 'firefox' else None
        self.tasks[name] = task(s,l)