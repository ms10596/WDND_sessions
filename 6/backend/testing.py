import unittest
from app import create_app

class TestingApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def test_length_of_output(self):
        """tests the length of the posts that is returned to homepage"""
        res = self.client().get("/posts")
        res_json = res.json
        self.assertEqual(len(res_json["posts"]), 10)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.status, "200 OK")
    
    def test_unknown_page(self):
        """test unknown page"""
        res = self.client().get("/posts?page=100")
        self.assertEqual(res.status_code, 404)



if __name__ == "__main__":
    unittest.main()