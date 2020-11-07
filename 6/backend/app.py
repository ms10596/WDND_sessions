from flask import Flask, request
from models import Post, setup_db



def create_app():
    app = Flask(__name__)
    setup_db(app)

    @app.route("/posts", methods=["GET"])
    def get_posts():
        page = request.args.get("page", type=int)

        posts = Post.query.paginate(page, 10)
        total = posts.total
        posts = [post.format() for post in posts.items]

        return {
            "posts": posts,
            "total": total
        }

    return app


