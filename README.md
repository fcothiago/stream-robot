# Stream-robot

A simple bot that checks if a streamer is on live and opens a new tab if it is. Working only for Twitch and Firefox currently.

## Install

To use the bot, you need Python 3. You may also need to install pip3. Check if Python 3 and pip3 is already installed in your computer.

```
python3 --version
pip3 --version
```

The bot use BeautifulSoup libraly to parse HTML and extract streamer's lives  infos. Install BeautifulSoup using pip3.

```
pip3 install beautifulsoup4
```

To use the GUI, you also need to install Tkinter in your computer.

```
sudo apt-get install python-tk
```

## Using the GUI

To run stream-robot GUI, run stream-bot.py file.

```
python3 stream-bot.py
```

### GUI basic usage

The window have a add button and a list where each item have two labels, representing a channel name and its status, and two buttons. The button actions os listed below.

* **Add Button**: Use it to add a new stremaer to the list. You ganna need to infor the streamer channel name. For instance, to add the streamer https://www.twitch.tv/casimito to the list, you only need to pass casimito.
* **X**: Use it to remove a stremer from the list.
* **Start/Stop Button**: When a new tab is opened for a streamer, the bot stop to monitor that streamer to avoid redundant tabs. You can make the bot start or stop monitoring the streaming using this button.

## Using sbot class.

You can use stream-robot without the GUI using the sbot class. You only need to make a new instance of sbot passing a list of itens with the streamer channel name, the streaming service site and the browser that will open the live.

```python
from scheduling.sched import sbot

#The Stremers List.
streamers = [['casimito','twitch','firefox'],['alanzoka','twitch','firefox']]
#Creating the bot
bot = sbot(streamers)
#bot.wait defines the period in seconds when the bot check streamers status. 
#Default value is 120s(2 minutes)
bot.wait = 120
#Starting the bot thread.
bot.start()
#looping
while True:
    #...Some stoping condition...
#Stoping the bot
bot.stop()
```

If you want to add a new streamer after the bot is created, user bot.add function.

```python
bot.add("stramer name","streaming site","browser")
```

The currently valid values is listed below.

* **Streming Sites**: twitch
* **Browser** : firefox 

As said before, when a new tab is opened, the bot stop to monitor streamer's status. The following code shows a easy way to start or stop a streamer monitoring.

```python
name = "Streamer's channel name"
#if status is False, the bot is being monitored.
status = bot.tasks[name].flag
#Force start
bot.tasks[name].flag = False
#Force stop
bot.tasks[name].flag = True
```
