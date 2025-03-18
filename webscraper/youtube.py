from webscraper.interface import webscraper
import json 

class youtube(webscraper):
    def __init__(self,name):
        self.__base_url__ = "https://www.youtube.com/@"
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
            try:
                self.streamer.onlive = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelFeaturedContentRenderer']['items'][0]['videoRenderer']['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['icon']['iconType'] == "LIVE"
                self.streamer.description = data["metadata"]["channelMetadataRenderer"]["description"]
                videoid = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelFeaturedContentRenderer']['items'][0]['videoRenderer']['videoId']
                self.live_url = f'{self.__base_url__}/watch?v={videoid}'
            except:
                self.streamer.onlive = False 
                self.streamer.description = "Offline"
        else:
            self.streamer.onlive = False 
            self.streamer.description = "Offline"
