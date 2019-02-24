import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE user_login (
            email text,
            username text,
            password text
            )""")

def create_user(userObj):
    with conn:
        c.execute("INSERT INTO user_login VALUES (:username, :password)", {'username': userObj.username, 'password': userObj.password})

conn.close()