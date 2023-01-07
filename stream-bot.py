from tkinter import *
import tkinter.simpledialog
from scheduling.sched import sbot
from tkinter.simpledialog import askstring
import json

class GUI(Frame):
    def __init__(self,master,data,bot):
        Frame.__init__(self, master)
        self.bot = bot
        self.data = data
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.container = Frame(self,borderwidth=1,relief="sunken")
        self.container.place(relx=0.5, rely=0.05,relwidth=0.95,relheigh=0.8,anchor=N)
        self.widgets = dict()
        for task in list(bot.tasks.values()):
            self.drawitem(task)
        add = Button(self, text="Add",command=lambda:self.add_task())
        add.place(relx=0.5, rely=0.925,anchor=CENTER)
        self.update()
    def drawitem(self,task):
        item = Frame(self.container,borderwidth=1,relief="groove")
        item.pack(fill=X)
        name = Label(item,text=task.streamer.name)
        name.pack(side="left")
        status = Label(item,borderwidth=0,relief="flat") 
        status.place(relx=0.5,rely=0.5,anchor=CENTER)
        delete=Button(item,text='x',command=lambda name=task.streamer.name,item=item:self.remove(name,item))
        delete.pack(side="right")
        runing = Button(item)
        runing.pack(side="right")
        self.widgets[task.streamer.name] = (task,name,status,delete,runing)

    def update(self,recall=True):
        for task,name,status,delete,runing in list(self.widgets.values()):
            name.config(text=task.streamer.name)
            status.config(text="Online" if task.streamer.streamer.onlive else "Offline")
            if not task.flag:
                runing.config(text="Stop",width=5,command=lambda t=task,f=True: self.task_flag(t,f))
            else:
                runing.config(text="Start",width=5,command=lambda t=task,f=False: self.task_flag(t,f))
        if recall:
            self.after(100, self.update)
    def task_flag(self,task,flag):
        task.flag = flag
        self.update(False)
    def add_task(self):
        name=askstring("Add Streamer","Streamer Name")
        self.bot.add(name,'twitch','firefox',[   ])
        self.data.append([name,'twitch','firefox',[]])
        self.drawitem(self.bot.tasks[name])
    def remove(self,name,item):
        item.destroy()
        del self.widgets[name]
        del self.bot.tasks[name]
        del self.data[name]
        self.update(False)

if __name__ == "__main__":
    file = open("streamers.json","r+")
    #Loading Streamers
    data = None
    try:
        data = json.load(file)["streamers"]
    except:
        data = {"streamers":[]}
    bot = sbot(data)
    bot.start()
    #Starting GUI
    root = Tk()
    app = GUI(root,data,bot)
    root.wm_title("Stream-robot")
    root.geometry("320x320")
    root.minsize(320,320)
    root.mainloop()
    #Saving all
    file.close()
    file = open("streamers.json","w")
    file.write(json.dumps({'streamers':data}))
    file.close()