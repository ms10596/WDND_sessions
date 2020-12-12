from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data import posts, names
import random

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/saturday"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return f"<id: {self.id}, body: {self.body}, user_id: {self.user_id}"

db.create_all()

# CRUD

def insert_user(user_name):
    new_user = User(name=user_name)
    db.session.add(new_user) 
    db.session.commit()


def insert_post(user_id, post_body):
    new_post = Post(user_id=user_id, body=post_body)
    db.session.add(new_post)
    db.session.commit()


def get_posts_by_user(user_id):
    return db.session.query(Post).filter_by(user_id=user_id).all() 
    # return Post.query.filter_by(user_id=user_id)

def get_posts_by_username(username):
    return db.session.query(User, Post).join(Post).filter(User.name == username).all()

def delete_post(post_id):
    new_post = Post.query.get(post_id)
    db.session.delete(new_post)
    db.session.commit()
    # Post.query.filter(User.user_id==user_id, Post.id == post_id).delete()


def update_post(post_id, new_post_body):
    new_post = Post.query.get(post_id)
    new_post.body = new_post_body
    db.session.add(new_post)
    db.session.commit()





