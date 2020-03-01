import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_regions_list():
    return ['شهید عراقی' ,'امیرآباد', 'گیشا']

