import time

import mysql.connector as connector

class Database:

    host = 'divar.cagmscbv5lcr.us-east-2.rds.amazonaws.com'
    user = 'admin'
    password = 'Vardast_db'
    db = 'Today'


    def __init__(self,dictionary=False):
        #google
        self.connection = connector.connect(host=self.host,port='3306',user=self.user, password=self.password, database=self.db,charset='utf8',autocommit=True)
        self.cursor = self.connection.cursor(dictionary=dictionary)

    def query(self, query):
        self.cursor.execute(query)
        output=self.cursor.fetchall()
        return output

    def call_func(self,funct,args=tuple()):
        try:
            self.cursor.callproc(funct,args)
            for result in self.cursor.stored_results():
                return result.fetchall()
        except:
            raise
        finally:
            if (self.connection.is_connected()):
                self.connection.close()

    def call_func_simple(self,funct):
        try:
            self.cursor.execute('call {}'.format(funct))
            return self.cursor.fetchall()
        except:
            raise
        finally:
            if (self.connection.is_connected()):
                self.connection.close()

def get_items(query_id,last_timestamp):
    db = Database(dictionary=True)
    return db.call_func_simple('get_items ({},{})'.format(query_id,last_timestamp))


def add_query(input_query,sql_query):
    db = Database()
    return db.call_func('add_query',(input_query,sql_query))[0]

def get_queries():
    db = Database(dictionary=True)
    return db.call_func_simple('get_queries()')

def del_query(query_id):
    db = Database()
    return db.call_func('del_query',(query_id,))[0]
