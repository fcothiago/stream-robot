from threading import Thread

class task():
    flag = False
    def __init__(self,streamer,launcher):
        self.streamer = streamer
        self.launcher = launcher
    def start(self):
        if self.flag:
            return
        self.streamer.update()
        if(self.streamer.streamer.onlive):
            self.launcher.launch()
            self.flag = True