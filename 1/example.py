import  psycopg2
import random

host = "localhost"
user = "postgres"
password = "postgres"
db_name = "saturday"

conn = psycopg2.connect(f"host = {host} user={user} password={password} dbname={db_name}")

cur = conn.cursor()

# names = ["Abeer", "Ahmed", "Sayed", "Eslam", "Fady", "Hossam"]
# for name in names:
#     cur.execute(f"""
#     --sql
#     INSERT INTO users(name) values('{name}') 
#     ;
#     """)

# conn.commit()
    
# cur.execute("""
# --sql
# SELECT * from users;
# ;
# """)

# res = cur.fetchall()

# print(res)

# cur.execute("""
# --sql
#  CREATE TABLE posts(
#      id SERIAL PRIMARY KEY,
#      body TEXT,
#      user_id INTEGER,
#      FOREIGN KEY(user_id) REFERENCES users(id)
#  )
# ;
# """)

# posts = ["post1", "post2", "post3", "post4"]
# user_ids = [1,8,9,10, 11, 12, 13]

# for post in posts:
#     cur.execute(f"""
#     --sql
#     INSERT INTO posts(body, user_id) 
#     VALUES('{post}', {random.choice(user_ids)}) 
#     ;
#     """)
# conn.commit()

cur.execute("""
--sql
SELECT name, body
FROM users
JOIN posts
ON users.id = posts.user_id
;
""")
res = cur.fetchall()
print(res)

cur.close()
conn.close()




