# Stream-robot

A simple bot that checks if a streamer is on live and opens a new tab if it is. Working only for Twitch currently.

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




