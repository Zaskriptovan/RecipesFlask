from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '123123123123123'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost/blog_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
