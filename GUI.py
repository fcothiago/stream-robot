from tkinter import *
import tkinter.simpledialog
from scheduling.sched import sbot
from tkinter.simpledialog import askstring

class GUI(Frame):
    def __init__(self,master,data,bot):
        Frame.__init__(self, master)
        self.bot = bot
        self.data = data
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        self.canvas = Canvas(self)
        self.canvas.place(relwidth=1,relheigh=0.8)
        self.scroll_bar = Scrollbar(self,orient=VERTICAL, command=self.canvas.yview)
        self.scroll_bar.pack(fill=Y, side="right")
        self.canvas.config(yscrollcommand = self.scroll_bar.set)
        self.canvas.bind('<Configure>',lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.itensFrame = Frame(self.canvas)
        self.widgets = dict()
        for task in list(bot.tasks.values()):
            self.drawitem(task)
        self.canvas.create_window((0,0),width=440,window=self.itensFrame,anchor="ne")
        add = Button(self, text="Add",command=lambda:self.add_task())
        add.place(relx=0.5, rely=0.925,anchor=CENTER)
        
        self.update_event()

    def drawitem(self,task):
        item = Frame(self.itensFrame,borderwidth=1,relief="groove")
        item.pack(fill=X)
        name = Label(item,text=task.streamer.name)
        name.pack(side="left")
        status = Label(item,borderwidth=0,relief="flat") 
        status.place(relx=0.5,rely=0.5,anchor=CENTER)
        delete=Button(item,text='x',command=lambda name=task.streamer.name,item=item:self.remove(name,item))
        delete.pack(side="right")
        runing = Button(item)
        runing.pack(side="right")
        name.config(text=task.streamer.name)
        status.config(text="Online" if task.streamer.streamer.onlive else "Offline")
        if not task.flag:
            runing.config(text="Stop",width=5,command=lambda t=task,f=True: self.task_flag(t,f))
        else:
            runing.config(text="Start",width=5,command=lambda t=task,f=False: self.task_flag(t,f))
        self.widgets[task.streamer.name] = (task,name,status,delete,runing)

    def update(self):
        for task,name,status,delete,runing in list(self.widgets.values()):
            name.config(text=task.streamer.name)
            status.config(text="Online" if task.streamer.streamer.onlive else "Offline")
            if not task.flag:
                runing.config(text="Stop",width=5,command=lambda t=task,f=True: self.task_flag(t,f))
            else:
                runing.config(text="Start",width=5,command=lambda t=task,f=False: self.task_flag(t,f))

    def update_event(self):
        self.update()
        self.after(self.bot.wait, self.update_event)
        
    def task_flag(self,task,flag):
        task.flag = flag
        self.update()

    def add_task(self):
        name=askstring("Add Streamer","Streamer Name")
        self.bot.add(name,'twitch','firefox')
        self.data.append([name,'twitch','firefox'])
        self.drawitem(self.bot.tasks[name])

    def remove(self,name,item):
        item.destroy()
        del self.widgets[name]
        del self.bot.tasks[name]
        for i in self.data:
            if i[0] == name:
                self.data.remove(i)
                break
        self.update()

    def update_size(self,e=None):
        self.canvas["scrollregion"] = self.canvas.bbox("all")