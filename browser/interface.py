import os

class browser:
    def __init__(self):
        self.url = ""
    def launch(self):
        os.system(self.getcmd())
