import sqlite3
from tkinter import messagebox
import hashlib

def create_login_table():
    db = sqlite3.connect("login.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT)")
    password_hash = hashlib.sha256('admin'.encode('utf-8')).hexdigest()
    db.execute("INSERT INTO login (username, password) VALUES ('admin', ?)", (password_hash, ))
    db.commit()
    db.close()

def validate_login(username, password):
    db = sqlite3.connect("login.sqlite")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM login where username = ? and password = ?", (username, password))
    row = cursor.fetchone()
    if row is None:
        return None
    stored_password = row[1]
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if password_hash == stored_password:
        return row
    else:
        return None
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

    # Store the username and password hash in the database
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, password_hash))
    cursor.connection.commit()
    db.close()