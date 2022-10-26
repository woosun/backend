from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})
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
    return result
#장고기준으로 서버실행해주는애
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)