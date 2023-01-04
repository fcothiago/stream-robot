from browser.interface import browser

class firefox(browser):
    def __init__(self,url):
        browser.__init__(self,url)
        self.cmd = f'firefox {self.url}'