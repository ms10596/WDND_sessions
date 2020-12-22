from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/sunday"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    email = db.Column(db.String())
    posts = db.relationship("Post")

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    hashtags = db.relationship("Hashtag", secondary="PostHash")

    def __repr__(self):
        return f"<id:{self.id}, body:{self.body}>\n"

class Hashtag(db.Model):
    __tablename__ = "hashtags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    posts = db.relationship("Post", secondary="postHash")

class PostHash(db.Model):
    __tablename__ = "postHash"
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    hashtag_id = db.Column(db.Integer, db.ForeignKey("hashtags.id"), primary_key=True)


# db.drop_all()
db.create_all()

@app.route("/<name>")
def index(name):
    return f"<h1>Hello {name}</h1>"

@app.route("/")
def index1():
    name = request.args.get("name")
    return f"<h1>Hello {name}</h1>"

@app.route("/json", methods=["POST"])
def index2():
    body = request.get_json()
    name = body.get("name")
    return f"<h1>Hello {name}</h1>"

@app.route("/form", methods=["POST"])
def index3():
    name = request.form["name"]
    return f"<h1>Hello {name}</h1>"