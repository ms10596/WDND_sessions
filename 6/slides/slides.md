---
marp: true
theme: gaia
---
# Session 6
## Advanced Web Development
---
## Agenda
* Project 2 `Trivia API`
* Testing
* Documentation

---
# Why testing?
* To confirm expected request handling behavior
* To confirm success-response structure is correct
* To confirm expected errors are handled appropriately
* To confirm CRUD operations persist
---
# Basic blocks of testing in python.
```python
import unittest

class Mytestcase(unittest.TestCase):
    def setup(self):
        self.app = create_app()
        self.client = self.app.testclient
        setup_db(app)

    def test_status(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)


```
---
# Why Documentation?
* To be used by others without contacting me.
* To be understood by others

---
# Basic blocks of documentation
* Project title
    * Description, motivation, screenshots.
* Prerequisites and Installation.
* How run your app.
* How to run test.
* API documentation.
---
![bg auto](../../udacity.gif)

