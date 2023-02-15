import tkinter 
import customtkinter
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


def resize_window(event):
    w = main_window.winfo_screenwidth()
    h = root_window.winfo_screenheight()
    main_window.geometry("%dx%d+0+0" % (w, h))

# Window settings 

customtkinter.set_default_color_theme("dark-blue")

main_window = tkinter.Tk()
main_window.title("Login App")
main_window.geometry("800x400+400+400")
main_window.resizable(True, True)
main_window.minsize(600, 300)
main_window.maxsize(1500, 750)

main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.rowconfigure(2, weight=1)


main_window.bind("<Configure>", resize_window)

padd=15
main_window['padx'] = padd

user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()

# Main heading
info_label = tkinter.Label(main_window, text="Login", font=("Arial", 20))
info_label.grid(row=0, column=1, pady=20, padx=20)

# Username input 
info_user = customtkinter.CTkLabel(main_window, text="Username", font=("Arial", 20))
info_user.grid(row=1, column=0, pady= 10, padx = 10)
user_input = tkinter.Entry(main_window, textvariable=user_input, width=30)
user_input.grid(row=1, column=1)

# Password input
info_pass = customtkinter.CTkLabel(main_window, text="Password", font=("Arial", 20))
info_pass.grid(row=2, column=0, pady= 10, padx = 10)
pass_input = tkinter.Entry(main_window, textvariable = pass_input, show='*', width=30)
pass_input.grid(row=2, column=1,)

# Login button 
login_button = customtkinter.CTkButton(main_window, 
                                        text="Login", 
                                        command=login, 
                                        font=("Arial", 20),
                                        width=70,
                                        height=40,
                                        border_width = 2,
                                        corner_radius = 10,
                                        border_color = "black")

login_button.grid(row=3, column=1, padx=20, pady=20)


main_window.mainloop()
