import time

import mysql.connector as connector

class Database:

    #google
    # host = '127.0.0.1'
    # user = 'administrator'
    # password = '@123456'
    host = 'divar.cagmscbv5lcr.us-east-2.rds.amazonaws.com'
    user = 'admin'
    password = 'Vardast_db'
    db = 'Divar'


    def __init__(self):
        #google
        self.connection = connector.connect(host=self.host,port='3306',user=self.user, password=self.password, database=self.db,charset='utf8',autocommit=True)
        self.cursor = self.connection.cursor()


    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            count=self.cursor.rowcount
            return count
        except:
            self.connection.rollback()
            raise

    def insert_batch(self,query,values,mesg=''):
        try:
            self.cursor.executemany(query, values)
            self.connection.commit()
            count=self.cursor.rowcount
            return count
        except:
            raise
        finally:
            if (self.connection.is_connected()):
                self.connection.close()


    def query(self, query):
        self.cursor.execute(query)
        output=self.cursor.fetchall()
        return output

    def call_func(self,funct):

        self.cursor.execute('call '+funct)
        output=self.cursor.fetchall()
        if (self.connection.is_connected()):
            self.connection.close()
        return output

def get_items_buy(query):
    db = Database()
    query = """select

        JSON_ARRAYAGG(
            JSON_OBJECT(
				'published_date', published_date
                ,'rooms', rooms
                ,'vadie', vadie
                ,'elevator', elevator
                ,'size', size
                ,'parking', parking
                ,'description', description
                ,'phone', phone
                ,'create_year', create_year
                ,'url',url
                )
           )

 from home_tehran_buy where """+query
    return db.query(query)

def get_items_rent(query):
    db = Database()
    query = """select

            JSON_ARRAYAGG(
                JSON_OBJECT(
    				'published_date', published_date
                    ,'rooms', rooms
                    ,'vadie', vadie
                    ,'elevator', elevator
                    ,'size', size
                    ,'parking', parking
                    ,'description', description
                    ,'phone', phone
                    ,'create_year', create_year
                    ,'url',url
                    )
               )

     from home_tehran_rent where """ + query

    return db.query(query)