import os
from flask import Flask

vardastan_app = Flask(__name__)

@app.route('/region_list')
def get_regions_list():
    return ['\"تهران، اندیشه\",\"تهران، اندیشه\",\"تهران، آهنگ\",\"-1\",\"تهران، پیروزی\",\"تهران، جیحون\",\"تهران، شهریار\",\"تهران، شوش\",\"تهران، منیریه\",\"-1\",\"تهران، نارمک\",\"تهران، مجیدیه\",\"تهران، مهرآباد جنوبی\",\"تهران، تهران‌سر\",\"تهران، قصر\",\"تهران، جوادیه\",\"تهران، شهر ری\",\"تهران، پونک\",\"تهران، کوی فردوس\",\"تهران، اکباتان\",\"تهران، جیحون\",\"تهران، جنت‌آباد جنوبی\",\"تهران، تهرانپارس شرقی\",\"تهران، شمس‌آباد\",\"تهران، پردیس\",\"-1\",\"تهران، شهرک تختی\",\"-1\",\"-1\",\"تهران، خزانه\",\"تهران، شهران جنوبی\",\"تهران، استاد معین\",\"-1\",\"تهران، جیحون\",\"تهران، سلیمانیه\",\"تهران، کوی فردوس\",\"تهران، چیتگر\",\"تهران، شهریار\",\"تهران، رباط کریم\",\"تهرا']


@app.route('/region_ads')
def get_region_ads(region):
    return






