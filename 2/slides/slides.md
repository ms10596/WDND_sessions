---
marp: true
theme: gaia
---
# Session 2
## Advanced Web Development
---
## Agenda
1. Why psycopg2 is not enough?
2. flask_sqlalchemy = SQLAlchemy + Flask 
---
## Problems with psycopg2
1. What are problems of writing raw sql?
* Not secure -> SQL injection
* Different dialects.
* Not maintanble -> Large code, large copy & paster

---

2. How will SQLAlchemy solves them.
* Convert python code to SQL

---
![bg 90%](classes.png)

---
![](connection.png)
---

---
![bg auto](../../udacity.gif)