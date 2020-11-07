from flask import Flask, request
from flask_cors import CORS
from models import Post, setup_db

app = Flask(__name__)
setup_db(app)
CORS(app, origins="http://localhost:3000", methods=["GET"])


@app.route("/posts", methods=["GET"])
def get_posts():
    page_no = request.args.get("page", type=int)
    posts = Post.query.paginate(page_no, 5)
    total_no = posts.total
    posts = [post.format() for post in posts.items]
    return {
        "posts": posts,
        "total_no": total_no
    }


