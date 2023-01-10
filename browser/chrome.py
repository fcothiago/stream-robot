from browser.interface import browser

class chrome(browser):
    def __init__(self,url):
        browser.__init__(self,url)
        self.cmd = f'chrome {self.url}'