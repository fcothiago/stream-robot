from threading import Thread

class task():
    flag = False
    def __init__(self,streamer,launcher):
        self.streamer = streamer
        self.launcher = launcher
    def start(self):
        self.streamer.update()
        if self.streamer.streamer.onlive and not self.flag:
            self.launcher.url = self.streamer.live_url
            self.launcher.launch()
            self.flag = True
        elif not elf.streamer.streamer.onlive and self.flag:
            self.flag = False