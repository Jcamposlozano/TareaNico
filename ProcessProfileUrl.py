from urllib.request import Request, urlopen
from pyquery import PyQuery
from ConectPostgres import *

class ProcessProfileUrl:

    def __init__(self):
        self.__datos = []
        self.sql = None

    def profile_URL(self,url):
        try:
            req = Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            content = urlopen(req).read()    
            pq = PyQuery(content)
            return str(pq('div')('link').eq(1)).strip()[27:-3]
        
        except (Exception) as error:
            print(error)

    def obtienedata(self):
        c = ConectPostgres()
        datosServidor = c.descargaUrl()
        for i in datosServidor:
            print(i.getArticle_url())
            i.setProfile_url(self.profile_URL(i.getArticle_url()))
            i.setValidado('true')
            c.ejecutarConsulta(i)
            
