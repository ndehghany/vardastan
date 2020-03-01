import os
from flask import Flask
from mysql_helper import get_items_deleted_time
app = Flask(__name__)

@app.route('/')
def show_regions_list():
    result = get_items_deleted_time(0)
    return str(result[0])
    # return ' '.join(['شهید عراقی' ,'امیرآباد', 'گیشا'])




