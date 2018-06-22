from flask import Flask
from flask import jsonify
import MySQLdb

app = Flask(__name__)

def connection():
    conn = MySQLdb.connect(host="192.168.21.57",
                           user = "bootcamp",
                           passwd = "bootcamp!",
                           db = "employees")
    c = conn.cursor()
    return c, conn


