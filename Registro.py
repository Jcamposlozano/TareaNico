

class Registro:

    def __init__(self):
        self.__article_url = None
        self.__brand = None
        self.__validado = None
        self.__profile_url = None

    def getArticle_url(self):
        return self.__article_url
    
    def getBrand(self):
        return self.__brand
    
    def getValidado(self):
        return self.__validado
    
    def getProfile_url(self):
        return  self.__profile_url

    def setArticle_url(self, dato : str):
        self.__article_url = dato

    def setBrand(self, dato : str):
        self.__brand = dato

    def setValidado(self, dato : str):
        self.__validado = dato

    def setProfile_url(self, dato : str):
        self.__profile_url = dato

    def __str__(self):
        return str("UPDATE br_tramiq.baseprofileurl SET " +
                    " brand = '" + str(self.__brand) + 
                    "', validado = '" + str(self.__validado) +
                    "', profile_url = '" + str(self.__profile_url) +
                    "' where article_url = '" + str(self.__article_url) + "';")