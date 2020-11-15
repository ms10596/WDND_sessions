import unittest
from app import create_app
from models import Post, setup_db


class TestPosts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client


    # def tearDown(self):
    #     last_post = Post.query.get(self.last_id)
    #     last_post.delete()

    def test_number_of_posts(self):
        """Testing number of returned posts from endpoint"""
        res = self.client().get("/posts")
        self.assertNotEqual(res.json, None)
        self.assertEqual(len(res.json["posts"]), 10)
        self.assertEqual(res.status_code, 200)

    def test_not_found_post(self):
        """Testing if the post with id 100 is found or not"""
        res = self.client().get("/posts/100")
        self.assertEqual(res.status_code, 422)

    def test_post_id(self):
        res = self.client().get("/posts/5")
        db_post = Post.query.get(5)
        self.assertEqual(res.json["post"]["body"], db_post.body)

    def test_insert(self):
        res = self.client().post("/posts")
        self.assertEqual(res.status_code, 200)




if __name__ == "__main__":
    unittest.main()
