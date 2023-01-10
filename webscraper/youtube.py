from webscraper.interface import webscraper
import json 

class youtube(webscraper):
    def __init__(self,name):
        self.__base_url__ = "https://www.youtube.com/"
        webscraper.__init__(self,name)

    def __check_infos__(self):
        tag = "script"
        fields = self.__html__.findAll(tag,{})
        field = None
        for i in fields:
            if i.text.startswith("var ytInitialData"):
                field = i
                break
        if field != None:
            index = field.text.find("{")
            data = field.text[index:-1]
            data = json.loads(data)
            self.streamer.onlive = "streams" in data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][3]["tabRenderer"]["endpoint"]["commandMetadata"]["webCommandMetadata"]["url"]
            self.streamer.description = data["metadata"]["channelMetadataRenderer"]["description"]
        else:
            self.streamer.onlive = False 
            self.streamer.description = "Offline"
            #self.streamer.thumb = ""