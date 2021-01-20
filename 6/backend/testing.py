# wrong method
# check status code
# call with invalid page
# return 5 results

import unittest
from app import create_app
from models import Post

class TestPost(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def test_posts_size(self):
        res = self.client().get("/posts")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json["posts"]), 5)

    def test_wrong_method(self):
        res = self.client().delete("/posts")

        self.assertEqual(res.status_code, 405)

    def test_invalid_page(self):
        res = self.client().get("/posts?page=hello")

        self.assertEqual(res.status_code, 200)

    def test_insert_post(self):
        res = self.client().post("/posts", json={"body": "It's Jan 10 2021", "user_id":7})

        post_id = res.json["id"]

        inserted_post = Post.query.get(post_id)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(post_id)
        self.assertEqual("It's Jan 10 2021", inserted_post.body)





if __name__ == "__main__":
    unittest.main()