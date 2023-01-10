from tkinter import *
from GUI import GUI
from scheduling.sched import sbot
import json

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
    root.geometry("360x360")
    root.mainloop()
    #Stoping Tasks
    bot.stop()
    #Saving all
    file.close()
    file = open("streamers.json","w")
    file.write(json.dumps({'streamers':data}))
    file.close()