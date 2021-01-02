from flask import Flask, request, jsonify
from models import Post, setup_db
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    cors = CORS(app, origins=["http://localhost:3000"])
    setup_db(app)

    @app.route("/")
    def index():
        return "Hello world"


    @app.route("/posts")
    def list_posts():
        result_per_page = 5
        page = request.args.get("page", 1 ,type=int)
        posts = Post.query.paginate(page, result_per_page)

        total = posts.total      
        posts = [i.format() for i in posts.items]

        return jsonify({
            "posts": posts,
            "total": total
        }), 200



    @app.errorhandler(404)
    def handle404(e):
        return jsonify(message="404 not found", another_msg="it's not found"), 404

    return app

