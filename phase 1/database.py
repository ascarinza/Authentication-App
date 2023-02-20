import sqlite3
from tkinter import messagebox

def create_login_table():
    db = sqlite3.connect("login.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT)")
    db.execute("INSERT INTO login (username, password) VALUES ('admin', 'admin')")
    db.commit()
    db.close()

def validate_login(username, password):
    db = sqlite3.connect("login.sqlite")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM login where username = ? and password = ?", (username, password))
    row = cursor.fetchone()
    cursor.connection.commit()
    db.close()
    return row
        
def user_exists(username):
    conn = sqlite3.connect('login.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM login WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def create_account(username, password):
    db = sqlite3.connect("login.sqlite")
    cursor = db.cursor()
    cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, password))
    cursor.connection.commit()
    db.close()