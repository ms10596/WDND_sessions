from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/sunday"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    db.app = app
    db.init_app(app)
    db.create_all()



class User(db.Model):
    __tablename__ =  "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    posts = db.relationship("Post")
    def __repr__(self):
        return f"{self.id}.{self.name}"

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    created_at = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "body": self.body,
            "user_id": self.user_id
        }
    

