# My facebook

This project illlusterates my understanding in flask and SQLAclhemy.

## Installation
```pip install -r requirements.txt```

## How to run app
```flask run```


## API Documentation
GET /posts
* This endpoint returns list of posts
* Query parameters `?page=5` page of the posts

```
curl http://localhost:5000/posts?page=5
{
  "posts": [
    {
      "body": "Earth is flat", 
      "id": 43, 
      "user_id": 6
    }, 
    {
      "body": "\u0639\u064a\u062f \u0633\u0639\u064a\u062f", 
      "id": 44, 
      "user_id": 3
    }, 
    {
      "body": "\u0644\u0646 \u0623\u0639\u064a\u0634 \u0641\u064a \u062c\u0644\u0628\u0627\u0628 \u0623\u0628\u064a", 
      "id": 45, 
      "user_id": 4
    }, 
    {
      "body": "Happy New Year", 
      "id": 46, 
      "user_id": 7
    }, 
    {
      "body": "Playing chess", 
      "id": 47, 
      "user_id": 6
    }, 
    {
      "body": "\u0644\u0646 \u0623\u0639\u064a\u0634 \u0641\u064a \u062c\u0644\u0628\u0627\u0628 \u0623\u0628\u064a", 
      "id": 48, 
      "user_id": 1
    }
  ]
}
```
