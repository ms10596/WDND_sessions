import psycopg2
import random

host = "localhost"
user = "postgres"
password = "postgres"
dbname = "sunday"

connection_string = f"host={host} user={user} password={password} dbname={dbname}"

connection = psycopg2.connect(connection_string)
cursor = connection.cursor()

# cursor.execute("""
# --sql
#  CREATE TABLE posts(
#      id SERIAL PRIMARY KEY,
#      body TEXT,
#      user_id INTEGER,
#      FOREIGN KEY(user_id) REFERENCES users(id)
#  )
# ;
# """)

# posts = ["Happy birthday", "Watching movies", "Stuck in the traffic", "Working from home", "learning web development"]

# for i in range(20):
#      cursor.execute(f"""
#     --sql
#     INSERT INTO posts(body, user_id) values('{random.choice(posts)}', {random.choice([1, 7, 8, 9, 10, 11])}) 
#     ;
#     """)


# connection.commit()



# names = ["Mohamed", "Amr", "Andrew", "Martina", "Noha"]
# for name in names:
#     cursor.execute(f"""
#     --sql
#     INSERT INTO users(name) values('{name}') 
#     ;
#     """)

# connection.commit()
# cursor.execute("""
# --sql
#  SELECT * FROM users
# ;
# """)

# result = cursor.fetchall()
# print(result)


cursor.execute("""
--sql
SELECT users.name, COUNT(*) 
FROM users
JOIN posts
ON users.id = posts.user_id
GROUP BY users.name
ORDER BY COUNT(*) DESC
;
""")

res = cursor.fetchall()

print(res)