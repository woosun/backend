from flask import Flask
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

host="svc-mysql"
port=3306
user="root"
passwd="qwer1234"
db="yoskr_db"
#장고기준으로 함수
@app.route("/")
def main():
    return "Hello World!"
#장고기준으로 url
@app.route("/hello")
def hello():
    result = {
        "code":200,
        "message":"hello Flask"
    } #json 형태로 반환되는형태
    return result\

@app.route("/db")
def db():
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM student;"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

#장고기준으로 서버실행해주는애
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)