import os

class browser:
    def __init__(self,url):
        self.url = url
    def launch(self):
        os.system(self.cmd)
