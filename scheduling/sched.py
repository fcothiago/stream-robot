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
        self.wait = 10
        self.tasks = []
        self.remove_task_list = []
        self.exit = Event()
        self.callback = lambda cb : ()
        for name, site, browser in configs:
            self.add(name, site, browser)

    def run(self):
        self.__runing__ = True
        with ThreadPoolExecutor(4) as executor:
            while(self.__runing__ == True):
                futures =  [executor.submit(t.start) for t in list(self.tasks)]
                for future in concurrent.futures.as_completed(futures):
                    pass
                self.callback()
                self.__clean_tasks__()
                self.exit.wait(self.wait)
            self.__clean_tasks__()
            self.__runing__ = False

    def stop(self):
        self.__runing__ = False
        self.exit.set()
            
    def add(self,name, site, browser,start=False):
        s = twitch(name) if site == 'twitch' else youtube(name) if site == "youtube" else None
        l = firefox() if browser == 'firefox' else None
        t = task(s,l)
        self.tasks.append(t)
        if start:
            t.start()

    def remove(self,name):
        self.remove_task_list += [name]

    def __clean_tasks__(self):
        names = [t.streamer.name for t in list(self.tasks)]
        for i,j in enumerate(names):
            print(j)
            if j in self.remove_task_list: 
                del self.tasks[i]
        self.remove_task_list = []

