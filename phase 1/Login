import tkinter 
import sqlite3
from tkinter import messagebox


# called when log in button is pressed to validate the user's credentials
def login():
    db = sqlite3.connect("login.sqlite")
    db.execute("CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT)")
    db.execute("INSERT INTO login (username, password) VALUES ('admin', 'admin')")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM login where username = ? and password = ?", (user_input.get(), pass_input.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', "Login Successful")
    else:
        messagebox.showerror('info', "Login Failed")
    cursor.connection.commit()
    db.close()


# Window settings 

main_window = tkinter.Tk()
main_window.title("Login App")
main_window.geometry("500x400")

padd=15
main_window['padx'] = padd

user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()

# Main heading
info_label = tkinter.Label(main_window, text="Login", font=("Arial", 20))
info_label.grid(row=0, column=1, pady=20, padx=20)

# Username input 
info_user = tkinter.Label(main_window, text="Username", font=("Arial", 15))
info_user.grid(row=1, column=0, pady= 10, padx = 10)
user_input = tkinter.Entry(main_window, textvariable=user_input, width=30)
user_input = tkinter.Entry(main_window, width=30)
user_input.grid(row=1, column=1,)

# Password input
info_pass = tkinter.Label(main_window, text="Password", font=("Arial", 15))
info_pass.grid(row=2, column=0, pady= 10, padx = 10)
pass_input = tkinter.Entry(main_window, textvariable = pass_input, show='*', width=30)
pass_input.grid(row=2, column=1,)

# Login button 
login_button = tkinter.Button(main_window, text="Login", command=login, font=("Arial", 15))
login_button.grid(row=3, column=1)


main_window.mainloop()
