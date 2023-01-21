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

# Creating a username Label, and entry, then gridding them to window
label_user = Label(root, text="Username:")
entry_user = Entry(root)
label_user.grid(row=0,column=0,padx=10, pady=10)
entry_user.grid(row=0,column=1,padx=10, pady=10)

# Creating a password label, and entry, then gridding them to window
label_passw = Label(root, text="Password:")
entry_passw = Entry(root, show="*")
label_passw.grid(row=1,column=0,padx=10, pady=10)
entry_passw.grid(row=1,column=1,padx=10, pady=10)

#Creating a login button and gridding it to window
button_login = Button(root, text="Login", command=check_details)
button_login.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

# Creating an output display area label, and gridding it to window
login_stat = Label(root)
login_stat.grid(row=3,column=0,columnspan=2,padx=10, pady=10)

root.mainloop() # Prevents window from closing automatically
