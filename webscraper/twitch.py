from webscraper.interface                                                                    import webscraper

class twitch(webscraper):
    def __init__(self,name):
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
            self.streamer.thumb = data['thumbnailUrl'][0]
        else:
            return 