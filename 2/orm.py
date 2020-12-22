from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from data import names, posts
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/saturday"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return f"<id:{self.id}, body:{self.body}>\n"

# db.drop_all()
db.create_all()

# CRUD
# CREATE READ UPDATE DELETE

def insert_user(name):
    user = User(name=name) 
    db.session.add(user) 
    db.session.commit() 


def insert_post(user_id, post_body):
    post = Post(body=post_body, user_id=user_id) 
    db.session.add(post) 
    db.session.commit() 


def get_posts_by_userid(user_id):
    res = Post.query.filter_by(user_id=user_id).all()
    return res


def update_post(post_id, new_post_body):
    post = Post.query.get(post_id) 
    post.body = new_post_body
    db.session.commit() 


def delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()

    # Post.query.filter_by(id=post_id).delete()
    # db.session.commit()


def get_posts_by_username(username):
    return db.session.query(User, Post).join(Post).filter(User.name==username).all()
