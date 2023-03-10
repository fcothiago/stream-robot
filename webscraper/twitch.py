from webscraper.interface import webscraper
import json 

class twitch(webscraper):
    def __init__(self,name):
        self.__base_url__="https://www.twitch.tv/"
        webscraper.__init__(self,name)

    def __check_infos__(self):
        tag = "script"
        query = {"type":"application/ld+json"}
        field = self.__html__.find(tag,query)
        if field != None:
            data = field.text[1:-1]
            data = json.loads(data)
            self.streamer.onlive = data['publication']['isLiveBroadcast']
            self.streamer.description = data['description']
            #self.streamer.thumb = data['thumbnailUrl'][0]
        else:
            self.streamer.onlive = False 
            self.streamer.description = "Offline"
            #self.streamer.thumb = ""