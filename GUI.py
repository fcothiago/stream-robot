import customtkinter as ctk

from scheduling.sched import sbot
from tkinter.simpledialog import askstring
from webscraper.twitch import twitch
from webscraper.youtube import youtube
from browser.firefox import firefox

class streamer_widget():
    def __init__(self,container,name,state):
        self.__name__ = name
        self.__frame__ = ctk.CTkFrame(container)
        self.__label_name__ = ctk.CTkLabel(self.__frame__, text=f"{name}", font=("Arial", 16),anchor="w")
        self.__label_state__ = ctk.CTkLabel(self.__frame__, text=f"{'onlive' if state else 'offline'}", font=("Arial", 16))
        self.__del_button__ = ctk.CTkButton(self.__frame__,text="del",fg_color="#FF0000",width=16,command=lambda : self.__delete__(container))
 
        self.__label_name__.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.__label_state__.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.__del_button__.grid(row=0, column=2)

        self.__frame__.grid_columnconfigure(0, weight=1)
        self.__frame__.pack(fill=ctk.X)

        self.__frame__.configure(fg_color=f"{'green' if state else 'gray'}")
        self.__label_name__.configure(text_color=f"{'white' if state else 'black'}")
        self.__label_state__.configure(text_color=f"{'white' if state else 'black'}")


    def update_state(self,state):
        self.__label_state__.configure(text=f"{'onlive' if state else 'offline'}")
        self.__frame__.configure(fg_color=f"{'green' if state else 'gray'}")
        self.__label_name__.configure(text_color=f"{'white' if state else 'black'}")
        self.__label_state__.configure(text_color=f"{'white' if state else 'black'}")

    def __delete__(self,gui):
        del gui.streamers[self.__name__]
        for i,j in enumerate(gui.data):
            if j[0] == self.__name__
                break
        del gui.data[i]
        self.__frame__.destroy()

class GUI(ctk.CTkFrame):
    def __init__(self,master,data,bot):
        ctk.CTkFrame.__init__(self, master)
        #Layout
        self.bot = bot
        self.data = data
        self.master = master
        #self.itens = [self.getItem(t) for t in self.bot.tasks]

        """ Adding Widgets """
        self.pack(fill=ctk.BOTH, expand=1)
        self.streamers = dict()
        
        for task in self.bot.tasks:
            name = task.streamer.name
            onlive = task.streamer.streamer.onlive
            swidget = streamer_widget(self,name,onlive)
            self.streamers[name] = swidget

        """ Add Buttons """ 
        self.btn_area = ctk.CTkFrame(master) 

        self.twitch_btn = ctk.CTkButton(self.btn_area,text="twitch",fg_color="#6441a5",command=lambda : self.add_streamer("twitch"))
        self.firefox_btn = ctk.CTkButton(self.btn_area,text="youtube",fg_color="#FF0000",command=lambda : self.add_streamer("youtube"))
        self.streamer_entry = ctk.CTkEntry(self.btn_area,placeholder_text="Add Streamer User")

        self.twitch_btn.grid(row=0,column=2)
        self.firefox_btn.grid(row=0,column=1)
        self.streamer_entry.grid(row=0,column=0,stick="nswe")
        
        self.btn_area.grid_columnconfigure(0, weight=1)
        self.btn_area.pack(fill=ctk.X)

        self.bot.callback = lambda: self.update()
        self.bot.start()

    def getItem(self,task):
        pass

    def update(self):
        for task in self.bot.tasks:
            name = task.streamer.name
            onlive = task.streamer.streamer.onlive
            self.streamers[name].update_state(onlive)

    def add_streamer(self,plataform):
        name = self.streamer_entry.get()
        if not name or name in self.streamers:
            return
        self.bot.add(name,plataform,'firefox',True)
        swidget = streamer_widget(self,name,False)
        self.streamers[name] = swidget
        self.data.append([name,plataform,'firefox'])
        self.streamer_entry.delete(0, "end")
    
    def del_task(self):
        pass
        """
        index = self.itensBox.curselection()
        if(index != ()):
            index = index[0]
            self.itensBox.delete(index)
            del self.bot.tasks[index]
            del self.data[index]
        """
