from threading import Thread

class task(Thread):
    flag = False
    def __init__(self,streamer,launcher):
        Thread.__init__(self)
        self.streamer = streamer
        self.launcher = launcher
    def run(self):
        if self.flag:
            return
        self.streamer.update()
        print(self.streamer.streamer.onlive,self.streamer.name)
        if(self.streamer.streamer.onlive):
            self.launcher.launch()
            self.flag = True
