from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/saturday"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    db.create_all()



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

    def __repr__(self):
        return f"<id:{self.id}, body:{self.body}>\n"

    def format(self):
        return {
            "id": self.id,
            "body": self.body,
            "user_id": self.user_id
        }


# db.drop_all()
# db.create_all()