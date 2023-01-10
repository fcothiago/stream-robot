from tkinter import *
import tkinter.simpledialog
from scheduling.sched import sbot
from tkinter.simpledialog import askstring
from webscraper.twitch import twitch
from webscraper.youtube import youtube
from browser.firefox import firefox

class GUI(Frame):
    def __init__(self,master,data,bot):
        Frame.__init__(self, master)
        #Layout
        self.bot = bot
        self.data = data
        self.master = master
        self.pack(fill=BOTH, expand=1)

        container = Frame(self)
        container.pack(fill=X)
        
        #Buttons        
        self.add = Button(container, text="Add",command=lambda:self.add_task())
        self.add.pack(side="left")

        self.choice = StringVar()
        self.choice.set('twitch')

        self.menu = OptionMenu(container,self.choice,"twitch", "youtube")
        self.menu.pack(side="left")

        self.delete = Button(container, text="Del",command=lambda:self.del_task())
        self.delete.pack(side="right")
        
        #Streamers List
        self.itens = [self.getItem(t) for t in self.bot.tasks]
        self.listitens = tkinter.Variable(value=self.itens)
        self.itensBox = Listbox(self,listvariable=self.listitens)
        self.itensBox.pack(fill=BOTH, expand=True)
        self.bot.callback = lambda: self.update()
        self.bot.start()

    def getItem(self,task):
        name = task.streamer.name
        onlive = "On live " if task.streamer.streamer.onlive else ""

        status = "Monitoring" if not task.flag else "Stoped"
        return f'{onlive}{name} - {status}'

    def update(self):
        self.itensBox.delete(0, END)
        for t in self.bot.tasks:
            self.itensBox.insert(END,self.getItem(t))

    def add_task(self):
        name=askstring("Add Streamer","Streamer Name")
        if name != None:
            site = self.choice.get()
            self.bot.add(name,site,'firefox',True)
            self.data.append([name,site,'firefox'])
            self.itensBox.insert(END,self.getItem(self.bot.tasks[-1]))
    
    def del_task(self):
        index = self.itensBox.curselection()
        if(index != ()):
            index = index[0]
            self.itensBox.delete(index,END)
            del self.bot.tasks[index]
            del self.data[index]
