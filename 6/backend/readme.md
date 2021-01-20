# Mini-Facebook

CRUD operations on users and posts

## How to install
```
$ pip install -r requirements.txt
```

## How to run
```
$ export FLASK_APP=app 
$ flask run
```

## API documentation
GET `/posts?page=3`

request body: N/A

response:
```json
{"posts":[{"body":"Hello world!!!!!!","id":4,"user_id":1},{"body":"Complex is better than complicated.","id":6,"user_id":4},{"body":"There should be one-- and preferably only one --obvious way to do it.","id":7,"user_id":10},{"body":"Namespaces are one honking great idea -- let's do more of those!","id":8,"user_id":10},{"body":"If the implementation is easy to explain, it may be a good idea.","id":9,"user_id":5}],"total":108}

```

POST `/posts`

request body:
```json
{
    "body": "this is a new post",
    "user_id": 5
}
```
response:
```json
{
    "id": 111
}
```