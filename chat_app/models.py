from chat_app import db
import datetime as datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return f'User {self.id}'

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    def __repr__(self):
        return f'(' + {self.title} + ', ' + {self.content} + ')'