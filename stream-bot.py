from tkinter import *
from GUI import GUI
from scheduling.sched import sbot
import os
import json

if __name__ == "__main__":
    print(os.path.dirname(__file__))
    file = open(f'{os.path.dirname(__file__)}/streamers.json',"r+")
    #Loading Streamers
    data = None
    try:
        data = json.load(file)["streamers"]
    except:
        data = {"streamers":[]}
    bot = sbot(data)
    #Starting GUI
    root = Tk()
    app = GUI(root,data,bot)
    root.wm_title("Stream-robot")
    root.geometry("360x360")
    root.mainloop()
    #Stoping Tasks
    bot.stop()
    #Saving all
    file.close()
    file = open("streamers.json","w")
    file.write(json.dumps({'streamers':data}))
    file.close()
