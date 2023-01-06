from tkinter import *
from scheduling.sched import sbot
import json

class GUI(Frame):
    def __init__(self,master,data,bot):
        Frame.__init__(self, master)
        self.master = master
        self.data = data
        self.bot = bot
        self.after(1000, self.update)
    def update(self):
        self.pack(fill=BOTH, expand=1)

        self.container = Frame(self,borderwidth=1,relief="sunken")
        self.container.place(relx=0.5, rely=0.05,relwidth=0.95,relheigh=0.8,anchor=N)

        for task in self.bot.tasks.values():
            item = Frame(self.container,borderwidth=1,relief="groove")
            item.pack(fill=X)
            Label(item,text=task.streamer.name).pack(side="left")
            Label(item,borderwidth=0,text="Online" if task.streamer.streamer.onlive else "Offline",relief="flat") .place(relx=0.5,rely=0.5,anchor=CENTER)
            Button(item, text="X").pack(side="right")
            if task.flag:
                Button(item, text="Stop").pack(side="right")
            else:
                Button(item, text="Start").pack(side="right")

        exitButton = Button(self, text="Add")
        exitButton.place(relx=0.5, rely=0.925,anchor=CENTER)


with open("streamers.json","r+") as file:
    #Loading Streamers
    data = None
    try:
        data = json.load(file)["streamers"]
    except:
        data = {"streamers":[]}
    print(data)
    bot = sbot(data)
    bot.start()
    #Starting GUI
    root = Tk()
    app = GUI(root,data,bot)
    root.wm_title("Stream-robot")
    root.geometry("320x320")
    root.mainloop()