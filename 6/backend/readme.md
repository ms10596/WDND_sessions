# MyFacebook

## Description


## Installation
```$ pip install -r requirements.txt```

## Run
```
$ export FLASK_APP = app
$ flask run
```

## API Documentation
GET /posts?page=1
* Returns json object having lists of 10 posts and total number of posts
```
curl https://localhost:5000/posts
{
    "posts": [
        {
            "body": "سمكة التونة العنيدة",
            "id": 3,
            "user_id": 4
        },
        {
            "body": "Playing chess",
            "id": 4,
            "user_id": 6
        },
        {
            "body": "Watching World Cup with the family",
            "id": 5,
            "user_id": 5
        },
        {
            "body": "Playing chess",
            "id": 6,
            "user_id": 6
        },
        {
            "body": "سمكة التونة العنيدة",
            "id": 7,
            "user_id": 5
        },
        {
            "body": "Playing chess",
            "id": 8,
            "user_id": 5
        },
        {
            "body": "لن أعيش في جلباب أبي",
            "id": 9,
            "user_id": 4
        },
        {
            "body": "Playing chess",
            "id": 10,
            "user_id": 4
        },
        {
            "body": "I have just completed the Web Development Track from FWD",
            "id": 11,
            "user_id": 1
        },
        {
            "body": "Watching World Cup with the family",
            "id": 12,
            "user_id": 7
        }
    ],
    "total": 48
}
```