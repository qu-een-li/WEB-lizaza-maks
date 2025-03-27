from flask import Flask
from config import KEY_CSRF
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY_CSRF

if __name__ == '__main__':
    db_session.global_init("db/reg_form.db")
    # init()
    app.run(port=8080, host='127.0.0.1')
