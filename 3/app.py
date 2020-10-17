from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/saturday"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ =  "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    def __repr__(self):
        return f"{self.id}.{self.name}"

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    def __repr__(self):
        return f"{self.id}.{self.body}-{self.user_id}"


def register_user(name: str):
    new_user = User(name = name)
    db.session.add(new_user)
    db.session.commit()

def create_post(user_id: int, post_body: str):
    new_post = Post(body = post_body,  user_id = user_id)
    db.session.add(new_post)
    db.session.commit()


def get_user_by_id(id: int):
    return User.query.get(id)


def get_posts_by_user_id(id:int):
    return Post.query.filter(Post.user_id == id).all()
    

def get_posts_by_username(user_name: str):
    return db.session.query(User, Post).join(Post).filter(User.name == user_name).all()


def update_post(post_id: int, new_body: str):
    target_post  = Post.query.get(post_id)
    target_post.body = new_body
    db.session.add(target_post)
    db.session.commit()


def delete_post(post_id:int):
    new_post = Post.query.get(post_id)
    db.session.delete(new_post)
    db.session.commit()

# db.drop_all()
db.create_all()


















