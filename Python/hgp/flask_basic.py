# cmd에서 pip install flask

from flask import Flask
app = Flask(__name__)

# 데코레이터
@app.route("/")

def hello():
    return "<h1>Hello world!<h1/>"

# 실행은
# set FLASK_APP=파일명.py
# flask run