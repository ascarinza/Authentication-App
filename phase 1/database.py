import sqlite3
from tkinter import messagebox
import hashlib


def create_login_table():
    db = sqlite3.connect("login.sqlite")
    try:
        db.execute("CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT)")
        db.commit()
        password_hash = hashlib.sha256('admin'.encode('utf-8')).hexdigest()
        db.execute("INSERT INTO login (username, password) VALUES ('admin', ?)", (password_hash, ))
        db.commit()
    except Exception as e:
        print("Error creating login table: ", e)
    db.close()

def validate_login(username, password):
    db = sqlite3.connect("login.sqlite")
    cursor = db.cursor()
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("SELECT * FROM login where username = ? and password = ?", (username, password_hash))
    row = cursor.fetchone()
    if row is None:
        return None
    else:
        return row
    db.close()
        
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

    # Store the username and password hash in the database
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, password_hash))
    cursor.connection.commit()
    db.close()