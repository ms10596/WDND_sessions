# WDND_sessions
## Resources used in the weekly online sessions of Advanced Web Development Track powered by FWD.

> C2, C4, C6

Week # | Session | Study
--- | --- | ---
Week 1 | SQL and Data Modeling for the Web	|   Course introduction <br> Interacting with databases
Week 2	| SQL and Data Modeling for the Web |  SQLAlchemy basics <br> SQLAlchemy ORM in depth
Week 3 |	SQL and Data Modeling for the Web |	 Build a CRUD App with SQLAlchemy - Part 1 <br> Migrations <br> Build a CRUD App with SQLAlchemy - Part 2 <br> **Submit P1: Fyyur**
Week 4	| API Development and Documentation	|  Introduction to APIs <br> HTTP and Flask Basics
Week 5 |	API Development and Documentation	|  Endpoints and Payloads
Week 6 |	API Development and Documentation |	 API Testing <br> API Documentation <br> **Submit P2:Trivia API**
Week 7 | 	Identity and Access Management | Foundation <br> Identity and Authentication
Week 8	| Identity and Access Management |	Passwords <br> Access and Authorization
Week 9	| Identity and Access Management |	Thinking Adversarially <br> **Submit P3: Coffee shop full stack**

# FAQ
I'm facing errors after cloning the project and installing the requirements.
> Make sure you're using python3.7 version

Setting environment variables
> *nix based systems: 
```export FLASK_APP=main FLASK_ENV=development```
> Windows:
```set FLASK_APP=main FLASK_ENV=development```

'NoneType' object has no attribute 'days'
> In case you are facing this error while trying to run Fyuur project started code.
You'll need to edit format_datetime function in app.py file.
Replace the last line of the function with
```return babel.dates.format_datetime(date, format, locale='en')```

How to store multiple genres for one artist or venue?
> Easy solution: Use Array type in Postgresql
> Another solution: Introduce many to many relationship through creating another table `genres` and association table `entity_genres`
How to get multiple genres as input?
> request.form.getlist('genres')

Why create_artist form looks bad?
> remove `id=form.state`
> {{ form.genres(class_ = 'form-control', placeholder='Genres', autofocus = true) }}

TypeError: Parser must be a string or character stream, not datetime.
> The template expects datetime to be a string. You may convert it to string before passing it to template.
Show.query.first().start_time.strftime("%d/%m/%Y, %H:%M")

How to query venues
> # select city, state, ARRAY_AGG(name||','||address||','||phone||','||genres) from venue group by city, state;

> print(db.session.query(Venue.state, Venue.city, func.array_agg(array([Venue.address, Venue.name, Venue.phone, Venue.genres]))).group_by(Venue.state, Venue.city).all())

I tried to graduate through submitting My Personal ID Card But I Get this error( Error: Unsupported document type)
> Try a valid passport or driving license or you can send [email](fwd-support@udacity.com) to the support team with your personal ID and they should graduate you manually.


Trivia Project return data
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    }
}
```
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "currentCategory": [
        4,
        5
    ],
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
    ],
    "total_questions": 2
}
```

Backend errors in Trivia project
> pip install --upgrade werkzeug

The `ALL` category id in Trivia Project
> 0

Paginate in Flask-sqlalchemy
> https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.BaseQuery.paginate

Too many files when submitting my project.
* upload without the node_module and env folders
* add node_modules to the .gitignore file [just write node_modules in the file]

Applications URIs in Auth0
* Application Login URI: https://127.0.0.1:8100/tabs/user-page
* Allowed Callback URLs: http://127.0.0.1:8100/tabs/user-page
* Allowed Logout URLs: http://127.0.0.1:8100/logout


Failures in Postman tests in coffeshop project.
* Assert 403 instead of 401 in authorizaiton tests.
* Send recipe as a list of objects.
```{
    "title": "Water3",
    "recipe": [{
        "name": "Water",
        "color": "blue",
        "parts": 1
    }]
}
```



