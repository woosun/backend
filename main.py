from flask import Flask
from flask_cors import CORS
import pymysql
import os

host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
user = os.environ['DB_USER']
passwd = os.environ['MYSQL_ROOT_PASSWORD']
db = os.environ['DB_DBNAME']
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

#장고기준으로 함수
@app.route("/")
def main():
    return "Hello World!"
#장고기준으로 url


@app.route("/hello")
def hello():
    result = { "code":200 ,"message": db_connector()}
    return result
def db_connector():
    cursor = conn.cursor()
    sql = "SELECT * FROM student;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


#장고기준으로 서버실행해주는애
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)