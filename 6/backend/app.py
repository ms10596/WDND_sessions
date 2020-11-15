from flask import Flask, request
from models import Post, setup_db

POSTS_PER_PAGE = 10

def create_app():
    app = Flask(__name__)
    setup_db(app)

    @app.route("/posts")
    def get_posts():
        page = request.args.get("page", type=int)
        posts = Post.query.paginate(page, POSTS_PER_PAGE)
        return {
            "posts": [post.format() for post in posts.items]
        }
    
    @app.route("/posts/<int:id>")
    def get_post_by_id(id):
        post = Post.query.get(id)
        if post is None:
            return {
                "message": "not found"
            }, 422
       
        return {
            "post": post.format()
        }

    @app.route("/posts", methods=["POST"])
    def insert_post():
        try:
            post = Post(body="udacity", user_id=5)
            post.insert()

            return {
                "message": "inserted successfully"
            }, 200
        except:
            return {
                "message": "something went wrong"
            }, 422


    return app



