import psycopg2
from Registro import *


class ConectPostgres:

    def __init__(self):
        self.database = 'db_brand_buzz'
        self.user = 'app_knime'
        self.password = 'knime2020#'
        self.host = '10.170.3.3'
        self.port = '5432'
        self.urls = []

    def descargaUrl(self):
        self.urls = []
        c = psycopg2.connect(database= self.database, user=self.user , password=self.password, host=self.host, port=self.port)
        try:
            with c.cursor() as cursor:
                sql = str("select " + 
                            "article_url " + 
                            ",brand " + 
                            ",validado " + 
                            "from br_tramiq.baseprofileurl " + 
                            "where validado = 'false' " + 
                            "and profile_url = '' " +
                            "and usuario = 'P1' "
                            "limit 1000")
                cursor.execute(sql)
                for (article_url,brand,validado) in cursor:
                    b = Registro()
                    b.setArticle_url(article_url)
                    b.setBrand(brand)
                    b.setValidado(validado)
                    self.urls.append(b)
                cursor.close()
                c.close()
            return self.urls
        finally:
            pass

    def ejecutarConsulta(self, sql):
        try:
            self.con = psycopg2.connect(database= self.database, user=self.user , password=self.password, host=self.host, port=self.port)
            self.cur = self.con.cursor()
            self.cur.execute(str(sql))
            #print(sql)
            self.con.commit()
            self.con.close()
        except (Exception, psycopg2.DatabaseError) as error:  
            controlarErr = str(error)         
            if controlarErr.find('(0x0000274C/10060)')>1 :
                print('Reintento de acceder')
                self.ejecutarConsulta(sql)
            else:   
                print(error) 
                print('*************************************')
                print(sql)
                print('*************************************')
               #sys.exit(1) 