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

If tou want to add a new Streamer or Youtuber, select the desired web site (youtube or twitch) in the choice menu and press the Add button. Infor the channel name of the streammer or youtuber. For instance, if you want to add the streamer wwww.twitch.tv/casimito, use casimito as a input. To delete a streamer, select the streamer in the list and press the del button.

When a new tab is opened, the bot stop to monitor that streamer. If a streamer is being monitored, it gonna be marked as "Monitoring" or "Stoped" cas not.


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

* **Streming Sites**: twitch,youtube
* **Browser** : firefox 

As said before, when a new tab is opened, the bot stop to monitor streamer's status. The following code shows a easy way to start or stop a streamer monitoring.

```python
index = streamers_channel_index
#if status is False, the bot is being monitored.
status = bot.tasks[index].flag
#Force start
bot.tasks[index].flag = False
#Force stop
bot.tasks[index].flag = True
```
