import psycopg2

import random
host = "localhost"
user = "postgres"
password = "postgres"
db = "sunday"

connection = psycopg2.connect(f"host={host} user={user} password={password} dbname={db}")

cursor = connection.cursor()
cursor.execute("insert into system_users(name) values('batata')")
# cursor.execute("""CREATE TABLE posts(
#                             id SERIAL PRIMARY KEY, 
#                             description VARCHAR(1000), 
#                              user_id INTEGER, 
#                              FOREIGN KEY(user_id) REFERENCES system_users(id))""")

# for post in ["Happy Birthday", "Life is good", "Good times", "New beggining new day", "Hello world"]:
#     user_id = random.choice([1,13,14,15,16,17])
#     cursor.execute(f"insert into posts(description, user_id) values('{post}', {user_id})")

# cursor.execute("""select system_users.name, count(*) from posts
#                             inner join system_users 
#                             on system_users.id = posts.user_id
#                             group by system_users.id 
#                             """)

# res = cursor.fetchall()
# print(res)
# connection.commit()
# cursor.close()
# connection.close()



