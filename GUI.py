import customtkinter as ctk

from scheduling.sched import sbot
from tkinter.simpledialog import askstring
from webscraper.twitch import twitch
from webscraper.youtube import youtube
from browser.firefox import firefox

class streamer_widget():
    def __init__(self,container,name,state):
        self.__frame__ = ctk.CTkFrame(container)
        self.__label_name__ = ctk.CTkLabel(self.__frame__, text=f"{name}", font=("Arial", 16),anchor="w")
        self.__label_state__ = ctk.CTkLabel(self.__frame__, text=f"{'onlive' if state else 'offline'}", font=("Arial", 16))
        self.__label_name__.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.__label_state__.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
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
        btn_area = ctk.CTkFrame(master)

        twitch_btn = ctk.CTkButton(btn_area,text="twitch",fg_color="#6441a5",command=lambda n: n)
        firefox_btn = ctk.CTkButton(btn_area,text="youtube",fg_color="#FF0000",command=lambda n: n)

        twitch_btn.pack(side="left")
        firefox_btn.pack(side="left")
        btn_area.pack()

        self.bot.callback = lambda: self.update()
        self.bot.start()

        """"
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
        """
    def getItem(self,task):
        pass
        """
        name = task.streamer.name
        onlive = "is On Live" if task.streamer.streamer.onlive else ""
        return f'{name} {onlive}
        """

    def update(self):
        for task in self.bot.tasks:
            name = task.streamer.name
            onlive = task.streamer.streamer.onlive
            self.streamers[name].update_state(onlive)
        """
        self.itensBox.delete(0, END)
        for t in self.bot.tasks:
            self.itensBox.insert(END,self.getItem(t))
        """

    def add_task(self):
        pass
        """
        name=askstring("Add Streamer","Streamer Name")
        if name != None:
            site = self.choice.get()
            self.bot.add(name,site,'firefox',True)
            self.data.append([name,site,'firefox'])
            self.itensBox.insert(END,self.getItem(self.bot.tasks[-1]))
        """
    
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
