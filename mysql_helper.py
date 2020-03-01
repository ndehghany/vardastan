import time

import mysql.connector as connector

class Database:

    #google
    # host = '127.0.0.1'
    # user = 'administrator'
    # password = '@123456'
    host = 'divar.cagmscbv5lcr.us-east-2.rds.amazonaws.com'
    user = 'admin'
    password = 'o915517979O'
    db = 'Divar'
    # connector.connect(host='127.0.0.1', port='3307', user='root', password='@123456', database='Divar')
    def __init__(self):
        #google
        self.connection = connector.connect(host=self.host,port='3306',user=self.user, password=self.password, database=self.db,charset='utf8',autocommit=True)
        # self.connection = connector.connect('127.0.0.1:3307', 'administrator', '@123456', 'Divar',charset='utf8', init_command='SET NAMES UTF8')
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
            # self.cursor.close()
            # self.connection.rollback()
            raise
            # print('sleep for deadlock...'+mesg)
            # time.sleep(random.randint(60,120))
            # db = Database()
            # print('insert again')
            # db.insert_batch(query, values)
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

    # def __del__(self):
    #     self.connection.close()
def add_items(values=[]):
    db = Database()
    query = "INSERT IGNORE INTO `divar_items`(`url`, `type`, `city_id`, `date`, `phone`) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE phone=phone"
    return db.insert_batch(query,values)

def add_phonenNmbers(phones=[]):
    db = Database()
    query = "UPDATE divar_results SET `phone`=%s,`status` =-1 WHERE `id` = %s"
    return db.insert_batch(query, phones)

def add_items_dict(items=[]):
    db = Database()
    query = "INSERT INTO `Divar`.`divar_results` (`title`,`image`,`description`,`has_chat`,`red_text`,`normal_text`,`token`,`city`,`district`,`category`,`adv_type`,`crawl_time`,`url`,`published_date`) VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE url=url"
    return db.insert_batch(query,items)

def get_items(worker_id):
    db = Database()
    items=db.call_func('get_items_3({});'.format(worker_id))
    return items

def get_items_without_phones(worker_id):
    db = Database()
    items=db.call_func('get_items_phones({});'.format(worker_id))
    return items

def get_items_dict(worker_id):
    db = Database()
    items=db.call_func('get_items({});'.format(worker_id))
    return items

def get_items_deleted_time(offset):
    db = Database()
    items=db.call_func('get_items_deleted_time({});'.format(offset))
    return items

def update_items(values):
    db = Database()
    query="UPDATE divar_items SET `new` =1 WHERE `id` = %s"
    return db.insert_batch(query,values)

def update_items_dict(values):
    db = Database()
    query="UPDATE divar_results SET `status` =1 WHERE `id` = %s"
    return db.insert_batch(query,values)
def update_last_access_time(values):
    db = Database()
    query="UPDATE divar_results SET `last_access_time` =Now() WHERE `id` = %s"
    return db.insert_batch(query,values)


def ignore_items(values):
    db = Database()
    query="UPDATE divar_items SET `new` =0 WHERE `id` = %s"
    return db.insert_batch(query,values,'ignoreeeee')

def insert_full_items_dict(city,type,values):
    db = Database()
    pre_query='INSERT IGNORE INTO home_'+city+'_'+type
    query = pre_query + " (`items_id`, `published_date`, `rooms`, `crawl_time`, `vadie`, `elevator`, `size`, `parking`, `description`, `rent`, `images`, `location`, `adv_type`, `floor`, `phone`, `adv_source`, `create_year`, `daste_bandi`, `url`,`orginal_published_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE `url`=`url`"
    total =db.insert_batch(query, values)

    db = Database()
    query = "UPDATE divar_results SET `status` =0 WHERE `id` = %s"
    total_id=[]
    for item in values:
        total_id.append((item[0],))
    db.insert_batch(query, total_id, 'ignor22222')
    return total
def update_items_deleted(values):

    db = Database()
    query = "UPDATE divar_results SET `deleted_time`=%s WHERE `id` = %s"
    total=db.insert_batch(query, values, 'ignor22222')
    return total


def insert_full_items(city,type,values):
    db = Database()
    pre_query='INSERT IGNORE INTO home_'+city+'_'+type
    query = pre_query + " (`items_id`, `published_date`, `rooms`, `crawl_time`, `vadie`, `elevator`, `size`, `parking`, `description`, `rent`, `images`, `location`, `adv_type`, `floor`, `phone`, `adv_source`, `create_year`, `daste_bandi`, `url`,`orginal_published_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE `url`=`url`"
    total =db.insert_batch(query, values)

    db = Database()
    query = "UPDATE divar_items SET `new` =0 WHERE `id` = %s"
    total_id=[]
    for item in values:
        total_id.append((item[0],))
    db.insert_batch(query, total_id, 'ignor22222')
    return total