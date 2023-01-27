from tkinter import *   # import tkinter module

#This function is called when the user clicks on the login button
def check_details():
    user = entry_user.get() # Get the data inside the user entry widget
    passw = entry_passw.get() # Get the data inside the password entry widget
    # Condition to check if the details entered are correct
    if user == "nyeya" and passw == "1234":
        login_stat.config(text="Successfully Logged in!") # A success message
    else:
        login_stat.config(text="Invalid username or password")

root = Tk() # Creates a window obect
root.geometry("250x200") #Sets the dimension of the window
root.title("Login Form") #Sets the title of the window

# Creating a username Label, and entry, then place them on window
label_user = Label(root, text="Username:")
entry_user = Entry(root)
label_user.place(x=20, y=20)
entry_user.place(x=100, y=20)

# Creating a password label, and entry, then placing them on window
label_passw = Label(root, text="Password:")
entry_passw = Entry(root, show="*")
label_passw.place(x=20, y=60)
entry_passw.place(x=100, y=60)

#Creating a login button and placing it on window
button_login = Button(root, text="Login", command=check_details)
button_login.place(x=80, y=110,width=80)

# Creating an output display area label, and placing it on window
login_stat = Label(root)
login_stat.place(x=20, y=150)

root.mainloop() # Prevents window from closing automatically
