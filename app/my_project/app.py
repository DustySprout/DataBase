import os
from flask import Flask, current_app
from flask_mysqldb import MySQL
from company_inventory.route import *
app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'company_inventory'

app.config['MYSQL_SSL_DISABLED'] = True

app.mysql = mysql

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT 1")
    rv = cur.fetchall()
    if len(rv) > 0:
        return "Connection successful"
    else:
        return "Connection failed"

app.register_blueprint(accesspoints_bp)
app.register_blueprint(select_bp)

if __name__ == '__main__':
    app.run(debug=True)
