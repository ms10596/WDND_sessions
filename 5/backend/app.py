from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from data import Post, User, setup_db

def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app, origins="http://localhost:3000", methods=["GET"])

    @app.route("/")
    def index():
        return "Hello world"

    @app.route("/posts")
    def get_posts():
        posts = Post.query.all()
        posts = [post.format() for post in posts]
        return {
            "posts": posts
        }

    @app.route("/posts/<int:id>")
    def get_post_by_id(id: int):
        try:
            return Post.query.get(id).format()
        except:
            abort(404)

    @app.errorhandler(404)
    def not_found(e):
        return {
            "message": "not found",
            "status_code": 404
        }, 404



    return app