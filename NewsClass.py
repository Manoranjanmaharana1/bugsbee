class News :
    def __init__(self, headline, shortDetails, imgURL, timestamp, sourceURL, sourceName) :
        self.__headline = headline
        self.__shortDetails = shortDetails
        self.__imgURL = imgURL
        self.__timestamp = timestamp
        self.__sourceURL = sourceURL
        self.__sourceName = sourceName
    
    def getHeadline(self) :
        return self.__headline
    
    def getshortDetails(self) :
        return self.__shortDetails
    
    def getimgURL(self) :
        return self.__imgURL
    
    def gettimestamp(self) :
        return self.__timestamp
    
    def getsourceURL(self) :
        return self.__sourceURL
    
    def getsourceName(self) :
        return self.__sourceName
    