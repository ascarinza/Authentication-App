import tkinter 
import customtkinter
import database
from tkinter import messagebox

def login():
    row = database.validate_login(user_input.get(), pass_input.get())
    if row:
        messagebox.showinfo('info', "Login Successful")
    else:
        messagebox.showerror('info', "Login Failed")

def create_account():
    username = new_user_input.get()
    password = new_pass_input.get()

    if database.user_exists(username):
        messagebox.showerror('Error', 'Username already exists')
    else:
        database.create_account(username, password)
        messagebox.showinfo('Info', 'Account created')

def resize_window(event):
    w = event.width
    h = event.height
    if w > main_window.winfo_width() or h > main_window.winfo_height():
        main_window.geometry("%dx%d+0+0" % (w, h))

# Window settings 
customtkinter.set_default_color_theme("green")

main_window = tkinter.Tk()
main_window.title("Sign in")
main_window.geometry("800x400+400+400")
main_window.resizable(True, True)
main_window.minsize(650, 300)
main_window.grid_propagate(1)

#configured rows and columns to adjust grid for window resize
num_colums = 5
num_rows = 5

for i in range(num_colums):
    main_window.columnconfigure(i, weight=1)
for i in range(num_rows):
    main_window.rowconfigure(i, weight=1)


main_window.bind("<Configure>", resize_window)
padd=25
main_window['padx'] = padd
user_input = tkinter.StringVar()
pass_input = tkinter.StringVar()
new_user_input = tkinter.StringVar()
new_pass_input = tkinter.StringVar()


# Main heading for log in side
login_label = customtkinter.CTkLabel(main_window, text="Login", font=("Arial", 26), text_color="black", width=150, height=80, corner_radius=8)
login_label.grid(row=0, column=0, pady=20, padx=20, columnspan=2)

#Labels and entried for log in 
# Username input 
info_user = customtkinter.CTkLabel(main_window, text="Username", font=("Arial", 20))
info_user.grid(row=1, column=0, pady= 10, padx = 10)
user_input = customtkinter.CTkEntry(main_window, textvariable=user_input, width=120)
user_input.grid(row=1, column=1)

# Password input
info_pass = customtkinter.CTkLabel(main_window, text="Password", font=("Arial", 20))
info_pass.grid(row=2, column=0, pady= 10, padx = 10)
pass_input = customtkinter.CTkEntry(main_window, textvariable = pass_input, show='*', width=120)
pass_input.grid(row=2, column=1,)

# Login button 
login_button = customtkinter.CTkButton(main_window, text="Login", command=login, font=("Arial", 16),width=110,
    height=50,border_width = 2,corner_radius = 10,border_color = "black")
login_button.grid(row=3, column=0, padx=20, pady=20, columnspan=2)


# Main heading for create account side
create_account_label = customtkinter.CTkLabel(main_window, text="Create Account", font=("Arial", 26), text_color="black", width=150, height=80, corner_radius=8)
create_account_label.grid(row=0, column=4, pady=20, padx=20, columnspan=2)

#Labels and entried for creating a new user 
# Username input 
new_info_user = customtkinter.CTkLabel(main_window, text="Username", font=("Arial", 20))
new_info_user.grid(row=1, column=4, pady= 10, padx = 10)
new_user_input = customtkinter.CTkEntry(main_window, textvariable= new_user_input, width=120)
new_user_input.grid(row=1, column=5)

# Password input
new_info_pass = customtkinter.CTkLabel(main_window, text="Password", font=("Arial", 20))
new_info_pass.grid(row=2, column=4, pady= 10, padx = 10)
new_pass_input = customtkinter.CTkEntry(main_window, textvariable = new_pass_input, show='*', width=120)
new_pass_input.grid(row=2, column=5)

# create an account
create_account_button = customtkinter.CTkButton(main_window, text="Create Account", command=create_account, font=("Arial", 16),width=70,
    height=50,border_width = 2,corner_radius = 10,border_color = "black")
create_account_button.grid(row=3, column=4, padx=20, pady=20, columnspan=2)

# middle text for the or label
or_seperator_label = customtkinter.CTkLabel(main_window, text="or", font=("Arial", 32), text_color="black", width=100, height=50, corner_radius=8)
or_seperator_label.grid(row=1, column=3, rowspan=2)


main_window.mainloop()
