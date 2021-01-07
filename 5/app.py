from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Post, setup_db


def create_app():
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, origins=["http://localhost:3000"])

    @app.route("/")
    def index():
        return "Hello world"

    @app.route("/posts")
    def get_posts():
        page = request.args.get('page', 1, type=int) 
        posts = Post.query.paginate(page, 5)

        total = posts.total
        posts = posts.items

        posts = [i.format() for i in posts]
        return jsonify(posts=posts, total=total)

    @app.errorhandler(405)
    def handle405(e):
        return jsonify(message="Method not allowed"), 405

    @app.errorhandler(404)
    def handle404(e):
        return jsonify(message="Page not found"), 404

    return app
