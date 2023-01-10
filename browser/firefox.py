from browser.interface import browser

class firefox(browser):
    def __init__(self):
        browser.__init__(self)
    def getcmd(self):
        return f'firefox {self.url}'