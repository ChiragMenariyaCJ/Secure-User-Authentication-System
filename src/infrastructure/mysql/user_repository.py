from extensions import mysql

def save_user(username, email, password):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mysql.connection.commit()
    cursor.close()

def find_user(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT username, email, password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return {'username': result[0], 'email': result[1], 'password': result[2]}
    return None