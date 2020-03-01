import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_regions_list():
    return ' '.join(['شهید عراقی' ,'امیرآباد', 'گیشا'])

